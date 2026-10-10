# Sistema de Roletas Personalizadas

> Substitua os trechos entre colchetes `[ ]` pelas informações reais do trabalho. Remova esta nota e as demais orientações em *itálico* antes da entrega.

[![Status](https://img.shields.io/badge/status-em_desenvolvimento-yellow)]()
[![Versão](https://img.shields.io/badge/versão-0.1.1-blue)]()
[![Licença](https://img.shields.io/badge/licença-acadêmica-lightgrey)]()

**Instituição:** Centro Universitário de Brasilia  
**Curso:** Análise e Desenvolvimento  
**Disciplina:** Desenvolvimento Web  
**Turma / Semestre:** 2025.4  
**Professor(a):** Felippe Pires Ferreira  
**Status do projeto:** [Protótipo / MVP / Em desenvolvimento / Concluído]  

---

## Sumário

- [1. Descrição do projeto](#1-descrição-do-projeto)
- [2. Funcionalidades](#2-funcionalidades)
- [3. Demonstração](#3-demonstração)
- [4. Tecnologias utilizadas](#4-tecnologias-utilizadas)
- [5. Arquitetura](#5-arquitetura)
- [6. Organização dos diretórios](#6-organização-dos-diretórios)
- [7. Participantes](#7-participantes)
- [8. Como executar](#8-como-executar)
- [9. Configuração](#9-configuração)
- [10. Testes](#10-testes)
- [11. Uso de inteligência artificial](#11-uso-de-inteligência-artificial)
- [12. Contribuição e fluxo de trabalho](#12-contribuição-e-fluxo-de-trabalho)
- [13. Histórico de versões](#13-histórico-de-versões)
- [14. Limitações e próximos passos](#14-limitações-e-próximos-passos)
- [15. Licença, referências e contato](#15-licença-referências-e-contato)

---

## 1. Descrição do projeto

Em diversas atividades acadêmicas, corporativas e recreativas, como dinâmicas de grupo, sorteios em sala de aula e tomadas de decisão casuais, há uma demanda constante por ferramentas visuais e imparciais de sorteio. No entanto, as soluções de roleta disponíveis na web frequentemente sofrem com a falta de persistência dos dados (perdendo as configurações ao fechar a página), a exigência burocrática de cadastros com e-mail ou opções bastante limitadas de customização visual e probabilística.

Para resolver essas limitações, este projeto consiste em uma aplicação web de **Roletas Personalizadas** desenvolvida com Python e Django. A plataforma oferece uma experiência leve e desburocratizada, permitindo que o usuário crie uma conta simplificada (utilizando apenas nome de usuário e senha) para construir e manter uma biblioteca de roletas privadas e salvas persistentemente em seu perfil. O sistema permite a customização livre de fatias através de seletores de cores (*color picker*) e a definição opcional de pesos de probabilidade para cada item.

Destinada a professores, estudantes, facilitadores de jogos e público em geral, a aplicação conta com uma interface responsiva adaptada para computadores e dispositivos móveis, além de simulação visual de giro com efeitos sonoros e animações de comemoração. Desenvolvido como projeto acadêmico, o software consolida conceitos fundamentais de desenvolvimento web moderna, integrando arquitetura Django, API REST via Django REST Framework e persistência em banco de dados relacional.

### Objetivos

- **Objetivo geral:** Desenvolver e publicar uma aplicação web responsiva baseada em Django e Jango REST Framework para criação, gestão, personlização e execução de roletas exclusivas salvas persistentemente no perfil do usuário.
- **Objetivos específicos:**
  - Implementar autenticação baseada unicamente em nome de usuário e senha
  - Oferecer seletor livre de cores para cada item e/ou fatia da roleta
  - Permitir a difinição opcional de pesos/probalidades para cada item da roleta, com padrão de pesos iguais/probalididade uniforme
  - Desenvolver uma interface interativa com animação de giro, efeitos sonoros e comemoração visual com confetes
  - Garantir privacidade total: roletas são estritamente exclusivas do perfil do usuário criador
  - Disponibilizar dashboard para gerenciamento completo das roletas ativas

### Público-alvo

- Pessoas que querem fazer decisões de atividades por divertimento
- Professores que querem fazer alguma atividade mais interativa

---

## 2. Funcionalidades

*Liste as funções implementadas (ou previstas) no sistema. Marque o status de cada uma.*
<!-- Status: Implementada / Em andamento / Planejada -->
| Funcionalidade | Descrição | Status |
| --- | --- | --- |
| Autenticação | login, logout | Planejada |
| Cadastro de usuários | criação e edição de perfis | Planejada |
| Validação de Campos Obrigatorios | Validação de campos obrigatorios evita que o usuário seja registrado sem nome ou senha, podendo causar um problema no banco de dados e/ou outras funcionalidades | Planejada |
| Alerta de duplicidade | Exibição de mensagem de erro caso o nome de usuário já exista no banco de dados | Planejada |
| Atalho de Login | Direcionamento para a tela de Login através da opção "Já possuo uma conta" | Planejada |
| Autenticação do Login | Validação de credenciais (Usuário e Senha) e inicialização de sessão privada | Planejada |
| Tratamento de credenciais invalidas | Exibição de mensagem de erro para usuário/senha incorretos com permissão para nova tentativa | Planejada |
| Listagem Roletas | Exibição da lista de roletas pertencentes ao usuário autenticado | Planejada |
| Criação de nova roleta | Interface para inserção de novas roletas a partir da lista | Planejada |
| Personalização visual | Seleção de tema/esquema de cores para a roleta | Planejada |
| Inclusão de itens na roleta | Adição de conteúdos textuais correspondentes às fatias da roleta | Planejada |
| Persistência de dados | Salvamento permanente da roleta, temas e itens no banco de dados | Planejada |
| Acionamento de giro da roleta | Botão "Girar" para iniciar o sorteio | Planejada |
| Animação gráfica da roleta | Rotação visual da roleta na interface do usuário | Planejada |
| Sorteio e destaque | Seleção de um dos itens configurados com destaque visual da fatia sorteada | Planejada |
| Exibição do resultado | Apresentação do item sorteado na tela após a conclusão da animação | Planejada |

### Requisitos não funcionais

*Informe restrições de qualidade, quando existirem.*

- **Desempenho:** [Ex.: respostas da API em menos de 2 segundos]
- **Segurança:** [Ex.: senhas armazenadas com hash; HTTPS em produção]
- **Usabilidade:** [Ex.: interface responsiva para desktop e celular]
- **Disponibilidade:** [Ex.: uso em ambiente local / laboratório da disciplina]

---

## 3. Demonstração

*Inclua capturas de tela, GIF ou link para vídeo. Coloque as imagens em `images/`.*
<!-- --- AINDA NÃO FOI ALTERADO --- -->
![Tela principal](images/[screenshot-principal].png)

| Tela | Descrição |
| --- | --- |
| [Login] | [Acesso ao sistema com e-mail e senha] |
| [Painel] | [Visão geral das reservas do dia] |

**Vídeo / protótipo:** [URL do YouTube, Loom ou Figma]

---

## 4. Tecnologias utilizadas

*Informe as tecnologias de fato usadas no projeto. Remova as linhas que não se aplicarem.*

| Camada | Tecnologia | Versão |
| --- | --- | --- |
| Linguagem | Python | 3.13+ |
| Frontend | HTML,CSS | [Ex.: 18] |
| Backend | [Ex.: Flask, Spring Boot, Node.js] | [Ex.: 3.x] |
| Banco de dados | PostgreSQL | [Ex.: 16] |
| Testes | pytest, Jest, lint | [Ex.: 8] |
| Infraestrutura | [Ex.: Docker, GitHub Actions] | — |
| Outras ferramentas | [Ex.: Git, Figma, Postman] | — |

---

## 5. Arquitetura

*Explique como o sistema está organizado: camadas, principais componentes e o fluxo entre eles. Inclua um diagrama no PDF de arquitetura ou de classes em `docs/` e descreva-o em texto.*

[Ex.: a solução segue uma arquitetura em camadas (apresentação, aplicação, domínio e persistência). O frontend consome uma API REST. O backend aplica as regras de negócio e persiste os dados no banco.]

```text
[Usuário] → [Interface / Frontend] → [API / Backend] → [Banco de dados]
```

**Decisões relevantes:**

- [Ex.: uso de API REST para separar cliente e servidor.]
- [Ex.: persistência relacional porque os dados possuem relacionamentos bem definidos.]

### Endpoints principais (quando houver API)

| Método | Rota | Descrição |
| --- | --- | --- |
| `POST` | `/api/[recurso]` | [Ex.: criar um registro] |
| `GET` | `/api/[recurso]` | [Ex.: listar registros] |
| `GET` | `/api/[recurso]/{id}` | [Ex.: obter um registro] |
| `PUT` | `/api/[recurso]/{id}` | [Ex.: atualizar um registro] |
| `DELETE` | `/api/[recurso]/{id}` | [Ex.: remover um registro] |

Documentação completa da API: [link para Swagger, Postman ou `docs/api.md`]

---

## 6. Organização dos diretórios

*Mantenha a árvore alinhada à estrutura real do repositório. Ajuste pastas conforme o tipo de projeto.*

```text
.
├── .github/                  # Configurações do GitHub (automações)
│   └── workflows/            # Pipelines de CI/CD
├── docs/                     # Documentação e artefatos técnicos do projeto
│   └── modelagem/            # Diagramas e especificações de modelagem
├── images/                   # Imagens e recursos visuais da documentação
├── roletas_customizadas/     # Módulo principal / raiz da aplicação Django
│   ├── roletas_customizadas/ # Módulo de configurações centrais do Django
│   │   ├── management/       # Comandos personalizados do Django
│   │   ├── __init__.py       # Inicialização do pacote Python
│   │   ├── asgi.py           # Ponto de entrada para servidores assíncronos (ASGI)
│   │   ├── settings.py       # Definições globais e configurações do projeto
│   │   ├── urls.py           # Roteamento central de URLs e endpoints
│   │   └── wsgi.py           # Ponto de entrada para servidores WSGI
│   ├── tests/                # Testes automatizados da aplicação
│   │   └── __init__.py       # Inicialização do pacote de testes
│   └── manage.py             # Utilitário de linha de comandos do Django
├── .gitignore                # Ficheiros e diretórios ignorados pelo Git
├── pyproject.toml            # Configuração do projeto e de ferramentas Python
├── README.md                 # Documentação principal do repositório
└── requirements.txt          # Lista de dependências e pacotes Python
```

| Diretório / arquivo | Função |
| --- | --- |
| `.github/` | Configurações do GitHub Actions e rotinas de automação/CI/CD |
| `docs/modelagem/` | Artefatos técnicos de análise e modelagem (diagramas e especificações) |
| `images/` | Figuras, capturas de tela e recursos visuais da documentação |
| `roletas_customizadas/` | Diretório raiz do código-fonte do projeto Django |
| `roletas_customizadas/roletas_customizadas/` | Módulo com as configurações globais da aplicação (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`) |
| `roletas_customizadas/tests/` | Casos de testes automatizados do sistema |
| `roletas_customizadas/manage.py` | Utilitário de linha de comando do Django para execução e migrações |
| `.gitignore` | Mapeamento de arquivos e diretórios ignorados pelo controle de versão Git |
| `pyproject.toml` | Configuração de ferramentas de desenvolvimento, linters e ambiente Python |
| `README.md` | Documentação principal com visão geral, arquitetura e instruções de uso |
| `requirements.txt` | Relação de dependências e bibliotecas Python necessárias para o projeto |

---

## 7. Participantes

*Informe nome completo, função no grupo e, se houver, o identificador acadêmico (matrícula).*

| Nome | Matrícula | Função no projeto |
| --- | --- | --- |
| João Pedro de Melo Naves | 22509476 | separar funções |
| Rodrigo Viera | 000000 | separar funções |
| Maurício | 000000 | separar funções |

**Professor(a) responsável:** Felippe Pires Ferreira

---

## 8. Como executar

*Preencha com os comandos reais do projeto para que outra pessoa consiga reproduzir o ambiente.*

### Pré-requisitos

- [Ex.: Git]
- [Ex.: Python 3.12+]
- [Ex.: Node.js 20+]
- [Ex.: Docker]

### Instalação e execução

```bash
# 1. Clonar o repositório
git clone [URL_DO_REPOSITORIO]
cd [NOME_DA_PASTA]

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Configurar variáveis de ambiente
cp .env.example .env
# edite o arquivo .env com as credenciais locais

# 4. Executar a aplicação
[comando de execução]
```

**Acesso local:** [Ex.: http://localhost:3000]

### Implantação (quando houver)

- **Ambiente:** [Ex.: Render, Railway, Vercel, servidor da instituição]
- **URL de produção:** [https://...]
- **Observações:** [Ex.: é necessário configurar as variáveis de ambiente no painel do provedor]

---

## 9. Configuração

*Liste as variáveis de ambiente usadas pelo sistema. Nunca publique senhas, tokens ou chaves neste arquivo.*

| Variável | Obrigatória | Descrição | Exemplo |
| --- | --- | --- | --- |
| `PORT` | Sim | Porta da aplicação | `3000` |
| `DATABASE_URL` | Sim | Conexão com o banco | `postgresql://user:senha@localhost:5432/app` |
| `SECRET_KEY` | Sim | Chave de sessão / JWT | `[gerar localmente]` |

Credenciais reais devem ficar apenas no arquivo `.env` (não versionado).

---

## 10. Testes

*Descreva como executar os testes e o que eles cobrem.*

```bash
[comando para executar os testes]
```

| Tipo | Ferramenta | O que verifica |
| --- | --- | --- |
| Unitários | [Ex.: pytest / JUnit / Jest] | [Ex.: regras de negócio isoladas] |
| Integração | [Ex.: ...] | [Ex.: API e banco de dados] |
| Manuais | [Ex.: checklist em `docs/`] | [Ex.: fluxos principais da interface] |

**Cobertura atual:** [Ex.: 70% / não medida]

---

## 11. Uso de inteligência artificial

Este repositório segue a política de uso de IA da disciplina (semáforo pedagógico):

![Política de uso de IA — semáforo](images/semaforo.png)

| Situação | Significado |
| --- | --- |
| **Vermelho — uso proibido** | Atividades de autonomia intelectual (ex.: provas presenciais sem consulta). |
| **Amarelo — uso limitado** | IA pode ser ferramenta auxiliar, desde que haja declaração de uso. |
| **Verde — uso permitido** | Uso livre ao longo da atividade acadêmica. |

### Declaração de uso

*Preencha de forma honesta. Se não houve uso de IA, declare explicitamente.*

- **Houve uso de IA neste projeto?** Sim
- **Ferramentas utilizadas:** GitHub, Visual Studio Code, Gemini
- **Finalidade:** Revisão textual, pesquisa de como fazer estruturas especificas fora do contexto da atividade
- **O que NÃO foi delegado à IA:** 

---

## 12. Contribuição e fluxo de trabalho

*Padronize o trabalho em equipe. Ajuste as regras ao combinado da disciplina.*

### Branches

- `main` — versão estável para avaliação
- `develop` — integração do grupo *(opcional)*
- `feat/[nome]` — nova funcionalidade
- `fix/[nome]` — correção de defeito
- `docs/[nome]` — alterações só de documentação

### Commits

Use mensagens curtas e no imperativo, por exemplo:

- `feat: adiciona cadastro de reservas`
- `fix: corrige validação de data`
- `docs: atualiza instruções de execução`

### Passos sugeridos

1. Criar uma branch a partir de `main`.
2. Implementar e testar localmente.
3. Abrir um *pull request* / *merge request* para revisão do grupo.
4. Só então integrar à branch principal.

**Issues e quadro de tarefas:** [link do GitHub Projects, Trello ou similar]

---

## 13. Histórico de versões

*Registre entregas relevantes (sprints, checkpoints ou versões avaliadas).*

<!-- 
Exemplo:
| `0.0.1` | [AAAA-MM-DD] | [Ex.: estrutura inicial do repositório] |

Empilhar os mais novos em cima
-->

| Versão | Data | Descrição |
| --- | --- | --- |
| `0.1.1` | [2026-10-08] | Atualização da documentação |
| `0.1.0` | [2026-10-05] | Estrutura Inicial do Projeto |

---

## 14. Limitações e próximos passos

### Problemas conhecidos

- [Ex.: a recuperação de senha ainda não envia e-mail]
- [Ex.: o layout quebra em telas menores que 360 px]

### Roadmap

- [ ] [Ex.: autenticação com dois fatores]
- [ ] [Ex.: exportação de relatórios em CSV]
- [ ] [Ex.: implantação em ambiente de homologação]

---

### 15. Integrações Externas

#### API de Data e Hora (World Time API)
- **Finalidade:** Sincronização de data, hora e fusos horários oficiais para registro de logs e auditoria.
- **Endpoint principal:** `GET /api/timezone/America/Sao_Paulo`
- **Autenticação:** Não necessária.
- **Tratamento de Falhas:** Em caso de indisponibilidade ou timeout da API, o sistema utiliza o horário local do servidor como *fallback*, garantindo que a aplicação continue funcionando normalmente.
- **Documentação:** [World Time API Docs](https://worldtimeapi.org)


---

## 16. Licença, referências e contato

**Licença:** [Ex.: uso exclusivamente acadêmico / MIT / outro]

Este material destina-se a fins educacionais. Verifique com a disciplina se o código pode ser reutilizado fora do curso.

### Documentação complementar

- Índice da pasta `docs/`: [`docs/README.pdf`](docs/README.pdf)
- Casos de uso (diagrama + especificações): [`docs/modelagem/casos-de-uso/especificacoes-casos-de-uso.pdf`](docs/modelagem/casos-de-uso/especificacoes-casos-de-uso.pdf)
- Diagrama de classes: [`docs/modelagem/classes/diagrama-de-classes.pdf`](docs/modelagem/classes/diagrama-de-classes.pdf)
- Modelo conceitual (ER): [`docs/modelagem/banco-de-dados/diagrama-er.pdf`](docs/modelagem/banco-de-dados/diagrama-er.pdf)
- Modelo lógico: [`docs/modelagem/banco-de-dados/modelo-logico.pdf`](docs/modelagem/banco-de-dados/modelo-logico.pdf)
- Apresentação: [`docs/apresentacao.pdf`](docs/)

### Referências

- [Autor. Título. Ano. URL ou dados bibliográficos.]
- [Documentação oficial da tecnologia X.]

### Contato

Dúvidas sobre o projeto: [e-mail institucional do grupo ou issue no repositório]

**Agradecimentos:** [Ex.: professor(a), monitoria, materiais da disciplina]
