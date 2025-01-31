# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/eventarc/v1/eventarc.proto
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
from google.cloud.eventarc.v1 import trigger_pb2 as google_dot_cloud_dot_eventarc_dot_v1_dot_trigger__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/eventarc/v1/eventarc.proto',
  package='google.cloud.eventarc.v1',
  syntax='proto3',
  serialized_options=b'\n\034com.google.cloud.eventarc.v1B\rEventarcProtoP\001Z@google.golang.org/genproto/googleapis/cloud/eventarc/v1;eventarc\252\002\030Google.Cloud.Eventarc.V1\312\002\030Google\\Cloud\\Eventarc\\V1\352\002\033Google::Cloud::Eventarc::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'google/cloud/eventarc/v1/eventarc.proto\x12\x18google.cloud.eventarc.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/eventarc/v1/trigger.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"Q\n\x11GetTriggerRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x65ventarc.googleapis.com/TriggerR\x04name\"\xae\x01\n\x13ListTriggersRequest\x12@\n\x06parent\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\x12\x1f\x65ventarc.googleapis.com/TriggerR\x06parent\x12\x1b\n\tpage_size\x18\x02 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12\x19\n\x08order_by\x18\x04 \x01(\tR\x07orderBy\"\x9f\x01\n\x14ListTriggersResponse\x12=\n\x08triggers\x18\x01 \x03(\x0b\x32!.google.cloud.eventarc.v1.TriggerR\x08triggers\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12 \n\x0bunreachable\x18\x03 \x03(\tR\x0bunreachable\"\xeb\x01\n\x14\x43reateTriggerRequest\x12@\n\x06parent\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\x12\x1f\x65ventarc.googleapis.com/TriggerR\x06parent\x12\x41\n\x07trigger\x18\x02 \x01(\x0b\x32!.google.cloud.eventarc.v1.TriggerB\x04\xe2\x41\x01\x02R\x07trigger\x12#\n\ntrigger_id\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\ttriggerId\x12)\n\rvalidate_only\x18\x04 \x01(\x08\x42\x04\xe2\x41\x01\x02R\x0cvalidateOnly\"\xe0\x01\n\x14UpdateTriggerRequest\x12;\n\x07trigger\x18\x01 \x01(\x0b\x32!.google.cloud.eventarc.v1.TriggerR\x07trigger\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12#\n\rallow_missing\x18\x03 \x01(\x08R\x0c\x61llowMissing\x12)\n\rvalidate_only\x18\x04 \x01(\x08\x42\x04\xe2\x41\x01\x02R\x0cvalidateOnly\"\xb8\x01\n\x14\x44\x65leteTriggerRequest\x12<\n\x04name\x18\x01 \x01(\tB(\xe2\x41\x01\x02\xfa\x41!\n\x1f\x65ventarc.googleapis.com/TriggerR\x04name\x12\x12\n\x04\x65tag\x18\x02 \x01(\tR\x04\x65tag\x12#\n\rallow_missing\x18\x03 \x01(\x08R\x0c\x61llowMissing\x12)\n\rvalidate_only\x18\x04 \x01(\x08\x42\x04\xe2\x41\x01\x02R\x0cvalidateOnly\"\xdc\x02\n\x11OperationMetadata\x12\x41\n\x0b\x63reate_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\ncreateTime\x12;\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x04\xe2\x41\x01\x03R\x07\x65ndTime\x12\x1c\n\x06target\x18\x03 \x01(\tB\x04\xe2\x41\x01\x03R\x06target\x12\x18\n\x04verb\x18\x04 \x01(\tB\x04\xe2\x41\x01\x03R\x04verb\x12+\n\x0estatus_message\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03R\rstatusMessage\x12;\n\x16requested_cancellation\x18\x06 \x01(\x08\x42\x04\xe2\x41\x01\x03R\x15requestedCancellation\x12%\n\x0b\x61pi_version\x18\x07 \x01(\tB\x04\xe2\x41\x01\x03R\napiVersion2\xb4\x08\n\x08\x45ventarc\x12\x99\x01\n\nGetTrigger\x12+.google.cloud.eventarc.v1.GetTriggerRequest\x1a!.google.cloud.eventarc.v1.Trigger\";\xda\x41\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/triggers/*}\x12\xac\x01\n\x0cListTriggers\x12-.google.cloud.eventarc.v1.ListTriggersRequest\x1a..google.cloud.eventarc.v1.ListTriggersResponse\"=\xda\x41\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/triggers\x12\xd8\x01\n\rCreateTrigger\x12..google.cloud.eventarc.v1.CreateTriggerRequest\x1a\x1d.google.longrunning.Operation\"x\xca\x41\x1c\n\x07Trigger\x12\x11OperationMetadata\xda\x41\x19parent,trigger,trigger_id\x82\xd3\xe4\x93\x02\x37\",/v1/{parent=projects/*/locations/*}/triggers:\x07trigger\x12\xe9\x01\n\rUpdateTrigger\x12..google.cloud.eventarc.v1.UpdateTriggerRequest\x1a\x1d.google.longrunning.Operation\"\x88\x01\xca\x41\x1c\n\x07Trigger\x12\x11OperationMetadata\xda\x41!trigger,update_mask,allow_missing\x82\xd3\xe4\x93\x02?24/v1/{trigger.name=projects/*/locations/*/triggers/*}:\x07trigger\x12\xc8\x01\n\rDeleteTrigger\x12..google.cloud.eventarc.v1.DeleteTriggerRequest\x1a\x1d.google.longrunning.Operation\"h\xca\x41\x1c\n\x07Trigger\x12\x11OperationMetadata\xda\x41\x12name,allow_missing\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/triggers/*}\x1aK\xca\x41\x17\x65ventarc.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xc5\x01\n\x1c\x63om.google.cloud.eventarc.v1B\rEventarcProtoP\x01Z@google.golang.org/genproto/googleapis/cloud/eventarc/v1;eventarc\xaa\x02\x18Google.Cloud.Eventarc.V1\xca\x02\x18Google\\Cloud\\Eventarc\\V1\xea\x02\x1bGoogle::Cloud::Eventarc::V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_eventarc_dot_v1_dot_trigger__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_GETTRIGGERREQUEST = _descriptor.Descriptor(
  name='GetTriggerRequest',
  full_name='google.cloud.eventarc.v1.GetTriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.eventarc.v1.GetTriggerRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A!\n\037eventarc.googleapis.com/Trigger', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=328,
  serialized_end=409,
)


