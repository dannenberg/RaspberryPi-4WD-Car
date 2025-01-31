# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/compute/v1small/compute_small.proto
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
import google.cloud.extended_operations_pb2
import google.cloud.compute.v1small.compute_small_pb2


class AddressesBase(abc.ABC):

    @abc.abstractmethod
    async def AggregatedList(self, stream: 'grpclib.server.Stream[google.cloud.compute.v1small.compute_small_pb2.AggregatedListAddressesRequest, google.cloud.compute.v1small.compute_small_pb2.AddressAggregatedList]') -> None:
        pass

    @abc.abstractmethod
    async def Delete(self, stream: 'grpclib.server.Stream[google.cloud.compute.v1small.compute_small_pb2.DeleteAddressRequest, google.cloud.compute.v1small.compute_small_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def Insert(self, stream: 'grpclib.server.Stream[google.cloud.compute.v1small.compute_small_pb2.InsertAddressRequest, google.cloud.compute.v1small.compute_small_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def List(self, stream: 'grpclib.server.Stream[google.cloud.compute.v1small.compute_small_pb2.ListAddressesRequest, google.cloud.compute.v1small.compute_small_pb2.AddressList]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.compute.v1small.Addresses/AggregatedList': grpclib.const.Handler(
                self.AggregatedList,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.compute.v1small.compute_small_pb2.AggregatedListAddressesRequest,
                google.cloud.compute.v1small.compute_small_pb2.AddressAggregatedList,
            ),
            '/google.cloud.compute.v1small.Addresses/Delete': grpclib.const.Handler(
                self.Delete,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.compute.v1small.compute_small_pb2.DeleteAddressRequest,
                google.cloud.compute.v1small.compute_small_pb2.Operation,
            ),
            '/google.cloud.compute.v1small.Addresses/Insert': grpclib.const.Handler(
                self.Insert,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.compute.v1small.compute_small_pb2.InsertAddressRequest,
                google.cloud.compute.v1small.compute_small_pb2.Operation,
            ),
            '/google.cloud.compute.v1small.Addresses/List': grpclib.const.Handler(
                self.List,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.compute.v1small.compute_small_pb2.ListAddressesRequest,
                google.cloud.compute.v1small.compute_small_pb2.AddressList,
            ),
        }


class AddressesStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.AggregatedList = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.compute.v1small.Addresses/AggregatedList',
            google.cloud.compute.v1small.compute_small_pb2.AggregatedListAddressesRequest,
            google.cloud.compute.v1small.compute_small_pb2.AddressAggregatedList,
        )
        self.Delete = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.compute.v1small.Addresses/Delete',
            google.cloud.compute.v1small.compute_small_pb2.DeleteAddressRequest,
            google.cloud.compute.v1small.compute_small_pb2.Operation,
        )
        self.Insert = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.compute.v1small.Addresses/Insert',
            google.cloud.compute.v1small.compute_small_pb2.InsertAddressRequest,
            google.cloud.compute.v1small.compute_small_pb2.Operation,
        )
        self.List = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.compute.v1small.Addresses/List',
            google.cloud.compute.v1small.compute_small_pb2.ListAddressesRequest,
            google.cloud.compute.v1small.compute_small_pb2.AddressList,
        )


class RegionOperationsBase(abc.ABC):

    @abc.abstractmethod
    async def Get(self, stream: 'grpclib.server.Stream[google.cloud.compute.v1small.compute_small_pb2.GetRegionOperationRequest, google.cloud.compute.v1small.compute_small_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def Wait(self, stream: 'grpclib.server.Stream[google.cloud.compute.v1small.compute_small_pb2.WaitRegionOperationRequest, google.cloud.compute.v1small.compute_small_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.compute.v1small.RegionOperations/Get': grpclib.const.Handler(
                self.Get,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.compute.v1small.compute_small_pb2.GetRegionOperationRequest,
                google.cloud.compute.v1small.compute_small_pb2.Operation,
            ),
            '/google.cloud.compute.v1small.RegionOperations/Wait': grpclib.const.Handler(
                self.Wait,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.compute.v1small.compute_small_pb2.WaitRegionOperationRequest,
                google.cloud.compute.v1small.compute_small_pb2.Operation,
            ),
        }


class RegionOperationsStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Get = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.compute.v1small.RegionOperations/Get',
            google.cloud.compute.v1small.compute_small_pb2.GetRegionOperationRequest,
            google.cloud.compute.v1small.compute_small_pb2.Operation,
        )
        self.Wait = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.compute.v1small.RegionOperations/Wait',
            google.cloud.compute.v1small.compute_small_pb2.WaitRegionOperationRequest,
            google.cloud.compute.v1small.compute_small_pb2.Operation,
        )
