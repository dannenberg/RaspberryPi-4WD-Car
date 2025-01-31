# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow/cx/v3/deployment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/dialogflow/cx/v3/deployment.proto',
  package='google.cloud.dialogflow.cx.v3',
  syntax='proto3',
  serialized_options=b'\n!com.google.cloud.dialogflow.cx.v3B\017DeploymentProtoP\001Z?google.golang.org/genproto/googleapis/cloud/dialogflow/cx/v3;cx\370\001\001\242\002\002DF\252\002\035Google.Cloud.Dialogflow.Cx.V3\352\002!Google::Cloud::Dialogflow::CX::V3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.google/cloud/dialogflow/cx/v3/deployment.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8c\x06\n\nDeployment\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12I\n\x0c\x66low_version\x18\x02 \x01(\tB&\xfa\x41#\n!dialogflow.googleapis.com/VersionR\x0b\x66lowVersion\x12\x45\n\x05state\x18\x03 \x01(\x0e\x32/.google.cloud.dialogflow.cx.v3.Deployment.StateR\x05state\x12H\n\x06result\x18\x04 \x01(\x0b\x32\x30.google.cloud.dialogflow.cx.v3.Deployment.ResultR\x06result\x12\x39\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x1a\xba\x01\n\x06Result\x12\x65\n\x17\x64\x65ployment_test_results\x18\x01 \x03(\tB-\xfa\x41*\n(dialogflow.googleapis.com/TestCaseResultR\x15\x64\x65ploymentTestResults\x12I\n\nexperiment\x18\x02 \x01(\tB)\xfa\x41&\n$dialogflow.googleapis.com/ExperimentR\nexperiment\"F\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03:\x96\x01\xea\x41\x92\x01\n$dialogflow.googleapis.com/Deployment\x12jprojects/{project}/locations/{location}/agents/{agent}/environments/{environment}/deployments/{deployment}\"\x9b\x01\n\x16ListDeploymentsRequest\x12\x45\n\x06parent\x18\x01 \x01(\tB-\xe2\x41\x01\x02\xfa\x41&\x12$dialogflow.googleapis.com/DeploymentR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\x8e\x01\n\x17ListDeploymentsResponse\x12K\n\x0b\x64\x65ployments\x18\x01 \x03(\x0b\x32).google.cloud.dialogflow.cx.v3.DeploymentR\x0b\x64\x65ployments\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"Y\n\x14GetDeploymentRequest\x12\x41\n\x04name\x18\x01 \x01(\tB-\xe2\x41\x01\x02\xfa\x41&\n$dialogflow.googleapis.com/DeploymentR\x04name2\xae\x04\n\x0b\x44\x65ployments\x12\xda\x01\n\x0fListDeployments\x12\x35.google.cloud.dialogflow.cx.v3.ListDeploymentsRequest\x1a\x36.google.cloud.dialogflow.cx.v3.ListDeploymentsResponse\"X\xda\x41\x06parent\x82\xd3\xe4\x93\x02I\x12G/v3/{parent=projects/*/locations/*/agents/*/environments/*}/deployments\x12\xc7\x01\n\rGetDeployment\x12\x33.google.cloud.dialogflow.cx.v3.GetDeploymentRequest\x1a).google.cloud.dialogflow.cx.v3.Deployment\"V\xda\x41\x04name\x82\xd3\xe4\x93\x02I\x12G/v3/{name=projects/*/locations/*/agents/*/environments/*/deployments/*}\x1ax\xca\x41\x19\x64ialogflow.googleapis.com\xd2\x41Yhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xc3\x01\n!com.google.cloud.dialogflow.cx.v3B\x0f\x44\x65ploymentProtoP\x01Z?google.golang.org/genproto/googleapis/cloud/dialogflow/cx/v3;cx\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_DEPLOYMENT_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='google.cloud.dialogflow.cx.v3.Deployment.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCEEDED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=850,
  serialized_end=920,
)
_sym_db.RegisterEnumDescriptor(_DEPLOYMENT_STATE)


_DEPLOYMENT_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='google.cloud.dialogflow.cx.v3.Deployment.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deployment_test_results', full_name='google.cloud.dialogflow.cx.v3.Deployment.Result.deployment_test_results', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A*\n(dialogflow.googleapis.com/TestCaseResult', json_name='deploymentTestResults', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='experiment', full_name='google.cloud.dialogflow.cx.v3.Deployment.Result.experiment', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A&\n$dialogflow.googleapis.com/Experiment', json_name='experiment', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=662,
  serialized_end=848,
)

_DEPLOYMENT = _descriptor.Descriptor(
  name='Deployment',
  full_name='google.cloud.dialogflow.cx.v3.Deployment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.cx.v3.Deployment.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flow_version', full_name='google.cloud.dialogflow.cx.v3.Deployment.flow_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A#\n!dialogflow.googleapis.com/Version', json_name='flowVersion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='google.cloud.dialogflow.cx.v3.Deployment.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='state', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='google.cloud.dialogflow.cx.v3.Deployment.result', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='result', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='google.cloud.dialogflow.cx.v3.Deployment.start_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='startTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.cloud.dialogflow.cx.v3.Deployment.end_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='endTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DEPLOYMENT_RESULT, ],
  enum_types=[
    _DEPLOYMENT_STATE,
  ],
  serialized_options=b'\352A\222\001\n$dialogflow.googleapis.com/Deployment\022jprojects/{project}/locations/{location}/agents/{agent}/environments/{environment}/deployments/{deployment}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=1073,
)


