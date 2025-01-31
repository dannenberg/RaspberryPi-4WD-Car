# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/apigeeconnect/v1/connection.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.cloud.apigeeconnect.v1.connection_pb2


class ConnectionServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ListConnections(self, stream: 'grpclib.server.Stream[google.cloud.apigeeconnect.v1.connection_pb2.ListConnectionsRequest, google.cloud.apigeeconnect.v1.connection_pb2.ListConnectionsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.apigeeconnect.v1.ConnectionService/ListConnections': grpclib.const.Handler(
                self.ListConnections,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.apigeeconnect.v1.connection_pb2.ListConnectionsRequest,
                google.cloud.apigeeconnect.v1.connection_pb2.ListConnectionsResponse,
            ),
        }


class ConnectionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListConnections = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.apigeeconnect.v1.ConnectionService/ListConnections',
            google.cloud.apigeeconnect.v1.connection_pb2.ListConnectionsRequest,
            google.cloud.apigeeconnect.v1.connection_pb2.ListConnectionsResponse,
        )
