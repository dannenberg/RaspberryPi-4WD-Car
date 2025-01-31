# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v7/services/mobile_device_constant_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v7.resources.mobile_device_constant_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v7.services.mobile_device_constant_service_pb2


class MobileDeviceConstantServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetMobileDeviceConstant(self, stream: 'grpclib.server.Stream[google.ads.googleads.v7.services.mobile_device_constant_service_pb2.GetMobileDeviceConstantRequest, google.ads.googleads.v7.resources.mobile_device_constant_pb2.MobileDeviceConstant]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v7.services.MobileDeviceConstantService/GetMobileDeviceConstant': grpclib.const.Handler(
                self.GetMobileDeviceConstant,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v7.services.mobile_device_constant_service_pb2.GetMobileDeviceConstantRequest,
                google.ads.googleads.v7.resources.mobile_device_constant_pb2.MobileDeviceConstant,
            ),
        }


class MobileDeviceConstantServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetMobileDeviceConstant = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v7.services.MobileDeviceConstantService/GetMobileDeviceConstant',
            google.ads.googleads.v7.services.mobile_device_constant_service_pb2.GetMobileDeviceConstantRequest,
            google.ads.googleads.v7.resources.mobile_device_constant_pb2.MobileDeviceConstant,
        )
