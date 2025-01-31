# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/devtools/build/v1/publish_build_event.proto
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
from google.devtools.build.v1 import build_events_pb2 as google_dot_devtools_dot_build_dot_v1_dot_build__events__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/devtools/build/v1/publish_build_event.proto',
  package='google.devtools.build.v1',
  syntax='proto3',
  serialized_options=b'\n\034com.google.devtools.build.v1B\014BackendProtoP\001Z=google.golang.org/genproto/googleapis/devtools/build/v1;build\370\001\001\312\002\025Google\\Cloud\\Build\\V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2google/devtools/build/v1/publish_build_event.proto\x12\x18google.devtools.build.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a+google/devtools/build/v1/build_events.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\"\xad\x03\n\x1cPublishLifecycleEventRequest\x12h\n\rservice_level\x18\x01 \x01(\x0e\x32\x43.google.devtools.build.v1.PublishLifecycleEventRequest.ServiceLevelR\x0cserviceLevel\x12R\n\x0b\x62uild_event\x18\x02 \x01(\x0b\x32+.google.devtools.build.v1.OrderedBuildEventB\x04\xe2\x41\x01\x02R\nbuildEvent\x12@\n\x0estream_timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\rstreamTimeout\x12\x33\n\x15notification_keywords\x18\x04 \x03(\tR\x14notificationKeywords\x12#\n\nproject_id\x18\x06 \x01(\tB\x04\xe2\x41\x01\x02R\tprojectId\"3\n\x0cServiceLevel\x12\x12\n\x0eNONINTERACTIVE\x10\x00\x12\x0f\n\x0bINTERACTIVE\x10\x01\"\x8f\x01\n#PublishBuildToolEventStreamResponse\x12?\n\tstream_id\x18\x01 \x01(\x0b\x32\".google.devtools.build.v1.StreamIdR\x08streamId\x12\'\n\x0fsequence_number\x18\x02 \x01(\x03R\x0esequenceNumber\"\xb9\x01\n\x11OrderedBuildEvent\x12?\n\tstream_id\x18\x01 \x01(\x0b\x32\".google.devtools.build.v1.StreamIdR\x08streamId\x12\'\n\x0fsequence_number\x18\x02 \x01(\x03R\x0esequenceNumber\x12:\n\x05\x65vent\x18\x03 \x01(\x0b\x32$.google.devtools.build.v1.BuildEventR\x05\x65vent\"\xe1\x01\n\"PublishBuildToolEventStreamRequest\x12\x61\n\x13ordered_build_event\x18\x04 \x01(\x0b\x32+.google.devtools.build.v1.OrderedBuildEventB\x04\xe2\x41\x01\x02R\x11orderedBuildEvent\x12\x33\n\x15notification_keywords\x18\x05 \x03(\tR\x14notificationKeywords\x12#\n\nproject_id\x18\x06 \x01(\tB\x04\xe2\x41\x01\x02R\tprojectId2\xde\x04\n\x11PublishBuildEvent\x12\xc9\x01\n\x15PublishLifecycleEvent\x12\x36.google.devtools.build.v1.PublishLifecycleEventRequest\x1a\x16.google.protobuf.Empty\"`\x82\xd3\xe4\x93\x02Z\"3/v1/projects/{project_id=*}/lifecycleEvents:publish:\x01*Z \"\x1b/v1/lifecycleEvents:publish:\x01*\x12\xa6\x02\n\x1bPublishBuildToolEventStream\x12<.google.devtools.build.v1.PublishBuildToolEventStreamRequest\x1a=.google.devtools.build.v1.PublishBuildToolEventStreamResponse\"\x85\x01\xda\x41\x34ordered_build_event,notification_keywords,project_id\x82\xd3\xe4\x93\x02H\"*/v1/projects/{project_id=*}/events:publish:\x01*Z\x17\"\x12/v1/events:publish:\x01*(\x01\x30\x01\x1aT\xca\x41 buildeventservice.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\x88\x01\n\x1c\x63om.google.devtools.build.v1B\x0c\x42\x61\x63kendProtoP\x01Z=google.golang.org/genproto/googleapis/devtools/build/v1;build\xf8\x01\x01\xca\x02\x15Google\\Cloud\\Build\\V1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_devtools_dot_build_dot_v1_dot_build__events__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])



