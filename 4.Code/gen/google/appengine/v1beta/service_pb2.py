# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/appengine/v1beta/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.appengine.v1beta import network_settings_pb2 as google_dot_appengine_dot_v1beta_dot_network__settings__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/appengine/v1beta/service.proto',
  package='google.appengine.v1beta',
  syntax='proto3',
  serialized_options=b'\n\033com.google.appengine.v1betaB\014ServiceProtoP\001Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\252\002\035Google.Cloud.AppEngine.V1Beta\312\002\035Google\\Cloud\\AppEngine\\V1beta\352\002 Google::Cloud::AppEngine::V1beta',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%google/appengine/v1beta/service.proto\x12\x17google.appengine.v1beta\x1a.google/appengine/v1beta/network_settings.proto\x1a\x1cgoogle/api/annotations.proto\"\xbf\x01\n\x07Service\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12;\n\x05split\x18\x03 \x01(\x0b\x32%.google.appengine.v1beta.TrafficSplitR\x05split\x12S\n\x10network_settings\x18\x06 \x01(\x0b\x32(.google.appengine.v1beta.NetworkSettingsR\x0fnetworkSettings\"\xae\x02\n\x0cTrafficSplit\x12H\n\x08shard_by\x18\x01 \x01(\x0e\x32-.google.appengine.v1beta.TrafficSplit.ShardByR\x07shardBy\x12X\n\x0b\x61llocations\x18\x02 \x03(\x0b\x32\x36.google.appengine.v1beta.TrafficSplit.AllocationsEntryR\x0b\x61llocations\x1a>\n\x10\x41llocationsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value:\x02\x38\x01\":\n\x07ShardBy\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\n\n\x06\x43OOKIE\x10\x01\x12\x06\n\x02IP\x10\x02\x12\n\n\x06RANDOM\x10\x03\x42\xd2\x01\n\x1b\x63om.google.appengine.v1betaB\x0cServiceProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3'
  ,
  dependencies=[google_dot_appengine_dot_v1beta_dot_network__settings__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_TRAFFICSPLIT_SHARDBY = _descriptor.EnumDescriptor(
  name='ShardBy',
  full_name='google.appengine.v1beta.TrafficSplit.ShardBy',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COOKIE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RANDOM', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=583,
  serialized_end=641,
)
_sym_db.RegisterEnumDescriptor(_TRAFFICSPLIT_SHARDBY)


_SERVICE = _descriptor.Descriptor(
  name='Service',
  full_name='google.appengine.v1beta.Service',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.appengine.v1beta.Service.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.appengine.v1beta.Service.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='split', full_name='google.appengine.v1beta.Service.split', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='split', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='network_settings', full_name='google.appengine.v1beta.Service.network_settings', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='networkSettings', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=145,
  serialized_end=336,
)


_TRAFFICSPLIT_ALLOCATIONSENTRY = _descriptor.Descriptor(
  name='AllocationsEntry',
  full_name='google.appengine.v1beta.TrafficSplit.AllocationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.appengine.v1beta.TrafficSplit.AllocationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.appengine.v1beta.TrafficSplit.AllocationsEntry.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=519,
  serialized_end=581,
)

_TRAFFICSPLIT = _descriptor.Descriptor(
  name='TrafficSplit',
  full_name='google.appengine.v1beta.TrafficSplit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='shard_by', full_name='google.appengine.v1beta.TrafficSplit.shard_by', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='shardBy', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='allocations', full_name='google.appengine.v1beta.TrafficSplit.allocations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='allocations', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TRAFFICSPLIT_ALLOCATIONSENTRY, ],
  enum_types=[
    _TRAFFICSPLIT_SHARDBY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=641,
)

_SERVICE.fields_by_name['split'].message_type = _TRAFFICSPLIT
_SERVICE.fields_by_name['network_settings'].message_type = google_dot_appengine_dot_v1beta_dot_network__settings__pb2._NETWORKSETTINGS
_TRAFFICSPLIT_ALLOCATIONSENTRY.containing_type = _TRAFFICSPLIT
_TRAFFICSPLIT.fields_by_name['shard_by'].enum_type = _TRAFFICSPLIT_SHARDBY
_TRAFFICSPLIT.fields_by_name['allocations'].message_type = _TRAFFICSPLIT_ALLOCATIONSENTRY
_TRAFFICSPLIT_SHARDBY.containing_type = _TRAFFICSPLIT
DESCRIPTOR.message_types_by_name['Service'] = _SERVICE
DESCRIPTOR.message_types_by_name['TrafficSplit'] = _TRAFFICSPLIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Service = _reflection.GeneratedProtocolMessageType('Service', (_message.Message,), {
  'DESCRIPTOR' : _SERVICE,
  '__module__' : 'google.appengine.v1beta.service_pb2'
  # @@protoc_insertion_point(class_scope:google.appengine.v1beta.Service)
  })
_sym_db.RegisterMessage(Service)

TrafficSplit = _reflection.GeneratedProtocolMessageType('TrafficSplit', (_message.Message,), {

  'AllocationsEntry' : _reflection.GeneratedProtocolMessageType('AllocationsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRAFFICSPLIT_ALLOCATIONSENTRY,
    '__module__' : 'google.appengine.v1beta.service_pb2'
    # @@protoc_insertion_point(class_scope:google.appengine.v1beta.TrafficSplit.AllocationsEntry)
    })
  ,
  'DESCRIPTOR' : _TRAFFICSPLIT,
  '__module__' : 'google.appengine.v1beta.service_pb2'
  # @@protoc_insertion_point(class_scope:google.appengine.v1beta.TrafficSplit)
  })
_sym_db.RegisterMessage(TrafficSplit)
_sym_db.RegisterMessage(TrafficSplit.AllocationsEntry)


DESCRIPTOR._options = None
_TRAFFICSPLIT_ALLOCATIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
