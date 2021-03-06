'''
    /------------------------------------------------------------------------------------------------------------------/
    FALTA
    /------------------------------------------------------------------------------------------------------------------/
        - Criar thread para ficar enviando as informações da máquina
        - Criar thread para receber os trabalhos vindo doo servidor
    /------------------------------------------------------------------------------------------------------------------/
    FUNÇÃO
    /------------------------------------------------------------------------------------------------------------------/
    Arquivo que inicializa todas as atividades do cliente. Ao iniciar o funcionamento, ela cria uma thread para ficar
    enviando as informações de uso do processador e da memória RAM para o servidor e outra thread é iniciada para ficar
    aguardando o recebimento de tarefas para serem realizadas
    /------------------------------------------------------------------------------------------------------------------/
'''
import socket, time
from comunicacao.shared.statusPC import status
from comunicacao.client.receberTarefa import receberTarefa
import _pickle as cPickle

HOST = '10.180.41.77'     # Endereco IP do Servidor
PORT = 8002              # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
msg = "123456"
msgS = cPickle.dumps(msg)
tcp.send(msgS)
receber = receberTarefa(tcp)
receber.start()
while True:
    try:
        msg = status()
        msgS = cPickle.dumps(msg)
        tcp.send(msgS)
        time.sleep(1)
    except:
        print("Conexão com o servidor Finalizada!")
        break
tcp.close()