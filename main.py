# https://levelup.gitconnected.com/understanding-grpc-a-practical-application-in-go-and-python-f3003c9158ef

# imports for functionality
from src.undirected import Undirected
from src.dag import Dag
from src.grid import Grid
from src.graph import Graph
from src.tree import Tree

# imports for the server
import grpc
from src.generated.query_servicer_pb2_grpc import ToyGraphDBServicer, add_ToyGraphDBServicer_to_server
import logging
from concurrent import futures

PORT_EXPOSED = 8080


class ToyGraphDBServicer(ToyGraphDBServicer):
    def __init__(self):
        pass

    def create_graph(self):
        pass

    def read_graph(self):
        pass

    def call_functionality_in_graph(self):
        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ToyGraphDBServicer_to_server(ToyGraphDBServicer(), server)
    server.add_insecure_port(f'[::]:{PORT_EXPOSED}')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    logger = logging.getLogger('ToyGraphDB')
    print(f"Let there be light at PORT {PORT_EXPOSED}")
    serve()
