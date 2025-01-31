# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/campaign_customizer_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.resources.campaign_customizer_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.rpc.status_pb2
import google.ads.googleads.v9.services.campaign_customizer_service_pb2


class CampaignCustomizerServiceBase(abc.ABC):

    @abc.abstractmethod
    async def MutateCampaignCustomizers(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.campaign_customizer_service_pb2.MutateCampaignCustomizersRequest, google.ads.googleads.v9.services.campaign_customizer_service_pb2.MutateCampaignCustomizersResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.CampaignCustomizerService/MutateCampaignCustomizers': grpclib.const.Handler(
                self.MutateCampaignCustomizers,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.campaign_customizer_service_pb2.MutateCampaignCustomizersRequest,
                google.ads.googleads.v9.services.campaign_customizer_service_pb2.MutateCampaignCustomizersResponse,
            ),
        }


class CampaignCustomizerServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.MutateCampaignCustomizers = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.CampaignCustomizerService/MutateCampaignCustomizers',
            google.ads.googleads.v9.services.campaign_customizer_service_pb2.MutateCampaignCustomizersRequest,
            google.ads.googleads.v9.services.campaign_customizer_service_pb2.MutateCampaignCustomizersResponse,
        )
