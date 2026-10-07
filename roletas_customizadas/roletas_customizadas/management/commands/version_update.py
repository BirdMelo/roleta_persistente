import re
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
            readme_way.write_text(readme_updated, encoding="utf-8")

            self.stdout.write(
                self.style.SUCCESS(
                    f"✓ pyproject.toml e README.md atualizados para a versão {new_version} com sucesso!"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    "Aviso: Tabela 'Versão | Data | Descrição' não encontrada no README.md."
                )
            )