# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/texttospeech/v1beta1/cloud_tts.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/texttospeech/v1beta1/cloud_tts.proto',
  package='google.cloud.texttospeech.v1beta1',
  syntax='proto3',
  serialized_options=b'\n%com.google.cloud.texttospeech.v1beta1B\021TextToSpeechProtoP\001ZMgoogle.golang.org/genproto/googleapis/cloud/texttospeech/v1beta1;texttospeech\370\001\001\252\002!Google.Cloud.TextToSpeech.V1Beta1\312\002!Google\\Cloud\\TextToSpeech\\V1beta1\352\002$Google::Cloud::TextToSpeech::V1beta1\352AU\n\033automl.googleapis.com/Model\0226projects/{project}/locations/{location}/models/{model}',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n1google/cloud/texttospeech/v1beta1/cloud_tts.proto\x12!google.cloud.texttospeech.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\">\n\x11ListVoicesRequest\x12)\n\rlanguage_code\x18\x01 \x01(\tB\x04\xe2\x41\x01\x01R\x0clanguageCode\"V\n\x12ListVoicesResponse\x12@\n\x06voices\x18\x01 \x03(\x0b\x32(.google.cloud.texttospeech.v1beta1.VoiceR\x06voices\"\xd2\x01\n\x05Voice\x12%\n\x0elanguage_codes\x18\x01 \x03(\tR\rlanguageCodes\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12S\n\x0bssml_gender\x18\x03 \x01(\x0e\x32\x32.google.cloud.texttospeech.v1beta1.SsmlVoiceGenderR\nssmlGender\x12\x39\n\x19natural_sample_rate_hertz\x18\x04 \x01(\x05R\x16naturalSampleRateHertz\"\xd2\x03\n\x17SynthesizeSpeechRequest\x12M\n\x05input\x18\x01 \x01(\x0b\x32\x31.google.cloud.texttospeech.v1beta1.SynthesisInputB\x04\xe2\x41\x01\x02R\x05input\x12S\n\x05voice\x18\x02 \x01(\x0b\x32\x37.google.cloud.texttospeech.v1beta1.VoiceSelectionParamsB\x04\xe2\x41\x01\x02R\x05voice\x12W\n\x0c\x61udio_config\x18\x03 \x01(\x0b\x32..google.cloud.texttospeech.v1beta1.AudioConfigB\x04\xe2\x41\x01\x02R\x0b\x61udioConfig\x12z\n\x14\x65nable_time_pointing\x18\x04 \x03(\x0e\x32H.google.cloud.texttospeech.v1beta1.SynthesizeSpeechRequest.TimepointTypeR\x12\x65nableTimePointing\">\n\rTimepointType\x12\x1e\n\x1aTIMEPOINT_TYPE_UNSPECIFIED\x10\x00\x12\r\n\tSSML_MARK\x10\x01\"L\n\x0eSynthesisInput\x12\x14\n\x04text\x18\x01 \x01(\tH\x00R\x04text\x12\x14\n\x04ssml\x18\x02 \x01(\tH\x00R\x04ssmlB\x0e\n\x0cinput_source\"\x83\x02\n\x14VoiceSelectionParams\x12)\n\rlanguage_code\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x0clanguageCode\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12S\n\x0bssml_gender\x18\x03 \x01(\x0e\x32\x32.google.cloud.texttospeech.v1beta1.SsmlVoiceGenderR\nssmlGender\x12W\n\x0c\x63ustom_voice\x18\x04 \x01(\x0b\x32\x34.google.cloud.texttospeech.v1beta1.CustomVoiceParamsR\x0b\x63ustomVoice\"\xc9\x02\n\x0b\x41udioConfig\x12]\n\x0e\x61udio_encoding\x18\x01 \x01(\x0e\x32\x30.google.cloud.texttospeech.v1beta1.AudioEncodingB\x04\xe2\x41\x01\x02R\raudioEncoding\x12*\n\rspeaking_rate\x18\x02 \x01(\x01\x42\x05\xe2\x41\x02\x04\x01R\x0cspeakingRate\x12\x1b\n\x05pitch\x18\x03 \x01(\x01\x42\x05\xe2\x41\x02\x04\x01R\x05pitch\x12+\n\x0evolume_gain_db\x18\x04 \x01(\x01\x42\x05\xe2\x41\x02\x04\x01R\x0cvolumeGainDb\x12\x30\n\x11sample_rate_hertz\x18\x05 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x0fsampleRateHertz\x12\x33\n\x12\x65\x66\x66\x65\x63ts_profile_id\x18\x06 \x03(\tB\x05\xe2\x41\x02\x04\x01R\x10\x65\x66\x66\x65\x63tsProfileId\"\x8c\x02\n\x11\x43ustomVoiceParams\x12:\n\x05model\x18\x01 \x01(\tB$\xe2\x41\x01\x02\xfa\x41\x1d\n\x1b\x61utoml.googleapis.com/ModelR\x05model\x12o\n\x0ereported_usage\x18\x03 \x01(\x0e\x32\x42.google.cloud.texttospeech.v1beta1.CustomVoiceParams.ReportedUsageB\x04\xe2\x41\x01\x01R\rreportedUsage\"J\n\rReportedUsage\x12\x1e\n\x1aREPORTED_USAGE_UNSPECIFIED\x10\x00\x12\x0c\n\x08REALTIME\x10\x01\x12\x0b\n\x07OFFLINE\x10\x02\"\xe0\x01\n\x18SynthesizeSpeechResponse\x12#\n\raudio_content\x18\x01 \x01(\x0cR\x0c\x61udioContent\x12L\n\ntimepoints\x18\x02 \x03(\x0b\x32,.google.cloud.texttospeech.v1beta1.TimepointR\ntimepoints\x12Q\n\x0c\x61udio_config\x18\x04 \x01(\x0b\x32..google.cloud.texttospeech.v1beta1.AudioConfigR\x0b\x61udioConfig\"K\n\tTimepoint\x12\x1b\n\tmark_name\x18\x04 \x01(\tR\x08markName\x12!\n\x0ctime_seconds\x18\x03 \x01(\x01R\x0btimeSeconds*W\n\x0fSsmlVoiceGender\x12!\n\x1dSSML_VOICE_GENDER_UNSPECIFIED\x10\x00\x12\x08\n\x04MALE\x10\x01\x12\n\n\x06\x46\x45MALE\x10\x02\x12\x0b\n\x07NEUTRAL\x10\x03*z\n\rAudioEncoding\x12\x1e\n\x1a\x41UDIO_ENCODING_UNSPECIFIED\x10\x00\x12\x0c\n\x08LINEAR16\x10\x01\x12\x07\n\x03MP3\x10\x02\x12\x0f\n\x0bMP3_64_KBPS\x10\x04\x12\x0c\n\x08OGG_OPUS\x10\x03\x12\t\n\x05MULAW\x10\x05\x12\x08\n\x04\x41LAW\x10\x06\x32\xd2\x03\n\x0cTextToSpeech\x12\xa2\x01\n\nListVoices\x12\x34.google.cloud.texttospeech.v1beta1.ListVoicesRequest\x1a\x35.google.cloud.texttospeech.v1beta1.ListVoicesResponse\"\'\xda\x41\rlanguage_code\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1beta1/voices\x12\xcb\x01\n\x10SynthesizeSpeech\x12:.google.cloud.texttospeech.v1beta1.SynthesizeSpeechRequest\x1a;.google.cloud.texttospeech.v1beta1.SynthesizeSpeechResponse\">\xda\x41\x18input,voice,audio_config\x82\xd3\xe4\x93\x02\x1d\"\x18/v1beta1/text:synthesize:\x01*\x1aO\xca\x41\x1btexttospeech.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xd5\x02\n%com.google.cloud.texttospeech.v1beta1B\x11TextToSpeechProtoP\x01ZMgoogle.golang.org/genproto/googleapis/cloud/texttospeech/v1beta1;texttospeech\xf8\x01\x01\xaa\x02!Google.Cloud.TextToSpeech.V1Beta1\xca\x02!Google\\Cloud\\TextToSpeech\\V1beta1\xea\x02$Google::Cloud::TextToSpeech::V1beta1\xea\x41U\n\x1b\x61utoml.googleapis.com/Model\x12\x36projects/{project}/locations/{location}/models/{model}b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,])

