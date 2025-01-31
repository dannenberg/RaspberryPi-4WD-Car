# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v7/services/currency_constant_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v7.resources.currency_constant_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v7.services.currency_constant_service_pb2


class CurrencyConstantServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetCurrencyConstant(self, stream: 'grpclib.server.Stream[google.ads.googleads.v7.services.currency_constant_service_pb2.GetCurrencyConstantRequest, google.ads.googleads.v7.resources.currency_constant_pb2.CurrencyConstant]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v7.services.CurrencyConstantService/GetCurrencyConstant': grpclib.const.Handler(
                self.GetCurrencyConstant,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v7.services.currency_constant_service_pb2.GetCurrencyConstantRequest,
                google.ads.googleads.v7.resources.currency_constant_pb2.CurrencyConstant,
            ),
        }


class CurrencyConstantServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetCurrencyConstant = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v7.services.CurrencyConstantService/GetCurrencyConstant',
            google.ads.googleads.v7.services.currency_constant_service_pb2.GetCurrencyConstantRequest,
            google.ads.googleads.v7.resources.currency_constant_pb2.CurrencyConstant,
        )
