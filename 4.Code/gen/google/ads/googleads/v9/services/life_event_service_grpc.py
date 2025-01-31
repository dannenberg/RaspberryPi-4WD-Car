# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/life_event_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.resources.life_event_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v9.services.life_event_service_pb2


class LifeEventServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetLifeEvent(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.life_event_service_pb2.GetLifeEventRequest, google.ads.googleads.v9.resources.life_event_pb2.LifeEvent]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.LifeEventService/GetLifeEvent': grpclib.const.Handler(
                self.GetLifeEvent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.life_event_service_pb2.GetLifeEventRequest,
                google.ads.googleads.v9.resources.life_event_pb2.LifeEvent,
            ),
        }


class LifeEventServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetLifeEvent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.LifeEventService/GetLifeEvent',
            google.ads.googleads.v9.services.life_event_service_pb2.GetLifeEventRequest,
            google.ads.googleads.v9.resources.life_event_pb2.LifeEvent,
        )
