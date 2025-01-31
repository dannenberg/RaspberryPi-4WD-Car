# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/services/customer_negative_criterion_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_response__content__type__pb2
from google.ads.googleads.v8.resources import customer_negative_criterion_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_customer__negative__criterion__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v8/services/customer_negative_criterion_service.proto',
  package='google.ads.googleads.v8.services',
  syntax='proto3',
  serialized_options=b'\n$com.google.ads.googleads.v8.servicesB%CustomerNegativeCriterionServiceProtoP\001ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\242\002\003GAA\252\002 Google.Ads.GoogleAds.V8.Services\312\002 Google\\Ads\\GoogleAds\\V8\\Services\352\002$Google::Ads::GoogleAds::V8::Services',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nJgoogle/ads/googleads/v8/services/customer_negative_criterion_service.proto\x12 google.ads.googleads.v8.services\x1a\x39google/ads/googleads/v8/enums/response_content_type.proto\x1a\x43google/ads/googleads/v8/resources/customer_negative_criterion.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto\"\x87\x01\n#GetCustomerNegativeCriterionRequest\x12`\n\rresource_name\x18\x01 \x01(\tB;\xe2\x41\x01\x02\xfa\x41\x34\n2googleads.googleapis.com/CustomerNegativeCriterionR\x0cresourceName\"\x88\x03\n%MutateCustomerNegativeCriteriaRequest\x12%\n\x0b\x63ustomer_id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\ncustomerId\x12j\n\noperations\x18\x02 \x03(\x0b\x32\x44.google.ads.googleads.v8.services.CustomerNegativeCriterionOperationB\x04\xe2\x41\x01\x02R\noperations\x12\'\n\x0fpartial_failure\x18\x03 \x01(\x08R\x0epartialFailure\x12#\n\rvalidate_only\x18\x04 \x01(\x08R\x0cvalidateOnly\x12~\n\x15response_content_type\x18\x05 \x01(\x0e\x32J.google.ads.googleads.v8.enums.ResponseContentTypeEnum.ResponseContentTypeR\x13responseContentType\"\xa3\x01\n\"CustomerNegativeCriterionOperation\x12V\n\x06\x63reate\x18\x01 \x01(\x0b\x32<.google.ads.googleads.v8.resources.CustomerNegativeCriterionH\x00R\x06\x63reate\x12\x18\n\x06remove\x18\x02 \x01(\tH\x00R\x06removeB\x0b\n\toperation\"\xd2\x01\n&MutateCustomerNegativeCriteriaResponse\x12\x46\n\x15partial_failure_error\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\x13partialFailureError\x12`\n\x07results\x18\x02 \x03(\x0b\x32\x46.google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaResultR\x07results\"\xc9\x01\n$MutateCustomerNegativeCriteriaResult\x12#\n\rresource_name\x18\x01 \x01(\tR\x0cresourceName\x12|\n\x1b\x63ustomer_negative_criterion\x18\x02 \x01(\x0b\x32<.google.ads.googleads.v8.resources.CustomerNegativeCriterionR\x19\x63ustomerNegativeCriterion2\xfc\x04\n CustomerNegativeCriterionService\x12\xf7\x01\n\x1cGetCustomerNegativeCriterion\x12\x45.google.ads.googleads.v8.services.GetCustomerNegativeCriterionRequest\x1a<.google.ads.googleads.v8.resources.CustomerNegativeCriterion\"R\xda\x41\rresource_name\x82\xd3\xe4\x93\x02<\x12:/v8/{resource_name=customers/*/customerNegativeCriteria/*}\x12\x96\x02\n\x1eMutateCustomerNegativeCriteria\x12G.google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaRequest\x1aH.google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaResponse\"a\xda\x41\x16\x63ustomer_id,operations\x82\xd3\xe4\x93\x02\x42\"=/v8/customers/{customer_id=*}/customerNegativeCriteria:mutate:\x01*\x1a\x45\xca\x41\x18googleads.googleapis.com\xd2\x41\'https://www.googleapis.com/auth/adwordsB\x8c\x02\n$com.google.ads.googleads.v8.servicesB%CustomerNegativeCriterionServiceProtoP\x01ZHgoogle.golang.org/genproto/googleapis/ads/googleads/v8/services;services\xa2\x02\x03GAA\xaa\x02 Google.Ads.GoogleAds.V8.Services\xca\x02 Google\\Ads\\GoogleAds\\V8\\Services\xea\x02$Google::Ads::GoogleAds::V8::Servicesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_response__content__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_customer__negative__criterion__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_GETCUSTOMERNEGATIVECRITERIONREQUEST = _descriptor.Descriptor(
  name='GetCustomerNegativeCriterionRequest',
  full_name='google.ads.googleads.v8.services.GetCustomerNegativeCriterionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v8.services.GetCustomerNegativeCriterionRequest.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A4\n2googleads.googleapis.com/CustomerNegativeCriterion', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=381,
  serialized_end=516,
)


