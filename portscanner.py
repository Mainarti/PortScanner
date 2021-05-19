#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Limpa a tela
# subprocess.call('clear', shell=True)

# Pergunta pela entrada
remoteServer = input ("https://www.google.com.br")
remoteServerIP  = socket.gethostbyname(remoteServer)

# imprime um banner da hora com informação de qual host vc ta scaneando
print ("-") * 60
print ("Porfavor espere, escaneando host remoto:"), remoteServerIP
print ("-") * 60

# da um check pra ver o tempo inicial
t1 = datetime.now()

# Usando o escopo da função para especificar portas (vai escanear aqui entre 1 e 1024)
# Try pra pegar alguns erros

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open").format(port)
        sock.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

# Checandoo tempo novamente
t2 = datetime.now()

# Calculando a diferença de tempo, para ver o quanto vai levar pra rodar o script
total =  t2 - t1

# Imprimindo a informação na tela
print ('Scanning Completed in: '), total