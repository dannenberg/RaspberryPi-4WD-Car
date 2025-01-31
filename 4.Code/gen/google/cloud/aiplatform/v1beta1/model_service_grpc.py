# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/aiplatform/v1beta1/model_service.proto
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
import google.cloud.aiplatform.v1beta1.io_pb2
import google.cloud.aiplatform.v1beta1.model_pb2
import google.cloud.aiplatform.v1beta1.model_evaluation_pb2
import google.cloud.aiplatform.v1beta1.model_evaluation_slice_pb2
import google.cloud.aiplatform.v1beta1.operation_pb2
import google.longrunning.operations_pb2
import google.protobuf.field_mask_pb2
import google.cloud.aiplatform.v1beta1.model_service_pb2


class ModelServiceBase(abc.ABC):

    @abc.abstractmethod
    async def UploadModel(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.model_service_pb2.UploadModelRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetModel(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.model_service_pb2.GetModelRequest, google.cloud.aiplatform.v1beta1.model_pb2.Model]') -> None:
        pass

    @abc.abstractmethod
    async def ListModels(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelsRequest, google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateModel(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.model_service_pb2.UpdateModelRequest, google.cloud.aiplatform.v1beta1.model_pb2.Model]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteModel(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.model_service_pb2.DeleteModelRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ExportModel(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.model_service_pb2.ExportModelRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetModelEvaluation(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.model_service_pb2.GetModelEvaluationRequest, google.cloud.aiplatform.v1beta1.model_evaluation_pb2.ModelEvaluation]') -> None:
        pass

    @abc.abstractmethod
    async def ListModelEvaluations(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelEvaluationsRequest, google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelEvaluationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetModelEvaluationSlice(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.model_service_pb2.GetModelEvaluationSliceRequest, google.cloud.aiplatform.v1beta1.model_evaluation_slice_pb2.ModelEvaluationSlice]') -> None:
        pass

    @abc.abstractmethod
    async def ListModelEvaluationSlices(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelEvaluationSlicesRequest, google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelEvaluationSlicesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.aiplatform.v1beta1.ModelService/UploadModel': grpclib.const.Handler(
                self.UploadModel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.model_service_pb2.UploadModelRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.aiplatform.v1beta1.ModelService/GetModel': grpclib.const.Handler(
                self.GetModel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.model_service_pb2.GetModelRequest,
                google.cloud.aiplatform.v1beta1.model_pb2.Model,
            ),
            '/google.cloud.aiplatform.v1beta1.ModelService/ListModels': grpclib.const.Handler(
                self.ListModels,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelsRequest,
                google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelsResponse,
            ),
            '/google.cloud.aiplatform.v1beta1.ModelService/UpdateModel': grpclib.const.Handler(
                self.UpdateModel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.model_service_pb2.UpdateModelRequest,
                google.cloud.aiplatform.v1beta1.model_pb2.Model,
            ),
            '/google.cloud.aiplatform.v1beta1.ModelService/DeleteModel': grpclib.const.Handler(
                self.DeleteModel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.model_service_pb2.DeleteModelRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.aiplatform.v1beta1.ModelService/ExportModel': grpclib.const.Handler(
                self.ExportModel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.model_service_pb2.ExportModelRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.aiplatform.v1beta1.ModelService/GetModelEvaluation': grpclib.const.Handler(
                self.GetModelEvaluation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.model_service_pb2.GetModelEvaluationRequest,
                google.cloud.aiplatform.v1beta1.model_evaluation_pb2.ModelEvaluation,
            ),
            '/google.cloud.aiplatform.v1beta1.ModelService/ListModelEvaluations': grpclib.const.Handler(
                self.ListModelEvaluations,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelEvaluationsRequest,
                google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelEvaluationsResponse,
            ),
            '/google.cloud.aiplatform.v1beta1.ModelService/GetModelEvaluationSlice': grpclib.const.Handler(
                self.GetModelEvaluationSlice,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.model_service_pb2.GetModelEvaluationSliceRequest,
                google.cloud.aiplatform.v1beta1.model_evaluation_slice_pb2.ModelEvaluationSlice,
            ),
            '/google.cloud.aiplatform.v1beta1.ModelService/ListModelEvaluationSlices': grpclib.const.Handler(
                self.ListModelEvaluationSlices,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelEvaluationSlicesRequest,
                google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelEvaluationSlicesResponse,
            ),
        }


class ModelServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.UploadModel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.ModelService/UploadModel',
            google.cloud.aiplatform.v1beta1.model_service_pb2.UploadModelRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetModel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.ModelService/GetModel',
            google.cloud.aiplatform.v1beta1.model_service_pb2.GetModelRequest,
            google.cloud.aiplatform.v1beta1.model_pb2.Model,
        )
        self.ListModels = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.ModelService/ListModels',
            google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelsRequest,
            google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelsResponse,
        )
        self.UpdateModel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.ModelService/UpdateModel',
            google.cloud.aiplatform.v1beta1.model_service_pb2.UpdateModelRequest,
            google.cloud.aiplatform.v1beta1.model_pb2.Model,
        )
        self.DeleteModel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.ModelService/DeleteModel',
            google.cloud.aiplatform.v1beta1.model_service_pb2.DeleteModelRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ExportModel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.ModelService/ExportModel',
            google.cloud.aiplatform.v1beta1.model_service_pb2.ExportModelRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetModelEvaluation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.ModelService/GetModelEvaluation',
            google.cloud.aiplatform.v1beta1.model_service_pb2.GetModelEvaluationRequest,
            google.cloud.aiplatform.v1beta1.model_evaluation_pb2.ModelEvaluation,
        )
        self.ListModelEvaluations = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.ModelService/ListModelEvaluations',
            google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelEvaluationsRequest,
            google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelEvaluationsResponse,
        )
        self.GetModelEvaluationSlice = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.ModelService/GetModelEvaluationSlice',
            google.cloud.aiplatform.v1beta1.model_service_pb2.GetModelEvaluationSliceRequest,
            google.cloud.aiplatform.v1beta1.model_evaluation_slice_pb2.ModelEvaluationSlice,
        )
        self.ListModelEvaluationSlices = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1beta1.ModelService/ListModelEvaluationSlices',
            google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelEvaluationSlicesRequest,
            google.cloud.aiplatform.v1beta1.model_service_pb2.ListModelEvaluationSlicesResponse,
        )
