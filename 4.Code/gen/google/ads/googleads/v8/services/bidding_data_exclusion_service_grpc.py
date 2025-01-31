# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/bidding_data_exclusion_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.enums.response_content_type_pb2
import google.ads.googleads.v8.resources.bidding_data_exclusion_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.ads.googleads.v8.services.bidding_data_exclusion_service_pb2


class BiddingDataExclusionServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetBiddingDataExclusion(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.bidding_data_exclusion_service_pb2.GetBiddingDataExclusionRequest, google.ads.googleads.v8.resources.bidding_data_exclusion_pb2.BiddingDataExclusion]') -> None:
        pass

    @abc.abstractmethod
    async def MutateBiddingDataExclusions(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.bidding_data_exclusion_service_pb2.MutateBiddingDataExclusionsRequest, google.ads.googleads.v8.services.bidding_data_exclusion_service_pb2.MutateBiddingDataExclusionsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.BiddingDataExclusionService/GetBiddingDataExclusion': grpclib.const.Handler(
                self.GetBiddingDataExclusion,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.bidding_data_exclusion_service_pb2.GetBiddingDataExclusionRequest,
                google.ads.googleads.v8.resources.bidding_data_exclusion_pb2.BiddingDataExclusion,
            ),
            '/google.ads.googleads.v8.services.BiddingDataExclusionService/MutateBiddingDataExclusions': grpclib.const.Handler(
                self.MutateBiddingDataExclusions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.bidding_data_exclusion_service_pb2.MutateBiddingDataExclusionsRequest,
                google.ads.googleads.v8.services.bidding_data_exclusion_service_pb2.MutateBiddingDataExclusionsResponse,
            ),
        }


class BiddingDataExclusionServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetBiddingDataExclusion = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.BiddingDataExclusionService/GetBiddingDataExclusion',
            google.ads.googleads.v8.services.bidding_data_exclusion_service_pb2.GetBiddingDataExclusionRequest,
            google.ads.googleads.v8.resources.bidding_data_exclusion_pb2.BiddingDataExclusion,
        )
        self.MutateBiddingDataExclusions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.BiddingDataExclusionService/MutateBiddingDataExclusions',
            google.ads.googleads.v8.services.bidding_data_exclusion_service_pb2.MutateBiddingDataExclusionsRequest,
            google.ads.googleads.v8.services.bidding_data_exclusion_service_pb2.MutateBiddingDataExclusionsResponse,
        )
