# Simple Contact Agenda

## Descrição
Um gerenciador de contatos que permite adicionar, listar, buscar e excluir contatos. O programa inclui **validação de entradas** e **tratamento de erros** com `try/except`, garantindo que nomes, telefones e emails sejam informados corretamente. Interativo e fácil de usar.  

---

## Funcionalidades
- Adicionar contato (nome, telefone e email)  
- Listar todos os contatos  
- Buscar contato pelo nome  
- Excluir contato  
- Menu interativo com tratamento de erros  

---

## Tecnologias
- Python 3.x  
- Estruturas de dados: listas e dicionários  
- Tratamento de erros com `try/except`  

---

## Como usar
1. Clone o repositório:  
```bash
git clone https://github.com/hadrielyharrizon/Contact-Agenda.git
```
2. Navegue até a pasta do projeto:
```bash
cd Contact-Agenda
```

3. Execute o programa:
```bash
python app.py
```

## Estrutura do Código
contacts → lista que armazena os contatos

## Funções principais:

- add_contact() → adiciona contato
- list_contacts() → lista todos os contatos
- search_contact() → busca contato pelo nome
- delete_contact() → exclui contato selecionado

## Diferenciais

- Validação de entradas (nome, telefone e email)
- Tratamento de erros para entradas inválidas
- Programa interativo e fácil de usar
- Pode ser expandido para salvar os contatos em arquivos CSV