_SSMLVOICEGENDER = _descriptor.EnumDescriptor(
  name='SsmlVoiceGender',
  full_name='google.cloud.texttospeech.v1beta1.SsmlVoiceGender',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SSML_VOICE_GENDER_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MALE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NEUTRAL', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2284,
  serialized_end=2371,
)
_sym_db.RegisterEnumDescriptor(_SSMLVOICEGENDER)

SsmlVoiceGender = enum_type_wrapper.EnumTypeWrapper(_SSMLVOICEGENDER)
_AUDIOENCODING = _descriptor.EnumDescriptor(
  name='AudioEncoding',
  full_name='google.cloud.texttospeech.v1beta1.AudioEncoding',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AUDIO_ENCODING_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LINEAR16', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MP3', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MP3_64_KBPS', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OGG_OPUS', index=4, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MULAW', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALAW', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2373,
  serialized_end=2495,
)
_sym_db.RegisterEnumDescriptor(_AUDIOENCODING)

AudioEncoding = enum_type_wrapper.EnumTypeWrapper(_AUDIOENCODING)
SSML_VOICE_GENDER_UNSPECIFIED = 0
MALE = 1
FEMALE = 2
NEUTRAL = 3
AUDIO_ENCODING_UNSPECIFIED = 0
LINEAR16 = 1
MP3 = 2
MP3_64_KBPS = 4
OGG_OPUS = 3
MULAW = 5
ALAW = 6


