# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/campaign_conversion_goal_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.resources.campaign_conversion_goal_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.protobuf.field_mask_pb2
import google.ads.googleads.v9.services.campaign_conversion_goal_service_pb2


class CampaignConversionGoalServiceBase(abc.ABC):

    @abc.abstractmethod
    async def MutateCampaignConversionGoals(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.campaign_conversion_goal_service_pb2.MutateCampaignConversionGoalsRequest, google.ads.googleads.v9.services.campaign_conversion_goal_service_pb2.MutateCampaignConversionGoalsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.CampaignConversionGoalService/MutateCampaignConversionGoals': grpclib.const.Handler(
                self.MutateCampaignConversionGoals,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.campaign_conversion_goal_service_pb2.MutateCampaignConversionGoalsRequest,
                google.ads.googleads.v9.services.campaign_conversion_goal_service_pb2.MutateCampaignConversionGoalsResponse,
            ),
        }


class CampaignConversionGoalServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.MutateCampaignConversionGoals = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.CampaignConversionGoalService/MutateCampaignConversionGoals',
            google.ads.googleads.v9.services.campaign_conversion_goal_service_pb2.MutateCampaignConversionGoalsRequest,
            google.ads.googleads.v9.services.campaign_conversion_goal_service_pb2.MutateCampaignConversionGoalsResponse,
        )
