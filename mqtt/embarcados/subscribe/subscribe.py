import paho.mqtt.client as mqtt
from struct import unpack
from time import sleep

import sys
sys.path.insert(0, "..")
import time
from random import randint
from opcua import ua, Server
 
# assinando todas as publicações dentro da area 10
TOPIC = "teste"
 
# função chamada quando a conexão for realizada, sendo
# então realizada a subscrição
def on_connect(client, data, rc,flag):
    client.subscribe([(TOPIC,0)])
 
# função chamada quando uma nova mensagem do tópico é gerada
def on_message(client, userdata, msg):
    # decodificando o valor recebido
    # v = unpack(">H",msg.payload)[0]
    # print (msg.topic + "/ number = " + str(v))
    print(str(msg.payload))
    print(int(msg.payload)+10)
    # opc_ua()
    # print(int(v) + 10)

server = Server()
idx = server.register_namespace("opc.tcp://0.0.0.0:4842/freeopcua/server/")
server.set_endpoint("opc.tcp://0.0.0.0:4842/freeopcua/server/")

# def opc_ua():
#     if __name__ == "__main__":
#         print("entrou no loop opc-ua")
#         server.start()
        # server.finish()
 
# clia um cliente para supervisã0
client = mqtt.Client(client_id = 'SCADA',
                     protocol = mqtt.MQTTv31)
# estabelece as funçõe de conexão e mensagens
client.on_connect = on_connect
client.on_message = on_message
 
# conecta no broker
client.connect("127.0.0.1", 1883)
 
# permace em loop, recebendo mensagens
client.loop_forever()


# if __name__ == "__main__":

#     server = Server()
#     idx = server.register_namespace("opc.tcp://0.0.0.0:4841/freeopcua/server/")
#     server.set_endpoint("opc.tcp://0.0.0.0:4841/freeopcua/server/")
#     server.start()