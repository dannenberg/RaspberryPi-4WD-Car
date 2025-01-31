# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/common/click_location.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v8/common/click_location.proto',
  package='google.ads.googleads.v8.common',
  syntax='proto3',
  serialized_options=b'\n\"com.google.ads.googleads.v8.commonB\022ClickLocationProtoP\001ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/common;common\242\002\003GAA\252\002\036Google.Ads.GoogleAds.V8.Common\312\002\036Google\\Ads\\GoogleAds\\V8\\Common\352\002\"Google::Ads::GoogleAds::V8::Common',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n3google/ads/googleads/v8/common/click_location.proto\x12\x1egoogle.ads.googleads.v8.common\x1a\x1cgoogle/api/annotations.proto\"\xe5\x01\n\rClickLocation\x12\x17\n\x04\x63ity\x18\x06 \x01(\tH\x00R\x04\x63ity\x88\x01\x01\x12\x1d\n\x07\x63ountry\x18\x07 \x01(\tH\x01R\x07\x63ountry\x88\x01\x01\x12\x19\n\x05metro\x18\x08 \x01(\tH\x02R\x05metro\x88\x01\x01\x12(\n\rmost_specific\x18\t \x01(\tH\x03R\x0cmostSpecific\x88\x01\x01\x12\x1b\n\x06region\x18\n \x01(\tH\x04R\x06region\x88\x01\x01\x42\x07\n\x05_cityB\n\n\x08_countryB\x08\n\x06_metroB\x10\n\x0e_most_specificB\t\n\x07_regionB\xed\x01\n\"com.google.ads.googleads.v8.commonB\x12\x43lickLocationProtoP\x01ZDgoogle.golang.org/genproto/googleapis/ads/googleads/v8/common;common\xa2\x02\x03GAA\xaa\x02\x1eGoogle.Ads.GoogleAds.V8.Common\xca\x02\x1eGoogle\\Ads\\GoogleAds\\V8\\Common\xea\x02\"Google::Ads::GoogleAds::V8::Commonb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CLICKLOCATION = _descriptor.Descriptor(
  name='ClickLocation',
  full_name='google.ads.googleads.v8.common.ClickLocation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='city', full_name='google.ads.googleads.v8.common.ClickLocation.city', index=0,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='city', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country', full_name='google.ads.googleads.v8.common.ClickLocation.country', index=1,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='country', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metro', full_name='google.ads.googleads.v8.common.ClickLocation.metro', index=2,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metro', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='most_specific', full_name='google.ads.googleads.v8.common.ClickLocation.most_specific', index=3,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='mostSpecific', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='google.ads.googleads.v8.common.ClickLocation.region', index=4,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='region', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='_city', full_name='google.ads.googleads.v8.common.ClickLocation._city',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_country', full_name='google.ads.googleads.v8.common.ClickLocation._country',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_metro', full_name='google.ads.googleads.v8.common.ClickLocation._metro',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_most_specific', full_name='google.ads.googleads.v8.common.ClickLocation._most_specific',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_region', full_name='google.ads.googleads.v8.common.ClickLocation._region',
      index=4, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=118,
  serialized_end=347,
)

_CLICKLOCATION.oneofs_by_name['_city'].fields.append(
  _CLICKLOCATION.fields_by_name['city'])
_CLICKLOCATION.fields_by_name['city'].containing_oneof = _CLICKLOCATION.oneofs_by_name['_city']
_CLICKLOCATION.oneofs_by_name['_country'].fields.append(
  _CLICKLOCATION.fields_by_name['country'])
_CLICKLOCATION.fields_by_name['country'].containing_oneof = _CLICKLOCATION.oneofs_by_name['_country']
_CLICKLOCATION.oneofs_by_name['_metro'].fields.append(
  _CLICKLOCATION.fields_by_name['metro'])
_CLICKLOCATION.fields_by_name['metro'].containing_oneof = _CLICKLOCATION.oneofs_by_name['_metro']
_CLICKLOCATION.oneofs_by_name['_most_specific'].fields.append(
  _CLICKLOCATION.fields_by_name['most_specific'])
_CLICKLOCATION.fields_by_name['most_specific'].containing_oneof = _CLICKLOCATION.oneofs_by_name['_most_specific']
_CLICKLOCATION.oneofs_by_name['_region'].fields.append(
  _CLICKLOCATION.fields_by_name['region'])
_CLICKLOCATION.fields_by_name['region'].containing_oneof = _CLICKLOCATION.oneofs_by_name['_region']
DESCRIPTOR.message_types_by_name['ClickLocation'] = _CLICKLOCATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClickLocation = _reflection.GeneratedProtocolMessageType('ClickLocation', (_message.Message,), {
  'DESCRIPTOR' : _CLICKLOCATION,
  '__module__' : 'google.ads.googleads.v8.common.click_location_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.common.ClickLocation)
  })
_sym_db.RegisterMessage(ClickLocation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
