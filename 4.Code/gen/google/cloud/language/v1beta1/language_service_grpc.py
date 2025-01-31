# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/language/v1beta1/language_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.cloud.language.v1beta1.language_service_pb2


class LanguageServiceBase(abc.ABC):

    @abc.abstractmethod
    async def AnalyzeSentiment(self, stream: 'grpclib.server.Stream[google.cloud.language.v1beta1.language_service_pb2.AnalyzeSentimentRequest, google.cloud.language.v1beta1.language_service_pb2.AnalyzeSentimentResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AnalyzeEntities(self, stream: 'grpclib.server.Stream[google.cloud.language.v1beta1.language_service_pb2.AnalyzeEntitiesRequest, google.cloud.language.v1beta1.language_service_pb2.AnalyzeEntitiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AnalyzeSyntax(self, stream: 'grpclib.server.Stream[google.cloud.language.v1beta1.language_service_pb2.AnalyzeSyntaxRequest, google.cloud.language.v1beta1.language_service_pb2.AnalyzeSyntaxResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AnnotateText(self, stream: 'grpclib.server.Stream[google.cloud.language.v1beta1.language_service_pb2.AnnotateTextRequest, google.cloud.language.v1beta1.language_service_pb2.AnnotateTextResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.language.v1beta1.LanguageService/AnalyzeSentiment': grpclib.const.Handler(
                self.AnalyzeSentiment,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.language.v1beta1.language_service_pb2.AnalyzeSentimentRequest,
                google.cloud.language.v1beta1.language_service_pb2.AnalyzeSentimentResponse,
            ),
            '/google.cloud.language.v1beta1.LanguageService/AnalyzeEntities': grpclib.const.Handler(
                self.AnalyzeEntities,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.language.v1beta1.language_service_pb2.AnalyzeEntitiesRequest,
                google.cloud.language.v1beta1.language_service_pb2.AnalyzeEntitiesResponse,
            ),
            '/google.cloud.language.v1beta1.LanguageService/AnalyzeSyntax': grpclib.const.Handler(
                self.AnalyzeSyntax,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.language.v1beta1.language_service_pb2.AnalyzeSyntaxRequest,
                google.cloud.language.v1beta1.language_service_pb2.AnalyzeSyntaxResponse,
            ),
            '/google.cloud.language.v1beta1.LanguageService/AnnotateText': grpclib.const.Handler(
                self.AnnotateText,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.language.v1beta1.language_service_pb2.AnnotateTextRequest,
                google.cloud.language.v1beta1.language_service_pb2.AnnotateTextResponse,
            ),
        }


class LanguageServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.AnalyzeSentiment = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.language.v1beta1.LanguageService/AnalyzeSentiment',
            google.cloud.language.v1beta1.language_service_pb2.AnalyzeSentimentRequest,
            google.cloud.language.v1beta1.language_service_pb2.AnalyzeSentimentResponse,
        )
        self.AnalyzeEntities = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.language.v1beta1.LanguageService/AnalyzeEntities',
            google.cloud.language.v1beta1.language_service_pb2.AnalyzeEntitiesRequest,
            google.cloud.language.v1beta1.language_service_pb2.AnalyzeEntitiesResponse,
        )
        self.AnalyzeSyntax = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.language.v1beta1.LanguageService/AnalyzeSyntax',
            google.cloud.language.v1beta1.language_service_pb2.AnalyzeSyntaxRequest,
            google.cloud.language.v1beta1.language_service_pb2.AnalyzeSyntaxResponse,
        )
        self.AnnotateText = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.language.v1beta1.LanguageService/AnnotateText',
            google.cloud.language.v1beta1.language_service_pb2.AnnotateTextRequest,
            google.cloud.language.v1beta1.language_service_pb2.AnnotateTextResponse,
        )
