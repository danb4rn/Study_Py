import random, string


lengh = int(input("Digite o tamanho de senha desejado: "))

chars = string.ascii_letters + string.digits + " !@#$%*()_+=-.,;]/["

rnd = random.SystemRandom()
print("" .join(rnd.choice(chars)for i in range(lengh)))