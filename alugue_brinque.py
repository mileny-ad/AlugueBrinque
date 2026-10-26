
print("LOCADORA DE BRINQUEDOS")
print("----------------")
print("Bam-vindo ao sistema!")
brinquedos = [
    {"codigo": "B001", "nome": "Banco Imobiliário", "valor": 50.00},
    {"codigo": "B002", "nome": "Jogo da Vida", "valor": 50.00},
    {"codigo": "B003", "nome": "Detetive", "valor": 50.00},
    {"codigo": "B004", "nome": "War", "valor": 50.00},
    {"codigo": "B005", "nome": "Dama e Xadrez", "valor": 50.00},
    {"codigo": "B006", "nome": "Imagem e Ação", "valor": 50.00},
    {"codigo": "B007", "nome": "Twister", "valor": 50.00},
    {"codigo": "B008", "nome": "Batalha Naval", "valor": 50.00}
]

alugueis=[]

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Cadastrar brinquedo")
    print("2 - Listar brinquedos")
    print("3 - Registrar aluguel")
    print("4 - Registrar devolução")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = input("Digite o código do brinquedo: ")
        nome = input("Digite o nome do brinquedo: ")
        brinquedos.append({
            "codigo": codigo,
            "nome": nome,
            "valor": 50.00
        })
        print("Brinquedo cadastrado com sucesso!")

    elif opcao == "2":
        print("\n--- BRINQUEDOS CADASTRADOS ---")
        for brinquedo in brinquedos:
            print(
                brinquedo["codigo"],
                "-",
                brinquedo["nome"],
                "- R$",
                f'{brinquedo["valor"]:.2f}'
            )

    elif opcao == "3":
        print("\n--- REGISTRAR ALUGUEL ---")
        cliente = input("Nome do cliente: ")
        telefone = input("Telefone do cliente: ")
        codigo = input("Código do brinquedo: ")
        alugueis.append({
            "cliente": cliente,
            "telefone": telefone,
            "codigo": codigo,
            "devolvido":False  
        }) 

        encontrado = False
        for brinquedo in brinquedos:
            if brinquedo["codigo"] == codigo:
                encontrado = True
                print("Brinquedo:", brinquedo["nome"])
                print("Valor do aluguel: R$ 50,00")
                print("Retirada: sexta-feira")
                print("Devolução prevista: segunda-feira")
                print("Aluguel registrado com sucesso!")
                break
        if not encontrado:
                print("Código de brinquedo não encontrado")
    elif opcao == "4":
            print("\n--- Registrar Devolução ---")
            cliente = input("Nome do cliente: ")
            codigo = input("código do brinquedo: ")
            encontrado = False
            for aluguel in alugueis:
                 if aluguel["cliente"] == cliente and aluguel["codigo"] == codigo:
                      encontrado = True
                      break 
            if not encontrado:
                 print("Aluguel não encontrado para esse cliente e brinquedo")
                 continue
            else:
                atraso = int(input("Quantos dias de atraso?"))
                pecas_faltando = int(input("Quantas peças estão faltando? "))
                danificado = input(" O brinquedo está danificado? (s/n):").lower()
                multa_atraso = atraso * 5
                multa_pecas = pecas_faltando * 15
                multa_dano = 25 if danificado == "s" else 0
                total_multas = multa_atraso + multa_pecas + multa_dano
                aluguel["devolvido"] = True
                print("Devolução registrada com sucesso")
                print("Multa por atraso: R$", multa_atraso)
                print("Multa por peças faltando: R$", multa_pecas)
                print("Multa por dano: R$", multa_dano)
                print("Total de multas: R$", total_multas)

    elif opcao == "5":
        print("Obrigado por utilizar o Alugue Brinque!")
        break

    else:
        print("Opção inválida. Tente novamente.")