# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/geographic_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.resources.geographic_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v9.services.geographic_view_service_pb2


class GeographicViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetGeographicView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.geographic_view_service_pb2.GetGeographicViewRequest, google.ads.googleads.v9.resources.geographic_view_pb2.GeographicView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.GeographicViewService/GetGeographicView': grpclib.const.Handler(
                self.GetGeographicView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.geographic_view_service_pb2.GetGeographicViewRequest,
                google.ads.googleads.v9.resources.geographic_view_pb2.GeographicView,
            ),
        }


class GeographicViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetGeographicView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.GeographicViewService/GetGeographicView',
            google.ads.googleads.v9.services.geographic_view_service_pb2.GetGeographicViewRequest,
            google.ads.googleads.v9.resources.geographic_view_pb2.GeographicView,
        )