_LISTTRIGGERSREQUEST = _descriptor.Descriptor(
  name='ListTriggersRequest',
  full_name='google.cloud.eventarc.v1.ListTriggersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.eventarc.v1.ListTriggersRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A!\022\037eventarc.googleapis.com/Trigger', json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.eventarc.v1.ListTriggersRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.eventarc.v1.ListTriggersRequest.page_token', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order_by', full_name='google.cloud.eventarc.v1.ListTriggersRequest.order_by', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=412,
  serialized_end=586,
)


_LISTTRIGGERSRESPONSE = _descriptor.Descriptor(
  name='ListTriggersResponse',
  full_name='google.cloud.eventarc.v1.ListTriggersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='triggers', full_name='google.cloud.eventarc.v1.ListTriggersResponse.triggers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='triggers', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.eventarc.v1.ListTriggersResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nextPageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unreachable', full_name='google.cloud.eventarc.v1.ListTriggersResponse.unreachable', index=2,
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
  serialized_start=589,
  serialized_end=748,
)


_CREATETRIGGERREQUEST = _descriptor.Descriptor(
  name='CreateTriggerRequest',
  full_name='google.cloud.eventarc.v1.CreateTriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.eventarc.v1.CreateTriggerRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A!\022\037eventarc.googleapis.com/Trigger', json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trigger', full_name='google.cloud.eventarc.v1.CreateTriggerRequest.trigger', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='trigger', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trigger_id', full_name='google.cloud.eventarc.v1.CreateTriggerRequest.trigger_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='triggerId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.cloud.eventarc.v1.CreateTriggerRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='validateOnly', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=751,
  serialized_end=986,
)


_UPDATETRIGGERREQUEST = _descriptor.Descriptor(
  name='UpdateTriggerRequest',
  full_name='google.cloud.eventarc.v1.UpdateTriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger', full_name='google.cloud.eventarc.v1.UpdateTriggerRequest.trigger', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='trigger', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.cloud.eventarc.v1.UpdateTriggerRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='updateMask', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allow_missing', full_name='google.cloud.eventarc.v1.UpdateTriggerRequest.allow_missing', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='allowMissing', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.cloud.eventarc.v1.UpdateTriggerRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='validateOnly', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=989,
  serialized_end=1213,
)


