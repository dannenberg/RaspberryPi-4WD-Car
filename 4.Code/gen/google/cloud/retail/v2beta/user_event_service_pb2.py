# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/retail/v2beta/user_event_service.proto
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
from google.api import httpbody_pb2 as google_dot_api_dot_httpbody__pb2
from google.cloud.retail.v2beta import export_config_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_export__config__pb2
from google.cloud.retail.v2beta import import_config_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_import__config__pb2
from google.cloud.retail.v2beta import purge_config_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_purge__config__pb2
from google.cloud.retail.v2beta import user_event_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_user__event__pb2
from google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/retail/v2beta/user_event_service.proto',
  package='google.cloud.retail.v2beta',
  syntax='proto3',
  serialized_options=b'\n\036com.google.cloud.retail.v2betaB\025UserEventServiceProtoP\001Z@google.golang.org/genproto/googleapis/cloud/retail/v2beta;retail\242\002\006RETAIL\252\002\032Google.Cloud.Retail.V2Beta\312\002\032Google\\Cloud\\Retail\\V2beta\352\002\035Google::Cloud::Retail::V2beta',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3google/cloud/retail/v2beta/user_event_service.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/httpbody.proto\x1a.google/cloud/retail/v2beta/export_config.proto\x1a.google/cloud/retail/v2beta/import_config.proto\x1a-google/cloud/retail/v2beta/purge_config.proto\x1a+google/cloud/retail/v2beta/user_event.proto\x1a#google/longrunning/operations.proto\"\x81\x01\n\x15WriteUserEventRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12J\n\nuser_event\x18\x02 \x01(\x0b\x32%.google.cloud.retail.v2beta.UserEventB\x04\xe2\x41\x01\x02R\tuserEvent\"\x80\x01\n\x17\x43ollectUserEventRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12#\n\nuser_event\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\tuserEvent\x12\x10\n\x03uri\x18\x03 \x01(\tR\x03uri\x12\x10\n\x03\x65ts\x18\x04 \x01(\x03R\x03\x65ts\"\xa1\x02\n\x17RejoinUserEventsRequest\x12\x1c\n\x06parent\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x06parent\x12\x7f\n\x17user_event_rejoin_scope\x18\x02 \x01(\x0e\x32H.google.cloud.retail.v2beta.RejoinUserEventsRequest.UserEventRejoinScopeR\x14userEventRejoinScope\"g\n\x14UserEventRejoinScope\x12\'\n#USER_EVENT_REJOIN_SCOPE_UNSPECIFIED\x10\x00\x12\x11\n\rJOINED_EVENTS\x10\x01\x12\x13\n\x0fUNJOINED_EVENTS\x10\x02\"W\n\x18RejoinUserEventsResponse\x12;\n\x1arejoined_user_events_count\x18\x01 \x01(\x03R\x17rejoinedUserEventsCount\"\x1a\n\x18RejoinUserEventsMetadata2\xfb\t\n\x10UserEventService\x12\xc3\x01\n\x0eWriteUserEvent\x12\x31.google.cloud.retail.v2beta.WriteUserEventRequest\x1a%.google.cloud.retail.v2beta.UserEvent\"W\x82\xd3\xe4\x93\x02Q\"C/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:write:\nuser_event\x12\xac\x01\n\x10\x43ollectUserEvent\x12\x33.google.cloud.retail.v2beta.CollectUserEventRequest\x1a\x14.google.api.HttpBody\"M\x82\xd3\xe4\x93\x02G\x12\x45/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:collect\x12\x96\x02\n\x0fPurgeUserEvents\x12\x32.google.cloud.retail.v2beta.PurgeUserEventsRequest\x1a\x1d.google.longrunning.Operation\"\xaf\x01\xca\x41^\n2google.cloud.retail.v2beta.PurgeUserEventsResponse\x12(google.cloud.retail.v2beta.PurgeMetadata\x82\xd3\xe4\x93\x02H\"C/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:purge:\x01*\x12\x9b\x02\n\x10ImportUserEvents\x12\x33.google.cloud.retail.v2beta.ImportUserEventsRequest\x1a\x1d.google.longrunning.Operation\"\xb2\x01\xca\x41`\n3google.cloud.retail.v2beta.ImportUserEventsResponse\x12)google.cloud.retail.v2beta.ImportMetadata\x82\xd3\xe4\x93\x02I\"D/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:import:\x01*\x12\xef\x01\n\x10RejoinUserEvents\x12\x33.google.cloud.retail.v2beta.RejoinUserEventsRequest\x1a\x1d.google.longrunning.Operation\"\x86\x01\xca\x41\x34\n\x18RejoinUserEventsResponse\x12\x18RejoinUserEventsMetadata\x82\xd3\xe4\x93\x02I\"D/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:rejoin:\x01*\x1aI\xca\x41\x15retail.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xde\x01\n\x1e\x63om.google.cloud.retail.v2betaB\x15UserEventServiceProtoP\x01Z@google.golang.org/genproto/googleapis/cloud/retail/v2beta;retail\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_httpbody__pb2.DESCRIPTOR,google_dot_cloud_dot_retail_dot_v2beta_dot_export__config__pb2.DESCRIPTOR,google_dot_cloud_dot_retail_dot_v2beta_dot_import__config__pb2.DESCRIPTOR,google_dot_cloud_dot_retail_dot_v2beta_dot_purge__config__pb2.DESCRIPTOR,google_dot_cloud_dot_retail_dot_v2beta_dot_user__event__pb2.DESCRIPTOR,google_dot_longrunning_dot_operations__pb2.DESCRIPTOR,])



