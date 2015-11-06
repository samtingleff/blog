from tservices import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

class LikesClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def count(self, device, page):
        return self.client.count(device, page)

    def connect(self):
        self.transport = TSocket.TSocket(self.host, self.port)
        self.transport = TTransport.TBufferedTransport(self.transport)
        protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self.client = TLikeService.Client(protocol)
        self.transport.open()

    def close(self):
        self.transport.close()
