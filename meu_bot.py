# Importar pacotes necessarios
from time import sleep
from whatsapp_api import WhatsApp
import os.path
from os import path
import os

# Inicializar o whatsapp
wp = WhatsApp()

# Esperar que enter seja pressionado
#input("Pressione enter apos escanear o QR Code")
wp.espera_abrir_whatsapp()
# Lista de nomes ou nomeros de telefone a serem pesquisados
# IMPORTANTE: O nome deve ser nao ambiguo pois ele retornara o primeiro resultado



def ExecutaEnvios():  

    
    while True:
    
    
        if path.exists("enviar_mensagens.txt"):
        
            
            arq_pause = open('pause.txt', 'w+')
            arq_pause.close()
            
            
            f = open('enviar_mensagens.txt', 'r', encoding = 'utf8')
            linha = f.readline()
            
            while (len(linha.rstrip('\n')) > 1) :
                splitando = linha.split("|")
                wp.search_contact(splitando[0])
                
                wp.send_message(splitando[1])
                
                linha = f.readline()
                print(linha)
                            
            f.close()
            
            
            os.remove('pause.txt')
            
            sleep(2)
            
            # Mensagem a ser enviada
            
            
        
        sleep(2)

ExecutaEnvios()
# wp.driver.close()