_REJOINUSEREVENTSREQUEST_USEREVENTREJOINSCOPE = _descriptor.EnumDescriptor(
  name='UserEventRejoinScope',
  full_name='google.cloud.retail.v2beta.RejoinUserEventsRequest.UserEventRejoinScope',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER_EVENT_REJOIN_SCOPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JOINED_EVENTS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNJOINED_EVENTS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=873,
  serialized_end=976,
)
_sym_db.RegisterEnumDescriptor(_REJOINUSEREVENTSREQUEST_USEREVENTREJOINSCOPE)


_WRITEUSEREVENTREQUEST = _descriptor.Descriptor(
  name='WriteUserEventRequest',
  full_name='google.cloud.retail.v2beta.WriteUserEventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.retail.v2beta.WriteUserEventRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_event', full_name='google.cloud.retail.v2beta.WriteUserEventRequest.user_event', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='userEvent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=424,
  serialized_end=553,
)


_COLLECTUSEREVENTREQUEST = _descriptor.Descriptor(
  name='CollectUserEventRequest',
  full_name='google.cloud.retail.v2beta.CollectUserEventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.retail.v2beta.CollectUserEventRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_event', full_name='google.cloud.retail.v2beta.CollectUserEventRequest.user_event', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='userEvent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uri', full_name='google.cloud.retail.v2beta.CollectUserEventRequest.uri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='uri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ets', full_name='google.cloud.retail.v2beta.CollectUserEventRequest.ets', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=556,
  serialized_end=684,
)


_REJOINUSEREVENTSREQUEST = _descriptor.Descriptor(
  name='RejoinUserEventsRequest',
  full_name='google.cloud.retail.v2beta.RejoinUserEventsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.retail.v2beta.RejoinUserEventsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_event_rejoin_scope', full_name='google.cloud.retail.v2beta.RejoinUserEventsRequest.user_event_rejoin_scope', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='userEventRejoinScope', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REJOINUSEREVENTSREQUEST_USEREVENTREJOINSCOPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=687,
  serialized_end=976,
)


_REJOINUSEREVENTSRESPONSE = _descriptor.Descriptor(
  name='RejoinUserEventsResponse',
  full_name='google.cloud.retail.v2beta.RejoinUserEventsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rejoined_user_events_count', full_name='google.cloud.retail.v2beta.RejoinUserEventsResponse.rejoined_user_events_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rejoinedUserEventsCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=978,
  serialized_end=1065,
)


_REJOINUSEREVENTSMETADATA = _descriptor.Descriptor(
  name='RejoinUserEventsMetadata',
  full_name='google.cloud.retail.v2beta.RejoinUserEventsMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1067,
  serialized_end=1093,
)

_WRITEUSEREVENTREQUEST.fields_by_name['user_event'].message_type = google_dot_cloud_dot_retail_dot_v2beta_dot_user__event__pb2._USEREVENT
_REJOINUSEREVENTSREQUEST.fields_by_name['user_event_rejoin_scope'].enum_type = _REJOINUSEREVENTSREQUEST_USEREVENTREJOINSCOPE
_REJOINUSEREVENTSREQUEST_USEREVENTREJOINSCOPE.containing_type = _REJOINUSEREVENTSREQUEST
DESCRIPTOR.message_types_by_name['WriteUserEventRequest'] = _WRITEUSEREVENTREQUEST
DESCRIPTOR.message_types_by_name['CollectUserEventRequest'] = _COLLECTUSEREVENTREQUEST
DESCRIPTOR.message_types_by_name['RejoinUserEventsRequest'] = _REJOINUSEREVENTSREQUEST
DESCRIPTOR.message_types_by_name['RejoinUserEventsResponse'] = _REJOINUSEREVENTSRESPONSE
DESCRIPTOR.message_types_by_name['RejoinUserEventsMetadata'] = _REJOINUSEREVENTSMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WriteUserEventRequest = _reflection.GeneratedProtocolMessageType('WriteUserEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITEUSEREVENTREQUEST,
  '__module__' : 'google.cloud.retail.v2beta.user_event_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2beta.WriteUserEventRequest)
  })