_PUBLISHLIFECYCLEEVENTREQUEST_SERVICELEVEL = _descriptor.EnumDescriptor(
  name='ServiceLevel',
  full_name='google.devtools.build.v1.PublishLifecycleEventRequest.ServiceLevel',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONINTERACTIVE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERACTIVE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=653,
  serialized_end=704,
)
_sym_db.RegisterEnumDescriptor(_PUBLISHLIFECYCLEEVENTREQUEST_SERVICELEVEL)


_PUBLISHLIFECYCLEEVENTREQUEST = _descriptor.Descriptor(
  name='PublishLifecycleEventRequest',
  full_name='google.devtools.build.v1.PublishLifecycleEventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_level', full_name='google.devtools.build.v1.PublishLifecycleEventRequest.service_level', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='serviceLevel', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='build_event', full_name='google.devtools.build.v1.PublishLifecycleEventRequest.build_event', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='buildEvent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stream_timeout', full_name='google.devtools.build.v1.PublishLifecycleEventRequest.stream_timeout', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='streamTimeout', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notification_keywords', full_name='google.devtools.build.v1.PublishLifecycleEventRequest.notification_keywords', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='notificationKeywords', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.build.v1.PublishLifecycleEventRequest.project_id', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='projectId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PUBLISHLIFECYCLEEVENTREQUEST_SERVICELEVEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=275,
  serialized_end=704,
)


_PUBLISHBUILDTOOLEVENTSTREAMRESPONSE = _descriptor.Descriptor(
  name='PublishBuildToolEventStreamResponse',
  full_name='google.devtools.build.v1.PublishBuildToolEventStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='google.devtools.build.v1.PublishBuildToolEventStreamResponse.stream_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='streamId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='google.devtools.build.v1.PublishBuildToolEventStreamResponse.sequence_number', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sequenceNumber', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=707,
  serialized_end=850,
)


_ORDEREDBUILDEVENT = _descriptor.Descriptor(
  name='OrderedBuildEvent',
  full_name='google.devtools.build.v1.OrderedBuildEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='google.devtools.build.v1.OrderedBuildEvent.stream_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='streamId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sequence_number', full_name='google.devtools.build.v1.OrderedBuildEvent.sequence_number', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sequenceNumber', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event', full_name='google.devtools.build.v1.OrderedBuildEvent.event', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='event', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=853,
  serialized_end=1038,
)


_PUBLISHBUILDTOOLEVENTSTREAMREQUEST = _descriptor.Descriptor(
  name='PublishBuildToolEventStreamRequest',
  full_name='google.devtools.build.v1.PublishBuildToolEventStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ordered_build_event', full_name='google.devtools.build.v1.PublishBuildToolEventStreamRequest.ordered_build_event', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='orderedBuildEvent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notification_keywords', full_name='google.devtools.build.v1.PublishBuildToolEventStreamRequest.notification_keywords', index=1,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='notificationKeywords', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.devtools.build.v1.PublishBuildToolEventStreamRequest.project_id', index=2,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='projectId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1041,
  serialized_end=1266,
)

_PUBLISHLIFECYCLEEVENTREQUEST.fields_by_name['service_level'].enum_type = _PUBLISHLIFECYCLEEVENTREQUEST_SERVICELEVEL
_PUBLISHLIFECYCLEEVENTREQUEST.fields_by_name['build_event'].message_type = _ORDEREDBUILDEVENT
_PUBLISHLIFECYCLEEVENTREQUEST.fields_by_name['stream_timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_PUBLISHLIFECYCLEEVENTREQUEST_SERVICELEVEL.containing_type = _PUBLISHLIFECYCLEEVENTREQUEST
_PUBLISHBUILDTOOLEVENTSTREAMRESPONSE.fields_by_name['stream_id'].message_type = google_dot_devtools_dot_build_dot_v1_dot_build__events__pb2._STREAMID
_ORDEREDBUILDEVENT.fields_by_name['stream_id'].message_type = google_dot_devtools_dot_build_dot_v1_dot_build__events__pb2._STREAMID
_ORDEREDBUILDEVENT.fields_by_name['event'].message_type = google_dot_devtools_dot_build_dot_v1_dot_build__events__pb2._BUILDEVENT
_PUBLISHBUILDTOOLEVENTSTREAMREQUEST.fields_by_name['ordered_build_event'].message_type = _ORDEREDBUILDEVENT
DESCRIPTOR.message_types_by_name['PublishLifecycleEventRequest'] = _PUBLISHLIFECYCLEEVENTREQUEST
DESCRIPTOR.message_types_by_name['PublishBuildToolEventStreamResponse'] = _PUBLISHBUILDTOOLEVENTSTREAMRESPONSE
DESCRIPTOR.message_types_by_name['OrderedBuildEvent'] = _ORDEREDBUILDEVENT
DESCRIPTOR.message_types_by_name['PublishBuildToolEventStreamRequest'] = _PUBLISHBUILDTOOLEVENTSTREAMREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PublishLifecycleEventRequest = _reflection.GeneratedProtocolMessageType('PublishLifecycleEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHLIFECYCLEEVENTREQUEST,
  '__module__' : 'google.devtools.build.v1.publish_build_event_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.build.v1.PublishLifecycleEventRequest)
  })
