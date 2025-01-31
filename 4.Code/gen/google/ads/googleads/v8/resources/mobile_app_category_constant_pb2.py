# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/mobile_app_category_constant.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v8/resources/mobile_app_category_constant.proto',
  package='google.ads.googleads.v8.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v8.resourcesB\036MobileAppCategoryConstantProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nDgoogle/ads/googleads/v8/resources/mobile_app_category_constant.proto\x12!google.ads.googleads.v8.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xb5\x02\n\x19MobileAppCategoryConstant\x12`\n\rresource_name\x18\x01 \x01(\tB;\xe2\x41\x01\x03\xfa\x41\x34\n2googleads.googleapis.com/MobileAppCategoryConstantR\x0cresourceName\x12\x19\n\x02id\x18\x04 \x01(\x05\x42\x04\xe2\x41\x01\x03H\x00R\x02id\x88\x01\x01\x12\x1d\n\x04name\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03H\x01R\x04name\x88\x01\x01:l\xea\x41i\n2googleads.googleapis.com/MobileAppCategoryConstant\x12\x33mobileAppCategoryConstants/{mobile_app_category_id}B\x05\n\x03_idB\x07\n\x05_nameB\x8b\x02\n%com.google.ads.googleads.v8.resourcesB\x1eMobileAppCategoryConstantProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_MOBILEAPPCATEGORYCONSTANT = _descriptor.Descriptor(
  name='MobileAppCategoryConstant',
  full_name='google.ads.googleads.v8.resources.MobileAppCategoryConstant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v8.resources.MobileAppCategoryConstant.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003\372A4\n2googleads.googleapis.com/MobileAppCategoryConstant', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v8.resources.MobileAppCategoryConstant.id', index=1,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.ads.googleads.v8.resources.MobileAppCategoryConstant.name', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352Ai\n2googleads.googleapis.com/MobileAppCategoryConstant\0223mobileAppCategoryConstants/{mobile_app_category_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_id', full_name='google.ads.googleads.v8.resources.MobileAppCategoryConstant._id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_name', full_name='google.ads.googleads.v8.resources.MobileAppCategoryConstant._name',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=198,
  serialized_end=507,
)

_MOBILEAPPCATEGORYCONSTANT.oneofs_by_name['_id'].fields.append(
  _MOBILEAPPCATEGORYCONSTANT.fields_by_name['id'])
_MOBILEAPPCATEGORYCONSTANT.fields_by_name['id'].containing_oneof = _MOBILEAPPCATEGORYCONSTANT.oneofs_by_name['_id']
_MOBILEAPPCATEGORYCONSTANT.oneofs_by_name['_name'].fields.append(
  _MOBILEAPPCATEGORYCONSTANT.fields_by_name['name'])
_MOBILEAPPCATEGORYCONSTANT.fields_by_name['name'].containing_oneof = _MOBILEAPPCATEGORYCONSTANT.oneofs_by_name['_name']
DESCRIPTOR.message_types_by_name['MobileAppCategoryConstant'] = _MOBILEAPPCATEGORYCONSTANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MobileAppCategoryConstant = _reflection.GeneratedProtocolMessageType('MobileAppCategoryConstant', (_message.Message,), {
  'DESCRIPTOR' : _MOBILEAPPCATEGORYCONSTANT,
  '__module__' : 'google.ads.googleads.v8.resources.mobile_app_category_constant_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.MobileAppCategoryConstant)
  })
_sym_db.RegisterMessage(MobileAppCategoryConstant)


DESCRIPTOR._options = None
_MOBILEAPPCATEGORYCONSTANT.fields_by_name['resource_name']._options = None
_MOBILEAPPCATEGORYCONSTANT.fields_by_name['id']._options = None
_MOBILEAPPCATEGORYCONSTANT.fields_by_name['name']._options = None
_MOBILEAPPCATEGORYCONSTANT._options = None
# @@protoc_insertion_point(module_scope)
