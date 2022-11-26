from http import client
import paho.mqtt.client as mqtt



def on_connect(client,userdata,flags,rc):
      print('connectado(%s)'% client._client_id)
      client.subscribe(topic='prueba', qos=2)

def on_message(client,userdata,message):
      print('-----------------')
      print('Topico: %s'% message.topic)
      print('Mensaje: %s'% message.payload)
      print('qos: %d'% message.qos)



client=mqtt.Client(client_id="Henry",clean_session=False)
client.on_connect=on_connect
client.on_message=on_message
client.connect(host='192.168.10.1',port=1883)
client.loop_forever()


