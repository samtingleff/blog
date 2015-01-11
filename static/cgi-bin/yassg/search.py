from tservices import *
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

class SearchClient(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def query(self, q):
        return self.client.search(q, 10, None)

    def connect(self):
        self.transport = TSocket.TSocket(self.host, self.port)
        self.transport = TTransport.TBufferedTransport(self.transport)
        protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self.client = TSearchService.Client(protocol)
        self.transport.open()

    def close(self):
        self.transport.close()
