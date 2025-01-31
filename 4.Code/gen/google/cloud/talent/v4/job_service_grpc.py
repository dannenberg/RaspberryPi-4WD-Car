# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/talent/v4/job_service.proto
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
import google.cloud.talent.v4.common_pb2
import google.cloud.talent.v4.filters_pb2
import google.cloud.talent.v4.histogram_pb2
import google.cloud.talent.v4.job_pb2
import google.longrunning.operations_pb2
import google.protobuf.any_pb2
import google.protobuf.duration_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.rpc.status_pb2
import google.cloud.talent.v4.job_service_pb2


class JobServiceBase(abc.ABC):

    @abc.abstractmethod
    async def CreateJob(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.job_service_pb2.CreateJobRequest, google.cloud.talent.v4.job_pb2.Job]') -> None:
        pass

    @abc.abstractmethod
    async def BatchCreateJobs(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.job_service_pb2.BatchCreateJobsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetJob(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.job_service_pb2.GetJobRequest, google.cloud.talent.v4.job_pb2.Job]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateJob(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.job_service_pb2.UpdateJobRequest, google.cloud.talent.v4.job_pb2.Job]') -> None:
        pass

    @abc.abstractmethod
    async def BatchUpdateJobs(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.job_service_pb2.BatchUpdateJobsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteJob(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.job_service_pb2.DeleteJobRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def BatchDeleteJobs(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.job_service_pb2.BatchDeleteJobsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ListJobs(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.job_service_pb2.ListJobsRequest, google.cloud.talent.v4.job_service_pb2.ListJobsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SearchJobs(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.job_service_pb2.SearchJobsRequest, google.cloud.talent.v4.job_service_pb2.SearchJobsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SearchJobsForAlert(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.job_service_pb2.SearchJobsRequest, google.cloud.talent.v4.job_service_pb2.SearchJobsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.talent.v4.JobService/CreateJob': grpclib.const.Handler(
                self.CreateJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.job_service_pb2.CreateJobRequest,
                google.cloud.talent.v4.job_pb2.Job,
            ),
            '/google.cloud.talent.v4.JobService/BatchCreateJobs': grpclib.const.Handler(
                self.BatchCreateJobs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.job_service_pb2.BatchCreateJobsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.talent.v4.JobService/GetJob': grpclib.const.Handler(
                self.GetJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.job_service_pb2.GetJobRequest,
                google.cloud.talent.v4.job_pb2.Job,
            ),
            '/google.cloud.talent.v4.JobService/UpdateJob': grpclib.const.Handler(
                self.UpdateJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.job_service_pb2.UpdateJobRequest,
                google.cloud.talent.v4.job_pb2.Job,
            ),
            '/google.cloud.talent.v4.JobService/BatchUpdateJobs': grpclib.const.Handler(
                self.BatchUpdateJobs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.job_service_pb2.BatchUpdateJobsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.talent.v4.JobService/DeleteJob': grpclib.const.Handler(
                self.DeleteJob,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.job_service_pb2.DeleteJobRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.talent.v4.JobService/BatchDeleteJobs': grpclib.const.Handler(
                self.BatchDeleteJobs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.job_service_pb2.BatchDeleteJobsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.talent.v4.JobService/ListJobs': grpclib.const.Handler(
                self.ListJobs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.job_service_pb2.ListJobsRequest,
                google.cloud.talent.v4.job_service_pb2.ListJobsResponse,
            ),
            '/google.cloud.talent.v4.JobService/SearchJobs': grpclib.const.Handler(
                self.SearchJobs,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.job_service_pb2.SearchJobsRequest,
                google.cloud.talent.v4.job_service_pb2.SearchJobsResponse,
            ),
            '/google.cloud.talent.v4.JobService/SearchJobsForAlert': grpclib.const.Handler(
                self.SearchJobsForAlert,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.job_service_pb2.SearchJobsRequest,
                google.cloud.talent.v4.job_service_pb2.SearchJobsResponse,
            ),
        }


class JobServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.JobService/CreateJob',
            google.cloud.talent.v4.job_service_pb2.CreateJobRequest,
            google.cloud.talent.v4.job_pb2.Job,
        )
        self.BatchCreateJobs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.JobService/BatchCreateJobs',
            google.cloud.talent.v4.job_service_pb2.BatchCreateJobsRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.JobService/GetJob',
            google.cloud.talent.v4.job_service_pb2.GetJobRequest,
            google.cloud.talent.v4.job_pb2.Job,
        )
        self.UpdateJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.JobService/UpdateJob',
            google.cloud.talent.v4.job_service_pb2.UpdateJobRequest,
            google.cloud.talent.v4.job_pb2.Job,
        )
        self.BatchUpdateJobs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.JobService/BatchUpdateJobs',
            google.cloud.talent.v4.job_service_pb2.BatchUpdateJobsRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteJob = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.JobService/DeleteJob',
            google.cloud.talent.v4.job_service_pb2.DeleteJobRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.BatchDeleteJobs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.JobService/BatchDeleteJobs',
            google.cloud.talent.v4.job_service_pb2.BatchDeleteJobsRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ListJobs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.JobService/ListJobs',
            google.cloud.talent.v4.job_service_pb2.ListJobsRequest,
            google.cloud.talent.v4.job_service_pb2.ListJobsResponse,
        )
        self.SearchJobs = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.JobService/SearchJobs',
            google.cloud.talent.v4.job_service_pb2.SearchJobsRequest,
            google.cloud.talent.v4.job_service_pb2.SearchJobsResponse,
        )
        self.SearchJobsForAlert = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.JobService/SearchJobsForAlert',
            google.cloud.talent.v4.job_service_pb2.SearchJobsRequest,
            google.cloud.talent.v4.job_service_pb2.SearchJobsResponse,
        )
