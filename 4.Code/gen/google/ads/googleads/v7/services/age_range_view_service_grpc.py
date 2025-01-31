# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v7/services/age_range_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v7.resources.age_range_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v7.services.age_range_view_service_pb2


class AgeRangeViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetAgeRangeView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v7.services.age_range_view_service_pb2.GetAgeRangeViewRequest, google.ads.googleads.v7.resources.age_range_view_pb2.AgeRangeView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v7.services.AgeRangeViewService/GetAgeRangeView': grpclib.const.Handler(
                self.GetAgeRangeView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v7.services.age_range_view_service_pb2.GetAgeRangeViewRequest,
                google.ads.googleads.v7.resources.age_range_view_pb2.AgeRangeView,
            ),
        }


class AgeRangeViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetAgeRangeView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v7.services.AgeRangeViewService/GetAgeRangeView',
            google.ads.googleads.v7.services.age_range_view_service_pb2.GetAgeRangeViewRequest,
            google.ads.googleads.v7.resources.age_range_view_pb2.AgeRangeView,
        )