_DELETETRIGGERREQUEST = _descriptor.Descriptor(
  name='DeleteTriggerRequest',
  full_name='google.cloud.eventarc.v1.DeleteTriggerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.eventarc.v1.DeleteTriggerRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A!\n\037eventarc.googleapis.com/Trigger', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='etag', full_name='google.cloud.eventarc.v1.DeleteTriggerRequest.etag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='etag', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allow_missing', full_name='google.cloud.eventarc.v1.DeleteTriggerRequest.allow_missing', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='allowMissing', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.cloud.eventarc.v1.DeleteTriggerRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='validateOnly', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1216,
  serialized_end=1400,
)


_OPERATIONMETADATA = _descriptor.Descriptor(
  name='OperationMetadata',
  full_name='google.cloud.eventarc.v1.OperationMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.eventarc.v1.OperationMetadata.create_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='createTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='google.cloud.eventarc.v1.OperationMetadata.end_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='endTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='google.cloud.eventarc.v1.OperationMetadata.target', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='target', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='verb', full_name='google.cloud.eventarc.v1.OperationMetadata.verb', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='verb', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status_message', full_name='google.cloud.eventarc.v1.OperationMetadata.status_message', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='statusMessage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='requested_cancellation', full_name='google.cloud.eventarc.v1.OperationMetadata.requested_cancellation', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='requestedCancellation', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='api_version', full_name='google.cloud.eventarc.v1.OperationMetadata.api_version', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='apiVersion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1403,
  serialized_end=1751,
)

_LISTTRIGGERSRESPONSE.fields_by_name['triggers'].message_type = google_dot_cloud_dot_eventarc_dot_v1_dot_trigger__pb2._TRIGGER
_CREATETRIGGERREQUEST.fields_by_name['trigger'].message_type = google_dot_cloud_dot_eventarc_dot_v1_dot_trigger__pb2._TRIGGER
_UPDATETRIGGERREQUEST.fields_by_name['trigger'].message_type = google_dot_cloud_dot_eventarc_dot_v1_dot_trigger__pb2._TRIGGER
_UPDATETRIGGERREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_OPERATIONMETADATA.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_OPERATIONMETADATA.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['GetTriggerRequest'] = _GETTRIGGERREQUEST
DESCRIPTOR.message_types_by_name['ListTriggersRequest'] = _LISTTRIGGERSREQUEST
DESCRIPTOR.message_types_by_name['ListTriggersResponse'] = _LISTTRIGGERSRESPONSE
DESCRIPTOR.message_types_by_name['CreateTriggerRequest'] = _CREATETRIGGERREQUEST
DESCRIPTOR.message_types_by_name['UpdateTriggerRequest'] = _UPDATETRIGGERREQUEST
DESCRIPTOR.message_types_by_name['DeleteTriggerRequest'] = _DELETETRIGGERREQUEST
DESCRIPTOR.message_types_by_name['OperationMetadata'] = _OPERATIONMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetTriggerRequest = _reflection.GeneratedProtocolMessageType('GetTriggerRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTRIGGERREQUEST,
  '__module__' : 'google.cloud.eventarc.v1.eventarc_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.eventarc.v1.GetTriggerRequest)
  })
_sym_db.RegisterMessage(GetTriggerRequest)

ListTriggersRequest = _reflection.GeneratedProtocolMessageType('ListTriggersRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRIGGERSREQUEST,
  '__module__' : 'google.cloud.eventarc.v1.eventarc_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.eventarc.v1.ListTriggersRequest)
  })
_sym_db.RegisterMessage(ListTriggersRequest)

ListTriggersResponse = _reflection.GeneratedProtocolMessageType('ListTriggersResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTTRIGGERSRESPONSE,
  '__module__' : 'google.cloud.eventarc.v1.eventarc_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.eventarc.v1.ListTriggersResponse)
  })
_sym_db.RegisterMessage(ListTriggersResponse)

CreateTriggerRequest = _reflection.GeneratedProtocolMessageType('CreateTriggerRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATETRIGGERREQUEST,
  '__module__' : 'google.cloud.eventarc.v1.eventarc_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.eventarc.v1.CreateTriggerRequest)
  })
_sym_db.RegisterMessage(CreateTriggerRequest)

UpdateTriggerRequest = _reflection.GeneratedProtocolMessageType('UpdateTriggerRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATETRIGGERREQUEST,
  '__module__' : 'google.cloud.eventarc.v1.eventarc_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.eventarc.v1.UpdateTriggerRequest)
  })
