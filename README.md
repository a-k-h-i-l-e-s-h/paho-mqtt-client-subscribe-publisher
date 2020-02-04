# paho-mqtt-client-subscribe-publisher

Please find below steps to install mqtt 

### Step:1
#### Ubuntu:

As of version 11.10 Oneiric Ocelot, mosquitto will be in the Ubuntu repositories so you can install as with any other package. If you are on an earlier version of Ubuntu or want a more recent version of mosquitto, add the mosquitto-dev PPA to your repositories list – see the link for details. mosquitto can then be installed from your package manager.

$ sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
$ sudo apt-get update
If the command “apt-add-repository” is not recognised, it can be installed with:

$ sudo apt-get install python-software-properties
Then mosquitto can be installed with:

$ sudo apt-get install mosquitto

For more please check below urls:
https://mosquitto.org/download/
https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-ubuntu-16-04

Log in to your server a second time, so you have two terminals side-by-side. In the new terminal, use mosquitto_sub to subscribe to the test topic:

$ mosquitto_sub -h localhost -t test

-h is used to specify the hostname of the MQTT server, and -t is the topic name. You’ll see no output after hitting ENTER because mosquitto_sub is waiting for messages to arrive. Switch back to your other terminal and publish a message:

$ mosquitto_pub -h localhost -t test -m "hello world"

The options for mosquitto_pub are the same as mosquitto_sub, though this time we use the additional -m option to specify our message. Hit ENTER, and you should see hello world pop up in the other terminal. You’ve sent your first MQTT message!

### Step:2

To install poho for python:
https://pypi.org/project/paho-mqtt/
$ pip install paho-mqtt


### Step:3: 
##### "client.connect("10.94.107.34""....)
Note: Change Ip address from below file and then Run.
To check you ip type: ipconfig or ifconfig

Then run these file to test
#### mqttpublish.py to publish the data
#### mqttsuscribr.py to suscribe the data
$ python3 mqttpublish.py
$ python3 mqttsuscribr.py




