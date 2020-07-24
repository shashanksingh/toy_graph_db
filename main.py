# https://levelup.gitconnected.com/understanding-grpc-a-practical-application-in-go-and-python-f3003c9158ef

# imports for functionality
from src.generated.query_servicer_pb2 import ToyGraphDBResponse, status
from src.undirected import Undirected
from src.dag import Dag
from src.grid import Grid
from src.graph import Graph
from src.tree import Tree

# for fun
import emoji

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


class ToyGraphDBServicerProxy(ToyGraphDBServicer):
    def __init__(self):
        pass

    def ping(self, request, context):
        return "pong"

    def read_graph(self, request, context):
        pass

    def create_graph(self, request, context):
        type_of_graph = request.type
        response = ToyGraphDBResponse()
        print(request, context)
        try:
            # can be better
            graph = (
                Grid(request.grid.data)
                if type_of_graph == query__servicer__pb2.type_of_graphs.GRID
                else None
            )
            graph = (
                Dag(request.grid.data)
                if type_of_graph == query__servicer__pb2.type_of_graphs.DAG
                else None
            )
        except ValueError as e:
            response.status.status = query__servicer__pb2.status.SOMETHING_WENT_WRONG
            response.status.status = query__servicer__pb2.status.ALL_GOOD

        return response

    def call_functionality_in_graph(self, request, context):
        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ToyGraphDBServicer_to_server(ToyGraphDBServicerProxy(), server)
    server.add_insecure_port(f"[::]:{PORT_EXPOSED}")
    print(emoji.emojize(f"All systems go :rocket:"))
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    print(emoji.emojize(f"Running on port {PORT_EXPOSED} :thumbs_up:"))
    serve()
