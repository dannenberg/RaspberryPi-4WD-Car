# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/maps/playablelocations/v3/playablelocations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.maps.playablelocations.v3 import resources_pb2 as google_dot_maps_dot_playablelocations_dot_v3_dot_resources__pb2
from google.maps.playablelocations.v3.sample import resources_pb2 as google_dot_maps_dot_playablelocations_dot_v3_dot_sample_dot_resources__pb2
from google.maps.unity import clientinfo_pb2 as google_dot_maps_dot_unity_dot_clientinfo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/maps/playablelocations/v3/playablelocations.proto',
  package='google.maps.playablelocations.v3',
  syntax='proto3',
  serialized_options=b'\n$com.google.maps.playablelocations.v3B\026PlayableLocationsProtoP\001ZQgoogle.golang.org/genproto/googleapis/maps/playablelocations/v3;playablelocations\242\002\004GMPL\252\002 Google.Maps.PlayableLocations.V3\312\002 Google\\Maps\\PlayableLocations\\V3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8google/maps/playablelocations/v3/playablelocations.proto\x12 google.maps.playablelocations.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x30google/maps/playablelocations/v3/resources.proto\x1a\x37google/maps/playablelocations/v3/sample/resources.proto\x1a\"google/maps/unity/clientinfo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x17google/api/client.proto\"\xd2\x01\n\x1eSamplePlayableLocationsRequest\x12Z\n\x0b\x61rea_filter\x18\x01 \x01(\x0b\x32\x33.google.maps.playablelocations.v3.sample.AreaFilterB\x04\xe2\x41\x01\x02R\nareaFilter\x12T\n\x08\x63riteria\x18\x02 \x03(\x0b\x32\x32.google.maps.playablelocations.v3.sample.CriterionB\x04\xe2\x41\x01\x02R\x08\x63riteria\"\x85\x03\n\x1fSamplePlayableLocationsResponse\x12\xa5\x01\n\x1elocations_per_game_object_type\x18\x01 \x03(\x0b\x32\x61.google.maps.playablelocations.v3.SamplePlayableLocationsResponse.LocationsPerGameObjectTypeEntryR\x1alocationsPerGameObjectType\x12+\n\x03ttl\x18\t \x01(\x0b\x32\x19.google.protobuf.DurationR\x03ttl\x1a\x8c\x01\n\x1fLocationsPerGameObjectTypeEntry\x12\x10\n\x03key\x18\x01 \x01(\x05R\x03key\x12S\n\x05value\x18\x02 \x01(\x0b\x32=.google.maps.playablelocations.v3.sample.PlayableLocationListR\x05value:\x02\x38\x01\"\xe1\x01\n\x17LogPlayerReportsRequest\x12[\n\x0eplayer_reports\x18\x01 \x03(\x0b\x32..google.maps.playablelocations.v3.PlayerReportB\x04\xe2\x41\x01\x02R\rplayerReports\x12#\n\nrequest_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\trequestId\x12\x44\n\x0b\x63lient_info\x18\x03 \x01(\x0b\x32\x1d.google.maps.unity.ClientInfoB\x04\xe2\x41\x01\x02R\nclientInfo\"\x1a\n\x18LogPlayerReportsResponse\"\xd8\x01\n\x15LogImpressionsRequest\x12T\n\x0bimpressions\x18\x01 \x03(\x0b\x32,.google.maps.playablelocations.v3.ImpressionB\x04\xe2\x41\x01\x02R\x0bimpressions\x12#\n\nrequest_id\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\trequestId\x12\x44\n\x0b\x63lient_info\x18\x03 \x01(\x0b\x32\x1d.google.maps.unity.ClientInfoB\x04\xe2\x41\x01\x02R\nclientInfo\"\x18\n\x16LogImpressionsResponse2\xd3\x04\n\x11PlayableLocations\x12\xc6\x01\n\x17SamplePlayableLocations\x12@.google.maps.playablelocations.v3.SamplePlayableLocationsRequest\x1a\x41.google.maps.playablelocations.v3.SamplePlayableLocationsResponse\"&\x82\xd3\xe4\x93\x02 \"\x1b/v3:samplePlayableLocations:\x01*\x12\xaa\x01\n\x10LogPlayerReports\x12\x39.google.maps.playablelocations.v3.LogPlayerReportsRequest\x1a:.google.maps.playablelocations.v3.LogPlayerReportsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/v3:logPlayerReports:\x01*\x12\xa2\x01\n\x0eLogImpressions\x12\x37.google.maps.playablelocations.v3.LogImpressionsRequest\x1a\x38.google.maps.playablelocations.v3.LogImpressionsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v3:logImpressions:\x01*\x1a#\xca\x41 playablelocations.googleapis.comB\xe0\x01\n$com.google.maps.playablelocations.v3B\x16PlayableLocationsProtoP\x01ZQgoogle.golang.org/genproto/googleapis/maps/playablelocations/v3;playablelocations\xa2\x02\x04GMPL\xaa\x02 Google.Maps.PlayableLocations.V3\xca\x02 Google\\Maps\\PlayableLocations\\V3b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_maps_dot_playablelocations_dot_v3_dot_resources__pb2.DESCRIPTOR,google_dot_maps_dot_playablelocations_dot_v3_dot_sample_dot_resources__pb2.DESCRIPTOR,google_dot_maps_dot_unity_dot_clientinfo__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,])




