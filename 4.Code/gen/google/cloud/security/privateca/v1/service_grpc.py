# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/security/privateca/v1/service.proto
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
import google.cloud.security.privateca.v1.resources_pb2
import google.longrunning.operations_pb2
import google.protobuf.duration_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.security.privateca.v1.service_pb2


class CertificateAuthorityServiceBase(abc.ABC):

    @abc.abstractmethod
    async def CreateCertificate(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.CreateCertificateRequest, google.cloud.security.privateca.v1.resources_pb2.Certificate]') -> None:
        pass

    @abc.abstractmethod
    async def GetCertificate(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.GetCertificateRequest, google.cloud.security.privateca.v1.resources_pb2.Certificate]') -> None:
        pass

    @abc.abstractmethod
    async def ListCertificates(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.ListCertificatesRequest, google.cloud.security.privateca.v1.service_pb2.ListCertificatesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RevokeCertificate(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.RevokeCertificateRequest, google.cloud.security.privateca.v1.resources_pb2.Certificate]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateCertificate(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.UpdateCertificateRequest, google.cloud.security.privateca.v1.resources_pb2.Certificate]') -> None:
        pass

    @abc.abstractmethod
    async def ActivateCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.ActivateCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def CreateCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.CreateCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DisableCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.DisableCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def EnableCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.EnableCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def FetchCertificateAuthorityCsr(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.FetchCertificateAuthorityCsrRequest, google.cloud.security.privateca.v1.service_pb2.FetchCertificateAuthorityCsrResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.GetCertificateAuthorityRequest, google.cloud.security.privateca.v1.resources_pb2.CertificateAuthority]') -> None:
        pass

    @abc.abstractmethod
    async def ListCertificateAuthorities(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.ListCertificateAuthoritiesRequest, google.cloud.security.privateca.v1.service_pb2.ListCertificateAuthoritiesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UndeleteCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.UndeleteCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.DeleteCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateCertificateAuthority(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.UpdateCertificateAuthorityRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def CreateCaPool(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.CreateCaPoolRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateCaPool(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.UpdateCaPoolRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetCaPool(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.GetCaPoolRequest, google.cloud.security.privateca.v1.resources_pb2.CaPool]') -> None:
        pass

    @abc.abstractmethod
    async def ListCaPools(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.ListCaPoolsRequest, google.cloud.security.privateca.v1.service_pb2.ListCaPoolsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteCaPool(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.DeleteCaPoolRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def FetchCaCerts(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.FetchCaCertsRequest, google.cloud.security.privateca.v1.service_pb2.FetchCaCertsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetCertificateRevocationList(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.GetCertificateRevocationListRequest, google.cloud.security.privateca.v1.resources_pb2.CertificateRevocationList]') -> None:
        pass

    @abc.abstractmethod
    async def ListCertificateRevocationLists(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.ListCertificateRevocationListsRequest, google.cloud.security.privateca.v1.service_pb2.ListCertificateRevocationListsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateCertificateRevocationList(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.UpdateCertificateRevocationListRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def CreateCertificateTemplate(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.CreateCertificateTemplateRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteCertificateTemplate(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.DeleteCertificateTemplateRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def GetCertificateTemplate(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.GetCertificateTemplateRequest, google.cloud.security.privateca.v1.resources_pb2.CertificateTemplate]') -> None:
        pass

    @abc.abstractmethod
    async def ListCertificateTemplates(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.ListCertificateTemplatesRequest, google.cloud.security.privateca.v1.service_pb2.ListCertificateTemplatesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateCertificateTemplate(self, stream: 'grpclib.server.Stream[google.cloud.security.privateca.v1.service_pb2.UpdateCertificateTemplateRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificate': grpclib.const.Handler(
                self.CreateCertificate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.CreateCertificateRequest,
                google.cloud.security.privateca.v1.resources_pb2.Certificate,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificate': grpclib.const.Handler(
                self.GetCertificate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.GetCertificateRequest,
                google.cloud.security.privateca.v1.resources_pb2.Certificate,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificates': grpclib.const.Handler(
                self.ListCertificates,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.ListCertificatesRequest,
                google.cloud.security.privateca.v1.service_pb2.ListCertificatesResponse,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/RevokeCertificate': grpclib.const.Handler(
                self.RevokeCertificate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.RevokeCertificateRequest,
                google.cloud.security.privateca.v1.resources_pb2.Certificate,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificate': grpclib.const.Handler(
                self.UpdateCertificate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.UpdateCertificateRequest,
                google.cloud.security.privateca.v1.resources_pb2.Certificate,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/ActivateCertificateAuthority': grpclib.const.Handler(
                self.ActivateCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.ActivateCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificateAuthority': grpclib.const.Handler(
                self.CreateCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.CreateCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/DisableCertificateAuthority': grpclib.const.Handler(
                self.DisableCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.DisableCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/EnableCertificateAuthority': grpclib.const.Handler(
                self.EnableCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.EnableCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/FetchCertificateAuthorityCsr': grpclib.const.Handler(
                self.FetchCertificateAuthorityCsr,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.FetchCertificateAuthorityCsrRequest,
                google.cloud.security.privateca.v1.service_pb2.FetchCertificateAuthorityCsrResponse,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateAuthority': grpclib.const.Handler(
                self.GetCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.GetCertificateAuthorityRequest,
                google.cloud.security.privateca.v1.resources_pb2.CertificateAuthority,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateAuthorities': grpclib.const.Handler(
                self.ListCertificateAuthorities,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.ListCertificateAuthoritiesRequest,
                google.cloud.security.privateca.v1.service_pb2.ListCertificateAuthoritiesResponse,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/UndeleteCertificateAuthority': grpclib.const.Handler(
                self.UndeleteCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.UndeleteCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCertificateAuthority': grpclib.const.Handler(
                self.DeleteCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.DeleteCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateAuthority': grpclib.const.Handler(
                self.UpdateCertificateAuthority,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.UpdateCertificateAuthorityRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCaPool': grpclib.const.Handler(
                self.CreateCaPool,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.CreateCaPoolRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCaPool': grpclib.const.Handler(
                self.UpdateCaPool,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.UpdateCaPoolRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCaPool': grpclib.const.Handler(
                self.GetCaPool,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.GetCaPoolRequest,
                google.cloud.security.privateca.v1.resources_pb2.CaPool,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCaPools': grpclib.const.Handler(
                self.ListCaPools,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.ListCaPoolsRequest,
                google.cloud.security.privateca.v1.service_pb2.ListCaPoolsResponse,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCaPool': grpclib.const.Handler(
                self.DeleteCaPool,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.DeleteCaPoolRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/FetchCaCerts': grpclib.const.Handler(
                self.FetchCaCerts,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.FetchCaCertsRequest,
                google.cloud.security.privateca.v1.service_pb2.FetchCaCertsResponse,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateRevocationList': grpclib.const.Handler(
                self.GetCertificateRevocationList,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.GetCertificateRevocationListRequest,
                google.cloud.security.privateca.v1.resources_pb2.CertificateRevocationList,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateRevocationLists': grpclib.const.Handler(
                self.ListCertificateRevocationLists,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.ListCertificateRevocationListsRequest,
                google.cloud.security.privateca.v1.service_pb2.ListCertificateRevocationListsResponse,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateRevocationList': grpclib.const.Handler(
                self.UpdateCertificateRevocationList,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.UpdateCertificateRevocationListRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificateTemplate': grpclib.const.Handler(
                self.CreateCertificateTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.CreateCertificateTemplateRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCertificateTemplate': grpclib.const.Handler(
                self.DeleteCertificateTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.DeleteCertificateTemplateRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateTemplate': grpclib.const.Handler(
                self.GetCertificateTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.GetCertificateTemplateRequest,
                google.cloud.security.privateca.v1.resources_pb2.CertificateTemplate,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateTemplates': grpclib.const.Handler(
                self.ListCertificateTemplates,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.ListCertificateTemplatesRequest,
                google.cloud.security.privateca.v1.service_pb2.ListCertificateTemplatesResponse,
            ),
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateTemplate': grpclib.const.Handler(
                self.UpdateCertificateTemplate,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.security.privateca.v1.service_pb2.UpdateCertificateTemplateRequest,
                google.longrunning.operations_pb2.Operation,
            ),
        }


class CertificateAuthorityServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateCertificate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificate',
            google.cloud.security.privateca.v1.service_pb2.CreateCertificateRequest,
            google.cloud.security.privateca.v1.resources_pb2.Certificate,
        )
        self.GetCertificate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificate',
            google.cloud.security.privateca.v1.service_pb2.GetCertificateRequest,
            google.cloud.security.privateca.v1.resources_pb2.Certificate,
        )
        self.ListCertificates = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificates',
            google.cloud.security.privateca.v1.service_pb2.ListCertificatesRequest,
            google.cloud.security.privateca.v1.service_pb2.ListCertificatesResponse,
        )
        self.RevokeCertificate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/RevokeCertificate',
            google.cloud.security.privateca.v1.service_pb2.RevokeCertificateRequest,
            google.cloud.security.privateca.v1.resources_pb2.Certificate,
        )
        self.UpdateCertificate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificate',
            google.cloud.security.privateca.v1.service_pb2.UpdateCertificateRequest,
            google.cloud.security.privateca.v1.resources_pb2.Certificate,
        )
        self.ActivateCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/ActivateCertificateAuthority',
            google.cloud.security.privateca.v1.service_pb2.ActivateCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.CreateCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificateAuthority',
            google.cloud.security.privateca.v1.service_pb2.CreateCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DisableCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/DisableCertificateAuthority',
            google.cloud.security.privateca.v1.service_pb2.DisableCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.EnableCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/EnableCertificateAuthority',
            google.cloud.security.privateca.v1.service_pb2.EnableCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.FetchCertificateAuthorityCsr = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/FetchCertificateAuthorityCsr',
            google.cloud.security.privateca.v1.service_pb2.FetchCertificateAuthorityCsrRequest,
            google.cloud.security.privateca.v1.service_pb2.FetchCertificateAuthorityCsrResponse,
        )
        self.GetCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateAuthority',
            google.cloud.security.privateca.v1.service_pb2.GetCertificateAuthorityRequest,
            google.cloud.security.privateca.v1.resources_pb2.CertificateAuthority,
        )
        self.ListCertificateAuthorities = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateAuthorities',
            google.cloud.security.privateca.v1.service_pb2.ListCertificateAuthoritiesRequest,
            google.cloud.security.privateca.v1.service_pb2.ListCertificateAuthoritiesResponse,
        )
        self.UndeleteCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/UndeleteCertificateAuthority',
            google.cloud.security.privateca.v1.service_pb2.UndeleteCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCertificateAuthority',
            google.cloud.security.privateca.v1.service_pb2.DeleteCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateCertificateAuthority = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateAuthority',
            google.cloud.security.privateca.v1.service_pb2.UpdateCertificateAuthorityRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.CreateCaPool = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCaPool',
            google.cloud.security.privateca.v1.service_pb2.CreateCaPoolRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateCaPool = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCaPool',
            google.cloud.security.privateca.v1.service_pb2.UpdateCaPoolRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetCaPool = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCaPool',
            google.cloud.security.privateca.v1.service_pb2.GetCaPoolRequest,
            google.cloud.security.privateca.v1.resources_pb2.CaPool,
        )
        self.ListCaPools = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCaPools',
            google.cloud.security.privateca.v1.service_pb2.ListCaPoolsRequest,
            google.cloud.security.privateca.v1.service_pb2.ListCaPoolsResponse,
        )
        self.DeleteCaPool = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCaPool',
            google.cloud.security.privateca.v1.service_pb2.DeleteCaPoolRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.FetchCaCerts = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/FetchCaCerts',
            google.cloud.security.privateca.v1.service_pb2.FetchCaCertsRequest,
            google.cloud.security.privateca.v1.service_pb2.FetchCaCertsResponse,
        )
        self.GetCertificateRevocationList = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateRevocationList',
            google.cloud.security.privateca.v1.service_pb2.GetCertificateRevocationListRequest,
            google.cloud.security.privateca.v1.resources_pb2.CertificateRevocationList,
        )
        self.ListCertificateRevocationLists = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateRevocationLists',
            google.cloud.security.privateca.v1.service_pb2.ListCertificateRevocationListsRequest,
            google.cloud.security.privateca.v1.service_pb2.ListCertificateRevocationListsResponse,
        )
        self.UpdateCertificateRevocationList = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateRevocationList',
            google.cloud.security.privateca.v1.service_pb2.UpdateCertificateRevocationListRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.CreateCertificateTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/CreateCertificateTemplate',
            google.cloud.security.privateca.v1.service_pb2.CreateCertificateTemplateRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteCertificateTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/DeleteCertificateTemplate',
            google.cloud.security.privateca.v1.service_pb2.DeleteCertificateTemplateRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.GetCertificateTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/GetCertificateTemplate',
            google.cloud.security.privateca.v1.service_pb2.GetCertificateTemplateRequest,
            google.cloud.security.privateca.v1.resources_pb2.CertificateTemplate,
        )
        self.ListCertificateTemplates = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/ListCertificateTemplates',
            google.cloud.security.privateca.v1.service_pb2.ListCertificateTemplatesRequest,
            google.cloud.security.privateca.v1.service_pb2.ListCertificateTemplatesResponse,
        )
        self.UpdateCertificateTemplate = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.security.privateca.v1.CertificateAuthorityService/UpdateCertificateTemplate',
            google.cloud.security.privateca.v1.service_pb2.UpdateCertificateTemplateRequest,
            google.longrunning.operations_pb2.Operation,
        )
