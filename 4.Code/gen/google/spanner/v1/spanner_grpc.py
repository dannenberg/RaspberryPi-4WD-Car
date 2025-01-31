# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/spanner/v1/spanner.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.spanner.v1.commit_response_pb2
import google.api.annotations_pb2
import google.api.client_pb2
import google.api.field_behavior_pb2
import google.api.resource_pb2
import google.protobuf.empty_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import google.rpc.status_pb2
import google.spanner.v1.keys_pb2
import google.spanner.v1.mutation_pb2
import google.spanner.v1.result_set_pb2
import google.spanner.v1.transaction_pb2
import google.spanner.v1.type_pb2
import google.spanner.v1.spanner_pb2


class SpannerBase(abc.ABC):

    @abc.abstractmethod
    async def CreateSession(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.CreateSessionRequest, google.spanner.v1.spanner_pb2.Session]') -> None:
        pass

    @abc.abstractmethod
    async def BatchCreateSessions(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.BatchCreateSessionsRequest, google.spanner.v1.spanner_pb2.BatchCreateSessionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetSession(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.GetSessionRequest, google.spanner.v1.spanner_pb2.Session]') -> None:
        pass

    @abc.abstractmethod
    async def ListSessions(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.ListSessionsRequest, google.spanner.v1.spanner_pb2.ListSessionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteSession(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.DeleteSessionRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ExecuteSql(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.ExecuteSqlRequest, google.spanner.v1.result_set_pb2.ResultSet]') -> None:
        pass

    @abc.abstractmethod
    async def ExecuteStreamingSql(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.ExecuteSqlRequest, google.spanner.v1.result_set_pb2.PartialResultSet]') -> None:
        pass

    @abc.abstractmethod
    async def ExecuteBatchDml(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.ExecuteBatchDmlRequest, google.spanner.v1.spanner_pb2.ExecuteBatchDmlResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Read(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.ReadRequest, google.spanner.v1.result_set_pb2.ResultSet]') -> None:
        pass

    @abc.abstractmethod
    async def StreamingRead(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.ReadRequest, google.spanner.v1.result_set_pb2.PartialResultSet]') -> None:
        pass

    @abc.abstractmethod
    async def BeginTransaction(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.BeginTransactionRequest, google.spanner.v1.transaction_pb2.Transaction]') -> None:
        pass

    @abc.abstractmethod
    async def Commit(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.CommitRequest, google.spanner.v1.commit_response_pb2.CommitResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Rollback(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.RollbackRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def PartitionQuery(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.PartitionQueryRequest, google.spanner.v1.spanner_pb2.PartitionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PartitionRead(self, stream: 'grpclib.server.Stream[google.spanner.v1.spanner_pb2.PartitionReadRequest, google.spanner.v1.spanner_pb2.PartitionResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.spanner.v1.Spanner/CreateSession': grpclib.const.Handler(
                self.CreateSession,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.CreateSessionRequest,
                google.spanner.v1.spanner_pb2.Session,
            ),
            '/google.spanner.v1.Spanner/BatchCreateSessions': grpclib.const.Handler(
                self.BatchCreateSessions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.BatchCreateSessionsRequest,
                google.spanner.v1.spanner_pb2.BatchCreateSessionsResponse,
            ),
            '/google.spanner.v1.Spanner/GetSession': grpclib.const.Handler(
                self.GetSession,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.GetSessionRequest,
                google.spanner.v1.spanner_pb2.Session,
            ),
            '/google.spanner.v1.Spanner/ListSessions': grpclib.const.Handler(
                self.ListSessions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.ListSessionsRequest,
                google.spanner.v1.spanner_pb2.ListSessionsResponse,
            ),
            '/google.spanner.v1.Spanner/DeleteSession': grpclib.const.Handler(
                self.DeleteSession,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.DeleteSessionRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.spanner.v1.Spanner/ExecuteSql': grpclib.const.Handler(
                self.ExecuteSql,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.ExecuteSqlRequest,
                google.spanner.v1.result_set_pb2.ResultSet,
            ),
            '/google.spanner.v1.Spanner/ExecuteStreamingSql': grpclib.const.Handler(
                self.ExecuteStreamingSql,
                grpclib.const.Cardinality.UNARY_STREAM,
                google.spanner.v1.spanner_pb2.ExecuteSqlRequest,
                google.spanner.v1.result_set_pb2.PartialResultSet,
            ),
            '/google.spanner.v1.Spanner/ExecuteBatchDml': grpclib.const.Handler(
                self.ExecuteBatchDml,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.ExecuteBatchDmlRequest,
                google.spanner.v1.spanner_pb2.ExecuteBatchDmlResponse,
            ),
            '/google.spanner.v1.Spanner/Read': grpclib.const.Handler(
                self.Read,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.ReadRequest,
                google.spanner.v1.result_set_pb2.ResultSet,
            ),
            '/google.spanner.v1.Spanner/StreamingRead': grpclib.const.Handler(
                self.StreamingRead,
                grpclib.const.Cardinality.UNARY_STREAM,
                google.spanner.v1.spanner_pb2.ReadRequest,
                google.spanner.v1.result_set_pb2.PartialResultSet,
            ),
            '/google.spanner.v1.Spanner/BeginTransaction': grpclib.const.Handler(
                self.BeginTransaction,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.BeginTransactionRequest,
                google.spanner.v1.transaction_pb2.Transaction,
            ),
            '/google.spanner.v1.Spanner/Commit': grpclib.const.Handler(
                self.Commit,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.CommitRequest,
                google.spanner.v1.commit_response_pb2.CommitResponse,
            ),
            '/google.spanner.v1.Spanner/Rollback': grpclib.const.Handler(
                self.Rollback,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.RollbackRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.spanner.v1.Spanner/PartitionQuery': grpclib.const.Handler(
                self.PartitionQuery,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.PartitionQueryRequest,
                google.spanner.v1.spanner_pb2.PartitionResponse,
            ),
            '/google.spanner.v1.Spanner/PartitionRead': grpclib.const.Handler(
                self.PartitionRead,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.spanner.v1.spanner_pb2.PartitionReadRequest,
                google.spanner.v1.spanner_pb2.PartitionResponse,
            ),
        }


class SpannerStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateSession = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/CreateSession',
            google.spanner.v1.spanner_pb2.CreateSessionRequest,
            google.spanner.v1.spanner_pb2.Session,
        )
        self.BatchCreateSessions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/BatchCreateSessions',
            google.spanner.v1.spanner_pb2.BatchCreateSessionsRequest,
            google.spanner.v1.spanner_pb2.BatchCreateSessionsResponse,
        )
        self.GetSession = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/GetSession',
            google.spanner.v1.spanner_pb2.GetSessionRequest,
            google.spanner.v1.spanner_pb2.Session,
        )
        self.ListSessions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/ListSessions',
            google.spanner.v1.spanner_pb2.ListSessionsRequest,
            google.spanner.v1.spanner_pb2.ListSessionsResponse,
        )
        self.DeleteSession = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/DeleteSession',
            google.spanner.v1.spanner_pb2.DeleteSessionRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ExecuteSql = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/ExecuteSql',
            google.spanner.v1.spanner_pb2.ExecuteSqlRequest,
            google.spanner.v1.result_set_pb2.ResultSet,
        )
        self.ExecuteStreamingSql = grpclib.client.UnaryStreamMethod(
            channel,
            '/google.spanner.v1.Spanner/ExecuteStreamingSql',
            google.spanner.v1.spanner_pb2.ExecuteSqlRequest,
            google.spanner.v1.result_set_pb2.PartialResultSet,
        )
        self.ExecuteBatchDml = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/ExecuteBatchDml',
            google.spanner.v1.spanner_pb2.ExecuteBatchDmlRequest,
            google.spanner.v1.spanner_pb2.ExecuteBatchDmlResponse,
        )
        self.Read = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/Read',
            google.spanner.v1.spanner_pb2.ReadRequest,
            google.spanner.v1.result_set_pb2.ResultSet,
        )
        self.StreamingRead = grpclib.client.UnaryStreamMethod(
            channel,
            '/google.spanner.v1.Spanner/StreamingRead',
            google.spanner.v1.spanner_pb2.ReadRequest,
            google.spanner.v1.result_set_pb2.PartialResultSet,
        )
        self.BeginTransaction = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/BeginTransaction',
            google.spanner.v1.spanner_pb2.BeginTransactionRequest,
            google.spanner.v1.transaction_pb2.Transaction,
        )
        self.Commit = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/Commit',
            google.spanner.v1.spanner_pb2.CommitRequest,
            google.spanner.v1.commit_response_pb2.CommitResponse,
        )
        self.Rollback = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/Rollback',
            google.spanner.v1.spanner_pb2.RollbackRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.PartitionQuery = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/PartitionQuery',
            google.spanner.v1.spanner_pb2.PartitionQueryRequest,
            google.spanner.v1.spanner_pb2.PartitionResponse,
        )
        self.PartitionRead = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.spanner.v1.Spanner/PartitionRead',
            google.spanner.v1.spanner_pb2.PartitionReadRequest,
            google.spanner.v1.spanner_pb2.PartitionResponse,
        )
