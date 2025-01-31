# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/api/servicecontrol/v1/service_controller.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.api.servicecontrol.v1.check_error_pb2
import google.api.servicecontrol.v1.operation_pb2
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import google.api.servicecontrol.v1.service_controller_pb2


class ServiceControllerBase(abc.ABC):

    @abc.abstractmethod
    async def Check(self, stream: 'grpclib.server.Stream[google.api.servicecontrol.v1.service_controller_pb2.CheckRequest, google.api.servicecontrol.v1.service_controller_pb2.CheckResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Report(self, stream: 'grpclib.server.Stream[google.api.servicecontrol.v1.service_controller_pb2.ReportRequest, google.api.servicecontrol.v1.service_controller_pb2.ReportResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.api.servicecontrol.v1.ServiceController/Check': grpclib.const.Handler(
                self.Check,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.api.servicecontrol.v1.service_controller_pb2.CheckRequest,
                google.api.servicecontrol.v1.service_controller_pb2.CheckResponse,
            ),
            '/google.api.servicecontrol.v1.ServiceController/Report': grpclib.const.Handler(
                self.Report,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.api.servicecontrol.v1.service_controller_pb2.ReportRequest,
                google.api.servicecontrol.v1.service_controller_pb2.ReportResponse,
            ),
        }


class ServiceControllerStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Check = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.api.servicecontrol.v1.ServiceController/Check',
            google.api.servicecontrol.v1.service_controller_pb2.CheckRequest,
            google.api.servicecontrol.v1.service_controller_pb2.CheckResponse,
        )
        self.Report = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.api.servicecontrol.v1.ServiceController/Report',
            google.api.servicecontrol.v1.service_controller_pb2.ReportRequest,
            google.api.servicecontrol.v1.service_controller_pb2.ReportResponse,
        )