_sym_db.RegisterMessage(UpdateTriggerRequest)

DeleteTriggerRequest = _reflection.GeneratedProtocolMessageType('DeleteTriggerRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETRIGGERREQUEST,
  '__module__' : 'google.cloud.eventarc.v1.eventarc_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.eventarc.v1.DeleteTriggerRequest)
  })
_sym_db.RegisterMessage(DeleteTriggerRequest)

OperationMetadata = _reflection.GeneratedProtocolMessageType('OperationMetadata', (_message.Message,), {
  'DESCRIPTOR' : _OPERATIONMETADATA,
  '__module__' : 'google.cloud.eventarc.v1.eventarc_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.eventarc.v1.OperationMetadata)
  })
_sym_db.RegisterMessage(OperationMetadata)


DESCRIPTOR._options = None
_GETTRIGGERREQUEST.fields_by_name['name']._options = None
_LISTTRIGGERSREQUEST.fields_by_name['parent']._options = None
_CREATETRIGGERREQUEST.fields_by_name['parent']._options = None
_CREATETRIGGERREQUEST.fields_by_name['trigger']._options = None
_CREATETRIGGERREQUEST.fields_by_name['trigger_id']._options = None
_CREATETRIGGERREQUEST.fields_by_name['validate_only']._options = None
_UPDATETRIGGERREQUEST.fields_by_name['validate_only']._options = None
_DELETETRIGGERREQUEST.fields_by_name['name']._options = None
_DELETETRIGGERREQUEST.fields_by_name['validate_only']._options = None
_OPERATIONMETADATA.fields_by_name['create_time']._options = None
_OPERATIONMETADATA.fields_by_name['end_time']._options = None
_OPERATIONMETADATA.fields_by_name['target']._options = None
_OPERATIONMETADATA.fields_by_name['verb']._options = None
_OPERATIONMETADATA.fields_by_name['status_message']._options = None
_OPERATIONMETADATA.fields_by_name['requested_cancellation']._options = None
_OPERATIONMETADATA.fields_by_name['api_version']._options = None

_EVENTARC = _descriptor.ServiceDescriptor(
  name='Eventarc',
  full_name='google.cloud.eventarc.v1.Eventarc',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\027eventarc.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  create_key=_descriptor._internal_create_key,
  serialized_start=1754,
  serialized_end=2830,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTrigger',
    full_name='google.cloud.eventarc.v1.Eventarc.GetTrigger',
    index=0,
    containing_service=None,
    input_type=_GETTRIGGERREQUEST,
    output_type=google_dot_cloud_dot_eventarc_dot_v1_dot_trigger__pb2._TRIGGER,
    serialized_options=b'\332A\004name\202\323\344\223\002.\022,/v1/{name=projects/*/locations/*/triggers/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListTriggers',
    full_name='google.cloud.eventarc.v1.Eventarc.ListTriggers',
    index=1,
    containing_service=None,
    input_type=_LISTTRIGGERSREQUEST,
    output_type=_LISTTRIGGERSRESPONSE,
    serialized_options=b'\332A\006parent\202\323\344\223\002.\022,/v1/{parent=projects/*/locations/*}/triggers',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateTrigger',
    full_name='google.cloud.eventarc.v1.Eventarc.CreateTrigger',
    index=2,
    containing_service=None,
    input_type=_CREATETRIGGERREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A\034\n\007Trigger\022\021OperationMetadata\332A\031parent,trigger,trigger_id\202\323\344\223\0027\",/v1/{parent=projects/*/locations/*}/triggers:\007trigger',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateTrigger',
    full_name='google.cloud.eventarc.v1.Eventarc.UpdateTrigger',
    index=3,
    containing_service=None,
    input_type=_UPDATETRIGGERREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A\034\n\007Trigger\022\021OperationMetadata\332A!trigger,update_mask,allow_missing\202\323\344\223\002?24/v1/{trigger.name=projects/*/locations/*/triggers/*}:\007trigger',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteTrigger',
    full_name='google.cloud.eventarc.v1.Eventarc.DeleteTrigger',
    index=4,
    containing_service=None,
    input_type=_DELETETRIGGERREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A\034\n\007Trigger\022\021OperationMetadata\332A\022name,allow_missing\202\323\344\223\002.*,/v1/{name=projects/*/locations/*/triggers/*}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTARC)

DESCRIPTOR.services_by_name['Eventarc'] = _EVENTARC

# @@protoc_insertion_point(module_scope)
