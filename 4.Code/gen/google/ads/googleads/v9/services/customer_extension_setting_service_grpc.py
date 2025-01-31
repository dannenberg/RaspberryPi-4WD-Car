# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v9/services/customer_extension_setting_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v9.enums.response_content_type_pb2
import google.ads.googleads.v9.resources.customer_extension_setting_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.ads.googleads.v9.services.customer_extension_setting_service_pb2


class CustomerExtensionSettingServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetCustomerExtensionSetting(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.customer_extension_setting_service_pb2.GetCustomerExtensionSettingRequest, google.ads.googleads.v9.resources.customer_extension_setting_pb2.CustomerExtensionSetting]') -> None:
        pass

    @abc.abstractmethod
    async def MutateCustomerExtensionSettings(self, stream: 'grpclib.server.Stream[google.ads.googleads.v9.services.customer_extension_setting_service_pb2.MutateCustomerExtensionSettingsRequest, google.ads.googleads.v9.services.customer_extension_setting_service_pb2.MutateCustomerExtensionSettingsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v9.services.CustomerExtensionSettingService/GetCustomerExtensionSetting': grpclib.const.Handler(
                self.GetCustomerExtensionSetting,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.customer_extension_setting_service_pb2.GetCustomerExtensionSettingRequest,
                google.ads.googleads.v9.resources.customer_extension_setting_pb2.CustomerExtensionSetting,
            ),
            '/google.ads.googleads.v9.services.CustomerExtensionSettingService/MutateCustomerExtensionSettings': grpclib.const.Handler(
                self.MutateCustomerExtensionSettings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v9.services.customer_extension_setting_service_pb2.MutateCustomerExtensionSettingsRequest,
                google.ads.googleads.v9.services.customer_extension_setting_service_pb2.MutateCustomerExtensionSettingsResponse,
            ),
        }


class CustomerExtensionSettingServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetCustomerExtensionSetting = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.CustomerExtensionSettingService/GetCustomerExtensionSetting',
            google.ads.googleads.v9.services.customer_extension_setting_service_pb2.GetCustomerExtensionSettingRequest,
            google.ads.googleads.v9.resources.customer_extension_setting_pb2.CustomerExtensionSetting,
        )
        self.MutateCustomerExtensionSettings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v9.services.CustomerExtensionSettingService/MutateCustomerExtensionSettings',
            google.ads.googleads.v9.services.customer_extension_setting_service_pb2.MutateCustomerExtensionSettingsRequest,
            google.ads.googleads.v9.services.customer_extension_setting_service_pb2.MutateCustomerExtensionSettingsResponse,
        )
