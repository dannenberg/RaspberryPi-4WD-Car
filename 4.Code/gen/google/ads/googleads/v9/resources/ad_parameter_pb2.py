# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/resources/ad_parameter.proto
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
  name='google/ads/googleads/v9/resources/ad_parameter.proto',
  package='google.ads.googleads.v9.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v9.resourcesB\020AdParameterProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V9.Resources\312\002!Google\\Ads\\GoogleAds\\V9\\Resources\352\002%Google::Ads::GoogleAds::V9::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4google/ads/googleads/v9/resources/ad_parameter.proto\x12!google.ads.googleads.v9.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xe6\x03\n\x0b\x41\x64Parameter\x12R\n\rresource_name\x18\x01 \x01(\tB-\xe2\x41\x01\x05\xfa\x41&\n$googleads.googleapis.com/AdParameterR\x0cresourceName\x12\x65\n\x12\x61\x64_group_criterion\x18\x05 \x01(\tB2\xe2\x41\x01\x05\xfa\x41+\n)googleads.googleapis.com/AdGroupCriterionH\x00R\x10\x61\x64GroupCriterion\x88\x01\x01\x12\x32\n\x0fparameter_index\x18\x06 \x01(\x03\x42\x04\xe2\x41\x01\x05H\x01R\x0eparameterIndex\x88\x01\x01\x12*\n\x0einsertion_text\x18\x07 \x01(\tH\x02R\rinsertionText\x88\x01\x01:~\xea\x41{\n$googleads.googleapis.com/AdParameter\x12Scustomers/{customer_id}/adParameters/{ad_group_id}~{criterion_id}~{parameter_index}B\x15\n\x13_ad_group_criterionB\x12\n\x10_parameter_indexB\x11\n\x0f_insertion_textB\xfd\x01\n%com.google.ads.googleads.v9.resourcesB\x10\x41\x64ParameterProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v9/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V9.Resources\xca\x02!Google\\Ads\\GoogleAds\\V9\\Resources\xea\x02%Google::Ads::GoogleAds::V9::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ADPARAMETER = _descriptor.Descriptor(
  name='AdParameter',
  full_name='google.ads.googleads.v9.resources.AdParameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v9.resources.AdParameter.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A&\n$googleads.googleapis.com/AdParameter', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group_criterion', full_name='google.ads.googleads.v9.resources.AdParameter.ad_group_criterion', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A+\n)googleads.googleapis.com/AdGroupCriterion', json_name='adGroupCriterion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parameter_index', full_name='google.ads.googleads.v9.resources.AdParameter.parameter_index', index=2,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005', json_name='parameterIndex', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='insertion_text', full_name='google.ads.googleads.v9.resources.AdParameter.insertion_text', index=3,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='insertionText', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A{\n$googleads.googleapis.com/AdParameter\022Scustomers/{customer_id}/adParameters/{ad_group_id}~{criterion_id}~{parameter_index}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_ad_group_criterion', full_name='google.ads.googleads.v9.resources.AdParameter._ad_group_criterion',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_parameter_index', full_name='google.ads.googleads.v9.resources.AdParameter._parameter_index',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_insertion_text', full_name='google.ads.googleads.v9.resources.AdParameter._insertion_text',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=182,
  serialized_end=668,
)

_ADPARAMETER.oneofs_by_name['_ad_group_criterion'].fields.append(
  _ADPARAMETER.fields_by_name['ad_group_criterion'])
_ADPARAMETER.fields_by_name['ad_group_criterion'].containing_oneof = _ADPARAMETER.oneofs_by_name['_ad_group_criterion']
_ADPARAMETER.oneofs_by_name['_parameter_index'].fields.append(
  _ADPARAMETER.fields_by_name['parameter_index'])
_ADPARAMETER.fields_by_name['parameter_index'].containing_oneof = _ADPARAMETER.oneofs_by_name['_parameter_index']
_ADPARAMETER.oneofs_by_name['_insertion_text'].fields.append(
  _ADPARAMETER.fields_by_name['insertion_text'])
_ADPARAMETER.fields_by_name['insertion_text'].containing_oneof = _ADPARAMETER.oneofs_by_name['_insertion_text']
DESCRIPTOR.message_types_by_name['AdParameter'] = _ADPARAMETER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdParameter = _reflection.GeneratedProtocolMessageType('AdParameter', (_message.Message,), {
  'DESCRIPTOR' : _ADPARAMETER,
  '__module__' : 'google.ads.googleads.v9.resources.ad_parameter_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.resources.AdParameter)
  })
_sym_db.RegisterMessage(AdParameter)


DESCRIPTOR._options = None
_ADPARAMETER.fields_by_name['resource_name']._options = None
_ADPARAMETER.fields_by_name['ad_group_criterion']._options = None
_ADPARAMETER.fields_by_name['parameter_index']._options = None
_ADPARAMETER._options = None
# @@protoc_insertion_point(module_scope)
