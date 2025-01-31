# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/genomics/v1/reads.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.genomics.v1.range_pb2
import google.genomics.v1.readalignment_pb2
import google.genomics.v1.readgroupset_pb2
import google.longrunning.operations_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.genomics.v1.reads_pb2


class StreamingReadServiceBase(abc.ABC):

    @abc.abstractmethod
    async def StreamReads(self, stream: 'grpclib.server.Stream[google.genomics.v1.reads_pb2.StreamReadsRequest, google.genomics.v1.reads_pb2.StreamReadsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.genomics.v1.StreamingReadService/StreamReads': grpclib.const.Handler(
                self.StreamReads,
                grpclib.const.Cardinality.UNARY_STREAM,
                google.genomics.v1.reads_pb2.StreamReadsRequest,
                google.genomics.v1.reads_pb2.StreamReadsResponse,
            ),
        }


class StreamingReadServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.StreamReads = grpclib.client.UnaryStreamMethod(
            channel,
            '/google.genomics.v1.StreamingReadService/StreamReads',
            google.genomics.v1.reads_pb2.StreamReadsRequest,
            google.genomics.v1.reads_pb2.StreamReadsResponse,
        )


class ReadServiceV1Base(abc.ABC):

    @abc.abstractmethod
    async def ImportReadGroupSets(self, stream: 'grpclib.server.Stream[google.genomics.v1.reads_pb2.ImportReadGroupSetsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def ExportReadGroupSet(self, stream: 'grpclib.server.Stream[google.genomics.v1.reads_pb2.ExportReadGroupSetRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def SearchReadGroupSets(self, stream: 'grpclib.server.Stream[google.genomics.v1.reads_pb2.SearchReadGroupSetsRequest, google.genomics.v1.reads_pb2.SearchReadGroupSetsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateReadGroupSet(self, stream: 'grpclib.server.Stream[google.genomics.v1.reads_pb2.UpdateReadGroupSetRequest, google.genomics.v1.readgroupset_pb2.ReadGroupSet]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteReadGroupSet(self, stream: 'grpclib.server.Stream[google.genomics.v1.reads_pb2.DeleteReadGroupSetRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def GetReadGroupSet(self, stream: 'grpclib.server.Stream[google.genomics.v1.reads_pb2.GetReadGroupSetRequest, google.genomics.v1.readgroupset_pb2.ReadGroupSet]') -> None:
        pass

    @abc.abstractmethod
    async def ListCoverageBuckets(self, stream: 'grpclib.server.Stream[google.genomics.v1.reads_pb2.ListCoverageBucketsRequest, google.genomics.v1.reads_pb2.ListCoverageBucketsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SearchReads(self, stream: 'grpclib.server.Stream[google.genomics.v1.reads_pb2.SearchReadsRequest, google.genomics.v1.reads_pb2.SearchReadsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.genomics.v1.ReadServiceV1/ImportReadGroupSets': grpclib.const.Handler(
                self.ImportReadGroupSets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.reads_pb2.ImportReadGroupSetsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.genomics.v1.ReadServiceV1/ExportReadGroupSet': grpclib.const.Handler(
                self.ExportReadGroupSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.reads_pb2.ExportReadGroupSetRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.genomics.v1.ReadServiceV1/SearchReadGroupSets': grpclib.const.Handler(
                self.SearchReadGroupSets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.reads_pb2.SearchReadGroupSetsRequest,
                google.genomics.v1.reads_pb2.SearchReadGroupSetsResponse,
            ),
            '/google.genomics.v1.ReadServiceV1/UpdateReadGroupSet': grpclib.const.Handler(
                self.UpdateReadGroupSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.reads_pb2.UpdateReadGroupSetRequest,
                google.genomics.v1.readgroupset_pb2.ReadGroupSet,
            ),
            '/google.genomics.v1.ReadServiceV1/DeleteReadGroupSet': grpclib.const.Handler(
                self.DeleteReadGroupSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.reads_pb2.DeleteReadGroupSetRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.genomics.v1.ReadServiceV1/GetReadGroupSet': grpclib.const.Handler(
                self.GetReadGroupSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.reads_pb2.GetReadGroupSetRequest,
                google.genomics.v1.readgroupset_pb2.ReadGroupSet,
            ),
            '/google.genomics.v1.ReadServiceV1/ListCoverageBuckets': grpclib.const.Handler(
                self.ListCoverageBuckets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.reads_pb2.ListCoverageBucketsRequest,
                google.genomics.v1.reads_pb2.ListCoverageBucketsResponse,
            ),
            '/google.genomics.v1.ReadServiceV1/SearchReads': grpclib.const.Handler(
                self.SearchReads,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.reads_pb2.SearchReadsRequest,
                google.genomics.v1.reads_pb2.SearchReadsResponse,
            ),
        }


class ReadServiceV1Stub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ImportReadGroupSets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.ReadServiceV1/ImportReadGroupSets',
            google.genomics.v1.reads_pb2.ImportReadGroupSetsRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.ExportReadGroupSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.ReadServiceV1/ExportReadGroupSet',
            google.genomics.v1.reads_pb2.ExportReadGroupSetRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.SearchReadGroupSets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.ReadServiceV1/SearchReadGroupSets',
            google.genomics.v1.reads_pb2.SearchReadGroupSetsRequest,
            google.genomics.v1.reads_pb2.SearchReadGroupSetsResponse,
        )
        self.UpdateReadGroupSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.ReadServiceV1/UpdateReadGroupSet',
            google.genomics.v1.reads_pb2.UpdateReadGroupSetRequest,
            google.genomics.v1.readgroupset_pb2.ReadGroupSet,
        )
        self.DeleteReadGroupSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.ReadServiceV1/DeleteReadGroupSet',
            google.genomics.v1.reads_pb2.DeleteReadGroupSetRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.GetReadGroupSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.ReadServiceV1/GetReadGroupSet',
            google.genomics.v1.reads_pb2.GetReadGroupSetRequest,
            google.genomics.v1.readgroupset_pb2.ReadGroupSet,
        )
        self.ListCoverageBuckets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.ReadServiceV1/ListCoverageBuckets',
            google.genomics.v1.reads_pb2.ListCoverageBucketsRequest,
            google.genomics.v1.reads_pb2.ListCoverageBucketsResponse,
        )
        self.SearchReads = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.ReadServiceV1/SearchReads',
            google.genomics.v1.reads_pb2.SearchReadsRequest,
            google.genomics.v1.reads_pb2.SearchReadsResponse,
        )
