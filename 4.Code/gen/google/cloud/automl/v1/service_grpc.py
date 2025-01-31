# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/automl/v1/service.proto
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
import google.cloud.automl.v1.annotation_payload_pb2
import google.cloud.automl.v1.annotation_spec_pb2
import google.cloud.automl.v1.dataset_pb2
import google.cloud.automl.v1.image_pb2
import google.cloud.automl.v1.io_pb2
import google.cloud.automl.v1.model_pb2
import google.cloud.automl.v1.model_evaluation_pb2
import google.cloud.automl.v1.operations_pb2
import google.longrunning.operations_pb2
import google.protobuf.field_mask_pb2
import google.cloud.automl.v1.service_pb2


class AutoMlBase(abc.ABC):

    @abc.abstractmethod
    async def CreateDataset(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.CreateDatasetRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetDataset(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.GetDatasetRequest, google.cloud.automl.v1.dataset_pb2.Dataset]') -> None:
        pass

    @abc.abstractmethod
    async def ListDatasets(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.ListDatasetsRequest, google.cloud.automl.v1.service_pb2.ListDatasetsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateDataset(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.UpdateDatasetRequest, google.cloud.automl.v1.dataset_pb2.Dataset]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteDataset(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.DeleteDatasetRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ImportData(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.ImportDataRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ExportData(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.ExportDataRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetAnnotationSpec(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.GetAnnotationSpecRequest, google.cloud.automl.v1.annotation_spec_pb2.AnnotationSpec]') -> None:
        pass

    @abc.abstractmethod
    async def CreateModel(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.CreateModelRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetModel(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.GetModelRequest, google.cloud.automl.v1.model_pb2.Model]') -> None:
        pass

    @abc.abstractmethod
    async def ListModels(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.ListModelsRequest, google.cloud.automl.v1.service_pb2.ListModelsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteModel(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.DeleteModelRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateModel(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.UpdateModelRequest, google.cloud.automl.v1.model_pb2.Model]') -> None:
        pass

    @abc.abstractmethod
    async def DeployModel(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.DeployModelRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UndeployModel(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.UndeployModelRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ExportModel(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.ExportModelRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetModelEvaluation(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.GetModelEvaluationRequest, google.cloud.automl.v1.model_evaluation_pb2.ModelEvaluation]') -> None:
        pass

    @abc.abstractmethod
    async def ListModelEvaluations(self, stream: 'grpclib.server.Stream[google.cloud.automl.v1.service_pb2.ListModelEvaluationsRequest, google.cloud.automl.v1.service_pb2.ListModelEvaluationsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.automl.v1.AutoMl/CreateDataset': grpclib.const.Handler(
                self.CreateDataset,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.CreateDatasetRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.automl.v1.AutoMl/GetDataset': grpclib.const.Handler(
                self.GetDataset,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.GetDatasetRequest,
                google.cloud.automl.v1.dataset_pb2.Dataset,
            ),
            '/google.cloud.automl.v1.AutoMl/ListDatasets': grpclib.const.Handler(
                self.ListDatasets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.ListDatasetsRequest,
                google.cloud.automl.v1.service_pb2.ListDatasetsResponse,
            ),
            '/google.cloud.automl.v1.AutoMl/UpdateDataset': grpclib.const.Handler(
                self.UpdateDataset,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.UpdateDatasetRequest,
                google.cloud.automl.v1.dataset_pb2.Dataset,
            ),
            '/google.cloud.automl.v1.AutoMl/DeleteDataset': grpclib.const.Handler(
                self.DeleteDataset,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.DeleteDatasetRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.automl.v1.AutoMl/ImportData': grpclib.const.Handler(
                self.ImportData,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.ImportDataRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.automl.v1.AutoMl/ExportData': grpclib.const.Handler(
                self.ExportData,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.ExportDataRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.automl.v1.AutoMl/GetAnnotationSpec': grpclib.const.Handler(
                self.GetAnnotationSpec,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.GetAnnotationSpecRequest,
                google.cloud.automl.v1.annotation_spec_pb2.AnnotationSpec,
            ),
            '/google.cloud.automl.v1.AutoMl/CreateModel': grpclib.const.Handler(
                self.CreateModel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.CreateModelRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.automl.v1.AutoMl/GetModel': grpclib.const.Handler(
                self.GetModel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.GetModelRequest,
                google.cloud.automl.v1.model_pb2.Model,
            ),
            '/google.cloud.automl.v1.AutoMl/ListModels': grpclib.const.Handler(
                self.ListModels,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.ListModelsRequest,
                google.cloud.automl.v1.service_pb2.ListModelsResponse,
            ),
            '/google.cloud.automl.v1.AutoMl/DeleteModel': grpclib.const.Handler(
                self.DeleteModel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.DeleteModelRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.automl.v1.AutoMl/UpdateModel': grpclib.const.Handler(
                self.UpdateModel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.UpdateModelRequest,
                google.cloud.automl.v1.model_pb2.Model,
            ),
            '/google.cloud.automl.v1.AutoMl/DeployModel': grpclib.const.Handler(
                self.DeployModel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.DeployModelRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.automl.v1.AutoMl/UndeployModel': grpclib.const.Handler(
                self.UndeployModel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.UndeployModelRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.automl.v1.AutoMl/ExportModel': grpclib.const.Handler(
                self.ExportModel,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.ExportModelRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.automl.v1.AutoMl/GetModelEvaluation': grpclib.const.Handler(
                self.GetModelEvaluation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.GetModelEvaluationRequest,
                google.cloud.automl.v1.model_evaluation_pb2.ModelEvaluation,
            ),
            '/google.cloud.automl.v1.AutoMl/ListModelEvaluations': grpclib.const.Handler(
                self.ListModelEvaluations,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.automl.v1.service_pb2.ListModelEvaluationsRequest,
                google.cloud.automl.v1.service_pb2.ListModelEvaluationsResponse,
            ),
        }


class AutoMlStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateDataset = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/CreateDataset',
            google.cloud.automl.v1.service_pb2.CreateDatasetRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetDataset = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/GetDataset',
            google.cloud.automl.v1.service_pb2.GetDatasetRequest,
            google.cloud.automl.v1.dataset_pb2.Dataset,
        )
        self.ListDatasets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/ListDatasets',
            google.cloud.automl.v1.service_pb2.ListDatasetsRequest,
            google.cloud.automl.v1.service_pb2.ListDatasetsResponse,
        )
        self.UpdateDataset = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/UpdateDataset',
            google.cloud.automl.v1.service_pb2.UpdateDatasetRequest,
            google.cloud.automl.v1.dataset_pb2.Dataset,
        )
        self.DeleteDataset = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/DeleteDataset',
            google.cloud.automl.v1.service_pb2.DeleteDatasetRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ImportData = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/ImportData',
            google.cloud.automl.v1.service_pb2.ImportDataRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ExportData = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/ExportData',
            google.cloud.automl.v1.service_pb2.ExportDataRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetAnnotationSpec = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/GetAnnotationSpec',
            google.cloud.automl.v1.service_pb2.GetAnnotationSpecRequest,
            google.cloud.automl.v1.annotation_spec_pb2.AnnotationSpec,
        )
        self.CreateModel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/CreateModel',
            google.cloud.automl.v1.service_pb2.CreateModelRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetModel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/GetModel',
            google.cloud.automl.v1.service_pb2.GetModelRequest,
            google.cloud.automl.v1.model_pb2.Model,
        )
        self.ListModels = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/ListModels',
            google.cloud.automl.v1.service_pb2.ListModelsRequest,
            google.cloud.automl.v1.service_pb2.ListModelsResponse,
        )
        self.DeleteModel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/DeleteModel',
            google.cloud.automl.v1.service_pb2.DeleteModelRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateModel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/UpdateModel',
            google.cloud.automl.v1.service_pb2.UpdateModelRequest,
            google.cloud.automl.v1.model_pb2.Model,
        )
        self.DeployModel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/DeployModel',
            google.cloud.automl.v1.service_pb2.DeployModelRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UndeployModel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/UndeployModel',
            google.cloud.automl.v1.service_pb2.UndeployModelRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ExportModel = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/ExportModel',
            google.cloud.automl.v1.service_pb2.ExportModelRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetModelEvaluation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/GetModelEvaluation',
            google.cloud.automl.v1.service_pb2.GetModelEvaluationRequest,
            google.cloud.automl.v1.model_evaluation_pb2.ModelEvaluation,
        )
        self.ListModelEvaluations = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.automl.v1.AutoMl/ListModelEvaluations',
            google.cloud.automl.v1.service_pb2.ListModelEvaluationsRequest,
            google.cloud.automl.v1.service_pb2.ListModelEvaluationsResponse,
        )
