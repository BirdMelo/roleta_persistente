import re
import subprocess
from datetime import datetime
from pathlib import Path
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Atualiza a versão no pyproject.toml e no README.md"

    def add_arguments(self, parser):
        parser.add_argument("versao", type=str, help="Nova versão (ex: 0.2.0)")
        parser.add_argument(
            "descricao", type=str, help="Descrição da alteração"
        )

    def handle(self, *args, **options):
        new_version = options["versao"]
        description = options["descricao"]
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Sobe 5 níveis até a raiz do repositório
        project_root = Path(__file__).resolve().parents[4]

        toml_way = project_root / "pyproject.toml"
        readme_way = project_root / "README.md"

        if not re.fullmatch(r"\d+\.\d+\.\d+", new_version):
            self.stderr.write(
                self.style.ERROR(
                    "Erro: a versão deve seguir o formato semântico X.Y.Z (ex: 0.2.0)"
                )
            )
            return

        if not toml_way.exists():
            self.stderr.write(
                self.style.ERROR(
                    f"Erro: pyproject.toml não encontrado em {toml_way}"
                )
            )
            return

        if not readme_way.exists():
            self.stderr.write(
                self.style.ERROR(
                    f"Erro: README.md não encontrado em {readme_way}"
                )
            )
            return

        if subprocess.run(
            ["git", "-C", str(project_root), "rev-parse", "--is-inside-work-tree"],
            capture_output=True,
            text=True,
        ).returncode != 0:
            self.stderr.write(
                self.style.ERROR("Erro: o projeto não está em um repositório Git.")
            )
            return

        tag_name = f"v{new_version}"
        existing_tags = subprocess.run(
            ["git", "-C", str(project_root), "tag", "--list"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout.splitlines()

        if tag_name in existing_tags or new_version in existing_tags:
            self.stderr.write(
                self.style.ERROR(
                    f"Erro: a tag '{tag_name}' ou '{new_version}' já existe."
                )
            )
            return

        # 1. Atualizar APENAS a versão do projeto no pyproject.toml
        toml_content = toml_way.read_text(encoding="utf-8")
        toml_updated = re.sub(
            r'^(version\s*=\s*["\']).*?(["\'])',
            rf"\g<1>{new_version}\2",
            toml_content,
            count=1,
            flags=re.MULTILINE,
        )
        toml_way.write_text(toml_updated, encoding="utf-8")

        # 2. Atualizar README.md
        readme_content = readme_way.read_text(encoding="utf-8")

        # Atualiza a Badge
        readme_updated = re.sub(
            r"(versão-)[^-\s]+(-blue)", rf"\g<1>{new_version}\2", readme_content
        )

        new_table_line = (
            f"| `{new_version}` | [{current_date}] | {description} |"
        )

        # Regex específico para capturar o CABEÇALHO da tabela de versões + O DIVISOR
        version_table_pattern = r"(\|\s*Vers[ãa]o\s*\|\s*Data\s*\|\s*Descri[çc][ãa]o\s*\|[\r\n]+\|\s*:?-+:?\s*\|\s*:?-+:?\s*\|\s*:?-+:?\s*\|)"

        match = re.search(
            version_table_pattern, readme_updated, flags=re.IGNORECASE
        )
        if match:
            header_and_divider = match.group(0)
            readme_updated = readme_updated.replace(
                header_and_divider,
                f"{header_and_divider}\n{new_table_line}",
                1,
            )
        else:
            self.stderr.write(
                self.style.ERROR(
                    "Erro: tabela 'Versão | Data | Descrição' não encontrada no README.md."
                )
            )
            return

        toml_way.write_text(toml_updated, encoding="utf-8")
        readme_way.write_text(readme_updated, encoding="utf-8")

        try:
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(project_root),
                    "add",
                    "--",
                    "pyproject.toml",
                    "README.md",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(project_root),
                    "commit",
                    "-m",
                    f"chore: atualiza versão para {tag_name}",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(project_root),
                    "tag",
                    "-a",
                    tag_name,
                    "-m",
                    f"Versão {new_version}",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            branch = subprocess.run(
                [
                    "git",
                    "-C",
                    str(project_root),
                    "branch",
                    "--show-current",
                ],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()

            if not branch:
                raise subprocess.CalledProcessError(
                    1,
                    "git branch --show-current",
                    stderr="Não foi possível identificar a branch atual.",
                )

            origin = subprocess.run(
                [
                    "git",
                    "-C",
                    str(project_root),
                    "remote",
                    "get-url",
                    "origin",
                ],
                check=True,
                capture_output=True,
                text=True,
            ).stdout.strip()

            if not origin:
                raise subprocess.CalledProcessError(
                    1,
                    "git remote get-url origin",
                    stderr="O remoto 'origin' não está configurado.",
                )

            subprocess.run(
                [
                    "git",
                    "-C",
                    str(project_root),
                    "push",
                    "--atomic",
                    "origin",
                    f"HEAD:{branch}",
                    f"refs/tags/{tag_name}",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as error:
            message = error.stderr.strip() if error.stderr else str(error)
            self.stderr.write(
                self.style.ERROR(
                    f"Erro ao criar commit, tag ou enviar ao GitHub: {message}"
                )
            )
            return

        self.stdout.write(
            self.style.SUCCESS(
                f"✓ Versão {new_version} atualizada, commitada e enviada ao GitHub "
                f"com a tag {tag_name}."
            )
        )