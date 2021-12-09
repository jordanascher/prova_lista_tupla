# Dicionário notas de alunos
notas = []

menu = "1 - Cadastrar aluno "
menu += "\n2 - Imprimir"
menu += "\n3 - Deletar"
menu += "\n0 - Encerrar"

opcao = None
while opcao != 0:
    print(menu)
    opcao = int(input("Informe a opção desejada: "))

    if opcao == 1:
        nomeAluno = input("Digite o nome do aluno: ")
        nota01 = float(input("Digite a nota 01: "))
        nota02 = float(input("Digite a nota 02: "))

        aluno = {'nome': nomeAluno, 'nota01': nota01, 'nota02': nota02, 'media': (nota01+nota02)/2}
        notas.append(aluno)
    
    elif opcao == 2:
        for nota in notas:
            print("------------------------------")
            print('Nome do Aluno: ' +nota.get('nome'))
            print('Média: ' +str(nota.get('media')))
            print("------------------------------")
    
    elif opcao == 3:
        i = 0
        for nota in notas:
            print("------------------------------")
            print('Aluno '+str(i)+' :' +nota.get('nome'))
            print('Média: ' +str(nota.get('media')))
            print("------------------------------")
            i += 1
        
        posicaoValida = False
        while posicaoValida == False:
            posicao = int(input("Selecione o aluno que deseja deletar: "))
        
            if posicao >= 0 and posicao <= len(notas):
                posicaoValida = True

                #deleta da lista
                del notas[posicao]           

                for nota in notas:
                    print("------------------------------")
                    print('Aluno: ' +nota.get('nome'))
                    print('Média: ' +str(nota.get('media')))
                    print("------------------------------")
            
            else:
                print("Informe uma posição válida entre 0 e "+str(len(notas)-1))    

    else: 
        print("Programa encerrado")