_MUTATECUSTOMERNEGATIVECRITERIAREQUEST = _descriptor.Descriptor(
  name='MutateCustomerNegativeCriteriaRequest',
  full_name='google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer_id', full_name='google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaRequest.customer_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='customerId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operations', full_name='google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaRequest.operations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='operations', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='partial_failure', full_name='google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaRequest.partial_failure', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='partialFailure', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaRequest.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='validateOnly', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_content_type', full_name='google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaRequest.response_content_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='responseContentType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=519,
  serialized_end=911,
)


_CUSTOMERNEGATIVECRITERIONOPERATION = _descriptor.Descriptor(
  name='CustomerNegativeCriterionOperation',
  full_name='google.ads.googleads.v8.services.CustomerNegativeCriterionOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='create', full_name='google.ads.googleads.v8.services.CustomerNegativeCriterionOperation.create', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='create', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remove', full_name='google.ads.googleads.v8.services.CustomerNegativeCriterionOperation.remove', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='remove', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='operation', full_name='google.ads.googleads.v8.services.CustomerNegativeCriterionOperation.operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=914,
  serialized_end=1077,
)


_MUTATECUSTOMERNEGATIVECRITERIARESPONSE = _descriptor.Descriptor(
  name='MutateCustomerNegativeCriteriaResponse',
  full_name='google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='partial_failure_error', full_name='google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaResponse.partial_failure_error', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='partialFailureError', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaResponse.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='results', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1080,
  serialized_end=1290,
)


_MUTATECUSTOMERNEGATIVECRITERIARESULT = _descriptor.Descriptor(
  name='MutateCustomerNegativeCriteriaResult',
  full_name='google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaResult.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='customer_negative_criterion', full_name='google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaResult.customer_negative_criterion', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='customerNegativeCriterion', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1293,
  serialized_end=1494,
)

_MUTATECUSTOMERNEGATIVECRITERIAREQUEST.fields_by_name['operations'].message_type = _CUSTOMERNEGATIVECRITERIONOPERATION
_MUTATECUSTOMERNEGATIVECRITERIAREQUEST.fields_by_name['response_content_type'].enum_type = google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_response__content__type__pb2._RESPONSECONTENTTYPEENUM_RESPONSECONTENTTYPE
_CUSTOMERNEGATIVECRITERIONOPERATION.fields_by_name['create'].message_type = google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_customer__negative__criterion__pb2._CUSTOMERNEGATIVECRITERION
_CUSTOMERNEGATIVECRITERIONOPERATION.oneofs_by_name['operation'].fields.append(
  _CUSTOMERNEGATIVECRITERIONOPERATION.fields_by_name['create'])
_CUSTOMERNEGATIVECRITERIONOPERATION.fields_by_name['create'].containing_oneof = _CUSTOMERNEGATIVECRITERIONOPERATION.oneofs_by_name['operation']
_CUSTOMERNEGATIVECRITERIONOPERATION.oneofs_by_name['operation'].fields.append(
  _CUSTOMERNEGATIVECRITERIONOPERATION.fields_by_name['remove'])
_CUSTOMERNEGATIVECRITERIONOPERATION.fields_by_name['remove'].containing_oneof = _CUSTOMERNEGATIVECRITERIONOPERATION.oneofs_by_name['operation']
_MUTATECUSTOMERNEGATIVECRITERIARESPONSE.fields_by_name['partial_failure_error'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_MUTATECUSTOMERNEGATIVECRITERIARESPONSE.fields_by_name['results'].message_type = _MUTATECUSTOMERNEGATIVECRITERIARESULT
_MUTATECUSTOMERNEGATIVECRITERIARESULT.fields_by_name['customer_negative_criterion'].message_type = google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_customer__negative__criterion__pb2._CUSTOMERNEGATIVECRITERION
DESCRIPTOR.message_types_by_name['GetCustomerNegativeCriterionRequest'] = _GETCUSTOMERNEGATIVECRITERIONREQUEST
DESCRIPTOR.message_types_by_name['MutateCustomerNegativeCriteriaRequest'] = _MUTATECUSTOMERNEGATIVECRITERIAREQUEST
DESCRIPTOR.message_types_by_name['CustomerNegativeCriterionOperation'] = _CUSTOMERNEGATIVECRITERIONOPERATION
DESCRIPTOR.message_types_by_name['MutateCustomerNegativeCriteriaResponse'] = _MUTATECUSTOMERNEGATIVECRITERIARESPONSE
DESCRIPTOR.message_types_by_name['MutateCustomerNegativeCriteriaResult'] = _MUTATECUSTOMERNEGATIVECRITERIARESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetCustomerNegativeCriterionRequest = _reflection.GeneratedProtocolMessageType('GetCustomerNegativeCriterionRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCUSTOMERNEGATIVECRITERIONREQUEST,
  '__module__' : 'google.ads.googleads.v8.services.customer_negative_criterion_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.GetCustomerNegativeCriterionRequest)
  })
