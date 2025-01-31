# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/metastore/v1alpha/metastore.proto
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
import google.protobuf.wrappers_pb2
import google.type.dayofweek_pb2
import google.cloud.metastore.v1alpha.metastore_pb2


class DataprocMetastoreBase(abc.ABC):

    @abc.abstractmethod
    async def ListServices(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.ListServicesRequest, google.cloud.metastore.v1alpha.metastore_pb2.ListServicesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetService(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.GetServiceRequest, google.cloud.metastore.v1alpha.metastore_pb2.Service]') -> None:
        pass

    @abc.abstractmethod
    async def CreateService(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.CreateServiceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateService(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.UpdateServiceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteService(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.DeleteServiceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ListMetadataImports(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.ListMetadataImportsRequest, google.cloud.metastore.v1alpha.metastore_pb2.ListMetadataImportsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetMetadataImport(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.GetMetadataImportRequest, google.cloud.metastore.v1alpha.metastore_pb2.MetadataImport]') -> None:
        pass

    @abc.abstractmethod
    async def CreateMetadataImport(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.CreateMetadataImportRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateMetadataImport(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.UpdateMetadataImportRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ExportMetadata(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.ExportMetadataRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def RestoreService(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.RestoreServiceRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ListBackups(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.ListBackupsRequest, google.cloud.metastore.v1alpha.metastore_pb2.ListBackupsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetBackup(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.GetBackupRequest, google.cloud.metastore.v1alpha.metastore_pb2.Backup]') -> None:
        pass

    @abc.abstractmethod
    async def CreateBackup(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.CreateBackupRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteBackup(self, stream: 'grpclib.server.Stream[google.cloud.metastore.v1alpha.metastore_pb2.DeleteBackupRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.metastore.v1alpha.DataprocMetastore/ListServices': grpclib.const.Handler(
                self.ListServices,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.ListServicesRequest,
                google.cloud.metastore.v1alpha.metastore_pb2.ListServicesResponse,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/GetService': grpclib.const.Handler(
                self.GetService,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.GetServiceRequest,
                google.cloud.metastore.v1alpha.metastore_pb2.Service,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/CreateService': grpclib.const.Handler(
                self.CreateService,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.CreateServiceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/UpdateService': grpclib.const.Handler(
                self.UpdateService,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.UpdateServiceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/DeleteService': grpclib.const.Handler(
                self.DeleteService,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.DeleteServiceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/ListMetadataImports': grpclib.const.Handler(
                self.ListMetadataImports,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.ListMetadataImportsRequest,
                google.cloud.metastore.v1alpha.metastore_pb2.ListMetadataImportsResponse,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/GetMetadataImport': grpclib.const.Handler(
                self.GetMetadataImport,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.GetMetadataImportRequest,
                google.cloud.metastore.v1alpha.metastore_pb2.MetadataImport,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/CreateMetadataImport': grpclib.const.Handler(
                self.CreateMetadataImport,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.CreateMetadataImportRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/UpdateMetadataImport': grpclib.const.Handler(
                self.UpdateMetadataImport,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.UpdateMetadataImportRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/ExportMetadata': grpclib.const.Handler(
                self.ExportMetadata,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.ExportMetadataRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/RestoreService': grpclib.const.Handler(
                self.RestoreService,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.RestoreServiceRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/ListBackups': grpclib.const.Handler(
                self.ListBackups,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.ListBackupsRequest,
                google.cloud.metastore.v1alpha.metastore_pb2.ListBackupsResponse,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/GetBackup': grpclib.const.Handler(
                self.GetBackup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.GetBackupRequest,
                google.cloud.metastore.v1alpha.metastore_pb2.Backup,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/CreateBackup': grpclib.const.Handler(
                self.CreateBackup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.CreateBackupRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.metastore.v1alpha.DataprocMetastore/DeleteBackup': grpclib.const.Handler(
                self.DeleteBackup,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.metastore.v1alpha.metastore_pb2.DeleteBackupRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class DataprocMetastoreStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListServices = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/ListServices',
            google.cloud.metastore.v1alpha.metastore_pb2.ListServicesRequest,
            google.cloud.metastore.v1alpha.metastore_pb2.ListServicesResponse,
        )
        self.GetService = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/GetService',
            google.cloud.metastore.v1alpha.metastore_pb2.GetServiceRequest,
            google.cloud.metastore.v1alpha.metastore_pb2.Service,
        )
        self.CreateService = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/CreateService',
            google.cloud.metastore.v1alpha.metastore_pb2.CreateServiceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateService = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/UpdateService',
            google.cloud.metastore.v1alpha.metastore_pb2.UpdateServiceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteService = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/DeleteService',
            google.cloud.metastore.v1alpha.metastore_pb2.DeleteServiceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ListMetadataImports = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/ListMetadataImports',
            google.cloud.metastore.v1alpha.metastore_pb2.ListMetadataImportsRequest,
            google.cloud.metastore.v1alpha.metastore_pb2.ListMetadataImportsResponse,
        )
        self.GetMetadataImport = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/GetMetadataImport',
            google.cloud.metastore.v1alpha.metastore_pb2.GetMetadataImportRequest,
            google.cloud.metastore.v1alpha.metastore_pb2.MetadataImport,
        )
        self.CreateMetadataImport = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/CreateMetadataImport',
            google.cloud.metastore.v1alpha.metastore_pb2.CreateMetadataImportRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateMetadataImport = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/UpdateMetadataImport',
            google.cloud.metastore.v1alpha.metastore_pb2.UpdateMetadataImportRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ExportMetadata = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/ExportMetadata',
            google.cloud.metastore.v1alpha.metastore_pb2.ExportMetadataRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.RestoreService = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/RestoreService',
            google.cloud.metastore.v1alpha.metastore_pb2.RestoreServiceRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ListBackups = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/ListBackups',
            google.cloud.metastore.v1alpha.metastore_pb2.ListBackupsRequest,
            google.cloud.metastore.v1alpha.metastore_pb2.ListBackupsResponse,
        )
        self.GetBackup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/GetBackup',
            google.cloud.metastore.v1alpha.metastore_pb2.GetBackupRequest,
            google.cloud.metastore.v1alpha.metastore_pb2.Backup,
        )
        self.CreateBackup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/CreateBackup',
            google.cloud.metastore.v1alpha.metastore_pb2.CreateBackupRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteBackup = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.metastore.v1alpha.DataprocMetastore/DeleteBackup',
            google.cloud.metastore.v1alpha.metastore_pb2.DeleteBackupRequest,
            google.longrunning.operations_pb2.Operation,
        )
