contacts = []

def add_contact():
    try:
        name = input('Nome do contato: ').strip()
        if not name.replace(" ", "").isalpha():
            raise ValueError('O nome deve conter apenas letras.')
        
        phone = input('Número de telefone: ').strip()
        if not phone.isdigit():
            raise ValueError('O telefone deve conter apenas números.')
        
        email = input('Email: ').strip()
        if '@' not in email or '.' not in email:
            raise ValueError('Email inválido.')
        
        contact = {'name': name, 'phone': phone, 'email': email}
        contacts.append(contact)
        print(f'Contato {name} adicionado com sucesso!\n')

    except ValueError as e:
        print(f'Erro: {e}\n')

def list_contacts():
    if not contacts:
        print('Nenhum contato cadastrado.\n')
    else:
        for i, c in enumerate(contacts, start=1):
            print(f'{i}. {c['name']} - {c['phone']} - {c['email']}')
        print()

def search_contact():
    search_name = input('Digite o nome para buscar: ').strip()
    found = [c for c in contacts if search_name.lower() in c['name'].lower()]
    if found:
        for c in found:
            print(f"{c['name']} - {c['phone']} - {c['email']}")
    else:
        print('Contato não encontrado.')
    print()

def delete_contact():
    list_contacts()
    try:
        index = int(input('Digite o número do contato que deseja excluir: '))
        if 1 <= index <= len(contacts):
            removed = contacts.pop(index - 1)
            print(f'Contato {removed['name']} deleted.\n')
        else:
            print('Número inválido.\n')
    except ValueError:
        print('Insira um número válido.')

def update_contact():
    list_contacts()
    try:
        index = int(input("Insira o número de telefone que deseja atualizar: "))
        if 1 <= index <= len(contacts):
            contact = contacts[index - 1]
            
            new_name = input(f"Novo nome ({contact['name']}): ").strip()
            if new_name:
                if not new_name.replace(" ", "").isalpha():
                    raise ValueError("O nome deve conter apenas letras.")
                contact['name'] = new_name

            new_phone = input(f"Novo número ({contact['phone']}): ").strip()
            if new_phone:
                if not new_phone.isdigit():
                    raise ValueError("O telefone deve conter apenas números.")
                contact['phone'] = new_phone

            new_email = input(f"Novo email ({contact['email']}): ").strip()
            if new_email:
                if "@" not in new_email or "." not in new_email:
                    raise ValueError("Email inválido.")
                contact['email'] = new_email

            print(f"Contato {contact['name']} atualizado com sucesso!\n")
        else:
            print("Número inválido.\n")
    except ValueError as e:
        print(f"Erro: {e}\n")

while True:
    print('1. Adicionar contato')
    print('2. Listar contatos')
    print('3. Buscar contato')
    print('4. Excluir contato')
    print('5. Sair')

    try:
        option = int(input('Escolha uma opção: '))
        if option == 1:
            add_contact()
        elif option == 2:
            list_contacts
        elif option == 3:
            search_contact()
        elif option == 4:
            delete_contact()
        elif option == 5:
            print('Finalizando.')
            break
        else:
            print('Opção inválida. \n')
    except ValueError:
        print('Digite um número válido. \n')