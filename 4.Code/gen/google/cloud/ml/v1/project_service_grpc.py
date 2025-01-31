# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/ml/v1/project_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.cloud.ml.v1.project_service_pb2


class ProjectManagementServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetConfig(self, stream: 'grpclib.server.Stream[google.cloud.ml.v1.project_service_pb2.GetConfigRequest, google.cloud.ml.v1.project_service_pb2.GetConfigResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.ml.v1.ProjectManagementService/GetConfig': grpclib.const.Handler(
                self.GetConfig,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.ml.v1.project_service_pb2.GetConfigRequest,
                google.cloud.ml.v1.project_service_pb2.GetConfigResponse,
            ),
        }


class ProjectManagementServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetConfig = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.ml.v1.ProjectManagementService/GetConfig',
            google.cloud.ml.v1.project_service_pb2.GetConfigRequest,
            google.cloud.ml.v1.project_service_pb2.GetConfigResponse,
        )
