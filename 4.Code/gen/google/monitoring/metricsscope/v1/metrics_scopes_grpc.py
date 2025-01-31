# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/monitoring/metricsscope/v1/metrics_scopes.proto
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
import google.monitoring.metricsscope.v1.metrics_scope_pb2
import google.protobuf.timestamp_pb2
import google.monitoring.metricsscope.v1.metrics_scopes_pb2


class MetricsScopesBase(abc.ABC):

    @abc.abstractmethod
    async def GetMetricsScope(self, stream: 'grpclib.server.Stream[google.monitoring.metricsscope.v1.metrics_scopes_pb2.GetMetricsScopeRequest, google.monitoring.metricsscope.v1.metrics_scope_pb2.MetricsScope]') -> None:
        pass

    @abc.abstractmethod
    async def ListMetricsScopesByMonitoredProject(self, stream: 'grpclib.server.Stream[google.monitoring.metricsscope.v1.metrics_scopes_pb2.ListMetricsScopesByMonitoredProjectRequest, google.monitoring.metricsscope.v1.metrics_scopes_pb2.ListMetricsScopesByMonitoredProjectResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateMonitoredProject(self, stream: 'grpclib.server.Stream[google.monitoring.metricsscope.v1.metrics_scopes_pb2.CreateMonitoredProjectRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteMonitoredProject(self, stream: 'grpclib.server.Stream[google.monitoring.metricsscope.v1.metrics_scopes_pb2.DeleteMonitoredProjectRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.monitoring.metricsscope.v1.MetricsScopes/GetMetricsScope': grpclib.const.Handler(
                self.GetMetricsScope,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.metricsscope.v1.metrics_scopes_pb2.GetMetricsScopeRequest,
                google.monitoring.metricsscope.v1.metrics_scope_pb2.MetricsScope,
            ),
            '/google.monitoring.metricsscope.v1.MetricsScopes/ListMetricsScopesByMonitoredProject': grpclib.const.Handler(
                self.ListMetricsScopesByMonitoredProject,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.metricsscope.v1.metrics_scopes_pb2.ListMetricsScopesByMonitoredProjectRequest,
                google.monitoring.metricsscope.v1.metrics_scopes_pb2.ListMetricsScopesByMonitoredProjectResponse,
            ),
            '/google.monitoring.metricsscope.v1.MetricsScopes/CreateMonitoredProject': grpclib.const.Handler(
                self.CreateMonitoredProject,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.metricsscope.v1.metrics_scopes_pb2.CreateMonitoredProjectRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.monitoring.metricsscope.v1.MetricsScopes/DeleteMonitoredProject': grpclib.const.Handler(
                self.DeleteMonitoredProject,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.monitoring.metricsscope.v1.metrics_scopes_pb2.DeleteMonitoredProjectRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class MetricsScopesStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetMetricsScope = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.metricsscope.v1.MetricsScopes/GetMetricsScope',
            google.monitoring.metricsscope.v1.metrics_scopes_pb2.GetMetricsScopeRequest,
            google.monitoring.metricsscope.v1.metrics_scope_pb2.MetricsScope,
        )
        self.ListMetricsScopesByMonitoredProject = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.metricsscope.v1.MetricsScopes/ListMetricsScopesByMonitoredProject',
            google.monitoring.metricsscope.v1.metrics_scopes_pb2.ListMetricsScopesByMonitoredProjectRequest,
            google.monitoring.metricsscope.v1.metrics_scopes_pb2.ListMetricsScopesByMonitoredProjectResponse,
        )
        self.CreateMonitoredProject = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.metricsscope.v1.MetricsScopes/CreateMonitoredProject',
            google.monitoring.metricsscope.v1.metrics_scopes_pb2.CreateMonitoredProjectRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteMonitoredProject = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.monitoring.metricsscope.v1.MetricsScopes/DeleteMonitoredProject',
            google.monitoring.metricsscope.v1.metrics_scopes_pb2.DeleteMonitoredProjectRequest,
            google.longrunning.operations_pb2.Operation,
        )
