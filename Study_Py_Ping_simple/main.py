import os  # importa o modulo ou biblioteca

print("#" * 60)
ip_host = input("Digite o IP ou HOST para verificação: ")
os.system('ping -c 6 {}'.format(ip_host))
print("#" * 60)
