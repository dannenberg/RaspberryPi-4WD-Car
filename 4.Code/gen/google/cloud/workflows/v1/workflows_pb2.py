# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/workflows/v1/workflows.proto
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
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/workflows/v1/workflows.proto',
  package='google.cloud.workflows.v1',
  syntax='proto3',
  serialized_options=b'\n\035com.google.cloud.workflows.v1B\016WorkflowsProtoP\001ZBgoogle.golang.org/genproto/googleapis/cloud/workflows/v1;workflows',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)google/cloud/workflows/v1/workflows.proto\x12\x19google.cloud.workflows.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x81\x06\n\x08Workflow\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x45\n\x05state\x18\x03 \x01(\x0e\x32).google.cloud.workflows.v1.Workflow.StateB\x04\xe2\x41\x01\x03R\x05state\x12%\n\x0brevision_id\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03R\nrevisionId\x12\x41\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12\x41\n\x0bupdate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\nupdateTime\x12R\n\x14revision_create_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x12revisionCreateTime\x12G\n\x06labels\x18\x08 \x03(\x0b\x32/.google.cloud.workflows.v1.Workflow.LabelsEntryR\x06labels\x12\'\n\x0fservice_account\x18\t \x01(\tR\x0eserviceAccount\x12)\n\x0fsource_contents\x18\n \x01(\tH\x00R\x0esourceContents\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"*\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01:d\xea\x41\x61\n!workflows.googleapis.com/Workflow\x12<projects/{project}/locations/{location}/workflows/{workflow}B\r\n\x0bsource_code\"\xc9\x01\n\x14ListWorkflowsRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12\x16\n\x06\x66ilter\x18\x04 \x01(\tR\x06\x66ilter\x12\x19\n\x08order_by\x18\x05 \x01(\tR\x07orderBy\"\xa4\x01\n\x15ListWorkflowsResponse\x12\x41\n\tworkflows\x18\x01 \x03(\x0b\x32#.google.cloud.workflows.v1.WorkflowR\tworkflows\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12 \n\x0bunreachable\x18\x03 \x03(\tR\x0bunreachable\"T\n\x12GetWorkflowRequest\x12>\n\x04name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!workflows.googleapis.com/WorkflowR\x04name\"\xc9\x01\n\x15\x43reateWorkflowRequest\x12\x42\n\x06parent\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!locations.googleapis.com/LocationR\x06parent\x12\x45\n\x08workflow\x18\x02 \x01(\x0b\x32#.google.cloud.workflows.v1.WorkflowB\x04\xe2\x41\x01\x02R\x08workflow\x12%\n\x0bworkflow_id\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\nworkflowId\"W\n\x15\x44\x65leteWorkflowRequest\x12>\n\x04name\x18\x01 \x01(\tB*\xe2\x41\x01\x02\xfa\x41#\n!workflows.googleapis.com/WorkflowR\x04name\"\x9b\x01\n\x15UpdateWorkflowRequest\x12\x45\n\x08workflow\x18\x01 \x01(\x0b\x32#.google.cloud.workflows.v1.WorkflowB\x04\xe2\x41\x01\x02R\x08workflow\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"\xd4\x01\n\x11OperationMetadata\x12;\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x35\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x16\n\x06target\x18\x03 \x01(\tR\x06target\x12\x12\n\x04verb\x18\x04 \x01(\tR\x04verb\x12\x1f\n\x0b\x61pi_version\x18\x05 \x01(\tR\napiVersion2\xc7\x08\n\tWorkflows\x12\xb2\x01\n\rListWorkflows\x12/.google.cloud.workflows.v1.ListWorkflowsRequest\x1a\x30.google.cloud.workflows.v1.ListWorkflowsResponse\">\xda\x41\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/workflows\x12\x9f\x01\n\x0bGetWorkflow\x12-.google.cloud.workflows.v1.GetWorkflowRequest\x1a#.google.cloud.workflows.v1.Workflow\"<\xda\x41\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/workflows/*}\x12\xe0\x01\n\x0e\x43reateWorkflow\x12\x30.google.cloud.workflows.v1.CreateWorkflowRequest\x1a\x1d.google.longrunning.Operation\"}\xca\x41\x1d\n\x08Workflow\x12\x11OperationMetadata\xda\x41\x1bparent,workflow,workflow_id\x82\xd3\xe4\x93\x02\x39\"-/v1/{parent=projects/*/locations/*}/workflows:\x08workflow\x12\xcc\x01\n\x0e\x44\x65leteWorkflow\x12\x30.google.cloud.workflows.v1.DeleteWorkflowRequest\x1a\x1d.google.longrunning.Operation\"i\xca\x41*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xda\x41\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/workflows/*}\x12\xe2\x01\n\x0eUpdateWorkflow\x12\x30.google.cloud.workflows.v1.UpdateWorkflowRequest\x1a\x1d.google.longrunning.Operation\"\x7f\xca\x41\x1d\n\x08Workflow\x12\x11OperationMetadata\xda\x41\x14workflow,update_mask\x82\xd3\xe4\x93\x02\x42\x32\x36/v1/{workflow.name=projects/*/locations/*/workflows/*}:\x08workflow\x1aL\xca\x41\x18workflows.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformBu\n\x1d\x63om.google.cloud.workflows.v1B\x0eWorkflowsProtoP\x01ZBgoogle.golang.org/genproto/googleapis/cloud/workflows/v1;workflowsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_WORKFLOW_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='google.cloud.workflows.v1.Workflow.State',
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
      name='ACTIVE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=902,
  serialized_end=944,
)
_sym_db.RegisterEnumDescriptor(_WORKFLOW_STATE)


