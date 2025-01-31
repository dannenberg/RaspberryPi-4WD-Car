# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/genomics/v1/annotations.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.struct_pb2
import google.protobuf.wrappers_pb2
import google.rpc.status_pb2
import google.genomics.v1.annotations_pb2


class AnnotationServiceV1Base(abc.ABC):

    @abc.abstractmethod
    async def CreateAnnotationSet(self, stream: 'grpclib.server.Stream[google.genomics.v1.annotations_pb2.CreateAnnotationSetRequest, google.genomics.v1.annotations_pb2.AnnotationSet]') -> None:
        pass

    @abc.abstractmethod
    async def GetAnnotationSet(self, stream: 'grpclib.server.Stream[google.genomics.v1.annotations_pb2.GetAnnotationSetRequest, google.genomics.v1.annotations_pb2.AnnotationSet]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateAnnotationSet(self, stream: 'grpclib.server.Stream[google.genomics.v1.annotations_pb2.UpdateAnnotationSetRequest, google.genomics.v1.annotations_pb2.AnnotationSet]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteAnnotationSet(self, stream: 'grpclib.server.Stream[google.genomics.v1.annotations_pb2.DeleteAnnotationSetRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def SearchAnnotationSets(self, stream: 'grpclib.server.Stream[google.genomics.v1.annotations_pb2.SearchAnnotationSetsRequest, google.genomics.v1.annotations_pb2.SearchAnnotationSetsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateAnnotation(self, stream: 'grpclib.server.Stream[google.genomics.v1.annotations_pb2.CreateAnnotationRequest, google.genomics.v1.annotations_pb2.Annotation]') -> None:
        pass

    @abc.abstractmethod
    async def BatchCreateAnnotations(self, stream: 'grpclib.server.Stream[google.genomics.v1.annotations_pb2.BatchCreateAnnotationsRequest, google.genomics.v1.annotations_pb2.BatchCreateAnnotationsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetAnnotation(self, stream: 'grpclib.server.Stream[google.genomics.v1.annotations_pb2.GetAnnotationRequest, google.genomics.v1.annotations_pb2.Annotation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateAnnotation(self, stream: 'grpclib.server.Stream[google.genomics.v1.annotations_pb2.UpdateAnnotationRequest, google.genomics.v1.annotations_pb2.Annotation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteAnnotation(self, stream: 'grpclib.server.Stream[google.genomics.v1.annotations_pb2.DeleteAnnotationRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def SearchAnnotations(self, stream: 'grpclib.server.Stream[google.genomics.v1.annotations_pb2.SearchAnnotationsRequest, google.genomics.v1.annotations_pb2.SearchAnnotationsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.genomics.v1.AnnotationServiceV1/CreateAnnotationSet': grpclib.const.Handler(
                self.CreateAnnotationSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.annotations_pb2.CreateAnnotationSetRequest,
                google.genomics.v1.annotations_pb2.AnnotationSet,
            ),
            '/google.genomics.v1.AnnotationServiceV1/GetAnnotationSet': grpclib.const.Handler(
                self.GetAnnotationSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.annotations_pb2.GetAnnotationSetRequest,
                google.genomics.v1.annotations_pb2.AnnotationSet,
            ),
            '/google.genomics.v1.AnnotationServiceV1/UpdateAnnotationSet': grpclib.const.Handler(
                self.UpdateAnnotationSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.annotations_pb2.UpdateAnnotationSetRequest,
                google.genomics.v1.annotations_pb2.AnnotationSet,
            ),
            '/google.genomics.v1.AnnotationServiceV1/DeleteAnnotationSet': grpclib.const.Handler(
                self.DeleteAnnotationSet,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.annotations_pb2.DeleteAnnotationSetRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.genomics.v1.AnnotationServiceV1/SearchAnnotationSets': grpclib.const.Handler(
                self.SearchAnnotationSets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.annotations_pb2.SearchAnnotationSetsRequest,
                google.genomics.v1.annotations_pb2.SearchAnnotationSetsResponse,
            ),
            '/google.genomics.v1.AnnotationServiceV1/CreateAnnotation': grpclib.const.Handler(
                self.CreateAnnotation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.annotations_pb2.CreateAnnotationRequest,
                google.genomics.v1.annotations_pb2.Annotation,
            ),
            '/google.genomics.v1.AnnotationServiceV1/BatchCreateAnnotations': grpclib.const.Handler(
                self.BatchCreateAnnotations,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.annotations_pb2.BatchCreateAnnotationsRequest,
                google.genomics.v1.annotations_pb2.BatchCreateAnnotationsResponse,
            ),
            '/google.genomics.v1.AnnotationServiceV1/GetAnnotation': grpclib.const.Handler(
                self.GetAnnotation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.annotations_pb2.GetAnnotationRequest,
                google.genomics.v1.annotations_pb2.Annotation,
            ),
            '/google.genomics.v1.AnnotationServiceV1/UpdateAnnotation': grpclib.const.Handler(
                self.UpdateAnnotation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.annotations_pb2.UpdateAnnotationRequest,
                google.genomics.v1.annotations_pb2.Annotation,
            ),
            '/google.genomics.v1.AnnotationServiceV1/DeleteAnnotation': grpclib.const.Handler(
                self.DeleteAnnotation,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.annotations_pb2.DeleteAnnotationRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.genomics.v1.AnnotationServiceV1/SearchAnnotations': grpclib.const.Handler(
                self.SearchAnnotations,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.genomics.v1.annotations_pb2.SearchAnnotationsRequest,
                google.genomics.v1.annotations_pb2.SearchAnnotationsResponse,
            ),
        }


class AnnotationServiceV1Stub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateAnnotationSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.AnnotationServiceV1/CreateAnnotationSet',
            google.genomics.v1.annotations_pb2.CreateAnnotationSetRequest,
            google.genomics.v1.annotations_pb2.AnnotationSet,
        )
        self.GetAnnotationSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.AnnotationServiceV1/GetAnnotationSet',
            google.genomics.v1.annotations_pb2.GetAnnotationSetRequest,
            google.genomics.v1.annotations_pb2.AnnotationSet,
        )
        self.UpdateAnnotationSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.AnnotationServiceV1/UpdateAnnotationSet',
            google.genomics.v1.annotations_pb2.UpdateAnnotationSetRequest,
            google.genomics.v1.annotations_pb2.AnnotationSet,
        )
        self.DeleteAnnotationSet = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.AnnotationServiceV1/DeleteAnnotationSet',
            google.genomics.v1.annotations_pb2.DeleteAnnotationSetRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.SearchAnnotationSets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.AnnotationServiceV1/SearchAnnotationSets',
            google.genomics.v1.annotations_pb2.SearchAnnotationSetsRequest,
            google.genomics.v1.annotations_pb2.SearchAnnotationSetsResponse,
        )
        self.CreateAnnotation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.AnnotationServiceV1/CreateAnnotation',
            google.genomics.v1.annotations_pb2.CreateAnnotationRequest,
            google.genomics.v1.annotations_pb2.Annotation,
        )
        self.BatchCreateAnnotations = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.AnnotationServiceV1/BatchCreateAnnotations',
            google.genomics.v1.annotations_pb2.BatchCreateAnnotationsRequest,
            google.genomics.v1.annotations_pb2.BatchCreateAnnotationsResponse,
        )
        self.GetAnnotation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.AnnotationServiceV1/GetAnnotation',
            google.genomics.v1.annotations_pb2.GetAnnotationRequest,
            google.genomics.v1.annotations_pb2.Annotation,
        )
        self.UpdateAnnotation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.AnnotationServiceV1/UpdateAnnotation',
            google.genomics.v1.annotations_pb2.UpdateAnnotationRequest,
            google.genomics.v1.annotations_pb2.Annotation,
        )
        self.DeleteAnnotation = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.AnnotationServiceV1/DeleteAnnotation',
            google.genomics.v1.annotations_pb2.DeleteAnnotationRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.SearchAnnotations = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.genomics.v1.AnnotationServiceV1/SearchAnnotations',
            google.genomics.v1.annotations_pb2.SearchAnnotationsRequest,
            google.genomics.v1.annotations_pb2.SearchAnnotationsResponse,
        )