_sym_db.RegisterMessage(PublishLifecycleEventRequest)

PublishBuildToolEventStreamResponse = _reflection.GeneratedProtocolMessageType('PublishBuildToolEventStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHBUILDTOOLEVENTSTREAMRESPONSE,
  '__module__' : 'google.devtools.build.v1.publish_build_event_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.build.v1.PublishBuildToolEventStreamResponse)
  })
_sym_db.RegisterMessage(PublishBuildToolEventStreamResponse)

OrderedBuildEvent = _reflection.GeneratedProtocolMessageType('OrderedBuildEvent', (_message.Message,), {
  'DESCRIPTOR' : _ORDEREDBUILDEVENT,
  '__module__' : 'google.devtools.build.v1.publish_build_event_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.build.v1.OrderedBuildEvent)
  })
_sym_db.RegisterMessage(OrderedBuildEvent)

PublishBuildToolEventStreamRequest = _reflection.GeneratedProtocolMessageType('PublishBuildToolEventStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHBUILDTOOLEVENTSTREAMREQUEST,
  '__module__' : 'google.devtools.build.v1.publish_build_event_pb2'
  # @@protoc_insertion_point(class_scope:google.devtools.build.v1.PublishBuildToolEventStreamRequest)
  })
_sym_db.RegisterMessage(PublishBuildToolEventStreamRequest)


DESCRIPTOR._options = None
_PUBLISHLIFECYCLEEVENTREQUEST.fields_by_name['build_event']._options = None
_PUBLISHLIFECYCLEEVENTREQUEST.fields_by_name['project_id']._options = None
_PUBLISHBUILDTOOLEVENTSTREAMREQUEST.fields_by_name['ordered_build_event']._options = None
_PUBLISHBUILDTOOLEVENTSTREAMREQUEST.fields_by_name['project_id']._options = None

_PUBLISHBUILDEVENT = _descriptor.ServiceDescriptor(
  name='PublishBuildEvent',
  full_name='google.devtools.build.v1.PublishBuildEvent',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A buildeventservice.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  create_key=_descriptor._internal_create_key,
  serialized_start=1269,
  serialized_end=1875,
  methods=[
  _descriptor.MethodDescriptor(
    name='PublishLifecycleEvent',
    full_name='google.devtools.build.v1.PublishBuildEvent.PublishLifecycleEvent',
    index=0,
    containing_service=None,
    input_type=_PUBLISHLIFECYCLEEVENTREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002Z\"3/v1/projects/{project_id=*}/lifecycleEvents:publish:\001*Z \"\033/v1/lifecycleEvents:publish:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PublishBuildToolEventStream',
    full_name='google.devtools.build.v1.PublishBuildEvent.PublishBuildToolEventStream',
    index=1,
    containing_service=None,
    input_type=_PUBLISHBUILDTOOLEVENTSTREAMREQUEST,
    output_type=_PUBLISHBUILDTOOLEVENTSTREAMRESPONSE,
    serialized_options=b'\332A4ordered_build_event,notification_keywords,project_id\202\323\344\223\002H\"*/v1/projects/{project_id=*}/events:publish:\001*Z\027\"\022/v1/events:publish:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PUBLISHBUILDEVENT)

DESCRIPTOR.services_by_name['PublishBuildEvent'] = _PUBLISHBUILDEVENT

# @@protoc_insertion_point(module_scope)
