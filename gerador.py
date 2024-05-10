import random
import string

char_lenght = int(input('insira o tamanho da senha: '))
punctuation = str(input("deseja que sua senha tenha caracteres especiais. 's' para sim, 'n' para não: "))

def gerar_senha(comprimento):
    while True:
        if punctuation == 's':
            caracteres = string.ascii_letters + string.digits + string.punctuation
            senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
            return senha
        elif punctuation == 'n': 
            caracteres = string.ascii_letters + string.digits
            senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
            return senha
        else:
            print('opção inválida')
            break
            
        
    

# Exemplo de uso: gerar senha com comprimento 12
senha_gerada = gerar_senha(char_lenght)

print("Senha gerada:", senha_gerada)