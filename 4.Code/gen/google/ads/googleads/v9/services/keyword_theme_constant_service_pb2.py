# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v9/services/keyword_theme_constant_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v9.resources import keyword_theme_constant_pb2 as google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_keyword__theme__constant__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v9/services/keyword_theme_constant_service.proto',
  package='google.ads.googleads.v9.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v9.servicesB KeywordThemeConstantServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V9.Services\312\002 Google\\Ads\\GoogleAds\\V9\\Services\352\002$Google::Ads::GoogleAds::V9::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nEgoogle/ads/googleads/v9/services/keyword_theme_constant_service.proto\x12 google.ads.googleads.v9.services\x1a>google/ads/googleads/v9/resources/keyword_theme_constant.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"}\n\x1eGetKeywordThemeConstantRequest\x12[\n\rresource_name\x18\x01 \x01(\tB6\xe2\x41\x01\x02\xfa\x41/\n-googleads.googleapis.com/KeywordThemeConstantR\x0cresourceName\"\x8c\x01\n#SuggestKeywordThemeConstantsRequest\x12\x1d\n\nquery_text\x18\x01 \x01(\tR\tqueryText\x12!\n\x0c\x63ountry_code\x18\x02 \x01(\tR\x0b\x63ountryCode\x12#\n\rlanguage_code\x18\x03 \x01(\tR\x0clanguageCode\"\x97\x01\n$SuggestKeywordThemeConstantsResponse\x12o\n\x17keyword_theme_constants\x18\x01 \x03(\x0b\x32\x37.google.ads.googleads.v9.resources.KeywordThemeConstantR\x15keywordThemeConstants2\x9e\x04\n\x1bKeywordThemeConstantService\x12\xd9\x01\n\x17GetKeywordThemeConstant\x12@.google.ads.googleads.v9.services.GetKeywordThemeConstantRequest\x1a\x37.google.ads.googleads.v9.resources.KeywordThemeConstant\"C\xda\x41\rresource_name\x82\xd3\xe4\x93\x02-\x12+/v9/{resource_name=keywordThemeConstants/*}\x12\xdb\x01\n\x1cSuggestKeywordThemeConstants\x12\x45.google.ads.googleads.v9.services.SuggestKeywordThemeConstantsRequest\x1a\x46.google.ads.googleads.v9.services.SuggestKeywordThemeConstantsResponse\",\x82\xd3\xe4\x93\x02&\"!/v9/keywordThemeConstants:suggest:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x87\x02\n$com.google.ads.googleads.v9.servicesB KeywordThemeConstantServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v9/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V9.Services\xca\x02 Google\\Ads\\GoogleAds\\V9\\Services\xea\x02$Google::Ads::GoogleAds::V9::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_keyword__theme__constant__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETKEYWORDTHEMECONSTANTREQUEST = _descriptor.Descriptor(
  name='GetKeywordThemeConstantRequest',
  full_name='google.ads.googleads.v9.services.GetKeywordThemeConstantRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v9.services.GetKeywordThemeConstantRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A/\n-googleads.googleapis.com/KeywordThemeConstant', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=286,
  serialized_end=411,
)


_SUGGESTKEYWORDTHEMECONSTANTSREQUEST = _descriptor.Descriptor(
  name='SuggestKeywordThemeConstantsRequest',
  full_name='google.ads.googleads.v9.services.SuggestKeywordThemeConstantsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_text', full_name='google.ads.googleads.v9.services.SuggestKeywordThemeConstantsRequest.query_text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='queryText', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='google.ads.googleads.v9.services.SuggestKeywordThemeConstantsRequest.country_code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='countryCode', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.ads.googleads.v9.services.SuggestKeywordThemeConstantsRequest.language_code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='languageCode', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=414,
  serialized_end=554,
)


