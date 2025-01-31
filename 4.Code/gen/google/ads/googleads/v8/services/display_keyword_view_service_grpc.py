# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/display_keyword_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.resources.display_keyword_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v8.services.display_keyword_view_service_pb2


class DisplayKeywordViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetDisplayKeywordView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.display_keyword_view_service_pb2.GetDisplayKeywordViewRequest, google.ads.googleads.v8.resources.display_keyword_view_pb2.DisplayKeywordView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.DisplayKeywordViewService/GetDisplayKeywordView': grpclib.const.Handler(
                self.GetDisplayKeywordView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.display_keyword_view_service_pb2.GetDisplayKeywordViewRequest,
                google.ads.googleads.v8.resources.display_keyword_view_pb2.DisplayKeywordView,
            ),
        }


class DisplayKeywordViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetDisplayKeywordView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.DisplayKeywordViewService/GetDisplayKeywordView',
            google.ads.googleads.v8.services.display_keyword_view_service_pb2.GetDisplayKeywordViewRequest,
            google.ads.googleads.v8.resources.display_keyword_view_pb2.DisplayKeywordView,
        )
