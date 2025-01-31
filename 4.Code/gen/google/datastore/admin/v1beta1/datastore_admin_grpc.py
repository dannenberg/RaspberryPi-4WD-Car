# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/datastore/admin/v1beta1/datastore_admin.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.longrunning.operations_pb2
import google.protobuf.timestamp_pb2
import google.datastore.admin.v1beta1.datastore_admin_pb2


class DatastoreAdminBase(abc.ABC):

    @abc.abstractmethod
    async def ExportEntities(self, stream: 'grpclib.server.Stream[google.datastore.admin.v1beta1.datastore_admin_pb2.ExportEntitiesRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ImportEntities(self, stream: 'grpclib.server.Stream[google.datastore.admin.v1beta1.datastore_admin_pb2.ImportEntitiesRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.datastore.admin.v1beta1.DatastoreAdmin/ExportEntities': grpclib.const.Handler(
                self.ExportEntities,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.datastore.admin.v1beta1.datastore_admin_pb2.ExportEntitiesRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.datastore.admin.v1beta1.DatastoreAdmin/ImportEntities': grpclib.const.Handler(
                self.ImportEntities,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.datastore.admin.v1beta1.datastore_admin_pb2.ImportEntitiesRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class DatastoreAdminStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ExportEntities = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.datastore.admin.v1beta1.DatastoreAdmin/ExportEntities',
            google.datastore.admin.v1beta1.datastore_admin_pb2.ExportEntitiesRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ImportEntities = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.datastore.admin.v1beta1.DatastoreAdmin/ImportEntities',
            google.datastore.admin.v1beta1.datastore_admin_pb2.ImportEntitiesRequest,
            google.longrunning.operations_pb2.Operation,
        )
