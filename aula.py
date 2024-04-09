senha = input("Digite a senha:")

if len(senha) < 8:
    print("Senha inválida!")
else:
    #Verificar se a senha contém pelo menos uma letra maiúscula
    tem_letra_