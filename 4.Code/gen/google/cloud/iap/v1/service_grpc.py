# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/iap/v1/service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.api.field_behavior_pb2
import google.iam.v1.iam_policy_pb2
import google.iam.v1.policy_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.wrappers_pb2
import google.api.client_pb2
import google.cloud.iap.v1.service_pb2


class IdentityAwareProxyAdminServiceBase(abc.ABC):

    @abc.abstractmethod
    async def SetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def GetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def TestIamPermissions(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetIapSettings(self, stream: 'grpclib.server.Stream[google.cloud.iap.v1.service_pb2.GetIapSettingsRequest, google.cloud.iap.v1.service_pb2.IapSettings]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateIapSettings(self, stream: 'grpclib.server.Stream[google.cloud.iap.v1.service_pb2.UpdateIapSettingsRequest, google.cloud.iap.v1.service_pb2.IapSettings]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.iap.v1.IdentityAwareProxyAdminService/SetIamPolicy': grpclib.const.Handler(
                self.SetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.cloud.iap.v1.IdentityAwareProxyAdminService/GetIamPolicy': grpclib.const.Handler(
                self.GetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.cloud.iap.v1.IdentityAwareProxyAdminService/TestIamPermissions': grpclib.const.Handler(
                self.TestIamPermissions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
            ),
            '/google.cloud.iap.v1.IdentityAwareProxyAdminService/GetIapSettings': grpclib.const.Handler(
                self.GetIapSettings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.iap.v1.service_pb2.GetIapSettingsRequest,
                google.cloud.iap.v1.service_pb2.IapSettings,
            ),
            '/google.cloud.iap.v1.IdentityAwareProxyAdminService/UpdateIapSettings': grpclib.const.Handler(
                self.UpdateIapSettings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.iap.v1.service_pb2.UpdateIapSettingsRequest,
                google.cloud.iap.v1.service_pb2.IapSettings,
            ),
        }


class IdentityAwareProxyAdminServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyAdminService/SetIamPolicy',
            google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.GetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyAdminService/GetIamPolicy',
            google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.TestIamPermissions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyAdminService/TestIamPermissions',
            google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
        )
        self.GetIapSettings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyAdminService/GetIapSettings',
            google.cloud.iap.v1.service_pb2.GetIapSettingsRequest,
            google.cloud.iap.v1.service_pb2.IapSettings,
        )
        self.UpdateIapSettings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyAdminService/UpdateIapSettings',
            google.cloud.iap.v1.service_pb2.UpdateIapSettingsRequest,
            google.cloud.iap.v1.service_pb2.IapSettings,
        )


class IdentityAwareProxyOAuthServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ListBrands(self, stream: 'grpclib.server.Stream[google.cloud.iap.v1.service_pb2.ListBrandsRequest, google.cloud.iap.v1.service_pb2.ListBrandsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CreateBrand(self, stream: 'grpclib.server.Stream[google.cloud.iap.v1.service_pb2.CreateBrandRequest, google.cloud.iap.v1.service_pb2.Brand]') -> None:
        pass

    @abc.abstractmethod
    async def GetBrand(self, stream: 'grpclib.server.Stream[google.cloud.iap.v1.service_pb2.GetBrandRequest, google.cloud.iap.v1.service_pb2.Brand]') -> None:
        pass

    @abc.abstractmethod
    async def CreateIdentityAwareProxyClient(self, stream: 'grpclib.server.Stream[google.cloud.iap.v1.service_pb2.CreateIdentityAwareProxyClientRequest, google.cloud.iap.v1.service_pb2.IdentityAwareProxyClient]') -> None:
        pass

    @abc.abstractmethod
    async def ListIdentityAwareProxyClients(self, stream: 'grpclib.server.Stream[google.cloud.iap.v1.service_pb2.ListIdentityAwareProxyClientsRequest, google.cloud.iap.v1.service_pb2.ListIdentityAwareProxyClientsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetIdentityAwareProxyClient(self, stream: 'grpclib.server.Stream[google.cloud.iap.v1.service_pb2.GetIdentityAwareProxyClientRequest, google.cloud.iap.v1.service_pb2.IdentityAwareProxyClient]') -> None:
        pass

    @abc.abstractmethod
    async def ResetIdentityAwareProxyClientSecret(self, stream: 'grpclib.server.Stream[google.cloud.iap.v1.service_pb2.ResetIdentityAwareProxyClientSecretRequest, google.cloud.iap.v1.service_pb2.IdentityAwareProxyClient]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteIdentityAwareProxyClient(self, stream: 'grpclib.server.Stream[google.cloud.iap.v1.service_pb2.DeleteIdentityAwareProxyClientRequest, google.protobuf.empty_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/ListBrands': grpclib.const.Handler(
                self.ListBrands,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.iap.v1.service_pb2.ListBrandsRequest,
                google.cloud.iap.v1.service_pb2.ListBrandsResponse,
            ),
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/CreateBrand': grpclib.const.Handler(
                self.CreateBrand,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.iap.v1.service_pb2.CreateBrandRequest,
                google.cloud.iap.v1.service_pb2.Brand,
            ),
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/GetBrand': grpclib.const.Handler(
                self.GetBrand,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.iap.v1.service_pb2.GetBrandRequest,
                google.cloud.iap.v1.service_pb2.Brand,
            ),
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/CreateIdentityAwareProxyClient': grpclib.const.Handler(
                self.CreateIdentityAwareProxyClient,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.iap.v1.service_pb2.CreateIdentityAwareProxyClientRequest,
                google.cloud.iap.v1.service_pb2.IdentityAwareProxyClient,
            ),
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/ListIdentityAwareProxyClients': grpclib.const.Handler(
                self.ListIdentityAwareProxyClients,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.iap.v1.service_pb2.ListIdentityAwareProxyClientsRequest,
                google.cloud.iap.v1.service_pb2.ListIdentityAwareProxyClientsResponse,
            ),
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/GetIdentityAwareProxyClient': grpclib.const.Handler(
                self.GetIdentityAwareProxyClient,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.iap.v1.service_pb2.GetIdentityAwareProxyClientRequest,
                google.cloud.iap.v1.service_pb2.IdentityAwareProxyClient,
            ),
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/ResetIdentityAwareProxyClientSecret': grpclib.const.Handler(
                self.ResetIdentityAwareProxyClientSecret,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.iap.v1.service_pb2.ResetIdentityAwareProxyClientSecretRequest,
                google.cloud.iap.v1.service_pb2.IdentityAwareProxyClient,
            ),
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/DeleteIdentityAwareProxyClient': grpclib.const.Handler(
                self.DeleteIdentityAwareProxyClient,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.iap.v1.service_pb2.DeleteIdentityAwareProxyClientRequest,
                google.protobuf.empty_pb2.Empty,
            ),
        }


class IdentityAwareProxyOAuthServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListBrands = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/ListBrands',
            google.cloud.iap.v1.service_pb2.ListBrandsRequest,
            google.cloud.iap.v1.service_pb2.ListBrandsResponse,
        )
        self.CreateBrand = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/CreateBrand',
            google.cloud.iap.v1.service_pb2.CreateBrandRequest,
            google.cloud.iap.v1.service_pb2.Brand,
        )
        self.GetBrand = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/GetBrand',
            google.cloud.iap.v1.service_pb2.GetBrandRequest,
            google.cloud.iap.v1.service_pb2.Brand,
        )
        self.CreateIdentityAwareProxyClient = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/CreateIdentityAwareProxyClient',
            google.cloud.iap.v1.service_pb2.CreateIdentityAwareProxyClientRequest,
            google.cloud.iap.v1.service_pb2.IdentityAwareProxyClient,
        )
        self.ListIdentityAwareProxyClients = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/ListIdentityAwareProxyClients',
            google.cloud.iap.v1.service_pb2.ListIdentityAwareProxyClientsRequest,
            google.cloud.iap.v1.service_pb2.ListIdentityAwareProxyClientsResponse,
        )
        self.GetIdentityAwareProxyClient = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/GetIdentityAwareProxyClient',
            google.cloud.iap.v1.service_pb2.GetIdentityAwareProxyClientRequest,
            google.cloud.iap.v1.service_pb2.IdentityAwareProxyClient,
        )
        self.ResetIdentityAwareProxyClientSecret = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/ResetIdentityAwareProxyClientSecret',
            google.cloud.iap.v1.service_pb2.ResetIdentityAwareProxyClientSecretRequest,
            google.cloud.iap.v1.service_pb2.IdentityAwareProxyClient,
        )
        self.DeleteIdentityAwareProxyClient = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/DeleteIdentityAwareProxyClient',
            google.cloud.iap.v1.service_pb2.DeleteIdentityAwareProxyClientRequest,
            google.protobuf.empty_pb2.Empty,
        )
