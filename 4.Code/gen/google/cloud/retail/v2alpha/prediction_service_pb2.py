# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/retail/v2alpha/prediction_service.proto
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
from google.cloud.retail.v2alpha import user_event_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_user__event__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/retail/v2alpha/prediction_service.proto',
  package='google.cloud.retail.v2alpha',
  syntax='proto3',
  serialized_options=b'\n\037com.google.cloud.retail.v2alphaB\026PredictionServiceProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/retail/v2alpha;retail\242\002\006RETAIL\252\002\033Google.Cloud.Retail.V2Alpha\312\002\033Google\\Cloud\\Retail\\V2alpha\352\002\036Google::Cloud::Retail::V2alpha',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n4google/cloud/retail/v2alpha/prediction_service.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/cloud/retail/v2alpha/user_event.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xaa\x04\n\x0ePredictRequest\x12\"\n\tplacement\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\tplacement\x12K\n\nuser_event\x18\x02 \x01(\x0b\x32&.google.cloud.retail.v2alpha.UserEventB\x04\xe2\x41\x01\x02R\tuserEvent\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x04 \x01(\tR\tpageToken\x12\x16\n\x06\x66ilter\x18\x05 \x01(\tR\x06\x66ilter\x12#\n\rvalidate_only\x18\x06 \x01(\x08R\x0cvalidateOnly\x12O\n\x06params\x18\x07 \x03(\x0b\x32\x37.google.cloud.retail.v2alpha.PredictRequest.ParamsEntryR\x06params\x12O\n\x06labels\x18\x08 \x03(\x0b\x32\x37.google.cloud.retail.v2alpha.PredictRequest.LabelsEntryR\x06labels\x1aQ\n\x0bParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\x1a\x39\n\x0bLabelsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xc0\x03\n\x0fPredictResponse\x12W\n\x07results\x18\x01 \x03(\x0b\x32=.google.cloud.retail.v2alpha.PredictResponse.PredictionResultR\x07results\x12+\n\x11\x61ttribution_token\x18\x02 \x01(\tR\x10\x61ttributionToken\x12\x1f\n\x0bmissing_ids\x18\x03 \x03(\tR\nmissingIds\x12#\n\rvalidate_only\x18\x04 \x01(\x08R\x0cvalidateOnly\x1a\xe0\x01\n\x10PredictionResult\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12g\n\x08metadata\x18\x02 \x03(\x0b\x32K.google.cloud.retail.v2alpha.PredictResponse.PredictionResult.MetadataEntryR\x08metadata\x1aS\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueR\x05value:\x02\x38\x01\x32\x9d\x02\n\x11PredictionService\x12\xbc\x01\n\x07Predict\x12+.google.cloud.retail.v2alpha.PredictRequest\x1a,.google.cloud.retail.v2alpha.PredictResponse\"V\x82\xd3\xe4\x93\x02P\"K/v2alpha/{placement=projects/*/locations/*/catalogs/*/placements/*}:predict:\x01*\x1aI\xca\x41\x15retail.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xe4\x01\n\x1f\x63om.google.cloud.retail.v2alphaB\x16PredictionServiceProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/retail/v2alpha;retail\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_cloud_dot_retail_dot_v2alpha_dot_user__event__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])




_PREDICTREQUEST_PARAMSENTRY = _descriptor.Descriptor(
  name='ParamsEntry',
  full_name='google.cloud.retail.v2alpha.PredictRequest.ParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.retail.v2alpha.PredictRequest.ParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.retail.v2alpha.PredictRequest.ParamsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=664,
  serialized_end=745,
)

_PREDICTREQUEST_LABELSENTRY = _descriptor.Descriptor(
  name='LabelsEntry',
  full_name='google.cloud.retail.v2alpha.PredictRequest.LabelsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.retail.v2alpha.PredictRequest.LabelsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.retail.v2alpha.PredictRequest.LabelsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=747,
  serialized_end=804,
)

_PREDICTREQUEST = _descriptor.Descriptor(
  name='PredictRequest',
  full_name='google.cloud.retail.v2alpha.PredictRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='placement', full_name='google.cloud.retail.v2alpha.PredictRequest.placement', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='placement', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_event', full_name='google.cloud.retail.v2alpha.PredictRequest.user_event', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='userEvent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.retail.v2alpha.PredictRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.retail.v2alpha.PredictRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.cloud.retail.v2alpha.PredictRequest.filter', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='filter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.cloud.retail.v2alpha.PredictRequest.validate_only', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='validateOnly', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='google.cloud.retail.v2alpha.PredictRequest.params', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='params', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='google.cloud.retail.v2alpha.PredictRequest.labels', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTREQUEST_PARAMSENTRY, _PREDICTREQUEST_LABELSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=250,
  serialized_end=804,
)


_PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='google.cloud.retail.v2alpha.PredictResponse.PredictionResult.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.cloud.retail.v2alpha.PredictResponse.PredictionResult.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.cloud.retail.v2alpha.PredictResponse.PredictionResult.MetadataEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1172,
  serialized_end=1255,
)

_PREDICTRESPONSE_PREDICTIONRESULT = _descriptor.Descriptor(
  name='PredictionResult',
  full_name='google.cloud.retail.v2alpha.PredictResponse.PredictionResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='google.cloud.retail.v2alpha.PredictResponse.PredictionResult.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='google.cloud.retail.v2alpha.PredictResponse.PredictionResult.metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metadata', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1031,
  serialized_end=1255,
)

