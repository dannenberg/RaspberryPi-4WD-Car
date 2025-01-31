# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/storagetransfer/v1/transfer.proto
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
import google.longrunning.operations_pb2
import google.protobuf.duration_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.storagetransfer.v1.transfer_types_pb2
import google.storagetransfer.v1.transfer_pb2


class StorageTransferServiceBase(abc.ABC):

    @abc.abstractmethod
    async def GetGoogleServiceAccount(self, stream: 'grpclib.server.Stream[google.storagetransfer.v1.transfer_pb2.GetGoogleServiceAccountRequest, google.storagetransfer.v1.transfer_types_pb2.GoogleServiceAccount]') -> None:
        pass

    @abc.abstractmethod
    async def CreateTransferJob(self, stream: 'grpclib.server.Stream[google.storagetransfer.v1.transfer_pb2.CreateTransferJobRequest, google.storagetransfer.v1.transfer_types_pb2.TransferJob]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateTransferJob(self, stream: 'grpclib.server.Stream[google.storagetransfer.v1.transfer_pb2.UpdateTransferJobRequest, google.storagetransfer.v1.transfer_types_pb2.TransferJob]') -> None:
        pass

    @abc.abstractmethod
    async def GetTransferJob(self, stream: 'grpclib.server.Stream[google.storagetransfer.v1.transfer_pb2.GetTransferJobRequest, google.storagetransfer.v1.transfer_types_pb2.TransferJob]') -> None:
        pass

    @abc.abstractmethod
    async def ListTransferJobs(self, stream: 'grpclib.server.Stream[google.storagetransfer.v1.transfer_pb2.ListTransferJobsRequest, google.storagetransfer.v1.transfer_pb2.ListTransferJobsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PauseTransferOperation(self, stream: 'grpclib.server.Stream[google.storagetransfer.v1.transfer_pb2.PauseTransferOperationRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ResumeTransferOperation(self, stream: 'grpclib.server.Stream[google.storagetransfer.v1.transfer_pb2.ResumeTransferOperationRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def RunTransferJob(self, stream: 'grpclib.server.Stream[google.storagetransfer.v1.transfer_pb2.RunTransferJobRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.storagetransfer.v1.StorageTransferService/GetGoogleServiceAccount': grpclib.const.Handler(
                self.GetGoogleServiceAccount,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.storagetransfer.v1.transfer_pb2.GetGoogleServiceAccountRequest,
                google.storagetransfer.v1.transfer_types_pb2.GoogleServiceAccount,
            ),
            '/google.storagetransfer.v1.StorageTransferService/CreateTransferJob': grpclib.const.Handler(
                self.CreateTransferJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.storagetransfer.v1.transfer_pb2.CreateTransferJobRequest,
                google.storagetransfer.v1.transfer_types_pb2.TransferJob,
            ),
            '/google.storagetransfer.v1.StorageTransferService/UpdateTransferJob': grpclib.const.Handler(
                self.UpdateTransferJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.storagetransfer.v1.transfer_pb2.UpdateTransferJobRequest,
                google.storagetransfer.v1.transfer_types_pb2.TransferJob,
            ),
            '/google.storagetransfer.v1.StorageTransferService/GetTransferJob': grpclib.const.Handler(
                self.GetTransferJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.storagetransfer.v1.transfer_pb2.GetTransferJobRequest,
                google.storagetransfer.v1.transfer_types_pb2.TransferJob,
            ),
            '/google.storagetransfer.v1.StorageTransferService/ListTransferJobs': grpclib.const.Handler(
                self.ListTransferJobs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.storagetransfer.v1.transfer_pb2.ListTransferJobsRequest,
                google.storagetransfer.v1.transfer_pb2.ListTransferJobsResponse,
            ),
            '/google.storagetransfer.v1.StorageTransferService/PauseTransferOperation': grpclib.const.Handler(
                self.PauseTransferOperation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.storagetransfer.v1.transfer_pb2.PauseTransferOperationRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.storagetransfer.v1.StorageTransferService/ResumeTransferOperation': grpclib.const.Handler(
                self.ResumeTransferOperation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.storagetransfer.v1.transfer_pb2.ResumeTransferOperationRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.storagetransfer.v1.StorageTransferService/RunTransferJob': grpclib.const.Handler(
                self.RunTransferJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.storagetransfer.v1.transfer_pb2.RunTransferJobRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class StorageTransferServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetGoogleServiceAccount = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.storagetransfer.v1.StorageTransferService/GetGoogleServiceAccount',
            google.storagetransfer.v1.transfer_pb2.GetGoogleServiceAccountRequest,
            google.storagetransfer.v1.transfer_types_pb2.GoogleServiceAccount,
        )
        self.CreateTransferJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.storagetransfer.v1.StorageTransferService/CreateTransferJob',
            google.storagetransfer.v1.transfer_pb2.CreateTransferJobRequest,
            google.storagetransfer.v1.transfer_types_pb2.TransferJob,
        )
        self.UpdateTransferJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.storagetransfer.v1.StorageTransferService/UpdateTransferJob',
            google.storagetransfer.v1.transfer_pb2.UpdateTransferJobRequest,
            google.storagetransfer.v1.transfer_types_pb2.TransferJob,
        )
        self.GetTransferJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.storagetransfer.v1.StorageTransferService/GetTransferJob',
            google.storagetransfer.v1.transfer_pb2.GetTransferJobRequest,
            google.storagetransfer.v1.transfer_types_pb2.TransferJob,
        )
        self.ListTransferJobs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.storagetransfer.v1.StorageTransferService/ListTransferJobs',
            google.storagetransfer.v1.transfer_pb2.ListTransferJobsRequest,
            google.storagetransfer.v1.transfer_pb2.ListTransferJobsResponse,
        )
        self.PauseTransferOperation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.storagetransfer.v1.StorageTransferService/PauseTransferOperation',
            google.storagetransfer.v1.transfer_pb2.PauseTransferOperationRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ResumeTransferOperation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.storagetransfer.v1.StorageTransferService/ResumeTransferOperation',
            google.storagetransfer.v1.transfer_pb2.ResumeTransferOperationRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.RunTransferJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.storagetransfer.v1.StorageTransferService/RunTransferJob',
            google.storagetransfer.v1.transfer_pb2.RunTransferJobRequest,
            google.longrunning.operations_pb2.Operation,
        )
