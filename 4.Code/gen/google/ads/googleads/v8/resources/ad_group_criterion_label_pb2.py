# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/ad_group_criterion_label.proto
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
  name='google/ads/googleads/v8/resources/ad_group_criterion_label.proto',
  package='google.ads.googleads.v8.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v8.resourcesB\032AdGroupCriterionLabelProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n@google/ads/googleads/v8/resources/ad_group_criterion_label.proto\x12!google.ads.googleads.v8.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xd0\x03\n\x15\x41\x64GroupCriterionLabel\x12\\\n\rresource_name\x18\x01 \x01(\tB7\xe2\x41\x01\x05\xfa\x41\x30\n.googleads.googleapis.com/AdGroupCriterionLabelR\x0cresourceName\x12\x65\n\x12\x61\x64_group_criterion\x18\x04 \x01(\tB2\xe2\x41\x01\x05\xfa\x41+\n)googleads.googleapis.com/AdGroupCriterionH\x00R\x10\x61\x64GroupCriterion\x88\x01\x01\x12\x42\n\x05label\x18\x05 \x01(\tB\'\xe2\x41\x01\x05\xfa\x41 \n\x1egoogleads.googleapis.com/LabelH\x01R\x05label\x88\x01\x01:\x8c\x01\xea\x41\x88\x01\n.googleads.googleapis.com/AdGroupCriterionLabel\x12Vcustomers/{customer_id}/adGroupCriterionLabels/{ad_group_id}~{criterion_id}~{label_id}B\x15\n\x13_ad_group_criterionB\x08\n\x06_labelB\x87\x02\n%com.google.ads.googleads.v8.resourcesB\x1a\x41\x64GroupCriterionLabelProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_ADGROUPCRITERIONLABEL = _descriptor.Descriptor(
  name='AdGroupCriterionLabel',
  full_name='google.ads.googleads.v8.resources.AdGroupCriterionLabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v8.resources.AdGroupCriterionLabel.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A0\n.googleads.googleapis.com/AdGroupCriterionLabel', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ad_group_criterion', full_name='google.ads.googleads.v8.resources.AdGroupCriterionLabel.ad_group_criterion', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A+\n)googleads.googleapis.com/AdGroupCriterion', json_name='adGroupCriterion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='label', full_name='google.ads.googleads.v8.resources.AdGroupCriterionLabel.label', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A \n\036googleads.googleapis.com/Label', json_name='label', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A\210\001\n.googleads.googleapis.com/AdGroupCriterionLabel\022Vcustomers/{customer_id}/adGroupCriterionLabels/{ad_group_id}~{criterion_id}~{label_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_ad_group_criterion', full_name='google.ads.googleads.v8.resources.AdGroupCriterionLabel._ad_group_criterion',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_label', full_name='google.ads.googleads.v8.resources.AdGroupCriterionLabel._label',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=194,
  serialized_end=658,
)

_ADGROUPCRITERIONLABEL.oneofs_by_name['_ad_group_criterion'].fields.append(
  _ADGROUPCRITERIONLABEL.fields_by_name['ad_group_criterion'])
_ADGROUPCRITERIONLABEL.fields_by_name['ad_group_criterion'].containing_oneof = _ADGROUPCRITERIONLABEL.oneofs_by_name['_ad_group_criterion']
_ADGROUPCRITERIONLABEL.oneofs_by_name['_label'].fields.append(
  _ADGROUPCRITERIONLABEL.fields_by_name['label'])
_ADGROUPCRITERIONLABEL.fields_by_name['label'].containing_oneof = _ADGROUPCRITERIONLABEL.oneofs_by_name['_label']
DESCRIPTOR.message_types_by_name['AdGroupCriterionLabel'] = _ADGROUPCRITERIONLABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdGroupCriterionLabel = _reflection.GeneratedProtocolMessageType('AdGroupCriterionLabel', (_message.Message,), {
  'DESCRIPTOR' : _ADGROUPCRITERIONLABEL,
  '__module__' : 'google.ads.googleads.v8.resources.ad_group_criterion_label_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.AdGroupCriterionLabel)
  })
_sym_db.RegisterMessage(AdGroupCriterionLabel)


DESCRIPTOR._options = None
_ADGROUPCRITERIONLABEL.fields_by_name['resource_name']._options = None
_ADGROUPCRITERIONLABEL.fields_by_name['ad_group_criterion']._options = None
_ADGROUPCRITERIONLABEL.fields_by_name['label']._options = None
_ADGROUPCRITERIONLABEL._options = None
# @@protoc_insertion_point(module_scope)
