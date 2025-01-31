# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/documentai/v1/document_processor_service.proto
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
import google.cloud.documentai.v1.document_pb2
import google.cloud.documentai.v1.document_io_pb2
import google.cloud.documentai.v1.operation_metadata_pb2
import google.longrunning.operations_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import google.cloud.documentai.v1.document_processor_service_pb2


class DocumentProcessorServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ProcessDocument(self, stream: 'grpclib.server.Stream[google.cloud.documentai.v1.document_processor_service_pb2.ProcessRequest, google.cloud.documentai.v1.document_processor_service_pb2.ProcessResponse]') -> None:
        pass

    @abc.abstractmethod
    async def BatchProcessDocuments(self, stream: 'grpclib.server.Stream[google.cloud.documentai.v1.document_processor_service_pb2.BatchProcessRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ReviewDocument(self, stream: 'grpclib.server.Stream[google.cloud.documentai.v1.document_processor_service_pb2.ReviewDocumentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.documentai.v1.DocumentProcessorService/ProcessDocument': grpclib.const.Handler(
                self.ProcessDocument,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.documentai.v1.document_processor_service_pb2.ProcessRequest,
                google.cloud.documentai.v1.document_processor_service_pb2.ProcessResponse,
            ),
            '/google.cloud.documentai.v1.DocumentProcessorService/BatchProcessDocuments': grpclib.const.Handler(
                self.BatchProcessDocuments,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.documentai.v1.document_processor_service_pb2.BatchProcessRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.documentai.v1.DocumentProcessorService/ReviewDocument': grpclib.const.Handler(
                self.ReviewDocument,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.documentai.v1.document_processor_service_pb2.ReviewDocumentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class DocumentProcessorServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ProcessDocument = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.documentai.v1.DocumentProcessorService/ProcessDocument',
            google.cloud.documentai.v1.document_processor_service_pb2.ProcessRequest,
            google.cloud.documentai.v1.document_processor_service_pb2.ProcessResponse,
        )
        self.BatchProcessDocuments = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.documentai.v1.DocumentProcessorService/BatchProcessDocuments',
            google.cloud.documentai.v1.document_processor_service_pb2.BatchProcessRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ReviewDocument = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.documentai.v1.DocumentProcessorService/ReviewDocument',
            google.cloud.documentai.v1.document_processor_service_pb2.ReviewDocumentRequest,
            google.longrunning.operations_pb2.Operation,
        )
