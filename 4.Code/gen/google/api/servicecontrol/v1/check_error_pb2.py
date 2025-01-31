# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/servicecontrol/v1/check_error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/api/servicecontrol/v1/check_error.proto',
  package='google.api.servicecontrol.v1',
  syntax='proto3',
  serialized_options=b'\n com.google.api.servicecontrol.v1B\017CheckErrorProtoP\001ZJgoogle.golang.org/genproto/googleapis/api/servicecontrol/v1;servicecontrol\370\001\001\252\002\036Google.Cloud.ServiceControl.V1\312\002\036Google\\Cloud\\ServiceControl\\V1\352\002!Google::Cloud::ServiceControl::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.google/api/servicecontrol/v1/check_error.proto\x12\x1cgoogle.api.servicecontrol.v1\x1a\x17google/rpc/status.proto\"\xcd\x05\n\nCheckError\x12\x41\n\x04\x63ode\x18\x01 \x01(\x0e\x32-.google.api.servicecontrol.v1.CheckError.CodeR\x04\x63ode\x12\x18\n\x07subject\x18\x04 \x01(\tR\x07subject\x12\x16\n\x06\x64\x65tail\x18\x02 \x01(\tR\x06\x64\x65tail\x12*\n\x06status\x18\x03 \x01(\x0b\x32\x12.google.rpc.StatusR\x06status\"\x9d\x04\n\x04\x43ode\x12\x1a\n\x16\x45RROR_CODE_UNSPECIFIED\x10\x00\x12\r\n\tNOT_FOUND\x10\x05\x12\x15\n\x11PERMISSION_DENIED\x10\x07\x12\x16\n\x12RESOURCE_EXHAUSTED\x10\x08\x12\x19\n\x15SERVICE_NOT_ACTIVATED\x10h\x12\x14\n\x10\x42ILLING_DISABLED\x10k\x12\x13\n\x0fPROJECT_DELETED\x10l\x12\x13\n\x0fPROJECT_INVALID\x10r\x12\x14\n\x10\x43ONSUMER_INVALID\x10}\x12\x16\n\x12IP_ADDRESS_BLOCKED\x10m\x12\x13\n\x0fREFERER_BLOCKED\x10n\x12\x16\n\x12\x43LIENT_APP_BLOCKED\x10o\x12\x16\n\x12\x41PI_TARGET_BLOCKED\x10z\x12\x13\n\x0f\x41PI_KEY_INVALID\x10i\x12\x13\n\x0f\x41PI_KEY_EXPIRED\x10p\x12\x15\n\x11\x41PI_KEY_NOT_FOUND\x10q\x12\x16\n\x12INVALID_CREDENTIAL\x10{\x12!\n\x1cNAMESPACE_LOOKUP_UNAVAILABLE\x10\xac\x02\x12\x1f\n\x1aSERVICE_STATUS_UNAVAILABLE\x10\xad\x02\x12\x1f\n\x1a\x42ILLING_STATUS_UNAVAILABLE\x10\xae\x02\x12/\n*CLOUD_RESOURCE_MANAGER_BACKEND_UNAVAILABLE\x10\xb1\x02\x42\xea\x01\n com.google.api.servicecontrol.v1B\x0f\x43heckErrorProtoP\x01ZJgoogle.golang.org/genproto/googleapis/api/servicecontrol/v1;servicecontrol\xf8\x01\x01\xaa\x02\x1eGoogle.Cloud.ServiceControl.V1\xca\x02\x1eGoogle\\Cloud\\ServiceControl\\V1\xea\x02!Google::Cloud::ServiceControl::V1b\x06proto3'
  ,
  dependencies=[google_dot_rpc_dot_status__pb2.DESCRIPTOR,])



_CHECKERROR_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='google.api.servicecontrol.v1.CheckError.Code',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ERROR_CODE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=1, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PERMISSION_DENIED', index=2, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_EXHAUSTED', index=3, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_NOT_ACTIVATED', index=4, number=104,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BILLING_DISABLED', index=5, number=107,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROJECT_DELETED', index=6, number=108,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROJECT_INVALID', index=7, number=114,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CONSUMER_INVALID', index=8, number=125,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IP_ADDRESS_BLOCKED', index=9, number=109,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REFERER_BLOCKED', index=10, number=110,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLIENT_APP_BLOCKED', index=11, number=111,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='API_TARGET_BLOCKED', index=12, number=122,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='API_KEY_INVALID', index=13, number=105,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='API_KEY_EXPIRED', index=14, number=112,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='API_KEY_NOT_FOUND', index=15, number=113,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_CREDENTIAL', index=16, number=123,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NAMESPACE_LOOKUP_UNAVAILABLE', index=17, number=300,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_STATUS_UNAVAILABLE', index=18, number=301,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BILLING_STATUS_UNAVAILABLE', index=19, number=302,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLOUD_RESOURCE_MANAGER_BACKEND_UNAVAILABLE', index=20, number=305,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=282,
  serialized_end=823,
)
_sym_db.RegisterEnumDescriptor(_CHECKERROR_CODE)


_CHECKERROR = _descriptor.Descriptor(
  name='CheckError',
  full_name='google.api.servicecontrol.v1.CheckError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='google.api.servicecontrol.v1.CheckError.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='code', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='subject', full_name='google.api.servicecontrol.v1.CheckError.subject', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='subject', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detail', full_name='google.api.servicecontrol.v1.CheckError.detail', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='detail', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.api.servicecontrol.v1.CheckError.status', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHECKERROR_CODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=106,
  serialized_end=823,
)

_CHECKERROR.fields_by_name['code'].enum_type = _CHECKERROR_CODE
_CHECKERROR.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_CHECKERROR_CODE.containing_type = _CHECKERROR
DESCRIPTOR.message_types_by_name['CheckError'] = _CHECKERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckError = _reflection.GeneratedProtocolMessageType('CheckError', (_message.Message,), {
  'DESCRIPTOR' : _CHECKERROR,
  '__module__' : 'google.api.servicecontrol.v1.check_error_pb2'
  # @@protoc_insertion_point(class_scope:google.api.servicecontrol.v1.CheckError)
  })
_sym_db.RegisterMessage(CheckError)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
