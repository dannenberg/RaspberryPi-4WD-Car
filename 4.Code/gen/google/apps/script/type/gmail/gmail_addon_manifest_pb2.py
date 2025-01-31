# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/apps/script/type/gmail/gmail_addon_manifest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.apps.script.type import addon_widget_set_pb2 as google_dot_apps_dot_script_dot_type_dot_addon__widget__set__pb2
from google.apps.script.type import extension_point_pb2 as google_dot_apps_dot_script_dot_type_dot_extension__point__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/apps/script/type/gmail/gmail_addon_manifest.proto',
  package='google.apps.script.type.gmail',
  syntax='proto3',
  serialized_options=b'\n!com.google.apps.script.type.gmailB\027GmailAddOnManifestProtoP\001Z<google.golang.org/genproto/googleapis/apps/script/type/gmail\252\002\035Google.Apps.Script.Type.Gmail\312\002\035Google\\Apps\\Script\\Type\\Gmail\352\002!Google::Apps::Script::Type::Gmail',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8google/apps/script/type/gmail/gmail_addon_manifest.proto\x12\x1dgoogle.apps.script.type.gmail\x1a.google/apps/script/type/addon_widget_set.proto\x1a-google/apps/script/type/extension_point.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xca\x03\n\x12GmailAddOnManifest\x12Z\n\x10homepage_trigger\x18\x0e \x01(\x0b\x32/.google.apps.script.type.HomepageExtensionPointR\x0fhomepageTrigger\x12\x61\n\x13\x63ontextual_triggers\x18\x03 \x03(\x0b\x32\x30.google.apps.script.type.gmail.ContextualTriggerR\x12\x63ontextualTriggers\x12[\n\x11universal_actions\x18\x04 \x03(\x0b\x32..google.apps.script.type.gmail.UniversalActionR\x10universalActions\x12V\n\x0f\x63ompose_trigger\x18\x0c \x01(\x0b\x32-.google.apps.script.type.gmail.ComposeTriggerR\x0e\x63omposeTrigger\x12@\n\x1c\x61uthorization_check_function\x18\x07 \x01(\tR\x1a\x61uthorizationCheckFunction\"x\n\x0fUniversalAction\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x1d\n\topen_link\x18\x02 \x01(\tH\x00R\x08openLink\x12#\n\x0crun_function\x18\x03 \x01(\tH\x00R\x0brunFunctionB\r\n\x0b\x61\x63tion_type\"\xf1\x01\n\x0e\x43omposeTrigger\x12I\n\x07\x61\x63tions\x18\x05 \x03(\x0b\x32/.google.apps.script.type.MenuItemExtensionPointR\x07\x61\x63tions\x12\\\n\x0c\x64raft_access\x18\x04 \x01(\x0e\x32\x39.google.apps.script.type.gmail.ComposeTrigger.DraftAccessR\x0b\x64raftAccess\"6\n\x0b\x44raftAccess\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x0c\n\x08METADATA\x10\x02\"\xab\x01\n\x11\x43ontextualTrigger\x12[\n\runconditional\x18\x01 \x01(\x0b\x32\x33.google.apps.script.type.gmail.UnconditionalTriggerH\x00R\runconditional\x12.\n\x13on_trigger_function\x18\x04 \x01(\tR\x11onTriggerFunctionB\t\n\x07trigger\"\x16\n\x14UnconditionalTriggerB\xe0\x01\n!com.google.apps.script.type.gmailB\x17GmailAddOnManifestProtoP\x01Z<google.golang.org/genproto/googleapis/apps/script/type/gmail\xaa\x02\x1dGoogle.Apps.Script.Type.Gmail\xca\x02\x1dGoogle\\Apps\\Script\\Type\\Gmail\xea\x02!Google::Apps::Script::Type::Gmailb\x06proto3'
  ,
  dependencies=[google_dot_apps_dot_script_dot_type_dot_addon__widget__set__pb2.DESCRIPTOR,google_dot_apps_dot_script_dot_type_dot_extension__point__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,])



_COMPOSETRIGGER_DRAFTACCESS = _descriptor.EnumDescriptor(
  name='DraftAccess',
  full_name='google.apps.script.type.gmail.ComposeTrigger.DraftAccess',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NONE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='METADATA', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=987,
  serialized_end=1041,
)
_sym_db.RegisterEnumDescriptor(_COMPOSETRIGGER_DRAFTACCESS)


_GMAILADDONMANIFEST = _descriptor.Descriptor(
  name='GmailAddOnManifest',
  full_name='google.apps.script.type.gmail.GmailAddOnManifest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='homepage_trigger', full_name='google.apps.script.type.gmail.GmailAddOnManifest.homepage_trigger', index=0,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='homepageTrigger', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='contextual_triggers', full_name='google.apps.script.type.gmail.GmailAddOnManifest.contextual_triggers', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contextualTriggers', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='universal_actions', full_name='google.apps.script.type.gmail.GmailAddOnManifest.universal_actions', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='universalActions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='compose_trigger', full_name='google.apps.script.type.gmail.GmailAddOnManifest.compose_trigger', index=3,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='composeTrigger', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authorization_check_function', full_name='google.apps.script.type.gmail.GmailAddOnManifest.authorization_check_function', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='authorizationCheckFunction', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=217,
  serialized_end=675,
)


_UNIVERSALACTION = _descriptor.Descriptor(
  name='UniversalAction',
  full_name='google.apps.script.type.gmail.UniversalAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='google.apps.script.type.gmail.UniversalAction.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='text', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='open_link', full_name='google.apps.script.type.gmail.UniversalAction.open_link', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='openLink', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='run_function', full_name='google.apps.script.type.gmail.UniversalAction.run_function', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='runFunction', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='action_type', full_name='google.apps.script.type.gmail.UniversalAction.action_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=677,
  serialized_end=797,
)


_COMPOSETRIGGER = _descriptor.Descriptor(
  name='ComposeTrigger',
  full_name='google.apps.script.type.gmail.ComposeTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='actions', full_name='google.apps.script.type.gmail.ComposeTrigger.actions', index=0,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='actions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='draft_access', full_name='google.apps.script.type.gmail.ComposeTrigger.draft_access', index=1,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='draftAccess', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMPOSETRIGGER_DRAFTACCESS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=800,
  serialized_end=1041,
)


_CONTEXTUALTRIGGER = _descriptor.Descriptor(
  name='ContextualTrigger',
  full_name='google.apps.script.type.gmail.ContextualTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='unconditional', full_name='google.apps.script.type.gmail.ContextualTrigger.unconditional', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='unconditional', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='on_trigger_function', full_name='google.apps.script.type.gmail.ContextualTrigger.on_trigger_function', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='onTriggerFunction', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='trigger', full_name='google.apps.script.type.gmail.ContextualTrigger.trigger',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1044,
  serialized_end=1215,
)


_UNCONDITIONALTRIGGER = _descriptor.Descriptor(
  name='UnconditionalTrigger',
  full_name='google.apps.script.type.gmail.UnconditionalTrigger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=1217,
  serialized_end=1239,
)

_GMAILADDONMANIFEST.fields_by_name['homepage_trigger'].message_type = google_dot_apps_dot_script_dot_type_dot_extension__point__pb2._HOMEPAGEEXTENSIONPOINT
_GMAILADDONMANIFEST.fields_by_name['contextual_triggers'].message_type = _CONTEXTUALTRIGGER
_GMAILADDONMANIFEST.fields_by_name['universal_actions'].message_type = _UNIVERSALACTION
_GMAILADDONMANIFEST.fields_by_name['compose_trigger'].message_type = _COMPOSETRIGGER
_UNIVERSALACTION.oneofs_by_name['action_type'].fields.append(
  _UNIVERSALACTION.fields_by_name['open_link'])
_UNIVERSALACTION.fields_by_name['open_link'].containing_oneof = _UNIVERSALACTION.oneofs_by_name['action_type']
_UNIVERSALACTION.oneofs_by_name['action_type'].fields.append(
  _UNIVERSALACTION.fields_by_name['run_function'])
_UNIVERSALACTION.fields_by_name['run_function'].containing_oneof = _UNIVERSALACTION.oneofs_by_name['action_type']
_COMPOSETRIGGER.fields_by_name['actions'].message_type = google_dot_apps_dot_script_dot_type_dot_extension__point__pb2._MENUITEMEXTENSIONPOINT
_COMPOSETRIGGER.fields_by_name['draft_access'].enum_type = _COMPOSETRIGGER_DRAFTACCESS
_COMPOSETRIGGER_DRAFTACCESS.containing_type = _COMPOSETRIGGER
_CONTEXTUALTRIGGER.fields_by_name['unconditional'].message_type = _UNCONDITIONALTRIGGER
_CONTEXTUALTRIGGER.oneofs_by_name['trigger'].fields.append(
  _CONTEXTUALTRIGGER.fields_by_name['unconditional'])
_CONTEXTUALTRIGGER.fields_by_name['unconditional'].containing_oneof = _CONTEXTUALTRIGGER.oneofs_by_name['trigger']
DESCRIPTOR.message_types_by_name['GmailAddOnManifest'] = _GMAILADDONMANIFEST
DESCRIPTOR.message_types_by_name['UniversalAction'] = _UNIVERSALACTION
DESCRIPTOR.message_types_by_name['ComposeTrigger'] = _COMPOSETRIGGER
DESCRIPTOR.message_types_by_name['ContextualTrigger'] = _CONTEXTUALTRIGGER
DESCRIPTOR.message_types_by_name['UnconditionalTrigger'] = _UNCONDITIONALTRIGGER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GmailAddOnManifest = _reflection.GeneratedProtocolMessageType('GmailAddOnManifest', (_message.Message,), {
  'DESCRIPTOR' : _GMAILADDONMANIFEST,
  '__module__' : 'google.apps.script.type.gmail.gmail_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.gmail.GmailAddOnManifest)
  })
_sym_db.RegisterMessage(GmailAddOnManifest)

UniversalAction = _reflection.GeneratedProtocolMessageType('UniversalAction', (_message.Message,), {
  'DESCRIPTOR' : _UNIVERSALACTION,
  '__module__' : 'google.apps.script.type.gmail.gmail_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.gmail.UniversalAction)
  })
_sym_db.RegisterMessage(UniversalAction)

ComposeTrigger = _reflection.GeneratedProtocolMessageType('ComposeTrigger', (_message.Message,), {
  'DESCRIPTOR' : _COMPOSETRIGGER,
  '__module__' : 'google.apps.script.type.gmail.gmail_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.gmail.ComposeTrigger)
  })
_sym_db.RegisterMessage(ComposeTrigger)

ContextualTrigger = _reflection.GeneratedProtocolMessageType('ContextualTrigger', (_message.Message,), {
  'DESCRIPTOR' : _CONTEXTUALTRIGGER,
  '__module__' : 'google.apps.script.type.gmail.gmail_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.gmail.ContextualTrigger)
  })
_sym_db.RegisterMessage(ContextualTrigger)

UnconditionalTrigger = _reflection.GeneratedProtocolMessageType('UnconditionalTrigger', (_message.Message,), {
  'DESCRIPTOR' : _UNCONDITIONALTRIGGER,
  '__module__' : 'google.apps.script.type.gmail.gmail_addon_manifest_pb2'
  # @@protoc_insertion_point(class_scope:google.apps.script.type.gmail.UnconditionalTrigger)
  })
_sym_db.RegisterMessage(UnconditionalTrigger)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
