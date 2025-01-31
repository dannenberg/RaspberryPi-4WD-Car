# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/services/google_ads_field_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.resources import google_ads_field_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_google__ads__field__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v8/services/google_ads_field_service.proto',
  package='google.ads.googleads.v8.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v8.servicesB\032GoogleAdsFieldServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V8.Services\312\002 Google\\Ads\\GoogleAds\\V8\\Services\352\002$Google::Ads::GoogleAds::V8::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n?google/ads/googleads/v8/services/google_ads_field_service.proto\x12 google.ads.googleads.v8.services\x1a\x38google/ads/googleads/v8/resources/google_ads_field.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\"q\n\x18GetGoogleAdsFieldRequest\x12U\n\rresource_name\x18\x01 \x01(\tB0\xe2\x41\x01\x02\xfa\x41)\n\'googleads.googleapis.com/GoogleAdsFieldR\x0cresourceName\"v\n\x1cSearchGoogleAdsFieldsRequest\x12\x1a\n\x05query\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x05query\x12\x1d\n\npage_token\x18\x02 \x01(\tR\tpageToken\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\"\xc4\x01\n\x1dSearchGoogleAdsFieldsResponse\x12K\n\x07results\x18\x01 \x03(\x0b\x32\x31.google.ads.googleads.v8.resources.GoogleAdsFieldR\x07results\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x12.\n\x13total_results_count\x18\x03 \x01(\x03R\x11totalResultsCount2\xec\x03\n\x15GoogleAdsFieldService\x12\xc1\x01\n\x11GetGoogleAdsField\x12:.google.ads.googleads.v8.services.GetGoogleAdsFieldRequest\x1a\x31.google.ads.googleads.v8.resources.GoogleAdsField\"=\xda\x41\rresource_name\x82\xd3\xe4\x93\x02\'\x12%/v8/{resource_name=googleAdsFields/*}\x12\xc7\x01\n\x15SearchGoogleAdsFields\x12>.google.ads.googleads.v8.services.SearchGoogleAdsFieldsRequest\x1a?.google.ads.googleads.v8.services.SearchGoogleAdsFieldsResponse\"-\xda\x41\x05query\x82\xd3\xe4\x93\x02\x1f\"\x1a/v8/googleAdsFields:search:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x81\x02\n$com.google.ads.googleads.v8.servicesB\x1aGoogleAdsFieldServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V8.Services\xca\x02 Google\\Ads\\GoogleAds\\V8\\Services\xea\x02$Google::Ads::GoogleAds::V8::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_google__ads__field__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])




_GETGOOGLEADSFIELDREQUEST = _descriptor.Descriptor(
  name='GetGoogleAdsFieldRequest',
  full_name='google.ads.googleads.v8.services.GetGoogleAdsFieldRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v8.services.GetGoogleAdsFieldRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A)\n\'googleads.googleapis.com/GoogleAdsField', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=274,
  serialized_end=387,
)


_SEARCHGOOGLEADSFIELDSREQUEST = _descriptor.Descriptor(
  name='SearchGoogleAdsFieldsRequest',
  full_name='google.ads.googleads.v8.services.SearchGoogleAdsFieldsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='google.ads.googleads.v8.services.SearchGoogleAdsFieldsRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='query', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.ads.googleads.v8.services.SearchGoogleAdsFieldsRequest.page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.ads.googleads.v8.services.SearchGoogleAdsFieldsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=389,
  serialized_end=507,
)


_SEARCHGOOGLEADSFIELDSRESPONSE = _descriptor.Descriptor(
  name='SearchGoogleAdsFieldsResponse',
  full_name='google.ads.googleads.v8.services.SearchGoogleAdsFieldsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v8.services.SearchGoogleAdsFieldsResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='results', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.ads.googleads.v8.services.SearchGoogleAdsFieldsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nextPageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_results_count', full_name='google.ads.googleads.v8.services.SearchGoogleAdsFieldsResponse.total_results_count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='totalResultsCount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=510,
  serialized_end=706,
)

_SEARCHGOOGLEADSFIELDSRESPONSE.fields_by_name['results'].message_type = google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_google__ads__field__pb2._GOOGLEADSFIELD
DESCRIPTOR.message_types_by_name['GetGoogleAdsFieldRequest'] = _GETGOOGLEADSFIELDREQUEST
DESCRIPTOR.message_types_by_name['SearchGoogleAdsFieldsRequest'] = _SEARCHGOOGLEADSFIELDSREQUEST
DESCRIPTOR.message_types_by_name['SearchGoogleAdsFieldsResponse'] = _SEARCHGOOGLEADSFIELDSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetGoogleAdsFieldRequest = _reflection.GeneratedProtocolMessageType('GetGoogleAdsFieldRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETGOOGLEADSFIELDREQUEST,
  '__module__' : 'google.ads.googleads.v8.services.google_ads_field_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.GetGoogleAdsFieldRequest)
  })
_sym_db.RegisterMessage(GetGoogleAdsFieldRequest)

SearchGoogleAdsFieldsRequest = _reflection.GeneratedProtocolMessageType('SearchGoogleAdsFieldsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHGOOGLEADSFIELDSREQUEST,
  '__module__' : 'google.ads.googleads.v8.services.google_ads_field_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.SearchGoogleAdsFieldsRequest)
  })
_sym_db.RegisterMessage(SearchGoogleAdsFieldsRequest)

SearchGoogleAdsFieldsResponse = _reflection.GeneratedProtocolMessageType('SearchGoogleAdsFieldsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHGOOGLEADSFIELDSRESPONSE,
  '__module__' : 'google.ads.googleads.v8.services.google_ads_field_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.SearchGoogleAdsFieldsResponse)
  })
_sym_db.RegisterMessage(SearchGoogleAdsFieldsResponse)


DESCRIPTOR._options = None
_GETGOOGLEADSFIELDREQUEST.fields_by_name['resource_name']._options = None
_SEARCHGOOGLEADSFIELDSREQUEST.fields_by_name['query']._options = None

_GOOGLEADSFIELDSERVICE = _descriptor.ServiceDescriptor(
  name='GoogleAdsFieldService',
  full_name='google.ads.googleads.v8.services.GoogleAdsFieldService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords',
  create_key=_descriptor._internal_create_key,
  serialized_start=709,
  serialized_end=1201,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetGoogleAdsField',
    full_name='google.ads.googleads.v8.services.GoogleAdsFieldService.GetGoogleAdsField',
    index=0,
    containing_service=None,
    input_type=_GETGOOGLEADSFIELDREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_google__ads__field__pb2._GOOGLEADSFIELD,
    serialized_options=b'\332A\rresource_name\202\323\344\223\002\'\022%/v8/{resource_name=googleAdsFields/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchGoogleAdsFields',
    full_name='google.ads.googleads.v8.services.GoogleAdsFieldService.SearchGoogleAdsFields',
    index=1,
    containing_service=None,
    input_type=_SEARCHGOOGLEADSFIELDSREQUEST,
    output_type=_SEARCHGOOGLEADSFIELDSRESPONSE,
    serialized_options=b'\332A\005query\202\323\344\223\002\037\"\032/v8/googleAdsFields:search:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GOOGLEADSFIELDSERVICE)

DESCRIPTOR.services_by_name['GoogleAdsFieldService'] = _GOOGLEADSFIELDSERVICE

# @@protoc_insertion_point(module_scope)
