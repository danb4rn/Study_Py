
import os
import time

with open('Hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print("Verificando ip")
        print("#" * 60)
        os.system("ping -c 6 {}".format(ip))
        print("#" * 60)
        time.sleep(5)