# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/securitycenter/v1beta1/securitycenter_service.proto
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
import google.cloud.securitycenter.v1beta1.asset_pb2
import google.cloud.securitycenter.v1beta1.finding_pb2
import google.cloud.securitycenter.v1beta1.organization_settings_pb2
import google.cloud.securitycenter.v1beta1.security_marks_pb2
import google.cloud.securitycenter.v1beta1.source_pb2
import google.iam.v1.iam_policy_pb2
import google.iam.v1.policy_pb2
import google.longrunning.operations_pb2
import google.protobuf.duration_pb2
import google.protobuf.empty_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import google.cloud.securitycenter.v1beta1.securitycenter_service_pb2


class SecurityCenterBase(abc.ABC):

    @abc.abstractmethod
    async def CreateSource(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.CreateSourceRequest, google.cloud.securitycenter.v1beta1.source_pb2.Source]') -> None:
        pass

    @abc.abstractmethod
    async def CreateFinding(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.CreateFindingRequest, google.cloud.securitycenter.v1beta1.finding_pb2.Finding]') -> None:
        pass

    @abc.abstractmethod
    async def GetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def GetOrganizationSettings(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GetOrganizationSettingsRequest, google.cloud.securitycenter.v1beta1.organization_settings_pb2.OrganizationSettings]') -> None:
        pass

    @abc.abstractmethod
    async def GetSource(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GetSourceRequest, google.cloud.securitycenter.v1beta1.source_pb2.Source]') -> None:
        pass

    @abc.abstractmethod
    async def GroupAssets(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GroupAssetsRequest, google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GroupAssetsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GroupFindings(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GroupFindingsRequest, google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GroupFindingsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListAssets(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListAssetsRequest, google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListAssetsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListFindings(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListFindingsRequest, google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListFindingsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ListSources(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListSourcesRequest, google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListSourcesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def RunAssetDiscovery(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.RunAssetDiscoveryRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def SetFindingState(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.SetFindingStateRequest, google.cloud.securitycenter.v1beta1.finding_pb2.Finding]') -> None:
        pass

    @abc.abstractmethod
    async def SetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def TestIamPermissions(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateFinding(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.UpdateFindingRequest, google.cloud.securitycenter.v1beta1.finding_pb2.Finding]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateOrganizationSettings(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.UpdateOrganizationSettingsRequest, google.cloud.securitycenter.v1beta1.organization_settings_pb2.OrganizationSettings]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateSource(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.UpdateSourceRequest, google.cloud.securitycenter.v1beta1.source_pb2.Source]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateSecurityMarks(self, stream: 'grpclib.server.Stream[google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.UpdateSecurityMarksRequest, google.cloud.securitycenter.v1beta1.security_marks_pb2.SecurityMarks]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/CreateSource': grpclib.const.Handler(
                self.CreateSource,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.CreateSourceRequest,
                google.cloud.securitycenter.v1beta1.source_pb2.Source,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/CreateFinding': grpclib.const.Handler(
                self.CreateFinding,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.CreateFindingRequest,
                google.cloud.securitycenter.v1beta1.finding_pb2.Finding,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/GetIamPolicy': grpclib.const.Handler(
                self.GetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/GetOrganizationSettings': grpclib.const.Handler(
                self.GetOrganizationSettings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GetOrganizationSettingsRequest,
                google.cloud.securitycenter.v1beta1.organization_settings_pb2.OrganizationSettings,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/GetSource': grpclib.const.Handler(
                self.GetSource,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GetSourceRequest,
                google.cloud.securitycenter.v1beta1.source_pb2.Source,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/GroupAssets': grpclib.const.Handler(
                self.GroupAssets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GroupAssetsRequest,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GroupAssetsResponse,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/GroupFindings': grpclib.const.Handler(
                self.GroupFindings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GroupFindingsRequest,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GroupFindingsResponse,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/ListAssets': grpclib.const.Handler(
                self.ListAssets,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListAssetsRequest,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListAssetsResponse,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/ListFindings': grpclib.const.Handler(
                self.ListFindings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListFindingsRequest,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListFindingsResponse,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/ListSources': grpclib.const.Handler(
                self.ListSources,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListSourcesRequest,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListSourcesResponse,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/RunAssetDiscovery': grpclib.const.Handler(
                self.RunAssetDiscovery,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.RunAssetDiscoveryRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/SetFindingState': grpclib.const.Handler(
                self.SetFindingState,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.SetFindingStateRequest,
                google.cloud.securitycenter.v1beta1.finding_pb2.Finding,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/SetIamPolicy': grpclib.const.Handler(
                self.SetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/TestIamPermissions': grpclib.const.Handler(
                self.TestIamPermissions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/UpdateFinding': grpclib.const.Handler(
                self.UpdateFinding,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.UpdateFindingRequest,
                google.cloud.securitycenter.v1beta1.finding_pb2.Finding,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/UpdateOrganizationSettings': grpclib.const.Handler(
                self.UpdateOrganizationSettings,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.UpdateOrganizationSettingsRequest,
                google.cloud.securitycenter.v1beta1.organization_settings_pb2.OrganizationSettings,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/UpdateSource': grpclib.const.Handler(
                self.UpdateSource,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.UpdateSourceRequest,
                google.cloud.securitycenter.v1beta1.source_pb2.Source,
            ),
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/UpdateSecurityMarks': grpclib.const.Handler(
                self.UpdateSecurityMarks,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.UpdateSecurityMarksRequest,
                google.cloud.securitycenter.v1beta1.security_marks_pb2.SecurityMarks,
            ),
        }


class SecurityCenterStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.CreateSource = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/CreateSource',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.CreateSourceRequest,
            google.cloud.securitycenter.v1beta1.source_pb2.Source,
        )
        self.CreateFinding = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/CreateFinding',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.CreateFindingRequest,
            google.cloud.securitycenter.v1beta1.finding_pb2.Finding,
        )
        self.GetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/GetIamPolicy',
            google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.GetOrganizationSettings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/GetOrganizationSettings',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GetOrganizationSettingsRequest,
            google.cloud.securitycenter.v1beta1.organization_settings_pb2.OrganizationSettings,
        )
        self.GetSource = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/GetSource',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GetSourceRequest,
            google.cloud.securitycenter.v1beta1.source_pb2.Source,
        )
        self.GroupAssets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/GroupAssets',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GroupAssetsRequest,
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GroupAssetsResponse,
        )
        self.GroupFindings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/GroupFindings',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GroupFindingsRequest,
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.GroupFindingsResponse,
        )
        self.ListAssets = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/ListAssets',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListAssetsRequest,
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListAssetsResponse,
        )
        self.ListFindings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/ListFindings',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListFindingsRequest,
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListFindingsResponse,
        )
        self.ListSources = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/ListSources',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListSourcesRequest,
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.ListSourcesResponse,
        )
        self.RunAssetDiscovery = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/RunAssetDiscovery',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.RunAssetDiscoveryRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.SetFindingState = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/SetFindingState',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.SetFindingStateRequest,
            google.cloud.securitycenter.v1beta1.finding_pb2.Finding,
        )
        self.SetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/SetIamPolicy',
            google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.TestIamPermissions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/TestIamPermissions',
            google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
        )
        self.UpdateFinding = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/UpdateFinding',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.UpdateFindingRequest,
            google.cloud.securitycenter.v1beta1.finding_pb2.Finding,
        )
        self.UpdateOrganizationSettings = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/UpdateOrganizationSettings',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.UpdateOrganizationSettingsRequest,
            google.cloud.securitycenter.v1beta1.organization_settings_pb2.OrganizationSettings,
        )
        self.UpdateSource = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/UpdateSource',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.UpdateSourceRequest,
            google.cloud.securitycenter.v1beta1.source_pb2.Source,
        )
        self.UpdateSecurityMarks = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.securitycenter.v1beta1.SecurityCenter/UpdateSecurityMarks',
            google.cloud.securitycenter.v1beta1.securitycenter_service_pb2.UpdateSecurityMarksRequest,
            google.cloud.securitycenter.v1beta1.security_marks_pb2.SecurityMarks,
        )
