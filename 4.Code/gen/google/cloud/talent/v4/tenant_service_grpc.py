# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/talent/v4/tenant_service.proto
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
import google.cloud.talent.v4.tenant_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.cloud.talent.v4.tenant_service_pb2


class TenantServiceBase(abc.ABC):

    @abc.abstractmethod
    async def CreateTenant(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.tenant_service_pb2.CreateTenantRequest, google.cloud.talent.v4.tenant_pb2.Tenant]') -> None:
        pass

    @abc.abstractmethod
    async def GetTenant(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.tenant_service_pb2.GetTenantRequest, google.cloud.talent.v4.tenant_pb2.Tenant]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateTenant(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.tenant_service_pb2.UpdateTenantRequest, google.cloud.talent.v4.tenant_pb2.Tenant]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteTenant(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.tenant_service_pb2.DeleteTenantRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    @abc.abstractmethod
    async def ListTenants(self, stream: 'grpclib.server.Stream[google.cloud.talent.v4.tenant_service_pb2.ListTenantsRequest, google.cloud.talent.v4.tenant_service_pb2.ListTenantsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.talent.v4.TenantService/CreateTenant': grpclib.const.Handler(
                self.CreateTenant,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.tenant_service_pb2.CreateTenantRequest,
                google.cloud.talent.v4.tenant_pb2.Tenant,
            ),
            '/google.cloud.talent.v4.TenantService/GetTenant': grpclib.const.Handler(
                self.GetTenant,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.tenant_service_pb2.GetTenantRequest,
                google.cloud.talent.v4.tenant_pb2.Tenant,
            ),
            '/google.cloud.talent.v4.TenantService/UpdateTenant': grpclib.const.Handler(
                self.UpdateTenant,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.tenant_service_pb2.UpdateTenantRequest,
                google.cloud.talent.v4.tenant_pb2.Tenant,
            ),
            '/google.cloud.talent.v4.TenantService/DeleteTenant': grpclib.const.Handler(
                self.DeleteTenant,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.tenant_service_pb2.DeleteTenantRequest,
                google.protobuf.empty_pb2.Empty,
            ),
            '/google.cloud.talent.v4.TenantService/ListTenants': grpclib.const.Handler(
                self.ListTenants,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.talent.v4.tenant_service_pb2.ListTenantsRequest,
                google.cloud.talent.v4.tenant_service_pb2.ListTenantsResponse,
            ),
        }


class TenantServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateTenant = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.TenantService/CreateTenant',
            google.cloud.talent.v4.tenant_service_pb2.CreateTenantRequest,
            google.cloud.talent.v4.tenant_pb2.Tenant,
        )
        self.GetTenant = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.TenantService/GetTenant',
            google.cloud.talent.v4.tenant_service_pb2.GetTenantRequest,
            google.cloud.talent.v4.tenant_pb2.Tenant,
        )
        self.UpdateTenant = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.TenantService/UpdateTenant',
            google.cloud.talent.v4.tenant_service_pb2.UpdateTenantRequest,
            google.cloud.talent.v4.tenant_pb2.Tenant,
        )
        self.DeleteTenant = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.TenantService/DeleteTenant',
            google.cloud.talent.v4.tenant_service_pb2.DeleteTenantRequest,
            google.protobuf.empty_pb2.Empty,
        )
        self.ListTenants = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.talent.v4.TenantService/ListTenants',
            google.cloud.talent.v4.tenant_service_pb2.ListTenantsRequest,
            google.cloud.talent.v4.tenant_service_pb2.ListTenantsResponse,
        )