_sym_db.RegisterMessage(WriteUserEventRequest)

CollectUserEventRequest = _reflection.GeneratedProtocolMessageType('CollectUserEventRequest', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTUSEREVENTREQUEST,
  '__module__' : 'google.cloud.retail.v2beta.user_event_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2beta.CollectUserEventRequest)
  })
_sym_db.RegisterMessage(CollectUserEventRequest)

RejoinUserEventsRequest = _reflection.GeneratedProtocolMessageType('RejoinUserEventsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REJOINUSEREVENTSREQUEST,
  '__module__' : 'google.cloud.retail.v2beta.user_event_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2beta.RejoinUserEventsRequest)
  })
_sym_db.RegisterMessage(RejoinUserEventsRequest)

RejoinUserEventsResponse = _reflection.GeneratedProtocolMessageType('RejoinUserEventsResponse', (_message.Message,), {
  'DESCRIPTOR' : _REJOINUSEREVENTSRESPONSE,
  '__module__' : 'google.cloud.retail.v2beta.user_event_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2beta.RejoinUserEventsResponse)
  })
_sym_db.RegisterMessage(RejoinUserEventsResponse)

RejoinUserEventsMetadata = _reflection.GeneratedProtocolMessageType('RejoinUserEventsMetadata', (_message.Message,), {
  'DESCRIPTOR' : _REJOINUSEREVENTSMETADATA,
  '__module__' : 'google.cloud.retail.v2beta.user_event_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2beta.RejoinUserEventsMetadata)
  })
_sym_db.RegisterMessage(RejoinUserEventsMetadata)


DESCRIPTOR._options = None
_WRITEUSEREVENTREQUEST.fields_by_name['parent']._options = None
_WRITEUSEREVENTREQUEST.fields_by_name['user_event']._options = None
_COLLECTUSEREVENTREQUEST.fields_by_name['parent']._options = None
_COLLECTUSEREVENTREQUEST.fields_by_name['user_event']._options = None
_REJOINUSEREVENTSREQUEST.fields_by_name['parent']._options = None

_USEREVENTSERVICE = _descriptor.ServiceDescriptor(
  name='UserEventService',
  full_name='google.cloud.retail.v2beta.UserEventService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\025retail.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  create_key=_descriptor._internal_create_key,
  serialized_start=1096,
  serialized_end=2371,
  methods=[
  _descriptor.MethodDescriptor(
    name='WriteUserEvent',
    full_name='google.cloud.retail.v2beta.UserEventService.WriteUserEvent',
    index=0,
    containing_service=None,
    input_type=_WRITEUSEREVENTREQUEST,
    output_type=google_dot_cloud_dot_retail_dot_v2beta_dot_user__event__pb2._USEREVENT,
    serialized_options=b'\202\323\344\223\002Q\"C/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:write:\nuser_event',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CollectUserEvent',
    full_name='google.cloud.retail.v2beta.UserEventService.CollectUserEvent',
    index=1,
    containing_service=None,
    input_type=_COLLECTUSEREVENTREQUEST,
    output_type=google_dot_api_dot_httpbody__pb2._HTTPBODY,
    serialized_options=b'\202\323\344\223\002G\022E/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:collect',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='PurgeUserEvents',
    full_name='google.cloud.retail.v2beta.UserEventService.PurgeUserEvents',
    index=2,
    containing_service=None,
    input_type=google_dot_cloud_dot_retail_dot_v2beta_dot_purge__config__pb2._PURGEUSEREVENTSREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A^\n2google.cloud.retail.v2beta.PurgeUserEventsResponse\022(google.cloud.retail.v2beta.PurgeMetadata\202\323\344\223\002H\"C/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:purge:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ImportUserEvents',
    full_name='google.cloud.retail.v2beta.UserEventService.ImportUserEvents',
    index=3,
    containing_service=None,
    input_type=google_dot_cloud_dot_retail_dot_v2beta_dot_import__config__pb2._IMPORTUSEREVENTSREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A`\n3google.cloud.retail.v2beta.ImportUserEventsResponse\022)google.cloud.retail.v2beta.ImportMetadata\202\323\344\223\002I\"D/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:import:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RejoinUserEvents',
    full_name='google.cloud.retail.v2beta.UserEventService.RejoinUserEvents',
    index=4,
    containing_service=None,
    input_type=_REJOINUSEREVENTSREQUEST,
    output_type=google_dot_longrunning_dot_operations__pb2._OPERATION,
    serialized_options=b'\312A4\n\030RejoinUserEventsResponse\022\030RejoinUserEventsMetadata\202\323\344\223\002I\"D/v2beta/{parent=projects/*/locations/*/catalogs/*}/userEvents:rejoin:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USEREVENTSERVICE)

DESCRIPTOR.services_by_name['UserEventService'] = _USEREVENTSERVICE

# @@protoc_insertion_point(module_scope)
