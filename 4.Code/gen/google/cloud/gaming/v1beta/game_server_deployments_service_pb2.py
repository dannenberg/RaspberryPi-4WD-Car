# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/gaming/v1beta/game_server_deployments_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.cloud.gaming.v1beta import game_server_deployments_pb2 as google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/gaming/v1beta/game_server_deployments_service.proto',
  package='google.cloud.gaming.v1beta',
  syntax='proto3',
  serialized_options=b'\n\036com.google.cloud.gaming.v1betaP\001Z@google.golang.org/genproto/googleapis/cloud/gaming/v1beta;gaming\312\002\032Google\\Cloud\\Gaming\\V1beta',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n@google/cloud/gaming/v1beta/game_server_deployments_service.proto\x12\x1agoogle.cloud.gaming.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x38google/cloud/gaming/v1beta/game_server_deployments.proto\x1a#google/longrunning/operations.proto2\xc4\x13\n\x1cGameServerDeploymentsService\x12\xe8\x01\n\x19ListGameServerDeployments\x12<.google.cloud.gaming.v1beta.ListGameServerDeploymentsRequest\x1a=.google.cloud.gaming.v1beta.ListGameServerDeploymentsResponse\"N\xda\x41\x06parent\x82\xd3\xe4\x93\x02?\x12=/v1beta/{parent=projects/*/locations/*}/gameServerDeployments\x12\xd5\x01\n\x17GetGameServerDeployment\x12:.google.cloud.gaming.v1beta.GetGameServerDeploymentRequest\x1a\x30.google.cloud.gaming.v1beta.GameServerDeployment\"L\xda\x41\x04name\x82\xd3\xe4\x93\x02?\x12=/v1beta/{name=projects/*/locations/*/gameServerDeployments/*}\x12\xa6\x02\n\x1a\x43reateGameServerDeployment\x12=.google.cloud.gaming.v1beta.CreateGameServerDeploymentRequest\x1a\x1d.google.longrunning.Operation\"\xa9\x01\xca\x41)\n\x14GameServerDeployment\x12\x11OperationMetadata\xda\x41\x1dparent,game_server_deployment\x82\xd3\xe4\x93\x02W\"=/v1beta/{parent=projects/*/locations/*}/gameServerDeployments:\x16game_server_deployment\x12\xf5\x01\n\x1a\x44\x65leteGameServerDeployment\x12=.google.cloud.gaming.v1beta.DeleteGameServerDeploymentRequest\x1a\x1d.google.longrunning.Operation\"y\xca\x41*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xda\x41\x04name\x82\xd3\xe4\x93\x02?*=/v1beta/{name=projects/*/locations/*/gameServerDeployments/*}\x12\xc2\x02\n\x1aUpdateGameServerDeployment\x12=.google.cloud.gaming.v1beta.UpdateGameServerDeploymentRequest\x1a\x1d.google.longrunning.Operation\"\xc5\x01\xca\x41)\n\x14GameServerDeployment\x12\x11OperationMetadata\xda\x41\"game_server_deployment,update_mask\x82\xd3\xe4\x93\x02n2T/v1beta/{game_server_deployment.name=projects/*/locations/*/gameServerDeployments/*}:\x16game_server_deployment\x12\xf2\x01\n\x1eGetGameServerDeploymentRollout\x12\x41.google.cloud.gaming.v1beta.GetGameServerDeploymentRolloutRequest\x1a\x37.google.cloud.gaming.v1beta.GameServerDeploymentRollout\"T\xda\x41\x04name\x82\xd3\xe4\x93\x02G\x12\x45/v1beta/{name=projects/*/locations/*/gameServerDeployments/*}/rollout\x12\xab\x02\n!UpdateGameServerDeploymentRollout\x12\x44.google.cloud.gaming.v1beta.UpdateGameServerDeploymentRolloutRequest\x1a\x1d.google.longrunning.Operation\"\xa0\x01\xca\x41)\n\x14GameServerDeployment\x12\x11OperationMetadata\xda\x41\x13rollout,update_mask\x82\xd3\xe4\x93\x02X2M/v1beta/{rollout.name=projects/*/locations/*/gameServerDeployments/*}/rollout:\x07rollout\x12\x9b\x02\n\"PreviewGameServerDeploymentRollout\x12\x45.google.cloud.gaming.v1beta.PreviewGameServerDeploymentRolloutRequest\x1a\x46.google.cloud.gaming.v1beta.PreviewGameServerDeploymentRolloutResponse\"f\x82\xd3\xe4\x93\x02`2U/v1beta/{rollout.name=projects/*/locations/*/gameServerDeployments/*}/rollout:preview:\x07rollout\x12\xe8\x01\n\x14\x46\x65tchDeploymentState\x12\x37.google.cloud.gaming.v1beta.FetchDeploymentStateRequest\x1a\x38.google.cloud.gaming.v1beta.FetchDeploymentStateResponse\"]\x82\xd3\xe4\x93\x02W\"R/v1beta/{name=projects/*/locations/*/gameServerDeployments/*}:fetchDeploymentState:\x01*\x1aO\xca\x41\x1bgameservices.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\x81\x01\n\x1e\x63om.google.cloud.gaming.v1betaP\x01Z@google.golang.org/genproto/googleapis/cloud/gaming/v1beta;gaming\xca\x02\x1aGoogle\\Cloud\\Gaming\\V1betab\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_GAMESERVERDEPLOYMENTSSERVICE = _descriptor.ServiceDescriptor(
  name='GameServerDeploymentsService',
  full_name='google.cloud.gaming.v1beta.GameServerDeploymentsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\033gameservices.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  create_key=_descriptor._internal_create_key,
  serialized_start=247,
  serialized_end=2747,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListGameServerDeployments',
    full_name='google.cloud.gaming.v1beta.GameServerDeploymentsService.ListGameServerDeployments',
    index=0,
    containing_service=None,
    input_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._LISTGAMESERVERDEPLOYMENTSREQUEST,
    output_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._LISTGAMESERVERDEPLOYMENTSRESPONSE,
    serialized_options=b'\332A\006parent\202\323\344\223\002?\022=/v1beta/{parent=projects/*/locations/*}/gameServerDeployments',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetGameServerDeployment',
    full_name='google.cloud.gaming.v1beta.GameServerDeploymentsService.GetGameServerDeployment',
    index=1,
    containing_service=None,
    input_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._GETGAMESERVERDEPLOYMENTREQUEST,
    output_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._GAMESERVERDEPLOYMENT,
    serialized_options=b'\332A\004name\202\323\344\223\002?\022=/v1beta/{name=projects/*/locations/*/gameServerDeployments/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateGameServerDeployment',
    full_name='google.cloud.gaming.v1beta.GameServerDeploymentsService.CreateGameServerDeployment',
    index=2,
    containing_service=None,
    input_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._CREATEGAMESERVERDEPLOYMENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A)\n\024GameServerDeployment\022\021OperationMetadata\332A\035parent,game_server_deployment\202\323\344\223\002W\"=/v1beta/{parent=projects/*/locations/*}/gameServerDeployments:\026game_server_deployment',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteGameServerDeployment',
    full_name='google.cloud.gaming.v1beta.GameServerDeploymentsService.DeleteGameServerDeployment',
    index=3,
    containing_service=None,
    input_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._DELETEGAMESERVERDEPLOYMENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A*\n\025google.protobuf.Empty\022\021OperationMetadata\332A\004name\202\323\344\223\002?*=/v1beta/{name=projects/*/locations/*/gameServerDeployments/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateGameServerDeployment',
    full_name='google.cloud.gaming.v1beta.GameServerDeploymentsService.UpdateGameServerDeployment',
    index=4,
    containing_service=None,
    input_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._UPDATEGAMESERVERDEPLOYMENTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A)\n\024GameServerDeployment\022\021OperationMetadata\332A\"game_server_deployment,update_mask\202\323\344\223\002n2T/v1beta/{game_server_deployment.name=projects/*/locations/*/gameServerDeployments/*}:\026game_server_deployment',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetGameServerDeploymentRollout',
    full_name='google.cloud.gaming.v1beta.GameServerDeploymentsService.GetGameServerDeploymentRollout',
    index=5,
    containing_service=None,
    input_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._GETGAMESERVERDEPLOYMENTROLLOUTREQUEST,
    output_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._GAMESERVERDEPLOYMENTROLLOUT,
    serialized_options=b'\332A\004name\202\323\344\223\002G\022E/v1beta/{name=projects/*/locations/*/gameServerDeployments/*}/rollout',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateGameServerDeploymentRollout',
    full_name='google.cloud.gaming.v1beta.GameServerDeploymentsService.UpdateGameServerDeploymentRollout',
    index=6,
    containing_service=None,
    input_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._UPDATEGAMESERVERDEPLOYMENTROLLOUTREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A)\n\024GameServerDeployment\022\021OperationMetadata\332A\023rollout,update_mask\202\323\344\223\002X2M/v1beta/{rollout.name=projects/*/locations/*/gameServerDeployments/*}/rollout:\007rollout',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PreviewGameServerDeploymentRollout',
    full_name='google.cloud.gaming.v1beta.GameServerDeploymentsService.PreviewGameServerDeploymentRollout',
    index=7,
    containing_service=None,
    input_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._PREVIEWGAMESERVERDEPLOYMENTROLLOUTREQUEST,
    output_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._PREVIEWGAMESERVERDEPLOYMENTROLLOUTRESPONSE,
    serialized_options=b'\202\323\344\223\002`2U/v1beta/{rollout.name=projects/*/locations/*/gameServerDeployments/*}/rollout:preview:\007rollout',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FetchDeploymentState',
    full_name='google.cloud.gaming.v1beta.GameServerDeploymentsService.FetchDeploymentState',
    index=8,
    containing_service=None,
    input_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._FETCHDEPLOYMENTSTATEREQUEST,
    output_type=google_dot_cloud_dot_gaming_dot_v1beta_dot_game__server__deployments__pb2._FETCHDEPLOYMENTSTATERESPONSE,
    serialized_options=b'\202\323\344\223\002W\"R/v1beta/{name=projects/*/locations/*/gameServerDeployments/*}:fetchDeploymentState:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GAMESERVERDEPLOYMENTSSERVICE)

DESCRIPTOR.services_by_name['GameServerDeploymentsService'] = _GAMESERVERDEPLOYMENTSSERVICE

# @@protoc_insertion_point(module_scope)
