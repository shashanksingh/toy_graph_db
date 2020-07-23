# https://levelup.gitconnected.com/understanding-grpc-a-practical-application-in-go-and-python-f3003c9158ef

# imports for functionality
from src.generated.query_servicer_pb2 import ToyGraphDBResponse, status
from src.undirected import Undirected
from src.dag import Dag
from src.grid import Grid
from src.graph import Graph
from src.tree import Tree

# imports for the server
import grpc
from src.generated.query_servicer_pb2_grpc import (
    ToyGraphDBServicer,
    add_ToyGraphDBServicer_to_server,
)
from src.generated import query_servicer_pb2 as query__servicer__pb2

import logging
from concurrent import futures

PORT_EXPOSED = 9090


class ToyGraphDBServicer(ToyGraphDBServicer):
    def __init__(self):
        pass

    def ping(self, request, context):
        return "pong"

    def read_graph(self, request, context):
        pass

    def create_graph(self, request, context):
        type_of_graph = request.type
        if type_of_graph == query__servicer__pb2.type_of_graph.GRID:
            response = ToyGraphDBResponse()
            try:
                graph = Grid(request.grid.data)
            except:
                response.status.status = query__servicer__pb2.status.SOMETHING_WENT_WRONG
            response.status.status  = query__servicer__pb2.status.ALL_GOOD
        elif type_of_graph == type_of_graph.DAG:
            pass

    def call_functionality_in_graph(self, request, context):
        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ToyGraphDBServicer_to_server(ToyGraphDBServicer(), server)
    server.add_insecure_port(f"[::]:{PORT_EXPOSED}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    print(f"Running on port {PORT_EXPOSED}")
    serve()
