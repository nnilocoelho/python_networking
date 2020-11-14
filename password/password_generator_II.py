#random módulo para gerar numeros pseudoaleatorios.

import random

lower = "abcdefghijklmnopqrstuvxyz" #lowwer: letras minusculas
upper = "ABCDEFGHIJKLMNOPQRSTUVXYZ" #upper: letras maisculoas
numbers = "0123456789"              #numeros  
symbols = "[]{}*;/,._@#-+-&%^~"     #caracteres

all = lower + upper + numbers + symbols #junção das variaveis para criação da senha

length = 16 #tamanho da senha
password = "".join(random.sample(all,length)) #geracao da senha
print(password)   #comando de saida, informa a senha gerada.