_SAMPLEPLAYABLELOCATIONSREQUEST = _descriptor.Descriptor(
  name='SamplePlayableLocationsRequest',
  full_name='google.maps.playablelocations.v3.SamplePlayableLocationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='area_filter', full_name='google.maps.playablelocations.v3.SamplePlayableLocationsRequest.area_filter', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='areaFilter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='criteria', full_name='google.maps.playablelocations.v3.SamplePlayableLocationsRequest.criteria', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='criteria', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=358,
  serialized_end=568,
)


_SAMPLEPLAYABLELOCATIONSRESPONSE_LOCATIONSPERGAMEOBJECTTYPEENTRY = _descriptor.Descriptor(
  name='LocationsPerGameObjectTypeEntry',
  full_name='google.maps.playablelocations.v3.SamplePlayableLocationsResponse.LocationsPerGameObjectTypeEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.maps.playablelocations.v3.SamplePlayableLocationsResponse.LocationsPerGameObjectTypeEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.maps.playablelocations.v3.SamplePlayableLocationsResponse.LocationsPerGameObjectTypeEntry.value', index=1,
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
  serialized_start=820,
  serialized_end=960,
)

_SAMPLEPLAYABLELOCATIONSRESPONSE = _descriptor.Descriptor(
  name='SamplePlayableLocationsResponse',
  full_name='google.maps.playablelocations.v3.SamplePlayableLocationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='locations_per_game_object_type', full_name='google.maps.playablelocations.v3.SamplePlayableLocationsResponse.locations_per_game_object_type', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='locationsPerGameObjectType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='google.maps.playablelocations.v3.SamplePlayableLocationsResponse.ttl', index=1,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ttl', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SAMPLEPLAYABLELOCATIONSRESPONSE_LOCATIONSPERGAMEOBJECTTYPEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=571,
  serialized_end=960,
)


_LOGPLAYERREPORTSREQUEST = _descriptor.Descriptor(
  name='LogPlayerReportsRequest',
  full_name='google.maps.playablelocations.v3.LogPlayerReportsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_reports', full_name='google.maps.playablelocations.v3.LogPlayerReportsRequest.player_reports', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='playerReports', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='google.maps.playablelocations.v3.LogPlayerReportsRequest.request_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='requestId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_info', full_name='google.maps.playablelocations.v3.LogPlayerReportsRequest.client_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='clientInfo', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=963,
  serialized_end=1188,
)


_LOGPLAYERREPORTSRESPONSE = _descriptor.Descriptor(
  name='LogPlayerReportsResponse',
  full_name='google.maps.playablelocations.v3.LogPlayerReportsResponse',
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
  serialized_start=1190,
  serialized_end=1216,
)


_LOGIMPRESSIONSREQUEST = _descriptor.Descriptor(
  name='LogImpressionsRequest',
  full_name='google.maps.playablelocations.v3.LogImpressionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='impressions', full_name='google.maps.playablelocations.v3.LogImpressionsRequest.impressions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='impressions', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='google.maps.playablelocations.v3.LogImpressionsRequest.request_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='requestId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_info', full_name='google.maps.playablelocations.v3.LogImpressionsRequest.client_info', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='clientInfo', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1219,
  serialized_end=1435,
)


