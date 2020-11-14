#random módulo para gerar numeros pseudoaleatorios.

import random

lower = "abcdefghijklmnopqrstuvxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
numbers = "0123456789"
symbols = "[]{}*;/,._@#-+-&%^~"

all = lower + upper + numbers + symbols

length = 16
password = "".join(random.sample(all,length))
print(password)

