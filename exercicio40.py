'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''

nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
média = (nota1 + nota2) / 2
print('A primeira nota foi {:.1f} e a segunda foi {:.1f},  com isso a média é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em Recuperação!')
elif média < 5:
    print('O aluno está Reprovado!')
elif média >= 7:
    print('O aluno está Aprovado!')