_LOGIMPRESSIONSRESPONSE = _descriptor.Descriptor(
  name='LogImpressionsResponse',
  full_name='google.maps.playablelocations.v3.LogImpressionsResponse',
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
  serialized_start=1437,
  serialized_end=1461,
)

_SAMPLEPLAYABLELOCATIONSREQUEST.fields_by_name['area_filter'].message_type = google_dot_maps_dot_playablelocations_dot_v3_dot_sample_dot_resources__pb2._AREAFILTER
_SAMPLEPLAYABLELOCATIONSREQUEST.fields_by_name['criteria'].message_type = google_dot_maps_dot_playablelocations_dot_v3_dot_sample_dot_resources__pb2._CRITERION
_SAMPLEPLAYABLELOCATIONSRESPONSE_LOCATIONSPERGAMEOBJECTTYPEENTRY.fields_by_name['value'].message_type = google_dot_maps_dot_playablelocations_dot_v3_dot_sample_dot_resources__pb2._PLAYABLELOCATIONLIST
_SAMPLEPLAYABLELOCATIONSRESPONSE_LOCATIONSPERGAMEOBJECTTYPEENTRY.containing_type = _SAMPLEPLAYABLELOCATIONSRESPONSE
_SAMPLEPLAYABLELOCATIONSRESPONSE.fields_by_name['locations_per_game_object_type'].message_type = _SAMPLEPLAYABLELOCATIONSRESPONSE_LOCATIONSPERGAMEOBJECTTYPEENTRY
_SAMPLEPLAYABLELOCATIONSRESPONSE.fields_by_name['ttl'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_LOGPLAYERREPORTSREQUEST.fields_by_name['player_reports'].message_type = google_dot_maps_dot_playablelocations_dot_v3_dot_resources__pb2._PLAYERREPORT
_LOGPLAYERREPORTSREQUEST.fields_by_name['client_info'].message_type = google_dot_maps_dot_unity_dot_clientinfo__pb2._CLIENTINFO
_LOGIMPRESSIONSREQUEST.fields_by_name['impressions'].message_type = google_dot_maps_dot_playablelocations_dot_v3_dot_resources__pb2._IMPRESSION
_LOGIMPRESSIONSREQUEST.fields_by_name['client_info'].message_type = google_dot_maps_dot_unity_dot_clientinfo__pb2._CLIENTINFO
DESCRIPTOR.message_types_by_name['SamplePlayableLocationsRequest'] = _SAMPLEPLAYABLELOCATIONSREQUEST
DESCRIPTOR.message_types_by_name['SamplePlayableLocationsResponse'] = _SAMPLEPLAYABLELOCATIONSRESPONSE
DESCRIPTOR.message_types_by_name['LogPlayerReportsRequest'] = _LOGPLAYERREPORTSREQUEST
DESCRIPTOR.message_types_by_name['LogPlayerReportsResponse'] = _LOGPLAYERREPORTSRESPONSE
DESCRIPTOR.message_types_by_name['LogImpressionsRequest'] = _LOGIMPRESSIONSREQUEST
DESCRIPTOR.message_types_by_name['LogImpressionsResponse'] = _LOGIMPRESSIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SamplePlayableLocationsRequest = _reflection.GeneratedProtocolMessageType('SamplePlayableLocationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLEPLAYABLELOCATIONSREQUEST,
  '__module__' : 'google.maps.playablelocations.v3.playablelocations_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.playablelocations.v3.SamplePlayableLocationsRequest)
  })
_sym_db.RegisterMessage(SamplePlayableLocationsRequest)

SamplePlayableLocationsResponse = _reflection.GeneratedProtocolMessageType('SamplePlayableLocationsResponse', (_message.Message,), {

  'LocationsPerGameObjectTypeEntry' : _reflection.GeneratedProtocolMessageType('LocationsPerGameObjectTypeEntry', (_message.Message,), {
    'DESCRIPTOR' : _SAMPLEPLAYABLELOCATIONSRESPONSE_LOCATIONSPERGAMEOBJECTTYPEENTRY,
    '__module__' : 'google.maps.playablelocations.v3.playablelocations_pb2'
    # @@protoc_insertion_point(class_scope:google.maps.playablelocations.v3.SamplePlayableLocationsResponse.LocationsPerGameObjectTypeEntry)
    })
  ,
  'DESCRIPTOR' : _SAMPLEPLAYABLELOCATIONSRESPONSE,
  '__module__' : 'google.maps.playablelocations.v3.playablelocations_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.playablelocations.v3.SamplePlayableLocationsResponse)
  })