_WORKFLOW_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.cloud.workflows.v1.Workflow.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.workflows.v1.Workflow.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.workflows.v1.Workflow.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=843,
  serialized_end=900,
)

_WORKFLOW = _descriptor.Descriptor(
  name='Workflow',
  full_name='google.cloud.workflows.v1.Workflow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.workflows.v1.Workflow.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.workflows.v1.Workflow.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='google.cloud.workflows.v1.Workflow.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='state', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision_id', full_name='google.cloud.workflows.v1.Workflow.revision_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='revisionId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.workflows.v1.Workflow.create_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='createTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_time', full_name='google.cloud.workflows.v1.Workflow.update_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='updateTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision_create_time', full_name='google.cloud.workflows.v1.Workflow.revision_create_time', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='revisionCreateTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.cloud.workflows.v1.Workflow.labels', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service_account', full_name='google.cloud.workflows.v1.Workflow.service_account', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='serviceAccount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_contents', full_name='google.cloud.workflows.v1.Workflow.source_contents', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sourceContents', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_WORKFLOW_LABELSENTRY, ],
  enum_types=[
    _WORKFLOW_STATE,
  ],
  serialized_options=b'\352Aa\n!workflows.googleapis.com/Workflow\022<projects/{project}/locations/{location}/workflows/{workflow}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='source_code', full_name='google.cloud.workflows.v1.Workflow.source_code',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=292,
  serialized_end=1061,
)


_LISTWORKFLOWSREQUEST = _descriptor.Descriptor(
  name='ListWorkflowsRequest',
  full_name='google.cloud.workflows.v1.ListWorkflowsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.workflows.v1.ListWorkflowsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A#\n!locations.googleapis.com/Location', json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.workflows.v1.ListWorkflowsRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.workflows.v1.ListWorkflowsRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.cloud.workflows.v1.ListWorkflowsRequest.filter', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='filter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='google.cloud.workflows.v1.ListWorkflowsRequest.order_by', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='orderBy', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1064,
  serialized_end=1265,
)


_LISTWORKFLOWSRESPONSE = _descriptor.Descriptor(
  name='ListWorkflowsResponse',
  full_name='google.cloud.workflows.v1.ListWorkflowsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='workflows', full_name='google.cloud.workflows.v1.ListWorkflowsResponse.workflows', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='workflows', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.workflows.v1.ListWorkflowsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nextPageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unreachable', full_name='google.cloud.workflows.v1.ListWorkflowsResponse.unreachable', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='unreachable', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1268,
  serialized_end=1432,
)


_GETWORKFLOWREQUEST = _descriptor.Descriptor(
  name='GetWorkflowRequest',
  full_name='google.cloud.workflows.v1.GetWorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.workflows.v1.GetWorkflowRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A#\n!workflows.googleapis.com/Workflow', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1434,
  serialized_end=1518,
)


_CREATEWORKFLOWREQUEST = _descriptor.Descriptor(
  name='CreateWorkflowRequest',
  full_name='google.cloud.workflows.v1.CreateWorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.workflows.v1.CreateWorkflowRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A#\n!locations.googleapis.com/Location', json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workflow', full_name='google.cloud.workflows.v1.CreateWorkflowRequest.workflow', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='workflow', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='workflow_id', full_name='google.cloud.workflows.v1.CreateWorkflowRequest.workflow_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='workflowId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1521,
  serialized_end=1722,
)


