# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/asset/v1p7beta1/asset_service.proto
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
import google.cloud.asset.v1p7beta1.assets_pb2
import google.longrunning.operations_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.asset.v1p7beta1.asset_service_pb2


class AssetServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ExportAssets(self, stream: 'grpclib.server.Stream[google.cloud.asset.v1p7beta1.asset_service_pb2.ExportAssetsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.asset.v1p7beta1.AssetService/ExportAssets': grpclib.const.Handler(
                self.ExportAssets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.asset.v1p7beta1.asset_service_pb2.ExportAssetsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class AssetServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ExportAssets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.asset.v1p7beta1.AssetService/ExportAssets',
            google.cloud.asset.v1p7beta1.asset_service_pb2.ExportAssetsRequest,
            google.longrunning.operations_pb2.Operation,
        )
