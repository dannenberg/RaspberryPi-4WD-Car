# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/monitoring/dashboard/v1/layouts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.monitoring.dashboard.v1 import widget_pb2 as google_dot_monitoring_dot_dashboard_dot_v1_dot_widget__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/monitoring/dashboard/v1/layouts.proto',
  package='google.monitoring.dashboard.v1',
  syntax='proto3',
  serialized_options=b'\n\"com.google.monitoring.dashboard.v1B\014LayoutsProtoP\001ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\252\002$Google.Cloud.Monitoring.Dashboard.V1\312\002$Google\\Cloud\\Monitoring\\Dashboard\\V1\352\002(Google::Cloud::Monitoring::Dashboard::V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,google/monitoring/dashboard/v1/layouts.proto\x12\x1egoogle.monitoring.dashboard.v1\x1a+google/monitoring/dashboard/v1/widget.proto\"h\n\nGridLayout\x12\x18\n\x07\x63olumns\x18\x01 \x01(\x03R\x07\x63olumns\x12@\n\x07widgets\x18\x02 \x03(\x0b\x32&.google.monitoring.dashboard.v1.WidgetR\x07widgets\"\x92\x02\n\x0cMosaicLayout\x12\x18\n\x07\x63olumns\x18\x01 \x01(\x05R\x07\x63olumns\x12G\n\x05tiles\x18\x03 \x03(\x0b\x32\x31.google.monitoring.dashboard.v1.MosaicLayout.TileR\x05tiles\x1a\x9e\x01\n\x04Tile\x12\x13\n\x05x_pos\x18\x01 \x01(\x05R\x04xPos\x12\x13\n\x05y_pos\x18\x02 \x01(\x05R\x04yPos\x12\x14\n\x05width\x18\x03 \x01(\x05R\x05width\x12\x16\n\x06height\x18\x04 \x01(\x05R\x06height\x12>\n\x06widget\x18\x05 \x01(\x0b\x32&.google.monitoring.dashboard.v1.WidgetR\x06widget\"\xaf\x01\n\tRowLayout\x12\x41\n\x04rows\x18\x01 \x03(\x0b\x32-.google.monitoring.dashboard.v1.RowLayout.RowR\x04rows\x1a_\n\x03Row\x12\x16\n\x06weight\x18\x01 \x01(\x03R\x06weight\x12@\n\x07widgets\x18\x02 \x03(\x0b\x32&.google.monitoring.dashboard.v1.WidgetR\x07widgets\"\xc1\x01\n\x0c\x43olumnLayout\x12M\n\x07\x63olumns\x18\x01 \x03(\x0b\x32\x33.google.monitoring.dashboard.v1.ColumnLayout.ColumnR\x07\x63olumns\x1a\x62\n\x06\x43olumn\x12\x16\n\x06weight\x18\x01 \x01(\x03R\x06weight\x12@\n\x07widgets\x18\x02 \x03(\x0b\x32&.google.monitoring.dashboard.v1.WidgetR\x07widgetsB\xf6\x01\n\"com.google.monitoring.dashboard.v1B\x0cLayoutsProtoP\x01ZGgoogle.golang.org/genproto/googleapis/monitoring/dashboard/v1;dashboard\xaa\x02$Google.Cloud.Monitoring.Dashboard.V1\xca\x02$Google\\Cloud\\Monitoring\\Dashboard\\V1\xea\x02(Google::Cloud::Monitoring::Dashboard::V1b\x06proto3'
  ,
  dependencies=[google_dot_monitoring_dot_dashboard_dot_v1_dot_widget__pb2.DESCRIPTOR,])




_GRIDLAYOUT = _descriptor.Descriptor(
  name='GridLayout',
  full_name='google.monitoring.dashboard.v1.GridLayout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='google.monitoring.dashboard.v1.GridLayout.columns', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='columns', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='widgets', full_name='google.monitoring.dashboard.v1.GridLayout.widgets', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='widgets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=125,
  serialized_end=229,
)


_MOSAICLAYOUT_TILE = _descriptor.Descriptor(
  name='Tile',
  full_name='google.monitoring.dashboard.v1.MosaicLayout.Tile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_pos', full_name='google.monitoring.dashboard.v1.MosaicLayout.Tile.x_pos', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='xPos', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y_pos', full_name='google.monitoring.dashboard.v1.MosaicLayout.Tile.y_pos', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='yPos', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='google.monitoring.dashboard.v1.MosaicLayout.Tile.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='width', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='google.monitoring.dashboard.v1.MosaicLayout.Tile.height', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='height', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='widget', full_name='google.monitoring.dashboard.v1.MosaicLayout.Tile.widget', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='widget', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=348,
  serialized_end=506,
)

_MOSAICLAYOUT = _descriptor.Descriptor(
  name='MosaicLayout',
  full_name='google.monitoring.dashboard.v1.MosaicLayout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='google.monitoring.dashboard.v1.MosaicLayout.columns', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='columns', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tiles', full_name='google.monitoring.dashboard.v1.MosaicLayout.tiles', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tiles', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MOSAICLAYOUT_TILE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=506,
)


