import paho.mqtt.client as mqtt
# import random

mqttc = mqtt.Client()


# x = random.random()

# print(x)
# mqttc.loop_start()

mqttc.connect("broker.emqx.io", 1883)
mqttc.publish("teste/temperatura", "20")
mqttc.loop_forever()



