# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/tasks/v2beta3/task.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.tasks.v2beta3 import target_pb2 as google_dot_cloud_dot_tasks_dot_v2beta3_dot_target__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/tasks/v2beta3/task.proto',
  package='google.cloud.tasks.v2beta3',
  syntax='proto3',
  serialized_options=b'\n\036com.google.cloud.tasks.v2beta3B\tTaskProtoP\001Z?google.golang.org/genproto/googleapis/cloud/tasks/v2beta3;tasks',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%google/cloud/tasks/v2beta3/task.proto\x12\x1agoogle.cloud.tasks.v2beta3\x1a\x19google/api/resource.proto\x1a\'google/cloud/tasks/v2beta3/target.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1cgoogle/api/annotations.proto\"\xaf\x07\n\x04Task\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12i\n\x17\x61pp_engine_http_request\x18\x03 \x01(\x0b\x32\x30.google.cloud.tasks.v2beta3.AppEngineHttpRequestH\x00R\x14\x61ppEngineHttpRequest\x12L\n\x0chttp_request\x18\x0b \x01(\x0b\x32\'.google.cloud.tasks.v2beta3.HttpRequestH\x00R\x0bhttpRequest\x12L\n\x0cpull_message\x18\r \x01(\x0b\x32\'.google.cloud.tasks.v2beta3.PullMessageH\x00R\x0bpullMessage\x12?\n\rschedule_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cscheduleTime\x12;\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x46\n\x11\x64ispatch_deadline\x18\x0c \x01(\x0b\x32\x19.google.protobuf.DurationR\x10\x64ispatchDeadline\x12%\n\x0e\x64ispatch_count\x18\x06 \x01(\x05R\rdispatchCount\x12%\n\x0eresponse_count\x18\x07 \x01(\x05R\rresponseCount\x12H\n\rfirst_attempt\x18\x08 \x01(\x0b\x32#.google.cloud.tasks.v2beta3.AttemptR\x0c\x66irstAttempt\x12\x46\n\x0clast_attempt\x18\t \x01(\x0b\x32#.google.cloud.tasks.v2beta3.AttemptR\x0blastAttempt\x12\x39\n\x04view\x18\n \x01(\x0e\x32%.google.cloud.tasks.v2beta3.Task.ViewR\x04view\"1\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05\x42\x41SIC\x10\x01\x12\x08\n\x04\x46ULL\x10\x02:h\xea\x41\x65\n\x1e\x63loudtasks.googleapis.com/Task\x12\x43projects/{project}/locations/{location}/queues/{queue}/tasks/{task}B\x0e\n\x0cpayload_type\"\x89\x02\n\x07\x41ttempt\x12?\n\rschedule_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cscheduleTime\x12?\n\rdispatch_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x64ispatchTime\x12?\n\rresponse_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cresponseTime\x12;\n\x0fresponse_status\x18\x04 \x01(\x0b\x32\x12.google.rpc.StatusR\x0eresponseStatusBn\n\x1e\x63om.google.cloud.tasks.v2beta3B\tTaskProtoP\x01Z?google.golang.org/genproto/googleapis/cloud/tasks/v2beta3;tasksb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_tasks_dot_v2beta3_dot_target__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_TASK_VIEW = _descriptor.EnumDescriptor(
  name='View',
  full_name='google.cloud.tasks.v2beta3.Task.View',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VIEW_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BASIC', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FULL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1030,
  serialized_end=1079,
)
_sym_db.RegisterEnumDescriptor(_TASK_VIEW)


