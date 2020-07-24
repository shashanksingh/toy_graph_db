import grpc
from src.generated import query_servicer_pb2, query_servicer_pb2_grpc

PORT_EXPOSED = 9090
SAMPLE_GRID = [[0, 1, 1], [0, 1, 1], [0, 1, 1]]

# open a gRPC channel
channel = grpc.insecure_channel(f"localhost:{PORT_EXPOSED}")

# create a stub (client)
stub = query_servicer_pb2_grpc.ToyGraphDBStub(channel)

# create a valid request message
grid = query_servicer_pb2.list_of_list_of_integer(data=SAMPLE_GRID)

print(grid)
# make the call
response = stub.create_graph(grid)

print(response)