_PREDICTRESPONSE = _descriptor.Descriptor(
  name='PredictResponse',
  full_name='google.cloud.retail.v2alpha.PredictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='google.cloud.retail.v2alpha.PredictResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='results', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attribution_token', full_name='google.cloud.retail.v2alpha.PredictResponse.attribution_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='attributionToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='missing_ids', full_name='google.cloud.retail.v2alpha.PredictResponse.missing_ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='missingIds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='validate_only', full_name='google.cloud.retail.v2alpha.PredictResponse.validate_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='validateOnly', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PREDICTRESPONSE_PREDICTIONRESULT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=807,
  serialized_end=1255,
)

_PREDICTREQUEST_PARAMSENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_PREDICTREQUEST_PARAMSENTRY.containing_type = _PREDICTREQUEST
_PREDICTREQUEST_LABELSENTRY.containing_type = _PREDICTREQUEST
_PREDICTREQUEST.fields_by_name['user_event'].message_type = google_dot_cloud_dot_retail_dot_v2alpha_dot_user__event__pb2._USEREVENT
_PREDICTREQUEST.fields_by_name['params'].message_type = _PREDICTREQUEST_PARAMSENTRY
_PREDICTREQUEST.fields_by_name['labels'].message_type = _PREDICTREQUEST_LABELSENTRY
_PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY.fields_by_name['value'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY.containing_type = _PREDICTRESPONSE_PREDICTIONRESULT
_PREDICTRESPONSE_PREDICTIONRESULT.fields_by_name['metadata'].message_type = _PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY
_PREDICTRESPONSE_PREDICTIONRESULT.containing_type = _PREDICTRESPONSE
_PREDICTRESPONSE.fields_by_name['results'].message_type = _PREDICTRESPONSE_PREDICTIONRESULT
DESCRIPTOR.message_types_by_name['PredictRequest'] = _PREDICTREQUEST
DESCRIPTOR.message_types_by_name['PredictResponse'] = _PREDICTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PredictRequest = _reflection.GeneratedProtocolMessageType('PredictRequest', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTREQUEST_PARAMSENTRY,
    '__module__' : 'google.cloud.retail.v2alpha.prediction_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.retail.v2alpha.PredictRequest.ParamsEntry)
    })
  ,

  'LabelsEntry' : _reflection.GeneratedProtocolMessageType('LabelsEntry', (_message.Message,), {
    'DESCRIPTOR' : _PREDICTREQUEST_LABELSENTRY,
    '__module__' : 'google.cloud.retail.v2alpha.prediction_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.retail.v2alpha.PredictRequest.LabelsEntry)
    })
  ,
  'DESCRIPTOR' : _PREDICTREQUEST,
  '__module__' : 'google.cloud.retail.v2alpha.prediction_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2alpha.PredictRequest)
  })
_sym_db.RegisterMessage(PredictRequest)
_sym_db.RegisterMessage(PredictRequest.ParamsEntry)
_sym_db.RegisterMessage(PredictRequest.LabelsEntry)

PredictResponse = _reflection.GeneratedProtocolMessageType('PredictResponse', (_message.Message,), {

  'PredictionResult' : _reflection.GeneratedProtocolMessageType('PredictionResult', (_message.Message,), {

    'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
      'DESCRIPTOR' : _PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY,
      '__module__' : 'google.cloud.retail.v2alpha.prediction_service_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.retail.v2alpha.PredictResponse.PredictionResult.MetadataEntry)
      })
    ,
    'DESCRIPTOR' : _PREDICTRESPONSE_PREDICTIONRESULT,
    '__module__' : 'google.cloud.retail.v2alpha.prediction_service_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.retail.v2alpha.PredictResponse.PredictionResult)
    })
  ,
  'DESCRIPTOR' : _PREDICTRESPONSE,
  '__module__' : 'google.cloud.retail.v2alpha.prediction_service_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.retail.v2alpha.PredictResponse)
  })
_sym_db.RegisterMessage(PredictResponse)
_sym_db.RegisterMessage(PredictResponse.PredictionResult)
_sym_db.RegisterMessage(PredictResponse.PredictionResult.MetadataEntry)


DESCRIPTOR._options = None
_PREDICTREQUEST_PARAMSENTRY._options = None
_PREDICTREQUEST_LABELSENTRY._options = None
_PREDICTREQUEST.fields_by_name['placement']._options = None
_PREDICTREQUEST.fields_by_name['user_event']._options = None
_PREDICTRESPONSE_PREDICTIONRESULT_METADATAENTRY._options = None

_PREDICTIONSERVICE = _descriptor.ServiceDescriptor(
  name='PredictionService',
  full_name='google.cloud.retail.v2alpha.PredictionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\025retail.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  create_key=_descriptor._internal_create_key,
  serialized_start=1258,
  serialized_end=1543,
  methods=[
  _descriptor.MethodDescriptor(
    name='Predict',
    full_name='google.cloud.retail.v2alpha.PredictionService.Predict',
    index=0,
    containing_service=None,
    input_type=_PREDICTREQUEST,
    output_type=_PREDICTRESPONSE,
    serialized_options=b'\202\323\344\223\002P\"K/v2alpha/{placement=projects/*/locations/*/catalogs/*/placements/*}:predict:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICTIONSERVICE)

DESCRIPTOR.services_by_name['PredictionService'] = _PREDICTIONSERVICE

# @@protoc_insertion_point(module_scope)
