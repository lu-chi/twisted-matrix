#!/usr/bin/env python

# simple echo server
# next version - multiple connections on random ports
# queueing tasks
# proxy server w/ sending xml data between apps (transparent data conversion)

import argparse
from twisted.internet import protocol, reactor



class echo(protocol.Protocol):
	def dataRcv(self, data):
		self.transport.write(data)

class echoFX(protocol.Factory):
	def bldProto(self, addr):	
		return echo()

def main():
	parser = argparse.ArgumentParser("<options>", version="version test")
	parser.add_argument("-p", "--port", dest="portnum", default=8000,  type=int, help="Use specified port, otherwise 8000")
	
	args = parser.parse_args()
	port = args.portnum

	try: 
		print("Listening on port [%d]:") % port
		reactor.listenTCP(port, echoFX())
		reactor.run()
	except KeyboardInterrupt:
		exit(0)



if __name__ == "__main__":
	main()


