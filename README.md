# Sistema de Gestão Escolar

Aplicação de terminal desenvolvida em Python para gerenciar o cadastro de alunos de forma simples, usando listas e dicionários.

## Funcionalidades

- Cadastrar alunos (matrícula, nome, idade, turma e notas)
- Listar todos os alunos cadastrados
- Buscar aluno por matrícula
- Inserir ou alterar notas de Matemática e Português
- Excluir aluno

O sistema já inicia com alguns alunos de exemplo para facilitar os testes.

## Tecnologias

- Python 3

## Como executar

1. Clone o repositório:
```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
```
2. Entre na pasta do projeto:
```bash
   cd nome-do-repositorio
```
3. Execute o programa:
```bash
   python app.py
```

## Estrutura dos dados

Cada aluno é um dicionário no formato:

```python
{
    "matricula": 1,
    "nome": "João",
    "idade": 15,
    "turma": "A",
    "notas": {"matematica": 8.5, "portugues": 7.0}
}
```

## Melhorias futuras

- Salvar os dados em arquivo (JSON ou CSV) para não perder ao fechar o programa
- Cálculo de média e situação do aluno (aprovado/reprovado)
- Validação de entradas inválidas

## Autor

Matheus Campos
