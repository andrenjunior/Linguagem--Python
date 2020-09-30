aluno = dict()

aluno['nome'] = str(input('Digite nome: ')) #Digite nome: André
aluno['media'] = float(input('Média: ')) #Média: 9.5

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado' #media é > 7,  9.5

else:
    aluno['situacao'] = 'Reprovado'

for x, y in aluno.items():
    print(f'- {x} é igual a {y}') #media é igual a 9.5
print(aluno.keys())  #dict_keys(['nome', 'media', 'situacao'])
print(aluno.values())  #dict_values(['André', 9.5, 'Aprovado'])  



