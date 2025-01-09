from functions import addContact, listContacts, editContact, starContactOrUnstarContact, starredContactsList, deleteContact

contacts = []
while True:
    print("\n\n\n✦ AGENDA DE CONTATOS ✦\n")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Favoritar/Desfavoritar contato")
    print("5. Listar contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

    escolha = input("\nEscolha sua opção: ")
    
    if escolha == "1":
        name = input("Digite o nome do contato: ")
        phone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        addContact(contacts, name, phone, email)
    
    if escolha == "2":
        listContacts(contacts)

    if escolha == "3":
        listContacts(contacts)
        contactIndex = int(input("\nDigite o número do contato que deseja editar: "))
        print("\nO que você deseja editar?\nDigite 1 para o nome\nDigite 2 para o telefone\nDigite 3 para o email\n")
        whatToChange = int(input("Digite sua opção: "))
        newInfo = input("Digite o novo valor para trocar: ")
        editContact(contacts, contactIndex, whatToChange, newInfo)

    if escolha == "4":
        listContacts(contacts)
        contactIndex = int(input("\nDigite o número do contato que deseja favoritar/desfavoritar: "))
        starContactOrUnstarContact(contacts, contactIndex)

    if escolha == "5":
        starredContactsList(contacts)

    if escolha == "6":
        listContacts(contacts)
        contactIndex = int(input("\nDigite o número do contato que deseja deletar: "))
        deleteContact(contacts, contactIndex)
    
    if escolha == "7":
        break