_SUGGESTKEYWORDTHEMECONSTANTSRESPONSE = _descriptor.Descriptor(
  name='SuggestKeywordThemeConstantsResponse',
  full_name='google.ads.googleads.v9.services.SuggestKeywordThemeConstantsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keyword_theme_constants', full_name='google.ads.googleads.v9.services.SuggestKeywordThemeConstantsResponse.keyword_theme_constants', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='keywordThemeConstants', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=557,
  serialized_end=708,
)

_SUGGESTKEYWORDTHEMECONSTANTSRESPONSE.fields_by_name['keyword_theme_constants'].message_type = google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_keyword__theme__constant__pb2._KEYWORDTHEMECONSTANT
DESCRIPTOR.message_types_by_name['GetKeywordThemeConstantRequest'] = _GETKEYWORDTHEMECONSTANTREQUEST
DESCRIPTOR.message_types_by_name['SuggestKeywordThemeConstantsRequest'] = _SUGGESTKEYWORDTHEMECONSTANTSREQUEST
DESCRIPTOR.message_types_by_name['SuggestKeywordThemeConstantsResponse'] = _SUGGESTKEYWORDTHEMECONSTANTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetKeywordThemeConstantRequest = _reflection.GeneratedProtocolMessageType('GetKeywordThemeConstantRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETKEYWORDTHEMECONSTANTREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.keyword_theme_constant_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.GetKeywordThemeConstantRequest)
  })
_sym_db.RegisterMessage(GetKeywordThemeConstantRequest)

SuggestKeywordThemeConstantsRequest = _reflection.GeneratedProtocolMessageType('SuggestKeywordThemeConstantsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTKEYWORDTHEMECONSTANTSREQUEST,
  '__module__' : 'google.ads.googleads.v9.services.keyword_theme_constant_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.SuggestKeywordThemeConstantsRequest)
  })
_sym_db.RegisterMessage(SuggestKeywordThemeConstantsRequest)

SuggestKeywordThemeConstantsResponse = _reflection.GeneratedProtocolMessageType('SuggestKeywordThemeConstantsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUGGESTKEYWORDTHEMECONSTANTSRESPONSE,
  '__module__' : 'google.ads.googleads.v9.services.keyword_theme_constant_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v9.services.SuggestKeywordThemeConstantsResponse)
  })
_sym_db.RegisterMessage(SuggestKeywordThemeConstantsResponse)


DESCRIPTOR._options = None
_GETKEYWORDTHEMECONSTANTREQUEST.fields_by_name['resource_name']._options = None

_KEYWORDTHEMECONSTANTSERVICE = _descriptor.ServiceDescriptor(
  name='KeywordThemeConstantService',
  full_name='google.ads.googleads.v9.services.KeywordThemeConstantService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords',
  create_key=_descriptor._internal_create_key,
  serialized_start=711,
  serialized_end=1253,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetKeywordThemeConstant',
    full_name='google.ads.googleads.v9.services.KeywordThemeConstantService.GetKeywordThemeConstant',
    index=0,
    containing_service=None,
    input_type=_GETKEYWORDTHEMECONSTANTREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v9_dot_resources_dot_keyword__theme__constant__pb2._KEYWORDTHEMECONSTANT,
    serialized_options=b'\332A\rresource_name\202\323\344\223\002-\022+/v9/{resource_name=keywordThemeConstants/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SuggestKeywordThemeConstants',
    full_name='google.ads.googleads.v9.services.KeywordThemeConstantService.SuggestKeywordThemeConstants',
    index=1,
    containing_service=None,
    input_type=_SUGGESTKEYWORDTHEMECONSTANTSREQUEST,
    output_type=_SUGGESTKEYWORDTHEMECONSTANTSRESPONSE,
    serialized_options=b'\202\323\344\223\002&\"!/v9/keywordThemeConstants:suggest:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_KEYWORDTHEMECONSTANTSERVICE)

DESCRIPTOR.services_by_name['KeywordThemeConstantService'] = _KEYWORDTHEMECONSTANTSERVICE

# @@protoc_insertion_point(module_scope)
