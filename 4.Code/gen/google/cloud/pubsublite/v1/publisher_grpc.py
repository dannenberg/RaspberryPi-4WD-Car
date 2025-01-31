# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/pubsublite/v1/publisher.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.cloud.pubsublite.v1.common_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.cloud.pubsublite.v1.publisher_pb2


class PublisherServiceBase(abc.ABC):

    @abc.abstractmethod
    async def Publish(self, stream: 'grpclib.server.Stream[google.cloud.pubsublite.v1.publisher_pb2.PublishRequest, google.cloud.pubsublite.v1.publisher_pb2.PublishResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.pubsublite.v1.PublisherService/Publish': grpclib.const.Handler(
                self.Publish,
                grpclib.const.Cardinality.STREAM_STREAM,
                google.cloud.pubsublite.v1.publisher_pb2.PublishRequest,
                google.cloud.pubsublite.v1.publisher_pb2.PublishResponse,
            ),
        }


class PublisherServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Publish = grpclib.client.StreamStreamMethod(
            channel,
            '/google.cloud.pubsublite.v1.PublisherService/Publish',
            google.cloud.pubsublite.v1.publisher_pb2.PublishRequest,
            google.cloud.pubsublite.v1.publisher_pb2.PublishResponse,
        )
