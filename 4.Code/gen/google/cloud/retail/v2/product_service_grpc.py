# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/retail/v2/product_service.proto
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
import google.cloud.retail.v2.common_pb2
import google.cloud.retail.v2.import_config_pb2
import google.cloud.retail.v2.product_pb2
import google.cloud.retail.v2.purge_config_pb2
import google.longrunning.operations_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.retail.v2.product_service_pb2


class ProductServiceBase(abc.ABC):

    @abc.abstractmethod
    async def CreateProduct(self, stream: 'grpclib.server.Stream[google.cloud.retail.v2.product_service_pb2.CreateProductRequest, google.cloud.retail.v2.product_pb2.Product]') -> None:
        pass

    @abc.abstractmethod
    async def GetProduct(self, stream: 'grpclib.server.Stream[google.cloud.retail.v2.product_service_pb2.GetProductRequest, google.cloud.retail.v2.product_pb2.Product]') -> None:
        pass

    @abc.abstractmethod
    async def ListProducts(self, stream: 'grpclib.server.Stream[google.cloud.retail.v2.product_service_pb2.ListProductsRequest, google.cloud.retail.v2.product_service_pb2.ListProductsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateProduct(self, stream: 'grpclib.server.Stream[google.cloud.retail.v2.product_service_pb2.UpdateProductRequest, google.cloud.retail.v2.product_pb2.Product]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteProduct(self, stream: 'grpclib.server.Stream[google.cloud.retail.v2.product_service_pb2.DeleteProductRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ImportProducts(self, stream: 'grpclib.server.Stream[google.cloud.retail.v2.import_config_pb2.ImportProductsRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def SetInventory(self, stream: 'grpclib.server.Stream[google.cloud.retail.v2.product_service_pb2.SetInventoryRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def AddFulfillmentPlaces(self, stream: 'grpclib.server.Stream[google.cloud.retail.v2.product_service_pb2.AddFulfillmentPlacesRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def RemoveFulfillmentPlaces(self, stream: 'grpclib.server.Stream[google.cloud.retail.v2.product_service_pb2.RemoveFulfillmentPlacesRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.retail.v2.ProductService/CreateProduct': grpclib.const.Handler(
                self.CreateProduct,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.retail.v2.product_service_pb2.CreateProductRequest,
                google.cloud.retail.v2.product_pb2.Product,
            ),
            '/google.cloud.retail.v2.ProductService/GetProduct': grpclib.const.Handler(
                self.GetProduct,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.retail.v2.product_service_pb2.GetProductRequest,
                google.cloud.retail.v2.product_pb2.Product,
            ),
            '/google.cloud.retail.v2.ProductService/ListProducts': grpclib.const.Handler(
                self.ListProducts,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.retail.v2.product_service_pb2.ListProductsRequest,
                google.cloud.retail.v2.product_service_pb2.ListProductsResponse,
            ),
            '/google.cloud.retail.v2.ProductService/UpdateProduct': grpclib.const.Handler(
                self.UpdateProduct,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.retail.v2.product_service_pb2.UpdateProductRequest,
                google.cloud.retail.v2.product_pb2.Product,
            ),
            '/google.cloud.retail.v2.ProductService/DeleteProduct': grpclib.const.Handler(
                self.DeleteProduct,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.retail.v2.product_service_pb2.DeleteProductRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.retail.v2.ProductService/ImportProducts': grpclib.const.Handler(
                self.ImportProducts,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.retail.v2.import_config_pb2.ImportProductsRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.retail.v2.ProductService/SetInventory': grpclib.const.Handler(
                self.SetInventory,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.retail.v2.product_service_pb2.SetInventoryRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.retail.v2.ProductService/AddFulfillmentPlaces': grpclib.const.Handler(
                self.AddFulfillmentPlaces,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.retail.v2.product_service_pb2.AddFulfillmentPlacesRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.retail.v2.ProductService/RemoveFulfillmentPlaces': grpclib.const.Handler(
                self.RemoveFulfillmentPlaces,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.retail.v2.product_service_pb2.RemoveFulfillmentPlacesRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class ProductServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateProduct = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.retail.v2.ProductService/CreateProduct',
            google.cloud.retail.v2.product_service_pb2.CreateProductRequest,
            google.cloud.retail.v2.product_pb2.Product,
        )
        self.GetProduct = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.retail.v2.ProductService/GetProduct',
            google.cloud.retail.v2.product_service_pb2.GetProductRequest,
            google.cloud.retail.v2.product_pb2.Product,
        )
        self.ListProducts = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.retail.v2.ProductService/ListProducts',
            google.cloud.retail.v2.product_service_pb2.ListProductsRequest,
            google.cloud.retail.v2.product_service_pb2.ListProductsResponse,
        )
        self.UpdateProduct = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.retail.v2.ProductService/UpdateProduct',
            google.cloud.retail.v2.product_service_pb2.UpdateProductRequest,
            google.cloud.retail.v2.product_pb2.Product,
        )
        self.DeleteProduct = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.retail.v2.ProductService/DeleteProduct',
            google.cloud.retail.v2.product_service_pb2.DeleteProductRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ImportProducts = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.retail.v2.ProductService/ImportProducts',
            google.cloud.retail.v2.import_config_pb2.ImportProductsRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.SetInventory = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.retail.v2.ProductService/SetInventory',
            google.cloud.retail.v2.product_service_pb2.SetInventoryRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.AddFulfillmentPlaces = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.retail.v2.ProductService/AddFulfillmentPlaces',
            google.cloud.retail.v2.product_service_pb2.AddFulfillmentPlacesRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.RemoveFulfillmentPlaces = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.retail.v2.ProductService/RemoveFulfillmentPlaces',
            google.cloud.retail.v2.product_service_pb2.RemoveFulfillmentPlacesRequest,
            google.longrunning.operations_pb2.Operation,
        )
