# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/recommendation_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.common.extensions_pb2
import google.ads.googleads.v8.enums.keyword_match_type_pb2
import google.ads.googleads.v8.resources.ad_pb2
import google.ads.googleads.v8.resources.recommendation_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.rpc.status_pb2
import google.ads.googleads.v8.services.recommendation_service_pb2


class RecommendationServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetRecommendation(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.recommendation_service_pb2.GetRecommendationRequest, google.ads.googleads.v8.resources.recommendation_pb2.Recommendation]') -> None:
        pass

    @abc.abstractmethod
    async def ApplyRecommendation(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.recommendation_service_pb2.ApplyRecommendationRequest, google.ads.googleads.v8.services.recommendation_service_pb2.ApplyRecommendationResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DismissRecommendation(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.recommendation_service_pb2.DismissRecommendationRequest, google.ads.googleads.v8.services.recommendation_service_pb2.DismissRecommendationResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.RecommendationService/GetRecommendation': grpclib.const.Handler(
                self.GetRecommendation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.recommendation_service_pb2.GetRecommendationRequest,
                google.ads.googleads.v8.resources.recommendation_pb2.Recommendation,
            ),
            '/google.ads.googleads.v8.services.RecommendationService/ApplyRecommendation': grpclib.const.Handler(
                self.ApplyRecommendation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.recommendation_service_pb2.ApplyRecommendationRequest,
                google.ads.googleads.v8.services.recommendation_service_pb2.ApplyRecommendationResponse,
            ),
            '/google.ads.googleads.v8.services.RecommendationService/DismissRecommendation': grpclib.const.Handler(
                self.DismissRecommendation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.recommendation_service_pb2.DismissRecommendationRequest,
                google.ads.googleads.v8.services.recommendation_service_pb2.DismissRecommendationResponse,
            ),
        }


class RecommendationServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetRecommendation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.RecommendationService/GetRecommendation',
            google.ads.googleads.v8.services.recommendation_service_pb2.GetRecommendationRequest,
            google.ads.googleads.v8.resources.recommendation_pb2.Recommendation,
        )
        self.ApplyRecommendation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.RecommendationService/ApplyRecommendation',
            google.ads.googleads.v8.services.recommendation_service_pb2.ApplyRecommendationRequest,
            google.ads.googleads.v8.services.recommendation_service_pb2.ApplyRecommendationResponse,
        )
        self.DismissRecommendation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.RecommendationService/DismissRecommendation',
            google.ads.googleads.v8.services.recommendation_service_pb2.DismissRecommendationRequest,
            google.ads.googleads.v8.services.recommendation_service_pb2.DismissRecommendationResponse,
        )
