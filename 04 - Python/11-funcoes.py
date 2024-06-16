# Criando funções

def saudacao():
    print('Seja bem-vindo!')

saudacao()

# Função com parâmetro

def nova_saudacao(nome):
    print(f'Seja bem-vindo, {nome}!')

nova_saudacao('Matheus')

def saudacao_jedi(nome, curso):
    print(f'Seja bem-vindo, {nome}!')
    print(f'Novo aluno do curso: {curso}!')

saudacao_jedi('Matheus', 'Jedi')

#função com parâmetro default

def saudacao_xmen(nome, curso = 'X-Men' ):
    print(f'Seja bem-vindo, {nome}!')
    print(f'Novo aluno do curso: {curso}!')

saudacao_xmen('Matheus')

# Funçao com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(4, 6)

print( 'O resultado da soma é: ', resultado)