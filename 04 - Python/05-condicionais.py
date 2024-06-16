"""
Interessante
"""

media = float(input('Informe a média do estudante: '))
presenca = int(input('Informe a presença do estudante: '))
if media >= 7 and presenca >= 70:
    print('Você foi aprovado!')
elif media >=5:
    print('Recuperação')
else:
    print('Você foi reprovado.')