import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
# def on_connect(client, userdata, rc):
    # print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$test/#")

# The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
#client.on_connect = on_connect
#client.on_message = on_message

client.connect("10.94.107.34", 1883, 60)
print("Publishing Message")
client.publish("$test/temp","567")
print("Message Published")
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
# client.loop_forever()



