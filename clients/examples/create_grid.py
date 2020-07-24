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

# open a gRPC channel
channel = grpc.insecure_channel(f"localhost:{PORT_EXPOSED}")

# create a stub (client)
stub = query_servicer_pb2_grpc.ToyGraphDBStub(channel)


# request_data = query_servicer_pb2.list_of_list_of_integer()
# request_list = query_servicer_pb2.list_of_integer()
# # request_list.list_of_integer.data.append(2)
# print(request_list)
# request_data.data
# create a valid request message

# make the call
response = stub.ping(Empty())
print(response)

type_of_graph = Type_of_graphs(type=)  # query_servicer_pb2.Type_of_graphs.GRID
grid_request_object = grid(data=query_servicer_pb2.List_of_list_of_integer(data=None))

request = ToyGraphDBRequest(type=type_of_graph, grid=grid_request_object)
response = stub.create_graph(request)
print(response)
