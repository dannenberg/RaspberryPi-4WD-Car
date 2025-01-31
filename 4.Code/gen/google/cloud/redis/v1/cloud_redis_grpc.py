# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/redis/v1/cloud_redis.proto
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
import google.longrunning.operations_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.redis.v1.cloud_redis_pb2


class CloudRedisBase(abc.ABC):

    @abc.abstractmethod
    async def ListInstances(self, stream: 'grpclib.server.Stream[google.cloud.redis.v1.cloud_redis_pb2.ListInstancesRequest, google.cloud.redis.v1.cloud_redis_pb2.ListInstancesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetInstance(self, stream: 'grpclib.server.Stream[google.cloud.redis.v1.cloud_redis_pb2.GetInstanceRequest, google.cloud.redis.v1.cloud_redis_pb2.Instance]') -> None:
        pass

    @abc.abstractmethod
    async def CreateInstance(self, stream: 'grpclib.server.Stream[google.cloud.redis.v1.cloud_redis_pb2.CreateInstanceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateInstance(self, stream: 'grpclib.server.Stream[google.cloud.redis.v1.cloud_redis_pb2.UpdateInstanceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpgradeInstance(self, stream: 'grpclib.server.Stream[google.cloud.redis.v1.cloud_redis_pb2.UpgradeInstanceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ImportInstance(self, stream: 'grpclib.server.Stream[google.cloud.redis.v1.cloud_redis_pb2.ImportInstanceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ExportInstance(self, stream: 'grpclib.server.Stream[google.cloud.redis.v1.cloud_redis_pb2.ExportInstanceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def FailoverInstance(self, stream: 'grpclib.server.Stream[google.cloud.redis.v1.cloud_redis_pb2.FailoverInstanceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteInstance(self, stream: 'grpclib.server.Stream[google.cloud.redis.v1.cloud_redis_pb2.DeleteInstanceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.redis.v1.CloudRedis/ListInstances': grpclib.const.Handler(
                self.ListInstances,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.redis.v1.cloud_redis_pb2.ListInstancesRequest,
                google.cloud.redis.v1.cloud_redis_pb2.ListInstancesResponse,
            ),
            '/google.cloud.redis.v1.CloudRedis/GetInstance': grpclib.const.Handler(
                self.GetInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.redis.v1.cloud_redis_pb2.GetInstanceRequest,
                google.cloud.redis.v1.cloud_redis_pb2.Instance,
            ),
            '/google.cloud.redis.v1.CloudRedis/CreateInstance': grpclib.const.Handler(
                self.CreateInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.redis.v1.cloud_redis_pb2.CreateInstanceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.redis.v1.CloudRedis/UpdateInstance': grpclib.const.Handler(
                self.UpdateInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.redis.v1.cloud_redis_pb2.UpdateInstanceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.redis.v1.CloudRedis/UpgradeInstance': grpclib.const.Handler(
                self.UpgradeInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.redis.v1.cloud_redis_pb2.UpgradeInstanceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.redis.v1.CloudRedis/ImportInstance': grpclib.const.Handler(
                self.ImportInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.redis.v1.cloud_redis_pb2.ImportInstanceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.redis.v1.CloudRedis/ExportInstance': grpclib.const.Handler(
                self.ExportInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.redis.v1.cloud_redis_pb2.ExportInstanceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.redis.v1.CloudRedis/FailoverInstance': grpclib.const.Handler(
                self.FailoverInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.redis.v1.cloud_redis_pb2.FailoverInstanceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.redis.v1.CloudRedis/DeleteInstance': grpclib.const.Handler(
                self.DeleteInstance,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.redis.v1.cloud_redis_pb2.DeleteInstanceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class CloudRedisStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListInstances = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.redis.v1.CloudRedis/ListInstances',
            google.cloud.redis.v1.cloud_redis_pb2.ListInstancesRequest,
            google.cloud.redis.v1.cloud_redis_pb2.ListInstancesResponse,
        )
        self.GetInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.redis.v1.CloudRedis/GetInstance',
            google.cloud.redis.v1.cloud_redis_pb2.GetInstanceRequest,
            google.cloud.redis.v1.cloud_redis_pb2.Instance,
        )
        self.CreateInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.redis.v1.CloudRedis/CreateInstance',
            google.cloud.redis.v1.cloud_redis_pb2.CreateInstanceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.redis.v1.CloudRedis/UpdateInstance',
            google.cloud.redis.v1.cloud_redis_pb2.UpdateInstanceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpgradeInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.redis.v1.CloudRedis/UpgradeInstance',
            google.cloud.redis.v1.cloud_redis_pb2.UpgradeInstanceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ImportInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.redis.v1.CloudRedis/ImportInstance',
            google.cloud.redis.v1.cloud_redis_pb2.ImportInstanceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ExportInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.redis.v1.CloudRedis/ExportInstance',
            google.cloud.redis.v1.cloud_redis_pb2.ExportInstanceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.FailoverInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.redis.v1.CloudRedis/FailoverInstance',
            google.cloud.redis.v1.cloud_redis_pb2.FailoverInstanceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteInstance = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.redis.v1.CloudRedis/DeleteInstance',
            google.cloud.redis.v1.cloud_redis_pb2.DeleteInstanceRequest,
            google.longrunning.operations_pb2.Operation,
        )