_SYNTHESIZESPEECHREQUEST_TIMEPOINTTYPE = _descriptor.EnumDescriptor(
  name='TimepointType',
  full_name='google.cloud.texttospeech.v1beta1.SynthesizeSpeechRequest.TimepointType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TIMEPOINT_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SSML_MARK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=973,
  serialized_end=1035,
)
_sym_db.RegisterEnumDescriptor(_SYNTHESIZESPEECHREQUEST_TIMEPOINTTYPE)

_CUSTOMVOICEPARAMS_REPORTEDUSAGE = _descriptor.EnumDescriptor(
  name='ReportedUsage',
  full_name='google.cloud.texttospeech.v1beta1.CustomVoiceParams.ReportedUsage',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REPORTED_USAGE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REALTIME', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OFFLINE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1904,
  serialized_end=1978,
)
_sym_db.RegisterEnumDescriptor(_CUSTOMVOICEPARAMS_REPORTEDUSAGE)


_LISTVOICESREQUEST = _descriptor.Descriptor(
  name='ListVoicesRequest',
  full_name='google.cloud.texttospeech.v1beta1.ListVoicesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.cloud.texttospeech.v1beta1.ListVoicesRequest.language_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='languageCode', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=203,
  serialized_end=265,
)


_LISTVOICESRESPONSE = _descriptor.Descriptor(
  name='ListVoicesResponse',
  full_name='google.cloud.texttospeech.v1beta1.ListVoicesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='voices', full_name='google.cloud.texttospeech.v1beta1.ListVoicesResponse.voices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='voices', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=267,
  serialized_end=353,
)


_VOICE = _descriptor.Descriptor(
  name='Voice',
  full_name='google.cloud.texttospeech.v1beta1.Voice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language_codes', full_name='google.cloud.texttospeech.v1beta1.Voice.language_codes', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='languageCodes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.texttospeech.v1beta1.Voice.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssml_gender', full_name='google.cloud.texttospeech.v1beta1.Voice.ssml_gender', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ssmlGender', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='natural_sample_rate_hertz', full_name='google.cloud.texttospeech.v1beta1.Voice.natural_sample_rate_hertz', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='naturalSampleRateHertz', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=356,
  serialized_end=566,
)


_SYNTHESIZESPEECHREQUEST = _descriptor.Descriptor(
  name='SynthesizeSpeechRequest',
  full_name='google.cloud.texttospeech.v1beta1.SynthesizeSpeechRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='google.cloud.texttospeech.v1beta1.SynthesizeSpeechRequest.input', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='input', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='voice', full_name='google.cloud.texttospeech.v1beta1.SynthesizeSpeechRequest.voice', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='voice', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_config', full_name='google.cloud.texttospeech.v1beta1.SynthesizeSpeechRequest.audio_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='audioConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_time_pointing', full_name='google.cloud.texttospeech.v1beta1.SynthesizeSpeechRequest.enable_time_pointing', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='enableTimePointing', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SYNTHESIZESPEECHREQUEST_TIMEPOINTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=569,
  serialized_end=1035,
)


_SYNTHESISINPUT = _descriptor.Descriptor(
  name='SynthesisInput',
  full_name='google.cloud.texttospeech.v1beta1.SynthesisInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='google.cloud.texttospeech.v1beta1.SynthesisInput.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='text', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssml', full_name='google.cloud.texttospeech.v1beta1.SynthesisInput.ssml', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ssml', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='input_source', full_name='google.cloud.texttospeech.v1beta1.SynthesisInput.input_source',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1037,
  serialized_end=1113,
)