_sym_db.RegisterMessage(GetCustomerNegativeCriterionRequest)

MutateCustomerNegativeCriteriaRequest = _reflection.GeneratedProtocolMessageType('MutateCustomerNegativeCriteriaRequest', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERNEGATIVECRITERIAREQUEST,
  '__module__' : 'google.ads.googleads.v8.services.customer_negative_criterion_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaRequest)
  })
_sym_db.RegisterMessage(MutateCustomerNegativeCriteriaRequest)

CustomerNegativeCriterionOperation = _reflection.GeneratedProtocolMessageType('CustomerNegativeCriterionOperation', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMERNEGATIVECRITERIONOPERATION,
  '__module__' : 'google.ads.googleads.v8.services.customer_negative_criterion_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.CustomerNegativeCriterionOperation)
  })
_sym_db.RegisterMessage(CustomerNegativeCriterionOperation)

MutateCustomerNegativeCriteriaResponse = _reflection.GeneratedProtocolMessageType('MutateCustomerNegativeCriteriaResponse', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERNEGATIVECRITERIARESPONSE,
  '__module__' : 'google.ads.googleads.v8.services.customer_negative_criterion_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaResponse)
  })
_sym_db.RegisterMessage(MutateCustomerNegativeCriteriaResponse)

MutateCustomerNegativeCriteriaResult = _reflection.GeneratedProtocolMessageType('MutateCustomerNegativeCriteriaResult', (_message.Message,), {
  'DESCRIPTOR' : _MUTATECUSTOMERNEGATIVECRITERIARESULT,
  '__module__' : 'google.ads.googleads.v8.services.customer_negative_criterion_service_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.services.MutateCustomerNegativeCriteriaResult)
  })
_sym_db.RegisterMessage(MutateCustomerNegativeCriteriaResult)


DESCRIPTOR._options = None
_GETCUSTOMERNEGATIVECRITERIONREQUEST.fields_by_name['resource_name']._options = None
_MUTATECUSTOMERNEGATIVECRITERIAREQUEST.fields_by_name['customer_id']._options = None
_MUTATECUSTOMERNEGATIVECRITERIAREQUEST.fields_by_name['operations']._options = None

_CUSTOMERNEGATIVECRITERIONSERVICE = _descriptor.ServiceDescriptor(
  name='CustomerNegativeCriterionService',
  full_name='google.ads.googleads.v8.services.CustomerNegativeCriterionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\030googleads.googleapis.com\322A\'https://www.googleapis.com/auth/adwords',
  create_key=_descriptor._internal_create_key,
  serialized_start=1497,
  serialized_end=2133,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetCustomerNegativeCriterion',
    full_name='google.ads.googleads.v8.services.CustomerNegativeCriterionService.GetCustomerNegativeCriterion',
    index=0,
    containing_service=None,
    input_type=_GETCUSTOMERNEGATIVECRITERIONREQUEST,
    output_type=google_dot_ads_dot_googleads_dot_v8_dot_resources_dot_customer__negative__criterion__pb2._CUSTOMERNEGATIVECRITERION,
    serialized_options=b'\332A\rresource_name\202\323\344\223\002<\022:/v8/{resource_name=customers/*/customerNegativeCriteria/*}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MutateCustomerNegativeCriteria',
    full_name='google.ads.googleads.v8.services.CustomerNegativeCriterionService.MutateCustomerNegativeCriteria',
    index=1,
    containing_service=None,
    input_type=_MUTATECUSTOMERNEGATIVECRITERIAREQUEST,
    output_type=_MUTATECUSTOMERNEGATIVECRITERIARESPONSE,
    serialized_options=b'\332A\026customer_id,operations\202\323\344\223\002B\"=/v8/customers/{customer_id=*}/customerNegativeCriteria:mutate:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CUSTOMERNEGATIVECRITERIONSERVICE)

DESCRIPTOR.services_by_name['CustomerNegativeCriterionService'] = _CUSTOMERNEGATIVECRITERIONSERVICE

# @@protoc_insertion_point(module_scope)
