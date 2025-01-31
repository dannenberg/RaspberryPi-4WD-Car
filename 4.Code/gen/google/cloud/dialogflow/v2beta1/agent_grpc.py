# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/dialogflow/v2beta1/agent.proto
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
import google.cloud.dialogflow.v2beta1.environment_pb2
import google.cloud.dialogflow.v2beta1.validation_result_pb2
import google.longrunning.operations_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.cloud.dialogflow.v2beta1.agent_pb2


class AgentsBase(abc.ABC):

    @abc.abstractmethod
    async def GetAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.agent_pb2.GetAgentRequest, google.cloud.dialogflow.v2beta1.agent_pb2.Agent]') -> None:
        pass

    @abc.abstractmethod
    async def SetAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.agent_pb2.SetAgentRequest, google.cloud.dialogflow.v2beta1.agent_pb2.Agent]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.agent_pb2.DeleteAgentRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def SearchAgents(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.agent_pb2.SearchAgentsRequest, google.cloud.dialogflow.v2beta1.agent_pb2.SearchAgentsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TrainAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.agent_pb2.TrainAgentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ExportAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.agent_pb2.ExportAgentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ImportAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.agent_pb2.ImportAgentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def RestoreAgent(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.agent_pb2.RestoreAgentRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetValidationResult(self, stream: 'grpclib.server.Stream[google.cloud.dialogflow.v2beta1.agent_pb2.GetValidationResultRequest, google.cloud.dialogflow.v2beta1.validation_result_pb2.ValidationResult]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.dialogflow.v2beta1.Agents/GetAgent': grpclib.const.Handler(
                self.GetAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.agent_pb2.GetAgentRequest,
                google.cloud.dialogflow.v2beta1.agent_pb2.Agent,
            ),
            '/google.cloud.dialogflow.v2beta1.Agents/SetAgent': grpclib.const.Handler(
                self.SetAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.agent_pb2.SetAgentRequest,
                google.cloud.dialogflow.v2beta1.agent_pb2.Agent,
            ),
            '/google.cloud.dialogflow.v2beta1.Agents/DeleteAgent': grpclib.const.Handler(
                self.DeleteAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.agent_pb2.DeleteAgentRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.dialogflow.v2beta1.Agents/SearchAgents': grpclib.const.Handler(
                self.SearchAgents,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.agent_pb2.SearchAgentsRequest,
                google.cloud.dialogflow.v2beta1.agent_pb2.SearchAgentsResponse,
            ),
            '/google.cloud.dialogflow.v2beta1.Agents/TrainAgent': grpclib.const.Handler(
                self.TrainAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.agent_pb2.TrainAgentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.dialogflow.v2beta1.Agents/ExportAgent': grpclib.const.Handler(
                self.ExportAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.agent_pb2.ExportAgentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.dialogflow.v2beta1.Agents/ImportAgent': grpclib.const.Handler(
                self.ImportAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.agent_pb2.ImportAgentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.dialogflow.v2beta1.Agents/RestoreAgent': grpclib.const.Handler(
                self.RestoreAgent,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.agent_pb2.RestoreAgentRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.dialogflow.v2beta1.Agents/GetValidationResult': grpclib.const.Handler(
                self.GetValidationResult,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.dialogflow.v2beta1.agent_pb2.GetValidationResultRequest,
                google.cloud.dialogflow.v2beta1.validation_result_pb2.ValidationResult,
            ),
        }


class AgentsStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Agents/GetAgent',
            google.cloud.dialogflow.v2beta1.agent_pb2.GetAgentRequest,
            google.cloud.dialogflow.v2beta1.agent_pb2.Agent,
        )
        self.SetAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Agents/SetAgent',
            google.cloud.dialogflow.v2beta1.agent_pb2.SetAgentRequest,
            google.cloud.dialogflow.v2beta1.agent_pb2.Agent,
        )
        self.DeleteAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Agents/DeleteAgent',
            google.cloud.dialogflow.v2beta1.agent_pb2.DeleteAgentRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.SearchAgents = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Agents/SearchAgents',
            google.cloud.dialogflow.v2beta1.agent_pb2.SearchAgentsRequest,
            google.cloud.dialogflow.v2beta1.agent_pb2.SearchAgentsResponse,
        )
        self.TrainAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Agents/TrainAgent',
            google.cloud.dialogflow.v2beta1.agent_pb2.TrainAgentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ExportAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Agents/ExportAgent',
            google.cloud.dialogflow.v2beta1.agent_pb2.ExportAgentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ImportAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Agents/ImportAgent',
            google.cloud.dialogflow.v2beta1.agent_pb2.ImportAgentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.RestoreAgent = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Agents/RestoreAgent',
            google.cloud.dialogflow.v2beta1.agent_pb2.RestoreAgentRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetValidationResult = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.dialogflow.v2beta1.Agents/GetValidationResult',
            google.cloud.dialogflow.v2beta1.agent_pb2.GetValidationResultRequest,
            google.cloud.dialogflow.v2beta1.validation_result_pb2.ValidationResult,
        )
