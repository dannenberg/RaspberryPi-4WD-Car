# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/conversion_goal_campaign_config_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.resources.conversion_goal_campaign_config_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.protobuf.field_mask_pb2
import google.ads.googleads.v9.services.conversion_goal_campaign_config_service_pb2


class ConversionGoalCampaignConfigServiceBase(abc.ABC):

    @abc.abstractmethod
    async def MutateConversionGoalCampaignConfigs(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.conversion_goal_campaign_config_service_pb2.MutateConversionGoalCampaignConfigsRequest, google.ads.googleads.v9.services.conversion_goal_campaign_config_service_pb2.MutateConversionGoalCampaignConfigsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.ConversionGoalCampaignConfigService/MutateConversionGoalCampaignConfigs': grpclib.const.Handler(
                self.MutateConversionGoalCampaignConfigs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.conversion_goal_campaign_config_service_pb2.MutateConversionGoalCampaignConfigsRequest,
                google.ads.googleads.v9.services.conversion_goal_campaign_config_service_pb2.MutateConversionGoalCampaignConfigsResponse,
            ),
        }


class ConversionGoalCampaignConfigServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.MutateConversionGoalCampaignConfigs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.ConversionGoalCampaignConfigService/MutateConversionGoalCampaignConfigs',
            google.ads.googleads.v9.services.conversion_goal_campaign_config_service_pb2.MutateConversionGoalCampaignConfigsRequest,
            google.ads.googleads.v9.services.conversion_goal_campaign_config_service_pb2.MutateConversionGoalCampaignConfigsResponse,
        )
