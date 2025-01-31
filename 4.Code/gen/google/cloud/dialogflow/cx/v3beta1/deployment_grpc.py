# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/dialogflow/cx/v3beta1/deployment.proto
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
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.dialogflow.cx.v3beta1.deployment_pb2


class DeploymentsBase(abc.ABC):

    @abc.abstractmethod
    async def ListDeployments(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3beta1.deployment_pb2.ListDeploymentsRequest, google.cloud.dialogflow.cx.v3beta1.deployment_pb2.ListDeploymentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetDeployment(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.cx.v3beta1.deployment_pb2.GetDeploymentRequest, google.cloud.dialogflow.cx.v3beta1.deployment_pb2.Deployment]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.dialogflow.cx.v3beta1.Deployments/ListDeployments': grpclib.const.Handler(
                self.ListDeployments,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3beta1.deployment_pb2.ListDeploymentsRequest,
                google.cloud.dialogflow.cx.v3beta1.deployment_pb2.ListDeploymentsResponse,
            ),
            '/google.cloud.dialogflow.cx.v3beta1.Deployments/GetDeployment': grpclib.const.Handler(
                self.GetDeployment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.cx.v3beta1.deployment_pb2.GetDeploymentRequest,
                google.cloud.dialogflow.cx.v3beta1.deployment_pb2.Deployment,
            ),
        }


class DeploymentsStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListDeployments = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3beta1.Deployments/ListDeployments',
            google.cloud.dialogflow.cx.v3beta1.deployment_pb2.ListDeploymentsRequest,
            google.cloud.dialogflow.cx.v3beta1.deployment_pb2.ListDeploymentsResponse,
        )
        self.GetDeployment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.cx.v3beta1.Deployments/GetDeployment',
            google.cloud.dialogflow.cx.v3beta1.deployment_pb2.GetDeploymentRequest,
            google.cloud.dialogflow.cx.v3beta1.deployment_pb2.Deployment,
        )
