#!/usr/bin/python

from mininet.wifi.net import Mininet_wifi
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mininet.wifi.node import UserAP
from mininet.wifi.cli import CLI_wifi

def topology():
	net = Mininet_wifi (controller=Controller, accessPoint=UserAP, disableAutoAssociation=True)

	# Access Point sala de sistemas
	ap1 = net.addAccessPoint('ap1',ssid="Estudiantes,Docentes", mode='g', channel='11', mac='e0:10:7f:af:b7:a8', range=20, position="15,30,0")
	# Access Point Segundo piso de biblioteca
	ap2 = net.addAccessPoint('ap2',ssid="Estudiantes,Docentes", mode='g', channel='6', mac='f0:b0:52:7a:31:19', range=20,position="30,40,0")
	# Access Point restante (no encontrado)
	ap3 = net.addAccessPoint('ap3',ssid="Estudiantes,Docentes", mode='g', channel='1', mac='2c:5d:93:bd:83:5c',range=20,position="50,50,0")

	sta1 = net.addStation('sta1', mac="00:00:00:00:00:02", ip="10.0.0.2/8", position="10,20,0", range=20)


	#Controlador
	c1 = net.addController('c1', controller=Controller)

	net.propagationModel(model="logDistancePropagationLossModel", exp=3.5)

	info("*** Configuring wifi nodes \n")
	net.configureWifiNodes()

	#Enlaces
	net.addLink(ap1,ap2, link="wired")
	net.addLink(ap2,ap3, link="wired")
	#net.addLink(sta1, ap1)

	
	net.plotGraph(max_x=100, max_y=100)

	info(" *** Starting network *** \n")
	net.build()
	c1.start()
	ap1.start([c1])
	ap2.start([c1])
	ap3.start([c1])


	info("*** CLI *** \n")
	CLI_wifi(net)

	info("*** Stopping network \n")
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	topology()