_sym_db.RegisterMessage(SamplePlayableLocationsResponse)
_sym_db.RegisterMessage(SamplePlayableLocationsResponse.LocationsPerGameObjectTypeEntry)

LogPlayerReportsRequest = _reflection.GeneratedProtocolMessageType('LogPlayerReportsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGPLAYERREPORTSREQUEST,
  '__module__' : 'google.maps.playablelocations.v3.playablelocations_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.playablelocations.v3.LogPlayerReportsRequest)
  })
_sym_db.RegisterMessage(LogPlayerReportsRequest)

LogPlayerReportsResponse = _reflection.GeneratedProtocolMessageType('LogPlayerReportsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGPLAYERREPORTSRESPONSE,
  '__module__' : 'google.maps.playablelocations.v3.playablelocations_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.playablelocations.v3.LogPlayerReportsResponse)
  })
_sym_db.RegisterMessage(LogPlayerReportsResponse)

LogImpressionsRequest = _reflection.GeneratedProtocolMessageType('LogImpressionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGIMPRESSIONSREQUEST,
  '__module__' : 'google.maps.playablelocations.v3.playablelocations_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.playablelocations.v3.LogImpressionsRequest)
  })
_sym_db.RegisterMessage(LogImpressionsRequest)

LogImpressionsResponse = _reflection.GeneratedProtocolMessageType('LogImpressionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGIMPRESSIONSRESPONSE,
  '__module__' : 'google.maps.playablelocations.v3.playablelocations_pb2'
  # @@protoc_insertion_point(class_scope:google.maps.playablelocations.v3.LogImpressionsResponse)
  })
_sym_db.RegisterMessage(LogImpressionsResponse)


DESCRIPTOR._options = None
_SAMPLEPLAYABLELOCATIONSREQUEST.fields_by_name['area_filter']._options = None
_SAMPLEPLAYABLELOCATIONSREQUEST.fields_by_name['criteria']._options = None
_SAMPLEPLAYABLELOCATIONSRESPONSE_LOCATIONSPERGAMEOBJECTTYPEENTRY._options = None
_LOGPLAYERREPORTSREQUEST.fields_by_name['player_reports']._options = None
_LOGPLAYERREPORTSREQUEST.fields_by_name['request_id']._options = None
_LOGPLAYERREPORTSREQUEST.fields_by_name['client_info']._options = None
_LOGIMPRESSIONSREQUEST.fields_by_name['impressions']._options = None
_LOGIMPRESSIONSREQUEST.fields_by_name['request_id']._options = None
_LOGIMPRESSIONSREQUEST.fields_by_name['client_info']._options = None

_PLAYABLELOCATIONS = _descriptor.ServiceDescriptor(
  name='PlayableLocations',
  full_name='google.maps.playablelocations.v3.PlayableLocations',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A playablelocations.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=1464,
  serialized_end=2059,
  methods=[
  _descriptor.MethodDescriptor(
    name='SamplePlayableLocations',
    full_name='google.maps.playablelocations.v3.PlayableLocations.SamplePlayableLocations',
    index=0,
    containing_service=None,
    input_type=_SAMPLEPLAYABLELOCATIONSREQUEST,
    output_type=_SAMPLEPLAYABLELOCATIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002 \"\033/v3:samplePlayableLocations:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='LogPlayerReports',
    full_name='google.maps.playablelocations.v3.PlayableLocations.LogPlayerReports',
    index=1,
    containing_service=None,
    input_type=_LOGPLAYERREPORTSREQUEST,
    output_type=_LOGPLAYERREPORTSRESPONSE,
    serialized_options=b'\202\323\344\223\002\031\"\024/v3:logPlayerReports:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='LogImpressions',
    full_name='google.maps.playablelocations.v3.PlayableLocations.LogImpressions',
    index=2,
    containing_service=None,
    input_type=_LOGIMPRESSIONSREQUEST,
    output_type=_LOGIMPRESSIONSRESPONSE,
    serialized_options=b'\202\323\344\223\002\027\"\022/v3:logImpressions:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PLAYABLELOCATIONS)

DESCRIPTOR.services_by_name['PlayableLocations'] = _PLAYABLELOCATIONS

# @@protoc_insertion_point(module_scope)