_LISTDEPLOYMENTSREQUEST = _descriptor.Descriptor(
  name='ListDeploymentsRequest',
  full_name='google.cloud.dialogflow.cx.v3.ListDeploymentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.cx.v3.ListDeploymentsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A&\022$dialogflow.googleapis.com/Deployment', json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.dialogflow.cx.v3.ListDeploymentsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.dialogflow.cx.v3.ListDeploymentsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1076,
  serialized_end=1231,
)


_LISTDEPLOYMENTSRESPONSE = _descriptor.Descriptor(
  name='ListDeploymentsResponse',
  full_name='google.cloud.dialogflow.cx.v3.ListDeploymentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deployments', full_name='google.cloud.dialogflow.cx.v3.ListDeploymentsResponse.deployments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='deployments', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.dialogflow.cx.v3.ListDeploymentsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nextPageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1234,
  serialized_end=1376,
)


_GETDEPLOYMENTREQUEST = _descriptor.Descriptor(
  name='GetDeploymentRequest',
  full_name='google.cloud.dialogflow.cx.v3.GetDeploymentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.cx.v3.GetDeploymentRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A&\n$dialogflow.googleapis.com/Deployment', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1378,
  serialized_end=1467,
)

_DEPLOYMENT_RESULT.containing_type = _DEPLOYMENT
_DEPLOYMENT.fields_by_name['state'].enum_type = _DEPLOYMENT_STATE
_DEPLOYMENT.fields_by_name['result'].message_type = _DEPLOYMENT_RESULT
_DEPLOYMENT.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DEPLOYMENT.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_DEPLOYMENT_STATE.containing_type = _DEPLOYMENT
_LISTDEPLOYMENTSRESPONSE.fields_by_name['deployments'].message_type = _DEPLOYMENT
DESCRIPTOR.message_types_by_name['Deployment'] = _DEPLOYMENT
DESCRIPTOR.message_types_by_name['ListDeploymentsRequest'] = _LISTDEPLOYMENTSREQUEST
DESCRIPTOR.message_types_by_name['ListDeploymentsResponse'] = _LISTDEPLOYMENTSRESPONSE
DESCRIPTOR.message_types_by_name['GetDeploymentRequest'] = _GETDEPLOYMENTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Deployment = _reflection.GeneratedProtocolMessageType('Deployment', (_message.Message,), {

  'Result' : _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
    'DESCRIPTOR' : _DEPLOYMENT_RESULT,
    '__module__' : 'google.cloud.dialogflow.cx.v3.deployment_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.Deployment.Result)
    })
  ,
  'DESCRIPTOR' : _DEPLOYMENT,
  '__module__' : 'google.cloud.dialogflow.cx.v3.deployment_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.Deployment)
  })
_sym_db.RegisterMessage(Deployment)
_sym_db.RegisterMessage(Deployment.Result)

ListDeploymentsRequest = _reflection.GeneratedProtocolMessageType('ListDeploymentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEPLOYMENTSREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.deployment_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.ListDeploymentsRequest)
  })
_sym_db.RegisterMessage(ListDeploymentsRequest)

ListDeploymentsResponse = _reflection.GeneratedProtocolMessageType('ListDeploymentsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEPLOYMENTSRESPONSE,
  '__module__' : 'google.cloud.dialogflow.cx.v3.deployment_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.ListDeploymentsResponse)
  })
_sym_db.RegisterMessage(ListDeploymentsResponse)

GetDeploymentRequest = _reflection.GeneratedProtocolMessageType('GetDeploymentRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDEPLOYMENTREQUEST,
  '__module__' : 'google.cloud.dialogflow.cx.v3.deployment_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.cx.v3.GetDeploymentRequest)
  })
_sym_db.RegisterMessage(GetDeploymentRequest)


DESCRIPTOR._options = None
_DEPLOYMENT_RESULT.fields_by_name['deployment_test_results']._options = None
_DEPLOYMENT_RESULT.fields_by_name['experiment']._options = None
_DEPLOYMENT.fields_by_name['flow_version']._options = None
_DEPLOYMENT._options = None
_LISTDEPLOYMENTSREQUEST.fields_by_name['parent']._options = None
_GETDEPLOYMENTREQUEST.fields_by_name['name']._options = None

_DEPLOYMENTS = _descriptor.ServiceDescriptor(
  name='Deployments',
  full_name='google.cloud.dialogflow.cx.v3.Deployments',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\031dialogflow.googleapis.com\322AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow',
  create_key=_descriptor._internal_create_key,
  serialized_start=1470,
  serialized_end=2028,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListDeployments',
    full_name='google.cloud.dialogflow.cx.v3.Deployments.ListDeployments',
    index=0,
    containing_service=None,
    input_type=_LISTDEPLOYMENTSREQUEST,
    output_type=_LISTDEPLOYMENTSRESPONSE,
    serialized_options=b'\332A\006parent\202\323\344\223\002I\022G/v3/{parent=projects/*/locations/*/agents/*/environments/*}/deployments',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetDeployment',
    full_name='google.cloud.dialogflow.cx.v3.Deployments.GetDeployment',
    index=1,
    containing_service=None,
    input_type=_GETDEPLOYMENTREQUEST,
    output_type=_DEPLOYMENT,
    serialized_options=b'\332A\004name\202\323\344\223\002I\022G/v3/{name=projects/*/locations/*/agents/*/environments/*/deployments/*}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEPLOYMENTS)

DESCRIPTOR.services_by_name['Deployments'] = _DEPLOYMENTS

# @@protoc_insertion_point(module_scope)
