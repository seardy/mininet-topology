#!/usr/bin/python

from mininet.wifi.net import Mininet_wifi
from mininet.node import Controller
from mininet.log import setLogLevel, info
from mininet.wifi.node import UserAP
from mininet.wifi.cli import CLI_wifi

def topology():
	
	# Creating network
	net = Mininet_wifi (
			controller=Controller, 
			accessPoint=UserAP, 
			disableAutoAssociation=True)

	# Access Point -> Facultad de la salud (Acreditacion)
	ap1 = net.addAccessPoint('ap1',
		ssid="Estudiantes,Docentes,Administrativo",
		mode='g', channel='6', mac='e0:10:7f:2f:ef:48', range=20 , position="40.8854,29.1667,0")
	
	# Access Point -> Facultad de la salud (Sala de computo)
	ap2 = net.addAccessPoint('ap2',
		ssid="Estudiantes,Docentes,Administrativo",
		mode='g', channel='11', mac='58:93:96:25:1c:10', range=20, position="68.4896,52.3437,0")
	
	# Access Point -> Facultad de la salud (Maestria_temp)
	ap3 = net.addAccessPoint('ap3',
		ssid="Estudiantes,Docentes,Administrativo",
		 mode='g', channel='1', mac='2c:e6:cc:1f:76:50', range=20, position="47.9167,66.6667,0")


	# Station -> Station 1

	sta1 = net.addStation('sta1', mac="00:00:00:00:00:02",
		 ip="10.0.0.2/8", position="24.7396,41.1458,0", range=20)


	# Adding Controller to Network
	c1 = net.addController('c1', controller=Controller)

	# Establishing Propagation Model for network
	net.propagationModel(model="logDistancePropagationLossModel", exp=3.5)


	info("*** Configuring wifi nodes \n")
	net.configureWifiNodes()

	# Adding links between APs
	net.addLink(ap1,ap2, link="wired")
	net.addLink(ap2,ap3, link="wired")
	
	net.plotGraph(max_x=100, max_y=100)

	info(" *** Starting network *** \n")
	# Initialize network
	net.build()

	# Starting up Controller
	c1.start()

	# Starting up APs
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