_DELETEWORKFLOWREQUEST = _descriptor.Descriptor(
  name='DeleteWorkflowRequest',
  full_name='google.cloud.workflows.v1.DeleteWorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.workflows.v1.DeleteWorkflowRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A#\n!workflows.googleapis.com/Workflow', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1724,
  serialized_end=1811,
)


_UPDATEWORKFLOWREQUEST = _descriptor.Descriptor(
  name='UpdateWorkflowRequest',
  full_name='google.cloud.workflows.v1.UpdateWorkflowRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='workflow', full_name='google.cloud.workflows.v1.UpdateWorkflowRequest.workflow', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='workflow', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.cloud.workflows.v1.UpdateWorkflowRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='updateMask', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1814,
  serialized_end=1969,
)


_OPERATIONMETADATA = _descriptor.Descriptor(
  name='OperationMetadata',
  full_name='google.cloud.workflows.v1.OperationMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.workflows.v1.OperationMetadata.create_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='createTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.cloud.workflows.v1.OperationMetadata.end_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='endTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='google.cloud.workflows.v1.OperationMetadata.target', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='target', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='verb', full_name='google.cloud.workflows.v1.OperationMetadata.verb', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='verb', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='api_version', full_name='google.cloud.workflows.v1.OperationMetadata.api_version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='apiVersion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1972,
  serialized_end=2184,
)

_WORKFLOW_LABELSENTRY.containing_type = _WORKFLOW
_WORKFLOW.fields_by_name['state'].enum_type = _WORKFLOW_STATE
_WORKFLOW.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_WORKFLOW.fields_by_name['update_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_WORKFLOW.fields_by_name['revision_create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_WORKFLOW.fields_by_name['labels'].message_type = _WORKFLOW_LABELSENTRY
_WORKFLOW_STATE.containing_type = _WORKFLOW
_WORKFLOW.oneofs_by_name['source_code'].fields.append(
  _WORKFLOW.fields_by_name['source_contents'])
_WORKFLOW.fields_by_name['source_contents'].containing_oneof = _WORKFLOW.oneofs_by_name['source_code']
_LISTWORKFLOWSRESPONSE.fields_by_name['workflows'].message_type = _WORKFLOW
_CREATEWORKFLOWREQUEST.fields_by_name['workflow'].message_type = _WORKFLOW
_UPDATEWORKFLOWREQUEST.fields_by_name['workflow'].message_type = _WORKFLOW
_UPDATEWORKFLOWREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_OPERATIONMETADATA.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OPERATIONMETADATA.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Workflow'] = _WORKFLOW
DESCRIPTOR.message_types_by_name['ListWorkflowsRequest'] = _LISTWORKFLOWSREQUEST
DESCRIPTOR.message_types_by_name['ListWorkflowsResponse'] = _LISTWORKFLOWSRESPONSE
DESCRIPTOR.message_types_by_name['GetWorkflowRequest'] = _GETWORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['CreateWorkflowRequest'] = _CREATEWORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['DeleteWorkflowRequest'] = _DELETEWORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['UpdateWorkflowRequest'] = _UPDATEWORKFLOWREQUEST
DESCRIPTOR.message_types_by_name['OperationMetadata'] = _OPERATIONMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Workflow = _reflection.GeneratedProtocolMessageType('Workflow', (_message.Message,), {

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _WORKFLOW_LABELSENTRY,
    '__module__' : 'google.cloud.workflows.v1.workflows_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.workflows.v1.Workflow.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _WORKFLOW,
  '__module__' : 'google.cloud.workflows.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.workflows.v1.Workflow)
  })
_sym_db.RegisterMessage(Workflow)
_sym_db.RegisterMessage(Workflow.LabelsEntry)

ListWorkflowsRequest = _reflection.GeneratedProtocolMessageType('ListWorkflowsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTWORKFLOWSREQUEST,
  '__module__' : 'google.cloud.workflows.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.workflows.v1.ListWorkflowsRequest)
  })
_sym_db.RegisterMessage(ListWorkflowsRequest)

ListWorkflowsResponse = _reflection.GeneratedProtocolMessageType('ListWorkflowsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTWORKFLOWSRESPONSE,
  '__module__' : 'google.cloud.workflows.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.workflows.v1.ListWorkflowsResponse)
  })
_sym_db.RegisterMessage(ListWorkflowsResponse)

GetWorkflowRequest = _reflection.GeneratedProtocolMessageType('GetWorkflowRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETWORKFLOWREQUEST,
  '__module__' : 'google.cloud.workflows.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.workflows.v1.GetWorkflowRequest)
  })
_sym_db.RegisterMessage(GetWorkflowRequest)

