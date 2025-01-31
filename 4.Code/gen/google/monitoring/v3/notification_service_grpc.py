# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/monitoring/v3/notification_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.monitoring.v3.notification_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import google.monitoring.v3.notification_service_pb2


class NotificationChannelServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ListNotificationChannelDescriptors(self, stream: 'grpclib.server.Stream[google.monitoring.v3.notification_service_pb2.ListNotificationChannelDescriptorsRequest, google.monitoring.v3.notification_service_pb2.ListNotificationChannelDescriptorsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetNotificationChannelDescriptor(self, stream: 'grpclib.server.Stream[google.monitoring.v3.notification_service_pb2.GetNotificationChannelDescriptorRequest, google.monitoring.v3.notification_pb2.NotificationChannelDescriptor]') -> None:
        pass

    @abc.abstractmethod
    async def ListNotificationChannels(self, stream: 'grpclib.server.Stream[google.monitoring.v3.notification_service_pb2.ListNotificationChannelsRequest, google.monitoring.v3.notification_service_pb2.ListNotificationChannelsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetNotificationChannel(self, stream: 'grpclib.server.Stream[google.monitoring.v3.notification_service_pb2.GetNotificationChannelRequest, google.monitoring.v3.notification_pb2.NotificationChannel]') -> None:
        pass

    @abc.abstractmethod
    async def CreateNotificationChannel(self, stream: 'grpclib.server.Stream[google.monitoring.v3.notification_service_pb2.CreateNotificationChannelRequest, google.monitoring.v3.notification_pb2.NotificationChannel]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateNotificationChannel(self, stream: 'grpclib.server.Stream[google.monitoring.v3.notification_service_pb2.UpdateNotificationChannelRequest, google.monitoring.v3.notification_pb2.NotificationChannel]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteNotificationChannel(self, stream: 'grpclib.server.Stream[google.monitoring.v3.notification_service_pb2.DeleteNotificationChannelRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def SendNotificationChannelVerificationCode(self, stream: 'grpclib.server.Stream[google.monitoring.v3.notification_service_pb2.SendNotificationChannelVerificationCodeRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def GetNotificationChannelVerificationCode(self, stream: 'grpclib.server.Stream[google.monitoring.v3.notification_service_pb2.GetNotificationChannelVerificationCodeRequest, google.monitoring.v3.notification_service_pb2.GetNotificationChannelVerificationCodeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def VerifyNotificationChannel(self, stream: 'grpclib.server.Stream[google.monitoring.v3.notification_service_pb2.VerifyNotificationChannelRequest, google.monitoring.v3.notification_pb2.NotificationChannel]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.monitoring.v3.NotificationChannelService/ListNotificationChannelDescriptors': grpclib.const.Handler(
                self.ListNotificationChannelDescriptors,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.notification_service_pb2.ListNotificationChannelDescriptorsRequest,
                google.monitoring.v3.notification_service_pb2.ListNotificationChannelDescriptorsResponse,
            ),
            '/google.monitoring.v3.NotificationChannelService/GetNotificationChannelDescriptor': grpclib.const.Handler(
                self.GetNotificationChannelDescriptor,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.notification_service_pb2.GetNotificationChannelDescriptorRequest,
                google.monitoring.v3.notification_pb2.NotificationChannelDescriptor,
            ),
            '/google.monitoring.v3.NotificationChannelService/ListNotificationChannels': grpclib.const.Handler(
                self.ListNotificationChannels,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.notification_service_pb2.ListNotificationChannelsRequest,
                google.monitoring.v3.notification_service_pb2.ListNotificationChannelsResponse,
            ),
            '/google.monitoring.v3.NotificationChannelService/GetNotificationChannel': grpclib.const.Handler(
                self.GetNotificationChannel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.notification_service_pb2.GetNotificationChannelRequest,
                google.monitoring.v3.notification_pb2.NotificationChannel,
            ),
            '/google.monitoring.v3.NotificationChannelService/CreateNotificationChannel': grpclib.const.Handler(
                self.CreateNotificationChannel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.notification_service_pb2.CreateNotificationChannelRequest,
                google.monitoring.v3.notification_pb2.NotificationChannel,
            ),
            '/google.monitoring.v3.NotificationChannelService/UpdateNotificationChannel': grpclib.const.Handler(
                self.UpdateNotificationChannel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.notification_service_pb2.UpdateNotificationChannelRequest,
                google.monitoring.v3.notification_pb2.NotificationChannel,
            ),
            '/google.monitoring.v3.NotificationChannelService/DeleteNotificationChannel': grpclib.const.Handler(
                self.DeleteNotificationChannel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.notification_service_pb2.DeleteNotificationChannelRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.monitoring.v3.NotificationChannelService/SendNotificationChannelVerificationCode': grpclib.const.Handler(
                self.SendNotificationChannelVerificationCode,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.notification_service_pb2.SendNotificationChannelVerificationCodeRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.monitoring.v3.NotificationChannelService/GetNotificationChannelVerificationCode': grpclib.const.Handler(
                self.GetNotificationChannelVerificationCode,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.notification_service_pb2.GetNotificationChannelVerificationCodeRequest,
                google.monitoring.v3.notification_service_pb2.GetNotificationChannelVerificationCodeResponse,
            ),
            '/google.monitoring.v3.NotificationChannelService/VerifyNotificationChannel': grpclib.const.Handler(
                self.VerifyNotificationChannel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.v3.notification_service_pb2.VerifyNotificationChannelRequest,
                google.monitoring.v3.notification_pb2.NotificationChannel,
            ),
        }


class NotificationChannelServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListNotificationChannelDescriptors = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.NotificationChannelService/ListNotificationChannelDescriptors',
            google.monitoring.v3.notification_service_pb2.ListNotificationChannelDescriptorsRequest,
            google.monitoring.v3.notification_service_pb2.ListNotificationChannelDescriptorsResponse,
        )
        self.GetNotificationChannelDescriptor = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.NotificationChannelService/GetNotificationChannelDescriptor',
            google.monitoring.v3.notification_service_pb2.GetNotificationChannelDescriptorRequest,
            google.monitoring.v3.notification_pb2.NotificationChannelDescriptor,
        )
        self.ListNotificationChannels = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.NotificationChannelService/ListNotificationChannels',
            google.monitoring.v3.notification_service_pb2.ListNotificationChannelsRequest,
            google.monitoring.v3.notification_service_pb2.ListNotificationChannelsResponse,
        )
        self.GetNotificationChannel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.NotificationChannelService/GetNotificationChannel',
            google.monitoring.v3.notification_service_pb2.GetNotificationChannelRequest,
            google.monitoring.v3.notification_pb2.NotificationChannel,
        )
        self.CreateNotificationChannel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.NotificationChannelService/CreateNotificationChannel',
            google.monitoring.v3.notification_service_pb2.CreateNotificationChannelRequest,
            google.monitoring.v3.notification_pb2.NotificationChannel,
        )
        self.UpdateNotificationChannel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.NotificationChannelService/UpdateNotificationChannel',
            google.monitoring.v3.notification_service_pb2.UpdateNotificationChannelRequest,
            google.monitoring.v3.notification_pb2.NotificationChannel,
        )
        self.DeleteNotificationChannel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.NotificationChannelService/DeleteNotificationChannel',
            google.monitoring.v3.notification_service_pb2.DeleteNotificationChannelRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.SendNotificationChannelVerificationCode = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.NotificationChannelService/SendNotificationChannelVerificationCode',
            google.monitoring.v3.notification_service_pb2.SendNotificationChannelVerificationCodeRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.GetNotificationChannelVerificationCode = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.NotificationChannelService/GetNotificationChannelVerificationCode',
            google.monitoring.v3.notification_service_pb2.GetNotificationChannelVerificationCodeRequest,
            google.monitoring.v3.notification_service_pb2.GetNotificationChannelVerificationCodeResponse,
        )
        self.VerifyNotificationChannel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.v3.NotificationChannelService/VerifyNotificationChannel',
            google.monitoring.v3.notification_service_pb2.VerifyNotificationChannelRequest,
            google.monitoring.v3.notification_pb2.NotificationChannel,
        )