_VOICESELECTIONPARAMS = _descriptor.Descriptor(
  name='VoiceSelectionParams',
  full_name='google.cloud.texttospeech.v1beta1.VoiceSelectionParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language_code', full_name='google.cloud.texttospeech.v1beta1.VoiceSelectionParams.language_code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='languageCode', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.texttospeech.v1beta1.VoiceSelectionParams.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ssml_gender', full_name='google.cloud.texttospeech.v1beta1.VoiceSelectionParams.ssml_gender', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ssmlGender', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='custom_voice', full_name='google.cloud.texttospeech.v1beta1.VoiceSelectionParams.custom_voice', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='customVoice', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1116,
  serialized_end=1375,
)


_AUDIOCONFIG = _descriptor.Descriptor(
  name='AudioConfig',
  full_name='google.cloud.texttospeech.v1beta1.AudioConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio_encoding', full_name='google.cloud.texttospeech.v1beta1.AudioConfig.audio_encoding', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='audioEncoding', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speaking_rate', full_name='google.cloud.texttospeech.v1beta1.AudioConfig.speaking_rate', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\002\004\001', json_name='speakingRate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='google.cloud.texttospeech.v1beta1.AudioConfig.pitch', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\002\004\001', json_name='pitch', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='volume_gain_db', full_name='google.cloud.texttospeech.v1beta1.AudioConfig.volume_gain_db', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\002\004\001', json_name='volumeGainDb', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sample_rate_hertz', full_name='google.cloud.texttospeech.v1beta1.AudioConfig.sample_rate_hertz', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='sampleRateHertz', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='effects_profile_id', full_name='google.cloud.texttospeech.v1beta1.AudioConfig.effects_profile_id', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\002\004\001', json_name='effectsProfileId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1378,
  serialized_end=1707,
)


_CUSTOMVOICEPARAMS = _descriptor.Descriptor(
  name='CustomVoiceParams',
  full_name='google.cloud.texttospeech.v1beta1.CustomVoiceParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='google.cloud.texttospeech.v1beta1.CustomVoiceParams.model', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A\035\n\033automl.googleapis.com/Model', json_name='model', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reported_usage', full_name='google.cloud.texttospeech.v1beta1.CustomVoiceParams.reported_usage', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='reportedUsage', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CUSTOMVOICEPARAMS_REPORTEDUSAGE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1710,
  serialized_end=1978,
)


_SYNTHESIZESPEECHRESPONSE = _descriptor.Descriptor(
  name='SynthesizeSpeechResponse',
  full_name='google.cloud.texttospeech.v1beta1.SynthesizeSpeechResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='audio_content', full_name='google.cloud.texttospeech.v1beta1.SynthesizeSpeechResponse.audio_content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='audioContent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timepoints', full_name='google.cloud.texttospeech.v1beta1.SynthesizeSpeechResponse.timepoints', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timepoints', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audio_config', full_name='google.cloud.texttospeech.v1beta1.SynthesizeSpeechResponse.audio_config', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='audioConfig', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1981,
  serialized_end=2205,
)


_TIMEPOINT = _descriptor.Descriptor(
  name='Timepoint',
  full_name='google.cloud.texttospeech.v1beta1.Timepoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mark_name', full_name='google.cloud.texttospeech.v1beta1.Timepoint.mark_name', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='markName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_seconds', full_name='google.cloud.texttospeech.v1beta1.Timepoint.time_seconds', index=1,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timeSeconds', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2207,
  serialized_end=2282,
)

_LISTVOICESRESPONSE.fields_by_name['voices'].message_type = _VOICE
_VOICE.fields_by_name['ssml_gender'].enum_type = _SSMLVOICEGENDER
_SYNTHESIZESPEECHREQUEST.fields_by_name['input'].message_type = _SYNTHESISINPUT
_SYNTHESIZESPEECHREQUEST.fields_by_name['voice'].message_type = _VOICESELECTIONPARAMS
_SYNTHESIZESPEECHREQUEST.fields_by_name['audio_config'].message_type = _AUDIOCONFIG
_SYNTHESIZESPEECHREQUEST.fields_by_name['enable_time_pointing'].enum_type = _SYNTHESIZESPEECHREQUEST_TIMEPOINTTYPE
_SYNTHESIZESPEECHREQUEST_TIMEPOINTTYPE.containing_type = _SYNTHESIZESPEECHREQUEST
_SYNTHESISINPUT.oneofs_by_name['input_source'].fields.append(
  _SYNTHESISINPUT.fields_by_name['text'])
