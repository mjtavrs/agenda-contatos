def addContact(contacts, name, phone, email):
    contact = {"name": name, "phone": phone, "email": email, "starred": False}
    contacts.append(contact)
    print(f"\n{name} foi adicionado a sua lista de contatos")
    return

def listContacts(contacts):
    print("\nLista de contatos:")
    for index, contact in enumerate(contacts, start=1):
        isStarred = "★" if contact["starred"] else " "
        contactName = contact["name"]
        contactPhone = contact["phone"]
        contactEmail = contact["email"]
        print(f"{index}. [{isStarred}] {contactName} | {contactPhone} | {contactEmail}")
    return

def editContact(contacts, contactIndex, whatToChange, newInfo):
    adjustedContactIndex = contactIndex - 1
    if adjustedContactIndex >= 0 and adjustedContactIndex < len(contacts):
        if whatToChange == 1:
            contacts[adjustedContactIndex]["name"] = newInfo
            print(f"\nNome do contato trocado para {newInfo}.")
        elif whatToChange == 2:
            contacts[adjustedContactIndex]["phone"] = newInfo
            print(f"\nTelefone do contato trocado para {newInfo}.")
        else:
            contacts[adjustedContactIndex]["email"] = newInfo
            print(f"\nEmail do contato trocado para {newInfo}.")
    return

def starContactOrUnstarContact(contacts, contactIndex):
    adjustedContactIndex = contactIndex - 1
    if adjustedContactIndex >= 0 and adjustedContactIndex < len(contacts):
        contactName = contacts[adjustedContactIndex]["name"]
        if contacts[adjustedContactIndex]["starred"]:
            contacts[adjustedContactIndex]["starred"] = False
            print(f"\nContato {contactName} desfavoritado com sucesso!")
        else:
            contacts[adjustedContactIndex]["starred"] = True
            print(f"\nContato {contactName} favoritado com sucesso!")
    return

def starredContactsList(contacts):
    print("\nLista de contatos favoritos:")
    for index, contact in enumerate(contacts, start=1):
        if contact["starred"]:
            contactName = contact["name"]
            contactPhone = contact["phone"]
            contactEmail = contact["email"]
            print(f"{index}. [★] {contactName} | {contactPhone} | {contactEmail}")
    return

def deleteContact(contacts, contactIndex):
    adjustedContactIndex = contactIndex - 1
    for contact in contacts:
        if adjustedContactIndex == contacts.index(contact):
            contactName = contacts[adjustedContactIndex]["name"]
            contacts.remove(contact)
            print(f"\nContato {contactName} removido da sua lista de contatos.")
    return