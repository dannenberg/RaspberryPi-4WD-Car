# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/ads/googleads/v8/services/customer_client_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.ads.googleads.v8.resources.customer_client_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.ads.googleads.v8.services.customer_client_service_pb2


class CustomerClientServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetCustomerClient(self, stream: 'grpclib.server.Stream[google.ads.googleads.v8.services.customer_client_service_pb2.GetCustomerClientRequest, google.ads.googleads.v8.resources.customer_client_pb2.CustomerClient]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.ads.googleads.v8.services.CustomerClientService/GetCustomerClient': grpclib.const.Handler(
                self.GetCustomerClient,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.ads.googleads.v8.services.customer_client_service_pb2.GetCustomerClientRequest,
                google.ads.googleads.v8.resources.customer_client_pb2.CustomerClient,
            ),
        }


class CustomerClientServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetCustomerClient = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.ads.googleads.v8.services.CustomerClientService/GetCustomerClient',
            google.ads.googleads.v8.services.customer_client_service_pb2.GetCustomerClientRequest,
            google.ads.googleads.v8.resources.customer_client_pb2.CustomerClient,
        )
