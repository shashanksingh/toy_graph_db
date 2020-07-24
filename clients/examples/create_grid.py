import grpc
from src.generated import query_servicer_pb2, query_servicer_pb2_grpc
from src.generated.query_servicer_pb2 import (
    Empty,
    ToyGraphDBRequest,
    Type_of_graphs,
    grid,
)

PORT_EXPOSED = 9090
SAMPLE_GRID = [[0, 1, 1], [0, 1, 1], [0, 1, 1]]
DATABASE_NAME = "create_grid"
TABLE_NAME = "simple_grid"

# open a gRPC channel
channel = grpc.insecure_channel(f"localhost:{PORT_EXPOSED}")

# create a stub (client)
stub = query_servicer_pb2_grpc.ToyGraphDBStub(channel)


# make the call
response = stub.ping(Empty())
print(response)

# https://www.freecodecamp.org/news/googles-protocol-buffers-in-python/
# convert sample grid to data
grid_request_object = grid(data=query_servicer_pb2.List_of_list_of_integer(data=None))

request = ToyGraphDBRequest(
    type=query_servicer_pb2.Type_of_graphs.GRID,
    grid=grid_request_object,
    database=DATABASE_NAME,
    table=TABLE_NAME,
)
response = stub.create_graph(request)
print(response)