_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='google.cloud.tasks.v2beta3.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.tasks.v2beta3.Task.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='app_engine_http_request', full_name='google.cloud.tasks.v2beta3.Task.app_engine_http_request', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='appEngineHttpRequest', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='http_request', full_name='google.cloud.tasks.v2beta3.Task.http_request', index=2,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='httpRequest', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pull_message', full_name='google.cloud.tasks.v2beta3.Task.pull_message', index=3,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pullMessage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schedule_time', full_name='google.cloud.tasks.v2beta3.Task.schedule_time', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='scheduleTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='google.cloud.tasks.v2beta3.Task.create_time', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='createTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dispatch_deadline', full_name='google.cloud.tasks.v2beta3.Task.dispatch_deadline', index=6,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dispatchDeadline', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dispatch_count', full_name='google.cloud.tasks.v2beta3.Task.dispatch_count', index=7,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dispatchCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_count', full_name='google.cloud.tasks.v2beta3.Task.response_count', index=8,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='responseCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_attempt', full_name='google.cloud.tasks.v2beta3.Task.first_attempt', index=9,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='firstAttempt', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_attempt', full_name='google.cloud.tasks.v2beta3.Task.last_attempt', index=10,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='lastAttempt', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='view', full_name='google.cloud.tasks.v2beta3.Task.view', index=11,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='view', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TASK_VIEW,
  ],
  serialized_options=b'\352Ae\n\036cloudtasks.googleapis.com/Task\022Cprojects/{project}/locations/{location}/queues/{queue}/tasks/{task}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload_type', full_name='google.cloud.tasks.v2beta3.Task.payload_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=258,
  serialized_end=1201,
)


_ATTEMPT = _descriptor.Descriptor(
  name='Attempt',
  full_name='google.cloud.tasks.v2beta3.Attempt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedule_time', full_name='google.cloud.tasks.v2beta3.Attempt.schedule_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='scheduleTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dispatch_time', full_name='google.cloud.tasks.v2beta3.Attempt.dispatch_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dispatchTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_time', full_name='google.cloud.tasks.v2beta3.Attempt.response_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='responseTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_status', full_name='google.cloud.tasks.v2beta3.Attempt.response_status', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='responseStatus', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1204,
  serialized_end=1469,
)

_TASK.fields_by_name['app_engine_http_request'].message_type = google_dot_cloud_dot_tasks_dot_v2beta3_dot_target__pb2._APPENGINEHTTPREQUEST
_TASK.fields_by_name['http_request'].message_type = google_dot_cloud_dot_tasks_dot_v2beta3_dot_target__pb2._HTTPREQUEST
_TASK.fields_by_name['pull_message'].message_type = google_dot_cloud_dot_tasks_dot_v2beta3_dot_target__pb2._PULLMESSAGE
_TASK.fields_by_name['schedule_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASK.fields_by_name['create_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TASK.fields_by_name['dispatch_deadline'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_TASK.fields_by_name['first_attempt'].message_type = _ATTEMPT
_TASK.fields_by_name['last_attempt'].message_type = _ATTEMPT
_TASK.fields_by_name['view'].enum_type = _TASK_VIEW
_TASK_VIEW.containing_type = _TASK
_TASK.oneofs_by_name['payload_type'].fields.append(
  _TASK.fields_by_name['app_engine_http_request'])
_TASK.fields_by_name['app_engine_http_request'].containing_oneof = _TASK.oneofs_by_name['payload_type']
_TASK.oneofs_by_name['payload_type'].fields.append(
  _TASK.fields_by_name['http_request'])
_TASK.fields_by_name['http_request'].containing_oneof = _TASK.oneofs_by_name['payload_type']
_TASK.oneofs_by_name['payload_type'].fields.append(
  _TASK.fields_by_name['pull_message'])
_TASK.fields_by_name['pull_message'].containing_oneof = _TASK.oneofs_by_name['payload_type']
_ATTEMPT.fields_by_name['schedule_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ATTEMPT.fields_by_name['dispatch_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ATTEMPT.fields_by_name['response_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ATTEMPT.fields_by_name['response_status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['Task'] = _TASK
DESCRIPTOR.message_types_by_name['Attempt'] = _ATTEMPT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Task = _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
  'DESCRIPTOR' : _TASK,
  '__module__' : 'google.cloud.tasks.v2beta3.task_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2beta3.Task)
  })
_sym_db.RegisterMessage(Task)

Attempt = _reflection.GeneratedProtocolMessageType('Attempt', (_message.Message,), {
  'DESCRIPTOR' : _ATTEMPT,
  '__module__' : 'google.cloud.tasks.v2beta3.task_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.tasks.v2beta3.Attempt)
  })
_sym_db.RegisterMessage(Attempt)


DESCRIPTOR._options = None
_TASK._options = None
# @@protoc_insertion_point(module_scope)