_ROWLAYOUT_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='google.monitoring.dashboard.v1.RowLayout.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='google.monitoring.dashboard.v1.RowLayout.Row.weight', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='weight', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='widgets', full_name='google.monitoring.dashboard.v1.RowLayout.Row.widgets', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='widgets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=589,
  serialized_end=684,
)

_ROWLAYOUT = _descriptor.Descriptor(
  name='RowLayout',
  full_name='google.monitoring.dashboard.v1.RowLayout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rows', full_name='google.monitoring.dashboard.v1.RowLayout.rows', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='rows', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ROWLAYOUT_ROW, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=684,
)


_COLUMNLAYOUT_COLUMN = _descriptor.Descriptor(
  name='Column',
  full_name='google.monitoring.dashboard.v1.ColumnLayout.Column',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='google.monitoring.dashboard.v1.ColumnLayout.Column.weight', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='weight', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='widgets', full_name='google.monitoring.dashboard.v1.ColumnLayout.Column.widgets', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='widgets', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=782,
  serialized_end=880,
)

_COLUMNLAYOUT = _descriptor.Descriptor(
  name='ColumnLayout',
  full_name='google.monitoring.dashboard.v1.ColumnLayout',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='columns', full_name='google.monitoring.dashboard.v1.ColumnLayout.columns', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='columns', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COLUMNLAYOUT_COLUMN, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=687,
  serialized_end=880,
)

_GRIDLAYOUT.fields_by_name['widgets'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_widget__pb2._WIDGET
_MOSAICLAYOUT_TILE.fields_by_name['widget'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_widget__pb2._WIDGET
_MOSAICLAYOUT_TILE.containing_type = _MOSAICLAYOUT
_MOSAICLAYOUT.fields_by_name['tiles'].message_type = _MOSAICLAYOUT_TILE
_ROWLAYOUT_ROW.fields_by_name['widgets'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_widget__pb2._WIDGET
_ROWLAYOUT_ROW.containing_type = _ROWLAYOUT
_ROWLAYOUT.fields_by_name['rows'].message_type = _ROWLAYOUT_ROW
_COLUMNLAYOUT_COLUMN.fields_by_name['widgets'].message_type = google_dot_monitoring_dot_dashboard_dot_v1_dot_widget__pb2._WIDGET
_COLUMNLAYOUT_COLUMN.containing_type = _COLUMNLAYOUT
_COLUMNLAYOUT.fields_by_name['columns'].message_type = _COLUMNLAYOUT_COLUMN
DESCRIPTOR.message_types_by_name['GridLayout'] = _GRIDLAYOUT
DESCRIPTOR.message_types_by_name['MosaicLayout'] = _MOSAICLAYOUT
DESCRIPTOR.message_types_by_name['RowLayout'] = _ROWLAYOUT
DESCRIPTOR.message_types_by_name['ColumnLayout'] = _COLUMNLAYOUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GridLayout = _reflection.GeneratedProtocolMessageType('GridLayout', (_message.Message,), {
  'DESCRIPTOR' : _GRIDLAYOUT,
  '__module__' : 'google.monitoring.dashboard.v1.layouts_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.GridLayout)
  })
_sym_db.RegisterMessage(GridLayout)

MosaicLayout = _reflection.GeneratedProtocolMessageType('MosaicLayout', (_message.Message,), {

  'Tile' : _reflection.GeneratedProtocolMessageType('Tile', (_message.Message,), {
    'DESCRIPTOR' : _MOSAICLAYOUT_TILE,
    '__module__' : 'google.monitoring.dashboard.v1.layouts_pb2'
    # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.MosaicLayout.Tile)
    })
  ,
  'DESCRIPTOR' : _MOSAICLAYOUT,
  '__module__' : 'google.monitoring.dashboard.v1.layouts_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.MosaicLayout)
  })
_sym_db.RegisterMessage(MosaicLayout)
_sym_db.RegisterMessage(MosaicLayout.Tile)

RowLayout = _reflection.GeneratedProtocolMessageType('RowLayout', (_message.Message,), {

  'Row' : _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), {
    'DESCRIPTOR' : _ROWLAYOUT_ROW,
    '__module__' : 'google.monitoring.dashboard.v1.layouts_pb2'
    # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.RowLayout.Row)
    })
  ,
  'DESCRIPTOR' : _ROWLAYOUT,
  '__module__' : 'google.monitoring.dashboard.v1.layouts_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.RowLayout)
  })
_sym_db.RegisterMessage(RowLayout)
_sym_db.RegisterMessage(RowLayout.Row)

ColumnLayout = _reflection.GeneratedProtocolMessageType('ColumnLayout', (_message.Message,), {

  'Column' : _reflection.GeneratedProtocolMessageType('Column', (_message.Message,), {
    'DESCRIPTOR' : _COLUMNLAYOUT_COLUMN,
    '__module__' : 'google.monitoring.dashboard.v1.layouts_pb2'
    # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.ColumnLayout.Column)
    })
  ,
  'DESCRIPTOR' : _COLUMNLAYOUT,
  '__module__' : 'google.monitoring.dashboard.v1.layouts_pb2'
  # @@protoc_insertion_point(class_scope:google.monitoring.dashboard.v1.ColumnLayout)
  })
_sym_db.RegisterMessage(ColumnLayout)
_sym_db.RegisterMessage(ColumnLayout.Column)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