_SYNTHESISINPUT.fields_by_name['text'].containing_oneof = _SYNTHESISINPUT.oneofs_by_name['input_source']
_SYNTHESISINPUT.oneofs_by_name['input_source'].fields.append(
  _SYNTHESISINPUT.fields_by_name['ssml'])
_SYNTHESISINPUT.fields_by_name['ssml'].containing_oneof = _SYNTHESISINPUT.oneofs_by_name['input_source']
_VOICESELECTIONPARAMS.fields_by_name['ssml_gender'].enum_type = _SSMLVOICEGENDER
_VOICESELECTIONPARAMS.fields_by_name['custom_voice'].message_type = _CUSTOMVOICEPARAMS
_AUDIOCONFIG.fields_by_name['audio_encoding'].enum_type = _AUDIOENCODING
_CUSTOMVOICEPARAMS.fields_by_name['reported_usage'].enum_type = _CUSTOMVOICEPARAMS_REPORTEDUSAGE
_CUSTOMVOICEPARAMS_REPORTEDUSAGE.containing_type = _CUSTOMVOICEPARAMS
_SYNTHESIZESPEECHRESPONSE.fields_by_name['timepoints'].message_type = _TIMEPOINT
_SYNTHESIZESPEECHRESPONSE.fields_by_name['audio_config'].message_type = _AUDIOCONFIG
DESCRIPTOR.message_types_by_name['ListVoicesRequest'] = _LISTVOICESREQUEST
DESCRIPTOR.message_types_by_name['ListVoicesResponse'] = _LISTVOICESRESPONSE
DESCRIPTOR.message_types_by_name['Voice'] = _VOICE
DESCRIPTOR.message_types_by_name['SynthesizeSpeechRequest'] = _SYNTHESIZESPEECHREQUEST
DESCRIPTOR.message_types_by_name['SynthesisInput'] = _SYNTHESISINPUT
DESCRIPTOR.message_types_by_name['VoiceSelectionParams'] = _VOICESELECTIONPARAMS
DESCRIPTOR.message_types_by_name['AudioConfig'] = _AUDIOCONFIG
DESCRIPTOR.message_types_by_name['CustomVoiceParams'] = _CUSTOMVOICEPARAMS
DESCRIPTOR.message_types_by_name['SynthesizeSpeechResponse'] = _SYNTHESIZESPEECHRESPONSE
DESCRIPTOR.message_types_by_name['Timepoint'] = _TIMEPOINT
DESCRIPTOR.enum_types_by_name['SsmlVoiceGender'] = _SSMLVOICEGENDER
DESCRIPTOR.enum_types_by_name['AudioEncoding'] = _AUDIOENCODING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListVoicesRequest = _reflection.GeneratedProtocolMessageType('ListVoicesRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTVOICESREQUEST,
  '__module__' : 'google.cloud.texttospeech.v1beta1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1beta1.ListVoicesRequest)
  })
_sym_db.RegisterMessage(ListVoicesRequest)

ListVoicesResponse = _reflection.GeneratedProtocolMessageType('ListVoicesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTVOICESRESPONSE,
  '__module__' : 'google.cloud.texttospeech.v1beta1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1beta1.ListVoicesResponse)
  })
_sym_db.RegisterMessage(ListVoicesResponse)

Voice = _reflection.GeneratedProtocolMessageType('Voice', (_message.Message,), {
  'DESCRIPTOR' : _VOICE,
  '__module__' : 'google.cloud.texttospeech.v1beta1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1beta1.Voice)
  })
_sym_db.RegisterMessage(Voice)

SynthesizeSpeechRequest = _reflection.GeneratedProtocolMessageType('SynthesizeSpeechRequest', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESIZESPEECHREQUEST,
  '__module__' : 'google.cloud.texttospeech.v1beta1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1beta1.SynthesizeSpeechRequest)
  })
_sym_db.RegisterMessage(SynthesizeSpeechRequest)

SynthesisInput = _reflection.GeneratedProtocolMessageType('SynthesisInput', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESISINPUT,
  '__module__' : 'google.cloud.texttospeech.v1beta1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1beta1.SynthesisInput)
  })
