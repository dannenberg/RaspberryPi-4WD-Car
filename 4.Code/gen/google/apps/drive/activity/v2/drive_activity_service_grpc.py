# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: google/apps/drive/activity/v2/drive_activity_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import google.apps.drive.activity.v2.query_drive_activity_request_pb2
import google.apps.drive.activity.v2.query_drive_activity_response_pb2
import google.api.client_pb2
import google.apps.drive.activity.v2.drive_activity_service_pb2


class DriveActivityServiceBase(abc.ABC):

    @abc.abstractmethod
    async def QueryDriveActivity(self, stream: 'grpclib.server.Stream[google.apps.drive.activity.v2.query_drive_activity_request_pb2.QueryDriveActivityRequest, google.apps.drive.activity.v2.query_drive_activity_response_pb2.QueryDriveActivityResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/google.apps.drive.activity.v2.DriveActivityService/QueryDriveActivity': grpclib.const.Handler(
                self.QueryDriveActivity,
                grpclib.const.Cardinality.UNARY_UNARY,
                google.apps.drive.activity.v2.query_drive_activity_request_pb2.QueryDriveActivityRequest,
                google.apps.drive.activity.v2.query_drive_activity_response_pb2.QueryDriveActivityResponse,
            ),
        }


class DriveActivityServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.QueryDriveActivity = grpclib.client.UnaryUnaryMethod(
            channel,
            '/google.apps.drive.activity.v2.DriveActivityService/QueryDriveActivity',
            google.apps.drive.activity.v2.query_drive_activity_request_pb2.QueryDriveActivityRequest,
            google.apps.drive.activity.v2.query_drive_activity_response_pb2.QueryDriveActivityResponse,
        )
