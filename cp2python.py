#Armazenar o rm, nome e curso de 5 alunos. Consistir as entradas no sentido de obrigar a digitação de rm e nome
#O curso é opcional. Após a digitação, exibir os dados (nome, rm e curso) de todos os alunos.

rm = []
nome = []
curso = []

for i in range(0,5,1):
    rmnum=int(input("Insira o rm do aluno: "))
    rm.append(rmnum)
    
    nomeid = input("Insira o nome do aluno: ")
    nome.append(nomeid)

    statuscurso = input("Este aluno esta matriculado? (s/n)")
    if(statuscurso == 's'):
        cursoid=input("Insira o nome do curso que o aluno esta matriculado: ")
        curso.append(cursoid)
    else: 
        cursoidnegativo = ('Sem curso')
        curso.append(cursoidnegativo)

    print("______________________________________________________")


for i in range(0,5,1):
    print(f"Rm: {rm[i]} \nNome: {nome[i]} \nCurso: {curso[i]} ")
    print('')
