# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/gaming/v1/game_server_deployments_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.cloud.gaming.v1.game_server_deployments_pb2
import google.longrunning.operations_pb2
import google.cloud.gaming.v1.game_server_deployments_service_pb2


class GameServerDeploymentsServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ListGameServerDeployments(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_deployments_pb2.ListGameServerDeploymentsRequest, google.cloud.gaming.v1.game_server_deployments_pb2.ListGameServerDeploymentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetGameServerDeployment(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_deployments_pb2.GetGameServerDeploymentRequest, google.cloud.gaming.v1.game_server_deployments_pb2.GameServerDeployment]') -> None:
        pass

    @abc.abstractmethod
    async def CreateGameServerDeployment(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_deployments_pb2.CreateGameServerDeploymentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteGameServerDeployment(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_deployments_pb2.DeleteGameServerDeploymentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateGameServerDeployment(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_deployments_pb2.UpdateGameServerDeploymentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetGameServerDeploymentRollout(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_deployments_pb2.GetGameServerDeploymentRolloutRequest, google.cloud.gaming.v1.game_server_deployments_pb2.GameServerDeploymentRollout]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateGameServerDeploymentRollout(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_deployments_pb2.UpdateGameServerDeploymentRolloutRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def PreviewGameServerDeploymentRollout(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_deployments_pb2.PreviewGameServerDeploymentRolloutRequest, google.cloud.gaming.v1.game_server_deployments_pb2.PreviewGameServerDeploymentRolloutResponse]') -> None:
        pass

    @abc.abstractmethod
    async def FetchDeploymentState(self, stream: 'grpclib.server.Stream[google.cloud.gaming.v1.game_server_deployments_pb2.FetchDeploymentStateRequest, google.cloud.gaming.v1.game_server_deployments_pb2.FetchDeploymentStateResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.gaming.v1.GameServerDeploymentsService/ListGameServerDeployments': grpclib.const.Handler(
                self.ListGameServerDeployments,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_deployments_pb2.ListGameServerDeploymentsRequest,
                google.cloud.gaming.v1.game_server_deployments_pb2.ListGameServerDeploymentsResponse,
            ),
            '/google.cloud.gaming.v1.GameServerDeploymentsService/GetGameServerDeployment': grpclib.const.Handler(
                self.GetGameServerDeployment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_deployments_pb2.GetGameServerDeploymentRequest,
                google.cloud.gaming.v1.game_server_deployments_pb2.GameServerDeployment,
            ),
            '/google.cloud.gaming.v1.GameServerDeploymentsService/CreateGameServerDeployment': grpclib.const.Handler(
                self.CreateGameServerDeployment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_deployments_pb2.CreateGameServerDeploymentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.gaming.v1.GameServerDeploymentsService/DeleteGameServerDeployment': grpclib.const.Handler(
                self.DeleteGameServerDeployment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_deployments_pb2.DeleteGameServerDeploymentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.gaming.v1.GameServerDeploymentsService/UpdateGameServerDeployment': grpclib.const.Handler(
                self.UpdateGameServerDeployment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_deployments_pb2.UpdateGameServerDeploymentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.gaming.v1.GameServerDeploymentsService/GetGameServerDeploymentRollout': grpclib.const.Handler(
                self.GetGameServerDeploymentRollout,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_deployments_pb2.GetGameServerDeploymentRolloutRequest,
                google.cloud.gaming.v1.game_server_deployments_pb2.GameServerDeploymentRollout,
            ),
            '/google.cloud.gaming.v1.GameServerDeploymentsService/UpdateGameServerDeploymentRollout': grpclib.const.Handler(
                self.UpdateGameServerDeploymentRollout,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_deployments_pb2.UpdateGameServerDeploymentRolloutRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.gaming.v1.GameServerDeploymentsService/PreviewGameServerDeploymentRollout': grpclib.const.Handler(
                self.PreviewGameServerDeploymentRollout,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_deployments_pb2.PreviewGameServerDeploymentRolloutRequest,
                google.cloud.gaming.v1.game_server_deployments_pb2.PreviewGameServerDeploymentRolloutResponse,
            ),
            '/google.cloud.gaming.v1.GameServerDeploymentsService/FetchDeploymentState': grpclib.const.Handler(
                self.FetchDeploymentState,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.gaming.v1.game_server_deployments_pb2.FetchDeploymentStateRequest,
                google.cloud.gaming.v1.game_server_deployments_pb2.FetchDeploymentStateResponse,
            ),
        }


class GameServerDeploymentsServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListGameServerDeployments = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerDeploymentsService/ListGameServerDeployments',
            google.cloud.gaming.v1.game_server_deployments_pb2.ListGameServerDeploymentsRequest,
            google.cloud.gaming.v1.game_server_deployments_pb2.ListGameServerDeploymentsResponse,
        )
        self.GetGameServerDeployment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerDeploymentsService/GetGameServerDeployment',
            google.cloud.gaming.v1.game_server_deployments_pb2.GetGameServerDeploymentRequest,
            google.cloud.gaming.v1.game_server_deployments_pb2.GameServerDeployment,
        )
        self.CreateGameServerDeployment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerDeploymentsService/CreateGameServerDeployment',
            google.cloud.gaming.v1.game_server_deployments_pb2.CreateGameServerDeploymentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteGameServerDeployment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerDeploymentsService/DeleteGameServerDeployment',
            google.cloud.gaming.v1.game_server_deployments_pb2.DeleteGameServerDeploymentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateGameServerDeployment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerDeploymentsService/UpdateGameServerDeployment',
            google.cloud.gaming.v1.game_server_deployments_pb2.UpdateGameServerDeploymentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetGameServerDeploymentRollout = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerDeploymentsService/GetGameServerDeploymentRollout',
            google.cloud.gaming.v1.game_server_deployments_pb2.GetGameServerDeploymentRolloutRequest,
            google.cloud.gaming.v1.game_server_deployments_pb2.GameServerDeploymentRollout,
        )
        self.UpdateGameServerDeploymentRollout = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerDeploymentsService/UpdateGameServerDeploymentRollout',
            google.cloud.gaming.v1.game_server_deployments_pb2.UpdateGameServerDeploymentRolloutRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.PreviewGameServerDeploymentRollout = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerDeploymentsService/PreviewGameServerDeploymentRollout',
            google.cloud.gaming.v1.game_server_deployments_pb2.PreviewGameServerDeploymentRolloutRequest,
            google.cloud.gaming.v1.game_server_deployments_pb2.PreviewGameServerDeploymentRolloutResponse,
        )
        self.FetchDeploymentState = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.gaming.v1.GameServerDeploymentsService/FetchDeploymentState',
            google.cloud.gaming.v1.game_server_deployments_pb2.FetchDeploymentStateRequest,
            google.cloud.gaming.v1.game_server_deployments_pb2.FetchDeploymentStateResponse,
        )
