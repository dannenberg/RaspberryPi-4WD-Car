# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/shared_set_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.resources.shared_set_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.ads.googleads.v9.services.shared_set_service_pb2


class SharedSetServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetSharedSet(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.shared_set_service_pb2.GetSharedSetRequest, google.ads.googleads.v9.resources.shared_set_pb2.SharedSet]') -> None:
        pass

    @abc.abstractmethod
    async def MutateSharedSets(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.shared_set_service_pb2.MutateSharedSetsRequest, google.ads.googleads.v9.services.shared_set_service_pb2.MutateSharedSetsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.SharedSetService/GetSharedSet': grpclib.const.Handler(
                self.GetSharedSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.shared_set_service_pb2.GetSharedSetRequest,
                google.ads.googleads.v9.resources.shared_set_pb2.SharedSet,
            ),
            '/google.ads.googleads.v9.services.SharedSetService/MutateSharedSets': grpclib.const.Handler(
                self.MutateSharedSets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.shared_set_service_pb2.MutateSharedSetsRequest,
                google.ads.googleads.v9.services.shared_set_service_pb2.MutateSharedSetsResponse,
            ),
        }


class SharedSetServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetSharedSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.SharedSetService/GetSharedSet',
            google.ads.googleads.v9.services.shared_set_service_pb2.GetSharedSetRequest,
            google.ads.googleads.v9.resources.shared_set_pb2.SharedSet,
        )
        self.MutateSharedSets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.SharedSetService/MutateSharedSets',
            google.ads.googleads.v9.services.shared_set_service_pb2.MutateSharedSetsRequest,
            google.ads.googleads.v9.services.shared_set_service_pb2.MutateSharedSetsResponse,
        )
