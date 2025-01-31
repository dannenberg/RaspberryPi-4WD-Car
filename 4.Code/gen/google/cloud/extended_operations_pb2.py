# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/extended_operations.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/extended_operations.proto',
  package='google.cloud',
  syntax='proto3',
  serialized_options=b'\n\020com.google.cloudB\027ExtendedOperationsProtoP\001ZCgoogle.golang.org/genproto/googleapis/cloud/extendedops;extendedops\242\002\004GAPI',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&google/cloud/extended_operations.proto\x12\x0cgoogle.cloud\x1a google/protobuf/descriptor.proto*b\n\x18OperationResponseMapping\x12\r\n\tUNDEFINED\x10\x00\x12\x08\n\x04NAME\x10\x01\x12\n\n\x06STATUS\x10\x02\x12\x0e\n\nERROR_CODE\x10\x03\x12\x11\n\rERROR_MESSAGE\x10\x04:o\n\x0foperation_field\x12\x1d.google.protobuf.FieldOptions\x18\xfd\x08 \x01(\x0e\x32&.google.cloud.OperationResponseMappingR\x0eoperationField:V\n\x17operation_request_field\x12\x1d.google.protobuf.FieldOptions\x18\xfe\x08 \x01(\tR\x15operationRequestField:X\n\x18operation_response_field\x12\x1d.google.protobuf.FieldOptions\x18\xff\x08 \x01(\tR\x16operationResponseField:L\n\x11operation_service\x12\x1e.google.protobuf.MethodOptions\x18\xe1\t \x01(\tR\x10operationService:Y\n\x18operation_polling_method\x12\x1e.google.protobuf.MethodOptions\x18\xe2\t \x01(\x08R\x16operationPollingMethodBy\n\x10\x63om.google.cloudB\x17\x45xtendedOperationsProtoP\x01ZCgoogle.golang.org/genproto/googleapis/cloud/extendedops;extendedops\xa2\x02\x04GAPIb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_OPERATIONRESPONSEMAPPING = _descriptor.EnumDescriptor(
  name='OperationResponseMapping',
  full_name='google.cloud.OperationResponseMapping',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NAME', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATUS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR_CODE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ERROR_MESSAGE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=90,
  serialized_end=188,
)
_sym_db.RegisterEnumDescriptor(_OPERATIONRESPONSEMAPPING)

OperationResponseMapping = enum_type_wrapper.EnumTypeWrapper(_OPERATIONRESPONSEMAPPING)
UNDEFINED = 0
NAME = 1
STATUS = 2
ERROR_CODE = 3
ERROR_MESSAGE = 4

OPERATION_FIELD_FIELD_NUMBER = 1149
operation_field = _descriptor.FieldDescriptor(
  name='operation_field', full_name='google.cloud.operation_field', index=0,
  number=1149, type=14, cpp_type=8, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, json_name='operationField', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
OPERATION_REQUEST_FIELD_FIELD_NUMBER = 1150
operation_request_field = _descriptor.FieldDescriptor(
  name='operation_request_field', full_name='google.cloud.operation_request_field', index=1,
  number=1150, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, json_name='operationRequestField', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
OPERATION_RESPONSE_FIELD_FIELD_NUMBER = 1151
operation_response_field = _descriptor.FieldDescriptor(
  name='operation_response_field', full_name='google.cloud.operation_response_field', index=2,
  number=1151, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, json_name='operationResponseField', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
OPERATION_SERVICE_FIELD_NUMBER = 1249
operation_service = _descriptor.FieldDescriptor(
  name='operation_service', full_name='google.cloud.operation_service', index=3,
  number=1249, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=b"".decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, json_name='operationService', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)
OPERATION_POLLING_METHOD_FIELD_NUMBER = 1250
operation_polling_method = _descriptor.FieldDescriptor(
  name='operation_polling_method', full_name='google.cloud.operation_polling_method', index=4,
  number=1250, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, json_name='operationPollingMethod', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key)

DESCRIPTOR.enum_types_by_name['OperationResponseMapping'] = _OPERATIONRESPONSEMAPPING
DESCRIPTOR.extensions_by_name['operation_field'] = operation_field
DESCRIPTOR.extensions_by_name['operation_request_field'] = operation_request_field
DESCRIPTOR.extensions_by_name['operation_response_field'] = operation_response_field
DESCRIPTOR.extensions_by_name['operation_service'] = operation_service
DESCRIPTOR.extensions_by_name['operation_polling_method'] = operation_polling_method
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

operation_field.enum_type = _OPERATIONRESPONSEMAPPING
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(operation_field)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(operation_request_field)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(operation_response_field)
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(operation_service)
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(operation_polling_method)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
