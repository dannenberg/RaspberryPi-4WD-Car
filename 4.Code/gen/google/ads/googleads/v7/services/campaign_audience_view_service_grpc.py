# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v7/services/campaign_audience_view_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v7.resources.campaign_audience_view_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v7.services.campaign_audience_view_service_pb2


class CampaignAudienceViewServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetCampaignAudienceView(self, stream: 'grpclib.server.Stream[google.ads.googleads.v7.services.campaign_audience_view_service_pb2.GetCampaignAudienceViewRequest, google.ads.googleads.v7.resources.campaign_audience_view_pb2.CampaignAudienceView]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v7.services.CampaignAudienceViewService/GetCampaignAudienceView': grpclib.const.Handler(
                self.GetCampaignAudienceView,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v7.services.campaign_audience_view_service_pb2.GetCampaignAudienceViewRequest,
                google.ads.googleads.v7.resources.campaign_audience_view_pb2.CampaignAudienceView,
            ),
        }


class CampaignAudienceViewServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetCampaignAudienceView = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v7.services.CampaignAudienceViewService/GetCampaignAudienceView',
            google.ads.googleads.v7.services.campaign_audience_view_service_pb2.GetCampaignAudienceViewRequest,
            google.ads.googleads.v7.resources.campaign_audience_view_pb2.CampaignAudienceView,
        )
