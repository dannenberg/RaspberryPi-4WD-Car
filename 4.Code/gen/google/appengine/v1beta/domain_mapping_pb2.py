# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/appengine/v1beta/domain_mapping.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/appengine/v1beta/domain_mapping.proto',
  package='google.appengine.v1beta',
  syntax='proto3',
  serialized_options=b'\n\033com.google.appengine.v1betaB\022DomainMappingProtoP\001Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\252\002\035Google.Cloud.AppEngine.V1Beta\312\002\035Google\\Cloud\\AppEngine\\V1beta\352\002 Google::Cloud::AppEngine::V1beta',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,google/appengine/v1beta/domain_mapping.proto\x12\x17google.appengine.v1beta\x1a\x1cgoogle/api/annotations.proto\"\xd0\x01\n\rDomainMapping\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\x12G\n\x0cssl_settings\x18\x03 \x01(\x0b\x32$.google.appengine.v1beta.SslSettingsR\x0bsslSettings\x12R\n\x10resource_records\x18\x04 \x03(\x0b\x32\'.google.appengine.v1beta.ResourceRecordR\x0fresourceRecords\"\x91\x02\n\x0bSslSettings\x12%\n\x0e\x63\x65rtificate_id\x18\x01 \x01(\tR\rcertificateId\x12\x66\n\x13ssl_management_type\x18\x03 \x01(\x0e\x32\x36.google.appengine.v1beta.SslSettings.SslManagementTypeR\x11sslManagementType\x12\x43\n\x1epending_managed_certificate_id\x18\x04 \x01(\tR\x1bpendingManagedCertificateId\".\n\x11SslManagementType\x12\r\n\tAUTOMATIC\x10\x00\x12\n\n\x06MANUAL\x10\x01\"\xae\x01\n\x0eResourceRecord\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x16\n\x06rrdata\x18\x02 \x01(\tR\x06rrdata\x12\x46\n\x04type\x18\x03 \x01(\x0e\x32\x32.google.appengine.v1beta.ResourceRecord.RecordTypeR\x04type\"(\n\nRecordType\x12\x05\n\x01\x41\x10\x00\x12\x08\n\x04\x41\x41\x41\x41\x10\x01\x12\t\n\x05\x43NAME\x10\x02\x42\xd8\x01\n\x1b\x63om.google.appengine.v1betaB\x12\x44omainMappingProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine\xaa\x02\x1dGoogle.Cloud.AppEngine.V1Beta\xca\x02\x1dGoogle\\Cloud\\AppEngine\\V1beta\xea\x02 Google::Cloud::AppEngine::V1betab\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_SSLSETTINGS_SSLMANAGEMENTTYPE = _descriptor.EnumDescriptor(
  name='SslManagementType',
  full_name='google.appengine.v1beta.SslSettings.SslManagementType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUTOMATIC', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MANUAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=542,
  serialized_end=588,
)
_sym_db.RegisterEnumDescriptor(_SSLSETTINGS_SSLMANAGEMENTTYPE)

_RESOURCERECORD_RECORDTYPE = _descriptor.EnumDescriptor(
  name='RecordType',
  full_name='google.appengine.v1beta.ResourceRecord.RecordType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='A', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AAAA', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CNAME', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=725,
  serialized_end=765,
)
_sym_db.RegisterEnumDescriptor(_RESOURCERECORD_RECORDTYPE)


_DOMAINMAPPING = _descriptor.Descriptor(
  name='DomainMapping',
  full_name='google.appengine.v1beta.DomainMapping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.appengine.v1beta.DomainMapping.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.appengine.v1beta.DomainMapping.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssl_settings', full_name='google.appengine.v1beta.DomainMapping.ssl_settings', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sslSettings', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_records', full_name='google.appengine.v1beta.DomainMapping.resource_records', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='resourceRecords', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=104,
  serialized_end=312,
)


_SSLSETTINGS = _descriptor.Descriptor(
  name='SslSettings',
  full_name='google.appengine.v1beta.SslSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='certificate_id', full_name='google.appengine.v1beta.SslSettings.certificate_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='certificateId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssl_management_type', full_name='google.appengine.v1beta.SslSettings.ssl_management_type', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sslManagementType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pending_managed_certificate_id', full_name='google.appengine.v1beta.SslSettings.pending_managed_certificate_id', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pendingManagedCertificateId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SSLSETTINGS_SSLMANAGEMENTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=588,
)


_RESOURCERECORD = _descriptor.Descriptor(
  name='ResourceRecord',
  full_name='google.appengine.v1beta.ResourceRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.appengine.v1beta.ResourceRecord.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rrdata', full_name='google.appengine.v1beta.ResourceRecord.rrdata', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rrdata', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='google.appengine.v1beta.ResourceRecord.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='type', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RESOURCERECORD_RECORDTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=591,
  serialized_end=765,
)

_DOMAINMAPPING.fields_by_name['ssl_settings'].message_type = _SSLSETTINGS
_DOMAINMAPPING.fields_by_name['resource_records'].message_type = _RESOURCERECORD
_SSLSETTINGS.fields_by_name['ssl_management_type'].enum_type = _SSLSETTINGS_SSLMANAGEMENTTYPE
_SSLSETTINGS_SSLMANAGEMENTTYPE.containing_type = _SSLSETTINGS
_RESOURCERECORD.fields_by_name['type'].enum_type = _RESOURCERECORD_RECORDTYPE
_RESOURCERECORD_RECORDTYPE.containing_type = _RESOURCERECORD
DESCRIPTOR.message_types_by_name['DomainMapping'] = _DOMAINMAPPING
DESCRIPTOR.message_types_by_name['SslSettings'] = _SSLSETTINGS
DESCRIPTOR.message_types_by_name['ResourceRecord'] = _RESOURCERECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DomainMapping = _reflection.GeneratedProtocolMessageType('DomainMapping', (_message.Message,), {
  'DESCRIPTOR' : _DOMAINMAPPING,
  '__module__' : 'google.appengine.v1beta.domain_mapping_pb2'
  # @@protoc_insertion_point(class_scope:google.appengine.v1beta.DomainMapping)
  })
_sym_db.RegisterMessage(DomainMapping)

SslSettings = _reflection.GeneratedProtocolMessageType('SslSettings', (_message.Message,), {
  'DESCRIPTOR' : _SSLSETTINGS,
  '__module__' : 'google.appengine.v1beta.domain_mapping_pb2'
  # @@protoc_insertion_point(class_scope:google.appengine.v1beta.SslSettings)
  })
_sym_db.RegisterMessage(SslSettings)

ResourceRecord = _reflection.GeneratedProtocolMessageType('ResourceRecord', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCERECORD,
  '__module__' : 'google.appengine.v1beta.domain_mapping_pb2'
  # @@protoc_insertion_point(class_scope:google.appengine.v1beta.ResourceRecord)
  })
_sym_db.RegisterMessage(ResourceRecord)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