CreateWorkflowRequest = _reflection.GeneratedProtocolMessageType('CreateWorkflowRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEWORKFLOWREQUEST,
  '__module__' : 'google.cloud.workflows.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.workflows.v1.CreateWorkflowRequest)
  })
_sym_db.RegisterMessage(CreateWorkflowRequest)

DeleteWorkflowRequest = _reflection.GeneratedProtocolMessageType('DeleteWorkflowRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEWORKFLOWREQUEST,
  '__module__' : 'google.cloud.workflows.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.workflows.v1.DeleteWorkflowRequest)
  })
_sym_db.RegisterMessage(DeleteWorkflowRequest)

UpdateWorkflowRequest = _reflection.GeneratedProtocolMessageType('UpdateWorkflowRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEWORKFLOWREQUEST,
  '__module__' : 'google.cloud.workflows.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.workflows.v1.UpdateWorkflowRequest)
  })
_sym_db.RegisterMessage(UpdateWorkflowRequest)

OperationMetadata = _reflection.GeneratedProtocolMessageType('OperationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONMETADATA,
  '__module__' : 'google.cloud.workflows.v1.workflows_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.workflows.v1.OperationMetadata)
  })
_sym_db.RegisterMessage(OperationMetadata)


DESCRIPTOR._options = None
_WORKFLOW_LABELSENTRY._options = None
_WORKFLOW.fields_by_name['state']._options = None
_WORKFLOW.fields_by_name['revision_id']._options = None
_WORKFLOW.fields_by_name['create_time']._options = None
_WORKFLOW.fields_by_name['update_time']._options = None
_WORKFLOW.fields_by_name['revision_create_time']._options = None
_WORKFLOW._options = None
_LISTWORKFLOWSREQUEST.fields_by_name['parent']._options = None
_GETWORKFLOWREQUEST.fields_by_name['name']._options = None
_CREATEWORKFLOWREQUEST.fields_by_name['parent']._options = None
_CREATEWORKFLOWREQUEST.fields_by_name['workflow']._options = None
_CREATEWORKFLOWREQUEST.fields_by_name['workflow_id']._options = None
_DELETEWORKFLOWREQUEST.fields_by_name['name']._options = None
_UPDATEWORKFLOWREQUEST.fields_by_name['workflow']._options = None

_WORKFLOWS = _descriptor.ServiceDescriptor(
  name='Workflows',
  full_name='google.cloud.workflows.v1.Workflows',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030workflows.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  create_key=_descriptor._internal_create_key,
  serialized_start=2187,
  serialized_end=3282,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListWorkflows',
    full_name='google.cloud.workflows.v1.Workflows.ListWorkflows',
    index=0,
    containing_service=None,
    input_type=_LISTWORKFLOWSREQUEST,
    output_type=_LISTWORKFLOWSRESPONSE,
    serialized_options=b'\332A\006parent\202\323\344\223\002/\022-/v1/{parent=projects/*/locations/*}/workflows',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetWorkflow',
    full_name='google.cloud.workflows.v1.Workflows.GetWorkflow',
    index=1,
    containing_service=None,
    input_type=_GETWORKFLOWREQUEST,
    output_type=_WORKFLOW,
    serialized_options=b'\332A\004name\202\323\344\223\002/\022-/v1/{name=projects/*/locations/*/workflows/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateWorkflow',
    full_name='google.cloud.workflows.v1.Workflows.CreateWorkflow',
    index=2,
    containing_service=None,
    input_type=_CREATEWORKFLOWREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A\035\n\010Workflow\022\021OperationMetadata\332A\033parent,workflow,workflow_id\202\323\344\223\0029\"-/v1/{parent=projects/*/locations/*}/workflows:\010workflow',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteWorkflow',
    full_name='google.cloud.workflows.v1.Workflows.DeleteWorkflow',
    index=3,
    containing_service=None,
    input_type=_DELETEWORKFLOWREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A*\n\025google.protobuf.Empty\022\021OperationMetadata\332A\004name\202\323\344\223\002/*-/v1/{name=projects/*/locations/*/workflows/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateWorkflow',
    full_name='google.cloud.workflows.v1.Workflows.UpdateWorkflow',
    index=4,
    containing_service=None,
    input_type=_UPDATEWORKFLOWREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A\035\n\010Workflow\022\021OperationMetadata\332A\024workflow,update_mask\202\323\344\223\002B26/v1/{workflow.name=projects/*/locations/*/workflows/*}:\010workflow',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_WORKFLOWS)

DESCRIPTOR.services_by_name['Workflows'] = _WORKFLOWS

# @@protoc_insertion_point(module_scope)
