import paho.mqtt.client as mqtt
import random

mqttc = mqtt.Client()


x = random.random()

print(x)
mqttc.connect("test.mosquitto.org", 1883)
mqttc.loop_start()
# mqttc.publish("teste/temperatura", x)
mqttc.loop(2000)
mqttc.loop_forever()



