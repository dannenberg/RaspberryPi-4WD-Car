# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/aiplatform/v1/metadata_service.proto
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
import google.cloud.aiplatform.v1.artifact_pb2
import google.cloud.aiplatform.v1.context_pb2
import google.cloud.aiplatform.v1.event_pb2
import google.cloud.aiplatform.v1.execution_pb2
import google.cloud.aiplatform.v1.lineage_subgraph_pb2
import google.cloud.aiplatform.v1.metadata_schema_pb2
import google.cloud.aiplatform.v1.metadata_store_pb2
import google.cloud.aiplatform.v1.operation_pb2
import google.longrunning.operations_pb2
import google.protobuf.field_mask_pb2
import google.cloud.aiplatform.v1.metadata_service_pb2


class MetadataServiceBase(abc.ABC):

    @abc.abstractmethod
    async def CreateMetadataStore(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.CreateMetadataStoreRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetMetadataStore(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.GetMetadataStoreRequest, google.cloud.aiplatform.v1.metadata_store_pb2.MetadataStore]') -> None:
        pass

    @abc.abstractmethod
    async def ListMetadataStores(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.ListMetadataStoresRequest, google.cloud.aiplatform.v1.metadata_service_pb2.ListMetadataStoresResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteMetadataStore(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.DeleteMetadataStoreRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def CreateArtifact(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.CreateArtifactRequest, google.cloud.aiplatform.v1.artifact_pb2.Artifact]') -> None:
        pass

    @abc.abstractmethod
    async def GetArtifact(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.GetArtifactRequest, google.cloud.aiplatform.v1.artifact_pb2.Artifact]') -> None:
        pass

    @abc.abstractmethod
    async def ListArtifacts(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.ListArtifactsRequest, google.cloud.aiplatform.v1.metadata_service_pb2.ListArtifactsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateArtifact(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.UpdateArtifactRequest, google.cloud.aiplatform.v1.artifact_pb2.Artifact]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteArtifact(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.DeleteArtifactRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def PurgeArtifacts(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.PurgeArtifactsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def CreateContext(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.CreateContextRequest, google.cloud.aiplatform.v1.context_pb2.Context]') -> None:
        pass

    @abc.abstractmethod
    async def GetContext(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.GetContextRequest, google.cloud.aiplatform.v1.context_pb2.Context]') -> None:
        pass

    @abc.abstractmethod
    async def ListContexts(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.ListContextsRequest, google.cloud.aiplatform.v1.metadata_service_pb2.ListContextsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateContext(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.UpdateContextRequest, google.cloud.aiplatform.v1.context_pb2.Context]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteContext(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.DeleteContextRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def PurgeContexts(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.PurgeContextsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def AddContextArtifactsAndExecutions(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.AddContextArtifactsAndExecutionsRequest, google.cloud.aiplatform.v1.metadata_service_pb2.AddContextArtifactsAndExecutionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def AddContextChildren(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.AddContextChildrenRequest, google.cloud.aiplatform.v1.metadata_service_pb2.AddContextChildrenResponse]') -> None:
        pass

    @abc.abstractmethod
    async def QueryContextLineageSubgraph(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.QueryContextLineageSubgraphRequest, google.cloud.aiplatform.v1.lineage_subgraph_pb2.LineageSubgraph]') -> None:
        pass

    @abc.abstractmethod
    async def CreateExecution(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.CreateExecutionRequest, google.cloud.aiplatform.v1.execution_pb2.Execution]') -> None:
        pass

    @abc.abstractmethod
    async def GetExecution(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.GetExecutionRequest, google.cloud.aiplatform.v1.execution_pb2.Execution]') -> None:
        pass

    @abc.abstractmethod
    async def ListExecutions(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.ListExecutionsRequest, google.cloud.aiplatform.v1.metadata_service_pb2.ListExecutionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateExecution(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.UpdateExecutionRequest, google.cloud.aiplatform.v1.execution_pb2.Execution]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteExecution(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.DeleteExecutionRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def PurgeExecutions(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.PurgeExecutionsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def AddExecutionEvents(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.AddExecutionEventsRequest, google.cloud.aiplatform.v1.metadata_service_pb2.AddExecutionEventsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def QueryExecutionInputsAndOutputs(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.QueryExecutionInputsAndOutputsRequest, google.cloud.aiplatform.v1.lineage_subgraph_pb2.LineageSubgraph]') -> None:
        pass

    @abc.abstractmethod
    async def CreateMetadataSchema(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.CreateMetadataSchemaRequest, google.cloud.aiplatform.v1.metadata_schema_pb2.MetadataSchema]') -> None:
        pass

    @abc.abstractmethod
    async def GetMetadataSchema(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.GetMetadataSchemaRequest, google.cloud.aiplatform.v1.metadata_schema_pb2.MetadataSchema]') -> None:
        pass

    @abc.abstractmethod
    async def ListMetadataSchemas(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.ListMetadataSchemasRequest, google.cloud.aiplatform.v1.metadata_service_pb2.ListMetadataSchemasResponse]') -> None:
        pass

    @abc.abstractmethod
    async def QueryArtifactLineageSubgraph(self, stream: 'grpclib.server.Stream[google.cloud.aiplatform.v1.metadata_service_pb2.QueryArtifactLineageSubgraphRequest, google.cloud.aiplatform.v1.lineage_subgraph_pb2.LineageSubgraph]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.aiplatform.v1.MetadataService/CreateMetadataStore': grpclib.const.Handler(
                self.CreateMetadataStore,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.CreateMetadataStoreRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/GetMetadataStore': grpclib.const.Handler(
                self.GetMetadataStore,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.GetMetadataStoreRequest,
                google.cloud.aiplatform.v1.metadata_store_pb2.MetadataStore,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/ListMetadataStores': grpclib.const.Handler(
                self.ListMetadataStores,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.ListMetadataStoresRequest,
                google.cloud.aiplatform.v1.metadata_service_pb2.ListMetadataStoresResponse,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/DeleteMetadataStore': grpclib.const.Handler(
                self.DeleteMetadataStore,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.DeleteMetadataStoreRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/CreateArtifact': grpclib.const.Handler(
                self.CreateArtifact,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.CreateArtifactRequest,
                google.cloud.aiplatform.v1.artifact_pb2.Artifact,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/GetArtifact': grpclib.const.Handler(
                self.GetArtifact,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.GetArtifactRequest,
                google.cloud.aiplatform.v1.artifact_pb2.Artifact,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/ListArtifacts': grpclib.const.Handler(
                self.ListArtifacts,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.ListArtifactsRequest,
                google.cloud.aiplatform.v1.metadata_service_pb2.ListArtifactsResponse,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/UpdateArtifact': grpclib.const.Handler(
                self.UpdateArtifact,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.UpdateArtifactRequest,
                google.cloud.aiplatform.v1.artifact_pb2.Artifact,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/DeleteArtifact': grpclib.const.Handler(
                self.DeleteArtifact,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.DeleteArtifactRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/PurgeArtifacts': grpclib.const.Handler(
                self.PurgeArtifacts,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.PurgeArtifactsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/CreateContext': grpclib.const.Handler(
                self.CreateContext,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.CreateContextRequest,
                google.cloud.aiplatform.v1.context_pb2.Context,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/GetContext': grpclib.const.Handler(
                self.GetContext,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.GetContextRequest,
                google.cloud.aiplatform.v1.context_pb2.Context,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/ListContexts': grpclib.const.Handler(
                self.ListContexts,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.ListContextsRequest,
                google.cloud.aiplatform.v1.metadata_service_pb2.ListContextsResponse,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/UpdateContext': grpclib.const.Handler(
                self.UpdateContext,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.UpdateContextRequest,
                google.cloud.aiplatform.v1.context_pb2.Context,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/DeleteContext': grpclib.const.Handler(
                self.DeleteContext,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.DeleteContextRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/PurgeContexts': grpclib.const.Handler(
                self.PurgeContexts,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.PurgeContextsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/AddContextArtifactsAndExecutions': grpclib.const.Handler(
                self.AddContextArtifactsAndExecutions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.AddContextArtifactsAndExecutionsRequest,
                google.cloud.aiplatform.v1.metadata_service_pb2.AddContextArtifactsAndExecutionsResponse,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/AddContextChildren': grpclib.const.Handler(
                self.AddContextChildren,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.AddContextChildrenRequest,
                google.cloud.aiplatform.v1.metadata_service_pb2.AddContextChildrenResponse,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/QueryContextLineageSubgraph': grpclib.const.Handler(
                self.QueryContextLineageSubgraph,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.QueryContextLineageSubgraphRequest,
                google.cloud.aiplatform.v1.lineage_subgraph_pb2.LineageSubgraph,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/CreateExecution': grpclib.const.Handler(
                self.CreateExecution,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.CreateExecutionRequest,
                google.cloud.aiplatform.v1.execution_pb2.Execution,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/GetExecution': grpclib.const.Handler(
                self.GetExecution,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.GetExecutionRequest,
                google.cloud.aiplatform.v1.execution_pb2.Execution,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/ListExecutions': grpclib.const.Handler(
                self.ListExecutions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.ListExecutionsRequest,
                google.cloud.aiplatform.v1.metadata_service_pb2.ListExecutionsResponse,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/UpdateExecution': grpclib.const.Handler(
                self.UpdateExecution,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.UpdateExecutionRequest,
                google.cloud.aiplatform.v1.execution_pb2.Execution,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/DeleteExecution': grpclib.const.Handler(
                self.DeleteExecution,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.DeleteExecutionRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/PurgeExecutions': grpclib.const.Handler(
                self.PurgeExecutions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.PurgeExecutionsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/AddExecutionEvents': grpclib.const.Handler(
                self.AddExecutionEvents,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.AddExecutionEventsRequest,
                google.cloud.aiplatform.v1.metadata_service_pb2.AddExecutionEventsResponse,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/QueryExecutionInputsAndOutputs': grpclib.const.Handler(
                self.QueryExecutionInputsAndOutputs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.QueryExecutionInputsAndOutputsRequest,
                google.cloud.aiplatform.v1.lineage_subgraph_pb2.LineageSubgraph,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/CreateMetadataSchema': grpclib.const.Handler(
                self.CreateMetadataSchema,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.CreateMetadataSchemaRequest,
                google.cloud.aiplatform.v1.metadata_schema_pb2.MetadataSchema,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/GetMetadataSchema': grpclib.const.Handler(
                self.GetMetadataSchema,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.GetMetadataSchemaRequest,
                google.cloud.aiplatform.v1.metadata_schema_pb2.MetadataSchema,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/ListMetadataSchemas': grpclib.const.Handler(
                self.ListMetadataSchemas,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.ListMetadataSchemasRequest,
                google.cloud.aiplatform.v1.metadata_service_pb2.ListMetadataSchemasResponse,
            ),
            '/google.cloud.aiplatform.v1.MetadataService/QueryArtifactLineageSubgraph': grpclib.const.Handler(
                self.QueryArtifactLineageSubgraph,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.aiplatform.v1.metadata_service_pb2.QueryArtifactLineageSubgraphRequest,
                google.cloud.aiplatform.v1.lineage_subgraph_pb2.LineageSubgraph,
            ),
        }


class MetadataServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateMetadataStore = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/CreateMetadataStore',
            google.cloud.aiplatform.v1.metadata_service_pb2.CreateMetadataStoreRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetMetadataStore = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/GetMetadataStore',
            google.cloud.aiplatform.v1.metadata_service_pb2.GetMetadataStoreRequest,
            google.cloud.aiplatform.v1.metadata_store_pb2.MetadataStore,
        )
        self.ListMetadataStores = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/ListMetadataStores',
            google.cloud.aiplatform.v1.metadata_service_pb2.ListMetadataStoresRequest,
            google.cloud.aiplatform.v1.metadata_service_pb2.ListMetadataStoresResponse,
        )
        self.DeleteMetadataStore = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/DeleteMetadataStore',
            google.cloud.aiplatform.v1.metadata_service_pb2.DeleteMetadataStoreRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.CreateArtifact = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/CreateArtifact',
            google.cloud.aiplatform.v1.metadata_service_pb2.CreateArtifactRequest,
            google.cloud.aiplatform.v1.artifact_pb2.Artifact,
        )
        self.GetArtifact = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/GetArtifact',
            google.cloud.aiplatform.v1.metadata_service_pb2.GetArtifactRequest,
            google.cloud.aiplatform.v1.artifact_pb2.Artifact,
        )
        self.ListArtifacts = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/ListArtifacts',
            google.cloud.aiplatform.v1.metadata_service_pb2.ListArtifactsRequest,
            google.cloud.aiplatform.v1.metadata_service_pb2.ListArtifactsResponse,
        )
        self.UpdateArtifact = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/UpdateArtifact',
            google.cloud.aiplatform.v1.metadata_service_pb2.UpdateArtifactRequest,
            google.cloud.aiplatform.v1.artifact_pb2.Artifact,
        )
        self.DeleteArtifact = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/DeleteArtifact',
            google.cloud.aiplatform.v1.metadata_service_pb2.DeleteArtifactRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.PurgeArtifacts = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/PurgeArtifacts',
            google.cloud.aiplatform.v1.metadata_service_pb2.PurgeArtifactsRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.CreateContext = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/CreateContext',
            google.cloud.aiplatform.v1.metadata_service_pb2.CreateContextRequest,
            google.cloud.aiplatform.v1.context_pb2.Context,
        )
        self.GetContext = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/GetContext',
            google.cloud.aiplatform.v1.metadata_service_pb2.GetContextRequest,
            google.cloud.aiplatform.v1.context_pb2.Context,
        )
        self.ListContexts = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/ListContexts',
            google.cloud.aiplatform.v1.metadata_service_pb2.ListContextsRequest,
            google.cloud.aiplatform.v1.metadata_service_pb2.ListContextsResponse,
        )
        self.UpdateContext = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/UpdateContext',
            google.cloud.aiplatform.v1.metadata_service_pb2.UpdateContextRequest,
            google.cloud.aiplatform.v1.context_pb2.Context,
        )
        self.DeleteContext = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/DeleteContext',
            google.cloud.aiplatform.v1.metadata_service_pb2.DeleteContextRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.PurgeContexts = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/PurgeContexts',
            google.cloud.aiplatform.v1.metadata_service_pb2.PurgeContextsRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.AddContextArtifactsAndExecutions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/AddContextArtifactsAndExecutions',
            google.cloud.aiplatform.v1.metadata_service_pb2.AddContextArtifactsAndExecutionsRequest,
            google.cloud.aiplatform.v1.metadata_service_pb2.AddContextArtifactsAndExecutionsResponse,
        )
        self.AddContextChildren = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/AddContextChildren',
            google.cloud.aiplatform.v1.metadata_service_pb2.AddContextChildrenRequest,
            google.cloud.aiplatform.v1.metadata_service_pb2.AddContextChildrenResponse,
        )
        self.QueryContextLineageSubgraph = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/QueryContextLineageSubgraph',
            google.cloud.aiplatform.v1.metadata_service_pb2.QueryContextLineageSubgraphRequest,
            google.cloud.aiplatform.v1.lineage_subgraph_pb2.LineageSubgraph,
        )
        self.CreateExecution = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/CreateExecution',
            google.cloud.aiplatform.v1.metadata_service_pb2.CreateExecutionRequest,
            google.cloud.aiplatform.v1.execution_pb2.Execution,
        )
        self.GetExecution = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/GetExecution',
            google.cloud.aiplatform.v1.metadata_service_pb2.GetExecutionRequest,
            google.cloud.aiplatform.v1.execution_pb2.Execution,
        )
        self.ListExecutions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/ListExecutions',
            google.cloud.aiplatform.v1.metadata_service_pb2.ListExecutionsRequest,
            google.cloud.aiplatform.v1.metadata_service_pb2.ListExecutionsResponse,
        )
        self.UpdateExecution = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/UpdateExecution',
            google.cloud.aiplatform.v1.metadata_service_pb2.UpdateExecutionRequest,
            google.cloud.aiplatform.v1.execution_pb2.Execution,
        )
        self.DeleteExecution = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/DeleteExecution',
            google.cloud.aiplatform.v1.metadata_service_pb2.DeleteExecutionRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.PurgeExecutions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/PurgeExecutions',
            google.cloud.aiplatform.v1.metadata_service_pb2.PurgeExecutionsRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.AddExecutionEvents = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/AddExecutionEvents',
            google.cloud.aiplatform.v1.metadata_service_pb2.AddExecutionEventsRequest,
            google.cloud.aiplatform.v1.metadata_service_pb2.AddExecutionEventsResponse,
        )
        self.QueryExecutionInputsAndOutputs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/QueryExecutionInputsAndOutputs',
            google.cloud.aiplatform.v1.metadata_service_pb2.QueryExecutionInputsAndOutputsRequest,
            google.cloud.aiplatform.v1.lineage_subgraph_pb2.LineageSubgraph,
        )
        self.CreateMetadataSchema = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/CreateMetadataSchema',
            google.cloud.aiplatform.v1.metadata_service_pb2.CreateMetadataSchemaRequest,
            google.cloud.aiplatform.v1.metadata_schema_pb2.MetadataSchema,
        )
        self.GetMetadataSchema = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/GetMetadataSchema',
            google.cloud.aiplatform.v1.metadata_service_pb2.GetMetadataSchemaRequest,
            google.cloud.aiplatform.v1.metadata_schema_pb2.MetadataSchema,
        )
        self.ListMetadataSchemas = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/ListMetadataSchemas',
            google.cloud.aiplatform.v1.metadata_service_pb2.ListMetadataSchemasRequest,
            google.cloud.aiplatform.v1.metadata_service_pb2.ListMetadataSchemasResponse,
        )
        self.QueryArtifactLineageSubgraph = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.aiplatform.v1.MetadataService/QueryArtifactLineageSubgraph',
            google.cloud.aiplatform.v1.metadata_service_pb2.QueryArtifactLineageSubgraphRequest,
            google.cloud.aiplatform.v1.lineage_subgraph_pb2.LineageSubgraph,
        )
