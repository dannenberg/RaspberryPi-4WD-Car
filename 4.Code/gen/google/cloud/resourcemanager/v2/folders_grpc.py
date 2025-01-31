# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/cloud/resourcemanager/v2/folders.proto
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
import google.iam.v1.iam_policy_pb2
import google.iam.v1.policy_pb2
import google.longrunning.operations_pb2
import google.protobuf.field_mask_pb2
import google.protobuf.timestamp_pb2
import google.cloud.resourcemanager.v2.folders_pb2


class FoldersBase(abc.ABC):

    @abc.abstractmethod
    async def ListFolders(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v2.folders_pb2.ListFoldersRequest, google.cloud.resourcemanager.v2.folders_pb2.ListFoldersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def SearchFolders(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v2.folders_pb2.SearchFoldersRequest, google.cloud.resourcemanager.v2.folders_pb2.SearchFoldersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetFolder(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v2.folders_pb2.GetFolderRequest, google.cloud.resourcemanager.v2.folders_pb2.Folder]') -> None:
        pass

    @abc.abstractmethod
    async def CreateFolder(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v2.folders_pb2.CreateFolderRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def UpdateFolder(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v2.folders_pb2.UpdateFolderRequest, google.cloud.resourcemanager.v2.folders_pb2.Folder]') -> None:
        pass

    @abc.abstractmethod
    async def MoveFolder(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v2.folders_pb2.MoveFolderRequest, google.longrunning.operations_pb2.Operation]') -> None:
        pass

    @abc.abstractmethod
    async def DeleteFolder(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v2.folders_pb2.DeleteFolderRequest, google.cloud.resourcemanager.v2.folders_pb2.Folder]') -> None:
        pass

    @abc.abstractmethod
    async def UndeleteFolder(self, stream: 'grpclib.server.Stream[google.cloud.resourcemanager.v2.folders_pb2.UndeleteFolderRequest, google.cloud.resourcemanager.v2.folders_pb2.Folder]') -> None:
        pass

    @abc.abstractmethod
    async def GetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def SetIamPolicy(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, google.iam.v1.policy_pb2.Policy]') -> None:
        pass

    @abc.abstractmethod
    async def TestIamPermissions(self, stream: 'grpclib.server.Stream[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.cloud.resourcemanager.v2.Folders/ListFolders': grpclib.const.Handler(
                self.ListFolders,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v2.folders_pb2.ListFoldersRequest,
                google.cloud.resourcemanager.v2.folders_pb2.ListFoldersResponse,
            ),
            '/google.cloud.resourcemanager.v2.Folders/SearchFolders': grpclib.const.Handler(
                self.SearchFolders,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v2.folders_pb2.SearchFoldersRequest,
                google.cloud.resourcemanager.v2.folders_pb2.SearchFoldersResponse,
            ),
            '/google.cloud.resourcemanager.v2.Folders/GetFolder': grpclib.const.Handler(
                self.GetFolder,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v2.folders_pb2.GetFolderRequest,
                google.cloud.resourcemanager.v2.folders_pb2.Folder,
            ),
            '/google.cloud.resourcemanager.v2.Folders/CreateFolder': grpclib.const.Handler(
                self.CreateFolder,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v2.folders_pb2.CreateFolderRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.resourcemanager.v2.Folders/UpdateFolder': grpclib.const.Handler(
                self.UpdateFolder,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v2.folders_pb2.UpdateFolderRequest,
                google.cloud.resourcemanager.v2.folders_pb2.Folder,
            ),
            '/google.cloud.resourcemanager.v2.Folders/MoveFolder': grpclib.const.Handler(
                self.MoveFolder,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v2.folders_pb2.MoveFolderRequest,
                google.longrunning.operations_pb2.Operation,
            ),
            '/google.cloud.resourcemanager.v2.Folders/DeleteFolder': grpclib.const.Handler(
                self.DeleteFolder,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v2.folders_pb2.DeleteFolderRequest,
                google.cloud.resourcemanager.v2.folders_pb2.Folder,
            ),
            '/google.cloud.resourcemanager.v2.Folders/UndeleteFolder': grpclib.const.Handler(
                self.UndeleteFolder,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.cloud.resourcemanager.v2.folders_pb2.UndeleteFolderRequest,
                google.cloud.resourcemanager.v2.folders_pb2.Folder,
            ),
            '/google.cloud.resourcemanager.v2.Folders/GetIamPolicy': grpclib.const.Handler(
                self.GetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.cloud.resourcemanager.v2.Folders/SetIamPolicy': grpclib.const.Handler(
                self.SetIamPolicy,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
                google.iam.v1.policy_pb2.Policy,
            ),
            '/google.cloud.resourcemanager.v2.Folders/TestIamPermissions': grpclib.const.Handler(
                self.TestIamPermissions,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
                google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
            ),
        }


class FoldersStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ListFolders = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v2.Folders/ListFolders',
            google.cloud.resourcemanager.v2.folders_pb2.ListFoldersRequest,
            google.cloud.resourcemanager.v2.folders_pb2.ListFoldersResponse,
        )
        self.SearchFolders = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v2.Folders/SearchFolders',
            google.cloud.resourcemanager.v2.folders_pb2.SearchFoldersRequest,
            google.cloud.resourcemanager.v2.folders_pb2.SearchFoldersResponse,
        )
        self.GetFolder = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v2.Folders/GetFolder',
            google.cloud.resourcemanager.v2.folders_pb2.GetFolderRequest,
            google.cloud.resourcemanager.v2.folders_pb2.Folder,
        )
        self.CreateFolder = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v2.Folders/CreateFolder',
            google.cloud.resourcemanager.v2.folders_pb2.CreateFolderRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.UpdateFolder = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v2.Folders/UpdateFolder',
            google.cloud.resourcemanager.v2.folders_pb2.UpdateFolderRequest,
            google.cloud.resourcemanager.v2.folders_pb2.Folder,
        )
        self.MoveFolder = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v2.Folders/MoveFolder',
            google.cloud.resourcemanager.v2.folders_pb2.MoveFolderRequest,
            google.longrunning.operations_pb2.Operation,
        )
        self.DeleteFolder = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v2.Folders/DeleteFolder',
            google.cloud.resourcemanager.v2.folders_pb2.DeleteFolderRequest,
            google.cloud.resourcemanager.v2.folders_pb2.Folder,
        )
        self.UndeleteFolder = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v2.Folders/UndeleteFolder',
            google.cloud.resourcemanager.v2.folders_pb2.UndeleteFolderRequest,
            google.cloud.resourcemanager.v2.folders_pb2.Folder,
        )
        self.GetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v2.Folders/GetIamPolicy',
            google.iam.v1.iam_policy_pb2.GetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.SetIamPolicy = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v2.Folders/SetIamPolicy',
            google.iam.v1.iam_policy_pb2.SetIamPolicyRequest,
            google.iam.v1.policy_pb2.Policy,
        )
        self.TestIamPermissions = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.cloud.resourcemanager.v2.Folders/TestIamPermissions',
            google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest,
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse,
        )
