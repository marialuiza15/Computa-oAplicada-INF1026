# Exercício Fácil: Criando um Dicionário de Contatos

# Enunciado:
# Crie um dicionário onde as chaves são os nomes de pessoas e os valores são seus números de telefone.
# Adicione pelo menos três contatos e depois imprima o número de telefone de uma pessoa específica.

# Exemplo:

# # Dicionário de contatos
# contatos = {
#     "João": "1234-5678",
#     "Maria": "9876-5432",
#     "Carlos": "5555-6666"
# }

# # Acessando o número de telefone de Maria
# print(contatos["Maria"])

def agenda(contatos, acesso):
    for contato in contatos:
        if contato==acesso:
            print(contato)
            return contatos[acesso]
        
contatos = {
    "João": "1234-5678",
    "Maria": "9876-5432",
    "Carlos": "5555-6666"
}

print(agenda(contatos, "Maria"))