_sym_db.RegisterMessage(SynthesisInput)

VoiceSelectionParams = _reflection.GeneratedProtocolMessageType('VoiceSelectionParams', (_message.Message,), {
  'DESCRIPTOR' : _VOICESELECTIONPARAMS,
  '__module__' : 'google.cloud.texttospeech.v1beta1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1beta1.VoiceSelectionParams)
  })
_sym_db.RegisterMessage(VoiceSelectionParams)

AudioConfig = _reflection.GeneratedProtocolMessageType('AudioConfig', (_message.Message,), {
  'DESCRIPTOR' : _AUDIOCONFIG,
  '__module__' : 'google.cloud.texttospeech.v1beta1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1beta1.AudioConfig)
  })
_sym_db.RegisterMessage(AudioConfig)

CustomVoiceParams = _reflection.GeneratedProtocolMessageType('CustomVoiceParams', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMVOICEPARAMS,
  '__module__' : 'google.cloud.texttospeech.v1beta1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1beta1.CustomVoiceParams)
  })
_sym_db.RegisterMessage(CustomVoiceParams)

SynthesizeSpeechResponse = _reflection.GeneratedProtocolMessageType('SynthesizeSpeechResponse', (_message.Message,), {
  'DESCRIPTOR' : _SYNTHESIZESPEECHRESPONSE,
  '__module__' : 'google.cloud.texttospeech.v1beta1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1beta1.SynthesizeSpeechResponse)
  })
_sym_db.RegisterMessage(SynthesizeSpeechResponse)

Timepoint = _reflection.GeneratedProtocolMessageType('Timepoint', (_message.Message,), {
  'DESCRIPTOR' : _TIMEPOINT,
  '__module__' : 'google.cloud.texttospeech.v1beta1.cloud_tts_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.texttospeech.v1beta1.Timepoint)
  })
_sym_db.RegisterMessage(Timepoint)


DESCRIPTOR._options = None
_LISTVOICESREQUEST.fields_by_name['language_code']._options = None
_SYNTHESIZESPEECHREQUEST.fields_by_name['input']._options = None
_SYNTHESIZESPEECHREQUEST.fields_by_name['voice']._options = None
_SYNTHESIZESPEECHREQUEST.fields_by_name['audio_config']._options = None
_VOICESELECTIONPARAMS.fields_by_name['language_code']._options = None
_AUDIOCONFIG.fields_by_name['audio_encoding']._options = None
_AUDIOCONFIG.fields_by_name['speaking_rate']._options = None
_AUDIOCONFIG.fields_by_name['pitch']._options = None
_AUDIOCONFIG.fields_by_name['volume_gain_db']._options = None
_AUDIOCONFIG.fields_by_name['sample_rate_hertz']._options = None
_AUDIOCONFIG.fields_by_name['effects_profile_id']._options = None
_CUSTOMVOICEPARAMS.fields_by_name['model']._options = None
_CUSTOMVOICEPARAMS.fields_by_name['reported_usage']._options = None

_TEXTTOSPEECH = _descriptor.ServiceDescriptor(
  name='TextToSpeech',
  full_name='google.cloud.texttospeech.v1beta1.TextToSpeech',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\033texttospeech.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform',
  create_key=_descriptor._internal_create_key,
  serialized_start=2498,
  serialized_end=2964,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListVoices',
    full_name='google.cloud.texttospeech.v1beta1.TextToSpeech.ListVoices',
    index=0,
    containing_service=None,
    input_type=_LISTVOICESREQUEST,
    output_type=_LISTVOICESRESPONSE,
    serialized_options=b'\332A\rlanguage_code\202\323\344\223\002\021\022\017/v1beta1/voices',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SynthesizeSpeech',
    full_name='google.cloud.texttospeech.v1beta1.TextToSpeech.SynthesizeSpeech',
    index=1,
    containing_service=None,
    input_type=_SYNTHESIZESPEECHREQUEST,
    output_type=_SYNTHESIZESPEECHRESPONSE,
    serialized_options=b'\332A\030input,voice,audio_config\202\323\344\223\002\035\"\030/v1beta1/text:synthesize:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEXTTOSPEECH)

DESCRIPTOR.services_by_name['TextToSpeech'] = _TEXTTOSPEECH

# @@protoc_insertion_point(module_scope)
