# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/apps/script/type/sheets/sheets_addon_manifest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.apps.script.type import extension_point_pb2 as google_dot_apps_dot_script_dot_type_dot_extension__point__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/apps/script/type/sheets/sheets_addon_manifest.proto',
  package='google.apps.script.type.sheets',
  syntax='proto3',
  serialized_options=b'\n\"com.google.apps.script.type.sheetsB\030SheetsAddOnManifestProtoP\001Z=google.golang.org/genproto/googleapis/apps/script/type/sheets\252\002\036Google.Apps.Script.Type.Sheets\312\002\036Google\\Apps\\Script\\Type\\Sheets\352\002\"Google::Apps::Script::Type::Sheets',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n:google/apps/script/type/sheets/sheets_addon_manifest.proto\x12\x1egoogle.apps.script.type.sheets\x1a\x1fgoogle/api/field_behavior.proto\x1a-google/apps/script/type/extension_point.proto\"\xe9\x01\n\x13SheetsAddOnManifest\x12Z\n\x10homepage_trigger\x18\x03 \x01(\x0b\x32/.google.apps.script.type.HomepageExtensionPointR\x0fhomepageTrigger\x12v\n\x1don_file_scope_granted_trigger\x18\x05 \x01(\x0b\x32\x34.google.apps.script.type.sheets.SheetsExtensionPointR\x19onFileScopeGrantedTrigger\"?\n\x14SheetsExtensionPoint\x12\'\n\x0crun_function\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x0brunFunctionB\xe6\x01\n\"com.google.apps.script.type.sheetsB\x18SheetsAddOnManifestProtoP\x01Z=google.golang.org/genproto/googleapis/apps/script/type/sheets\xaa\x02\x1eGoogle.Apps.Script.Type.Sheets\xca\x02\x1eGoogle\\Apps\\Script\\Type\\Sheets\xea\x02\"Google::Apps::Script::Type::Sheetsb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_apps_dot_script_dot_type_dot_extension__point__pb2.DESCRIPTOR,])




_SHEETSADDONMANIFEST = _descriptor.Descriptor(
  name='SheetsAddOnManifest',
  full_name='google.apps.script.type.sheets.SheetsAddOnManifest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='homepage_trigger', full_name='google.apps.script.type.sheets.SheetsAddOnManifest.homepage_trigger', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='homepageTrigger', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='on_file_scope_granted_trigger', full_name='google.apps.script.type.sheets.SheetsAddOnManifest.on_file_scope_granted_trigger', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='onFileScopeGrantedTrigger', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=175,
  serialized_end=408,
)


_SHEETSEXTENSIONPOINT = _descriptor.Descriptor(
  name='SheetsExtensionPoint',
  full_name='google.apps.script.type.sheets.SheetsExtensionPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='run_function', full_name='google.apps.script.type.sheets.SheetsExtensionPoint.run_function', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='runFunction', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=410,
  serialized_end=473,
)

_SHEETSADDONMANIFEST.fields_by_name['homepage_trigger'].message_type = google_dot_apps_dot_script_dot_type_dot_extension__point__pb2._HOMEPAGEEXTENSIONPOINT
_SHEETSADDONMANIFEST.fields_by_name['on_file_scope_granted_trigger'].message_type = _SHEETSEXTENSIONPOINT
DESCRIPTOR.message_types_by_name['SheetsAddOnManifest'] = _SHEETSADDONMANIFEST
DESCRIPTOR.message_types_by_name['SheetsExtensionPoint'] = _SHEETSEXTENSIONPOINT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SheetsAddOnManifest = _reflection.GeneratedProtocolMessageType('SheetsAddOnManifest', (_message.Message,), {
  'DESCRIPTOR' : _SHEETSADDONMANIFEST,
  '__module__' : 'google.apps.script.type.sheets.sheets_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.sheets.SheetsAddOnManifest)
  })
_sym_db.RegisterMessage(SheetsAddOnManifest)

SheetsExtensionPoint = _reflection.GeneratedProtocolMessageType('SheetsExtensionPoint', (_message.Message,), {
  'DESCRIPTOR' : _SHEETSEXTENSIONPOINT,
  '__module__' : 'google.apps.script.type.sheets.sheets_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.sheets.SheetsExtensionPoint)
  })
_sym_db.RegisterMessage(SheetsExtensionPoint)


DESCRIPTOR._options = None
_SHEETSEXTENSIONPOINT.fields_by_name['run_function']._options = None
# @@protoc_insertion_point(module_scope)
