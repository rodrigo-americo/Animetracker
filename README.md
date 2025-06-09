# Animetracker

Aplicação Django para rastreamento de animes e mangás, permitindo que usuários acompanhem seu progresso e registrem avaliações.

## Objetivo

O projeto tem como foco organizar séries de anime ou mangá. Cada usuário pode registrar o quanto assistiu/leu, atribuir notas e comentários e consultar as informações cadastradas de cada série.

## Instalação

O projeto é gerenciado com [Poetry](https://python-poetry.org/). Após clonar o repositório, instale as dependências e configure o ambiente virtual:

```bash
poetry install
poetry shell
```

Com o ambiente ativado, crie a base de dados e aplique as migrações padrão do Django:

```bash
python animetracker/manage.py migrate
```

## Principais funcionalidades

- Gestão de usuários através do modelo customizado `Usuario`.
- Cadastro de séries (`Serie`) de tipo anime ou mangá com sinopse e total de episódios/capítulos.
- Registro de avaliações (`Avaliacao`) contendo nota, progresso e comentários do usuário.
- Acesso à interface administrativa do Django para gerenciar usuários, séries e avaliações.
- Execução do servidor de desenvolvimento com:
  ```bash
  python animetracker/manage.py runserver
  ```
