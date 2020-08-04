# https://levelup.gitconnected.com/understanding-grpc-a-practical-application-in-go-and-python-f3003c9158ef

# imports for functionality
from src.undirected import Undirected
from src.dag import Dag
from src.grid import Grid
from src.graph import Graph
from src.tree import Tree

# for fun
import emoji

# imports for the server
import grpc
from src.generated.query_servicer_pb2 import ToyGraphDBResponse, Pong, Status, Success
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
        return Pong(message="ALl hail GRPC")

    def read_graph(self, request, context):
        pass

    def create_graph(self, request, context):
        type_of_graph = request.type
        response = None
        print(request.type)
        try:
            # can be better
            graph = (
                Grid(request.grid.data)
                if type_of_graph == query__servicer__pb2.Type_of_graphs.GRID
                else None
            )
            graph = (
                Dag(request.grid.data)
                if type_of_graph == query__servicer__pb2.Type_of_graphs.DAG
                else None
            )
            graph = (
                Undirected(request.grid.data)
                if type_of_graph == query__servicer__pb2.Type_of_graphs.UNDIRECTED
                else None
            )
            response = ToyGraphDBResponse(
                status=None,
                error_message=None,
                success_message=Success(
                    code_number=query__servicer__pb2.Success.Code.ALL_GOOD,
                    message="yay",
                ),
            )

        except ValueError as e:
            response = ToyGraphDBResponse(
                status=None, error_message=None, success_message=None,
            )
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
