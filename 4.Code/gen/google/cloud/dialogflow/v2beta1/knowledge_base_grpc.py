# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/dialogflow/v2beta1/knowledge_base.proto
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
import google.cloud.dialogflow.v2beta1.knowledge_base_pb2


class KnowledgeBasesBase(abc.ABC):

    @abc.abstractmethod
    async def ListKnowledgeBases(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.knowledge_base_pb2.ListKnowledgeBasesRequest, google.cloud.dialogflow.v2beta1.knowledge_base_pb2.ListKnowledgeBasesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetKnowledgeBase(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.knowledge_base_pb2.GetKnowledgeBaseRequest, google.cloud.dialogflow.v2beta1.knowledge_base_pb2.KnowledgeBase]') -> None:
        pass

    @abc.abstractmethod
    async def CreateKnowledgeBase(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.knowledge_base_pb2.CreateKnowledgeBaseRequest, google.cloud.dialogflow.v2beta1.knowledge_base_pb2.KnowledgeBase]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteKnowledgeBase(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.knowledge_base_pb2.DeleteKnowledgeBaseRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateKnowledgeBase(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.knowledge_base_pb2.UpdateKnowledgeBaseRequest, google.cloud.dialogflow.v2beta1.knowledge_base_pb2.KnowledgeBase]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.dialogflow.v2beta1.KnowledgeBases/ListKnowledgeBases': grpclib.const.Handler(
                self.ListKnowledgeBases,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.knowledge_base_pb2.ListKnowledgeBasesRequest,
                google.cloud.dialogflow.v2beta1.knowledge_base_pb2.ListKnowledgeBasesResponse,
            ),
            '/google.cloud.dialogflow.v2beta1.KnowledgeBases/GetKnowledgeBase': grpclib.const.Handler(
                self.GetKnowledgeBase,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.knowledge_base_pb2.GetKnowledgeBaseRequest,
                google.cloud.dialogflow.v2beta1.knowledge_base_pb2.KnowledgeBase,
            ),
            '/google.cloud.dialogflow.v2beta1.KnowledgeBases/CreateKnowledgeBase': grpclib.const.Handler(
                self.CreateKnowledgeBase,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.knowledge_base_pb2.CreateKnowledgeBaseRequest,
                google.cloud.dialogflow.v2beta1.knowledge_base_pb2.KnowledgeBase,
            ),
            '/google.cloud.dialogflow.v2beta1.KnowledgeBases/DeleteKnowledgeBase': grpclib.const.Handler(
                self.DeleteKnowledgeBase,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.knowledge_base_pb2.DeleteKnowledgeBaseRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.dialogflow.v2beta1.KnowledgeBases/UpdateKnowledgeBase': grpclib.const.Handler(
                self.UpdateKnowledgeBase,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.knowledge_base_pb2.UpdateKnowledgeBaseRequest,
                google.cloud.dialogflow.v2beta1.knowledge_base_pb2.KnowledgeBase,
            ),
        }


class KnowledgeBasesStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListKnowledgeBases = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.KnowledgeBases/ListKnowledgeBases',
            google.cloud.dialogflow.v2beta1.knowledge_base_pb2.ListKnowledgeBasesRequest,
            google.cloud.dialogflow.v2beta1.knowledge_base_pb2.ListKnowledgeBasesResponse,
        )
        self.GetKnowledgeBase = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.KnowledgeBases/GetKnowledgeBase',
            google.cloud.dialogflow.v2beta1.knowledge_base_pb2.GetKnowledgeBaseRequest,
            google.cloud.dialogflow.v2beta1.knowledge_base_pb2.KnowledgeBase,
        )
        self.CreateKnowledgeBase = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.KnowledgeBases/CreateKnowledgeBase',
            google.cloud.dialogflow.v2beta1.knowledge_base_pb2.CreateKnowledgeBaseRequest,
            google.cloud.dialogflow.v2beta1.knowledge_base_pb2.KnowledgeBase,
        )
        self.DeleteKnowledgeBase = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.KnowledgeBases/DeleteKnowledgeBase',
            google.cloud.dialogflow.v2beta1.knowledge_base_pb2.DeleteKnowledgeBaseRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.UpdateKnowledgeBase = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.KnowledgeBases/UpdateKnowledgeBase',
            google.cloud.dialogflow.v2beta1.knowledge_base_pb2.UpdateKnowledgeBaseRequest,
            google.cloud.dialogflow.v2beta1.knowledge_base_pb2.KnowledgeBase,
        )
