# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import query_servicer_pb2 as query__servicer__pb2


class ToyGraphDBStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ping = channel.unary_unary(
                '/ToyGraphDB/ping',
                request_serializer=query__servicer__pb2.Empty.SerializeToString,
                response_deserializer=query__servicer__pb2.Pong.FromString,
                )
        self.read_graph = channel.unary_unary(
                '/ToyGraphDB/read_graph',
                request_serializer=query__servicer__pb2.ToyGraphDBRequest.SerializeToString,
                response_deserializer=query__servicer__pb2.ToyGraphDBResponse.FromString,
                )
        self.create_graph = channel.unary_unary(
                '/ToyGraphDB/create_graph',
                request_serializer=query__servicer__pb2.ToyGraphDBRequest.SerializeToString,
                response_deserializer=query__servicer__pb2.ToyGraphDBResponse.FromString,
                )
        self.call_functionality_in_graph = channel.unary_unary(
                '/ToyGraphDB/call_functionality_in_graph',
                request_serializer=query__servicer__pb2.ToyGraphDBRequest.SerializeToString,
                response_deserializer=query__servicer__pb2.ToyGraphDBResponse.FromString,
                )


class ToyGraphDBServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def read_graph(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_graph(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def call_functionality_in_graph(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ToyGraphDBServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ping': grpc.unary_unary_rpc_method_handler(
                    servicer.ping,
                    request_deserializer=query__servicer__pb2.Empty.FromString,
                    response_serializer=query__servicer__pb2.Pong.SerializeToString,
            ),
            'read_graph': grpc.unary_unary_rpc_method_handler(
                    servicer.read_graph,
                    request_deserializer=query__servicer__pb2.ToyGraphDBRequest.FromString,
                    response_serializer=query__servicer__pb2.ToyGraphDBResponse.SerializeToString,
            ),
            'create_graph': grpc.unary_unary_rpc_method_handler(
                    servicer.create_graph,
                    request_deserializer=query__servicer__pb2.ToyGraphDBRequest.FromString,
                    response_serializer=query__servicer__pb2.ToyGraphDBResponse.SerializeToString,
            ),
            'call_functionality_in_graph': grpc.unary_unary_rpc_method_handler(
                    servicer.call_functionality_in_graph,
                    request_deserializer=query__servicer__pb2.ToyGraphDBRequest.FromString,
                    response_serializer=query__servicer__pb2.ToyGraphDBResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ToyGraphDB', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ToyGraphDB(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ToyGraphDB/ping',
            query__servicer__pb2.Empty.SerializeToString,
            query__servicer__pb2.Pong.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def read_graph(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ToyGraphDB/read_graph',
            query__servicer__pb2.ToyGraphDBRequest.SerializeToString,
            query__servicer__pb2.ToyGraphDBResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def create_graph(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ToyGraphDB/create_graph',
            query__servicer__pb2.ToyGraphDBRequest.SerializeToString,
            query__servicer__pb2.ToyGraphDBResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def call_functionality_in_graph(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ToyGraphDB/call_functionality_in_graph',
            query__servicer__pb2.ToyGraphDBRequest.SerializeToString,
            query__servicer__pb2.ToyGraphDBResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
