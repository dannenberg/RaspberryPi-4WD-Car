# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/dialogflow/v2/answer_record.proto
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
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.dialogflow.v2 import participant_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_participant__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/dialogflow/v2/answer_record.proto',
  package='google.cloud.dialogflow.v2',
  syntax='proto3',
  serialized_options=b'\n\036com.google.cloud.dialogflow.v2B\022AnswerRecordsProtoP\001ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\370\001\001\242\002\002DF\252\002\032Google.Cloud.Dialogflow.V2',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.google/cloud/dialogflow/v2/answer_record.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/dialogflow/v2/participant.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9f\x03\n\x0c\x41nswerRecord\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12Y\n\x0f\x61nswer_feedback\x18\x02 \x01(\x0b\x32*.google.cloud.dialogflow.v2.AnswerFeedbackB\x04\xe2\x41\x01\x02R\x0e\x61nswerFeedback\x12n\n\x16\x61gent_assistant_record\x18\x04 \x01(\x0b\x32\x30.google.cloud.dialogflow.v2.AgentAssistantRecordB\x04\xe2\x41\x01\x03H\x00R\x14\x61gentAssistantRecord:\xa5\x01\xea\x41\xa1\x01\n&dialogflow.googleapis.com/AnswerRecord\x12\x30projects/{project}/answerRecords/{answer_record}\x12\x45projects/{project}/locations/{location}/answerRecords/{answer_record}B\x08\n\x06record\"\xc9\x01\n\x18ListAnswerRecordsRequest\x12G\n\x06parent\x18\x01 \x01(\tB/\xe2\x41\x01\x02\xfa\x41(\x12&dialogflow.googleapis.com/AnswerRecordR\x06parent\x12\x1c\n\x06\x66ilter\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x06\x66ilter\x12!\n\tpage_size\x18\x03 \x01(\x05\x42\x04\xe2\x41\x01\x01R\x08pageSize\x12#\n\npage_token\x18\x04 \x01(\tB\x04\xe2\x41\x01\x01R\tpageToken\"\x94\x01\n\x19ListAnswerRecordsResponse\x12O\n\x0e\x61nswer_records\x18\x01 \x03(\x0b\x32(.google.cloud.dialogflow.v2.AnswerRecordR\ranswerRecords\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\xb3\x01\n\x19UpdateAnswerRecordRequest\x12S\n\ranswer_record\x18\x01 \x01(\x0b\x32(.google.cloud.dialogflow.v2.AnswerRecordB\x04\xe2\x41\x01\x02R\x0c\x61nswerRecord\x12\x41\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskB\x04\xe2\x41\x01\x02R\nupdateMask\"\xae\x04\n\x0e\x41nswerFeedback\x12h\n\x11\x63orrectness_level\x18\x01 \x01(\x0e\x32;.google.cloud.dialogflow.v2.AnswerFeedback.CorrectnessLevelR\x10\x63orrectnessLevel\x12{\n\x1f\x61gent_assistant_detail_feedback\x18\x02 \x01(\x0b\x32\x32.google.cloud.dialogflow.v2.AgentAssistantFeedbackH\x00R\x1c\x61gentAssistantDetailFeedback\x12\x18\n\x07\x63licked\x18\x03 \x01(\x08R\x07\x63licked\x12\x39\n\nclick_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tclickTime\x12\x1c\n\tdisplayed\x18\x04 \x01(\x08R\tdisplayed\x12=\n\x0c\x64isplay_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64isplayTime\"p\n\x10\x43orrectnessLevel\x12!\n\x1d\x43ORRECTNESS_LEVEL_UNSPECIFIED\x10\x00\x12\x0f\n\x0bNOT_CORRECT\x10\x01\x12\x15\n\x11PARTIALLY_CORRECT\x10\x02\x12\x11\n\rFULLY_CORRECT\x10\x03\x42\x11\n\x0f\x64\x65tail_feedback\"\x93\x05\n\x16\x41gentAssistantFeedback\x12s\n\x10\x61nswer_relevance\x18\x01 \x01(\x0e\x32\x42.google.cloud.dialogflow.v2.AgentAssistantFeedback.AnswerRelevanceB\x04\xe2\x41\x01\x01R\x0f\x61nswerRelevance\x12\x7f\n\x14\x64ocument_correctness\x18\x02 \x01(\x0e\x32\x46.google.cloud.dialogflow.v2.AgentAssistantFeedback.DocumentCorrectnessB\x04\xe2\x41\x01\x01R\x13\x64ocumentCorrectness\x12|\n\x13\x64ocument_efficiency\x18\x03 \x01(\x0e\x32\x45.google.cloud.dialogflow.v2.AgentAssistantFeedback.DocumentEfficiencyB\x04\xe2\x41\x01\x01R\x12\x64ocumentEfficiency\"Q\n\x0f\x41nswerRelevance\x12 \n\x1c\x41NSWER_RELEVANCE_UNSPECIFIED\x10\x00\x12\x0e\n\nIRRELEVANT\x10\x01\x12\x0c\n\x08RELEVANT\x10\x02\"W\n\x13\x44ocumentCorrectness\x12$\n DOCUMENT_CORRECTNESS_UNSPECIFIED\x10\x00\x12\r\n\tINCORRECT\x10\x01\x12\x0b\n\x07\x43ORRECT\x10\x02\"Y\n\x12\x44ocumentEfficiency\x12#\n\x1f\x44OCUMENT_EFFICIENCY_UNSPECIFIED\x10\x00\x12\x0f\n\x0bINEFFICIENT\x10\x01\x12\r\n\tEFFICIENT\x10\x02\"\xdd\x01\n\x14\x41gentAssistantRecord\x12m\n\x19\x61rticle_suggestion_answer\x18\x05 \x01(\x0b\x32).google.cloud.dialogflow.v2.ArticleAnswerB\x04\xe2\x41\x01\x03H\x00R\x17\x61rticleSuggestionAnswer\x12L\n\nfaq_answer\x18\x06 \x01(\x0b\x32%.google.cloud.dialogflow.v2.FaqAnswerB\x04\xe2\x41\x01\x03H\x00R\tfaqAnswerB\x08\n\x06\x61nswer2\xad\x05\n\rAnswerRecords\x12\xed\x01\n\x11ListAnswerRecords\x12\x34.google.cloud.dialogflow.v2.ListAnswerRecordsRequest\x1a\x35.google.cloud.dialogflow.v2.ListAnswerRecordsResponse\"k\xda\x41\x06parent\x82\xd3\xe4\x93\x02\\\x12%/v2/{parent=projects/*}/answerRecordsZ3\x12\x31/v2/{parent=projects/*/locations/*}/answerRecords\x12\xb1\x02\n\x12UpdateAnswerRecord\x12\x35.google.cloud.dialogflow.v2.UpdateAnswerRecordRequest\x1a(.google.cloud.dialogflow.v2.AnswerRecord\"\xb9\x01\xda\x41\x19\x61nswer_record,update_mask\x82\xd3\xe4\x93\x02\x96\x01\x32\x33/v2/{answer_record.name=projects/*/answerRecords/*}:\ranswer_recordZP2?/v2/{answer_record.name=projects/*/locations/*/answerRecords/*}:\ranswer_record\x1ax\xca\x41\x19\x64ialogflow.googleapis.com\xd2\x41Yhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa1\x01\n\x1e\x63om.google.cloud.dialogflow.v2B\x12\x41nswerRecordsProtoP\x01ZDgoogle.golang.org/genproto/googleapis/cloud/dialogflow/v2;dialogflow\xf8\x01\x01\xa2\x02\x02\x44\x46\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_dialogflow_dot_v2_dot_participant__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_field__mask__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_ANSWERFEEDBACK_CORRECTNESSLEVEL = _descriptor.EnumDescriptor(
  name='CorrectnessLevel',
  full_name='google.cloud.dialogflow.v2.AnswerFeedback.CorrectnessLevel',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CORRECTNESS_LEVEL_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_CORRECT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PARTIALLY_CORRECT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FULLY_CORRECT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1718,
  serialized_end=1830,
)
_sym_db.RegisterEnumDescriptor(_ANSWERFEEDBACK_CORRECTNESSLEVEL)

_AGENTASSISTANTFEEDBACK_ANSWERRELEVANCE = _descriptor.EnumDescriptor(
  name='AnswerRelevance',
  full_name='google.cloud.dialogflow.v2.AgentAssistantFeedback.AnswerRelevance',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANSWER_RELEVANCE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IRRELEVANT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RELEVANT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2250,
  serialized_end=2331,
)
_sym_db.RegisterEnumDescriptor(_AGENTASSISTANTFEEDBACK_ANSWERRELEVANCE)

_AGENTASSISTANTFEEDBACK_DOCUMENTCORRECTNESS = _descriptor.EnumDescriptor(
  name='DocumentCorrectness',
  full_name='google.cloud.dialogflow.v2.AgentAssistantFeedback.DocumentCorrectness',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DOCUMENT_CORRECTNESS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INCORRECT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CORRECT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2333,
  serialized_end=2420,
)
_sym_db.RegisterEnumDescriptor(_AGENTASSISTANTFEEDBACK_DOCUMENTCORRECTNESS)

_AGENTASSISTANTFEEDBACK_DOCUMENTEFFICIENCY = _descriptor.EnumDescriptor(
  name='DocumentEfficiency',
  full_name='google.cloud.dialogflow.v2.AgentAssistantFeedback.DocumentEfficiency',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DOCUMENT_EFFICIENCY_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INEFFICIENT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EFFICIENT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2422,
  serialized_end=2511,
)
_sym_db.RegisterEnumDescriptor(_AGENTASSISTANTFEEDBACK_DOCUMENTEFFICIENCY)


_ANSWERRECORD = _descriptor.Descriptor(
  name='AnswerRecord',
  full_name='google.cloud.dialogflow.v2.AnswerRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.dialogflow.v2.AnswerRecord.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='answer_feedback', full_name='google.cloud.dialogflow.v2.AnswerRecord.answer_feedback', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='answerFeedback', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agent_assistant_record', full_name='google.cloud.dialogflow.v2.AnswerRecord.agent_assistant_record', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='agentAssistantRecord', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\352A\241\001\n&dialogflow.googleapis.com/AnswerRecord\0220projects/{project}/answerRecords/{answer_record}\022Eprojects/{project}/locations/{location}/answerRecords/{answer_record}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='record', full_name='google.cloud.dialogflow.v2.AnswerRecord.record',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=336,
  serialized_end=751,
)


_LISTANSWERRECORDSREQUEST = _descriptor.Descriptor(
  name='ListAnswerRecordsRequest',
  full_name='google.cloud.dialogflow.v2.ListAnswerRecordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='parent', full_name='google.cloud.dialogflow.v2.ListAnswerRecordsRequest.parent', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A(\022&dialogflow.googleapis.com/AnswerRecord', json_name='parent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='google.cloud.dialogflow.v2.ListAnswerRecordsRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='filter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='google.cloud.dialogflow.v2.ListAnswerRecordsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='pageSize', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='google.cloud.dialogflow.v2.ListAnswerRecordsRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='pageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=754,
  serialized_end=955,
)


_LISTANSWERRECORDSRESPONSE = _descriptor.Descriptor(
  name='ListAnswerRecordsResponse',
  full_name='google.cloud.dialogflow.v2.ListAnswerRecordsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='answer_records', full_name='google.cloud.dialogflow.v2.ListAnswerRecordsResponse.answer_records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='answerRecords', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='google.cloud.dialogflow.v2.ListAnswerRecordsResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nextPageToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=958,
  serialized_end=1106,
)


_UPDATEANSWERRECORDREQUEST = _descriptor.Descriptor(
  name='UpdateAnswerRecordRequest',
  full_name='google.cloud.dialogflow.v2.UpdateAnswerRecordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='answer_record', full_name='google.cloud.dialogflow.v2.UpdateAnswerRecordRequest.answer_record', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='answerRecord', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='update_mask', full_name='google.cloud.dialogflow.v2.UpdateAnswerRecordRequest.update_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='updateMask', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1109,
  serialized_end=1288,
)


_ANSWERFEEDBACK = _descriptor.Descriptor(
  name='AnswerFeedback',
  full_name='google.cloud.dialogflow.v2.AnswerFeedback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='correctness_level', full_name='google.cloud.dialogflow.v2.AnswerFeedback.correctness_level', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='correctnessLevel', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='agent_assistant_detail_feedback', full_name='google.cloud.dialogflow.v2.AnswerFeedback.agent_assistant_detail_feedback', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='agentAssistantDetailFeedback', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clicked', full_name='google.cloud.dialogflow.v2.AnswerFeedback.clicked', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='clicked', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='click_time', full_name='google.cloud.dialogflow.v2.AnswerFeedback.click_time', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='clickTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='displayed', full_name='google.cloud.dialogflow.v2.AnswerFeedback.displayed', index=4,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='displayed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_time', full_name='google.cloud.dialogflow.v2.AnswerFeedback.display_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='displayTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ANSWERFEEDBACK_CORRECTNESSLEVEL,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='detail_feedback', full_name='google.cloud.dialogflow.v2.AnswerFeedback.detail_feedback',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1291,
  serialized_end=1849,
)


_AGENTASSISTANTFEEDBACK = _descriptor.Descriptor(
  name='AgentAssistantFeedback',
  full_name='google.cloud.dialogflow.v2.AgentAssistantFeedback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='answer_relevance', full_name='google.cloud.dialogflow.v2.AgentAssistantFeedback.answer_relevance', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='answerRelevance', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='document_correctness', full_name='google.cloud.dialogflow.v2.AgentAssistantFeedback.document_correctness', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='documentCorrectness', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='document_efficiency', full_name='google.cloud.dialogflow.v2.AgentAssistantFeedback.document_efficiency', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\001', json_name='documentEfficiency', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AGENTASSISTANTFEEDBACK_ANSWERRELEVANCE,
    _AGENTASSISTANTFEEDBACK_DOCUMENTCORRECTNESS,
    _AGENTASSISTANTFEEDBACK_DOCUMENTEFFICIENCY,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1852,
  serialized_end=2511,
)


_AGENTASSISTANTRECORD = _descriptor.Descriptor(
  name='AgentAssistantRecord',
  full_name='google.cloud.dialogflow.v2.AgentAssistantRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='article_suggestion_answer', full_name='google.cloud.dialogflow.v2.AgentAssistantRecord.article_suggestion_answer', index=0,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='articleSuggestionAnswer', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='faq_answer', full_name='google.cloud.dialogflow.v2.AgentAssistantRecord.faq_answer', index=1,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='faqAnswer', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
      name='answer', full_name='google.cloud.dialogflow.v2.AgentAssistantRecord.answer',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=2514,
  serialized_end=2735,
)

_ANSWERRECORD.fields_by_name['answer_feedback'].message_type = _ANSWERFEEDBACK
_ANSWERRECORD.fields_by_name['agent_assistant_record'].message_type = _AGENTASSISTANTRECORD
_ANSWERRECORD.oneofs_by_name['record'].fields.append(
  _ANSWERRECORD.fields_by_name['agent_assistant_record'])
_ANSWERRECORD.fields_by_name['agent_assistant_record'].containing_oneof = _ANSWERRECORD.oneofs_by_name['record']
_LISTANSWERRECORDSRESPONSE.fields_by_name['answer_records'].message_type = _ANSWERRECORD
_UPDATEANSWERRECORDREQUEST.fields_by_name['answer_record'].message_type = _ANSWERRECORD
_UPDATEANSWERRECORDREQUEST.fields_by_name['update_mask'].message_type = google_dot_protobuf_dot_field__mask__pb2._FIELDMASK
_ANSWERFEEDBACK.fields_by_name['correctness_level'].enum_type = _ANSWERFEEDBACK_CORRECTNESSLEVEL
_ANSWERFEEDBACK.fields_by_name['agent_assistant_detail_feedback'].message_type = _AGENTASSISTANTFEEDBACK
_ANSWERFEEDBACK.fields_by_name['click_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ANSWERFEEDBACK.fields_by_name['display_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ANSWERFEEDBACK_CORRECTNESSLEVEL.containing_type = _ANSWERFEEDBACK
_ANSWERFEEDBACK.oneofs_by_name['detail_feedback'].fields.append(
  _ANSWERFEEDBACK.fields_by_name['agent_assistant_detail_feedback'])
_ANSWERFEEDBACK.fields_by_name['agent_assistant_detail_feedback'].containing_oneof = _ANSWERFEEDBACK.oneofs_by_name['detail_feedback']
_AGENTASSISTANTFEEDBACK.fields_by_name['answer_relevance'].enum_type = _AGENTASSISTANTFEEDBACK_ANSWERRELEVANCE
_AGENTASSISTANTFEEDBACK.fields_by_name['document_correctness'].enum_type = _AGENTASSISTANTFEEDBACK_DOCUMENTCORRECTNESS
_AGENTASSISTANTFEEDBACK.fields_by_name['document_efficiency'].enum_type = _AGENTASSISTANTFEEDBACK_DOCUMENTEFFICIENCY
_AGENTASSISTANTFEEDBACK_ANSWERRELEVANCE.containing_type = _AGENTASSISTANTFEEDBACK
_AGENTASSISTANTFEEDBACK_DOCUMENTCORRECTNESS.containing_type = _AGENTASSISTANTFEEDBACK
_AGENTASSISTANTFEEDBACK_DOCUMENTEFFICIENCY.containing_type = _AGENTASSISTANTFEEDBACK
_AGENTASSISTANTRECORD.fields_by_name['article_suggestion_answer'].message_type = google_dot_cloud_dot_dialogflow_dot_v2_dot_participant__pb2._ARTICLEANSWER
_AGENTASSISTANTRECORD.fields_by_name['faq_answer'].message_type = google_dot_cloud_dot_dialogflow_dot_v2_dot_participant__pb2._FAQANSWER
_AGENTASSISTANTRECORD.oneofs_by_name['answer'].fields.append(
  _AGENTASSISTANTRECORD.fields_by_name['article_suggestion_answer'])
_AGENTASSISTANTRECORD.fields_by_name['article_suggestion_answer'].containing_oneof = _AGENTASSISTANTRECORD.oneofs_by_name['answer']
_AGENTASSISTANTRECORD.oneofs_by_name['answer'].fields.append(
  _AGENTASSISTANTRECORD.fields_by_name['faq_answer'])
_AGENTASSISTANTRECORD.fields_by_name['faq_answer'].containing_oneof = _AGENTASSISTANTRECORD.oneofs_by_name['answer']
DESCRIPTOR.message_types_by_name['AnswerRecord'] = _ANSWERRECORD
DESCRIPTOR.message_types_by_name['ListAnswerRecordsRequest'] = _LISTANSWERRECORDSREQUEST
DESCRIPTOR.message_types_by_name['ListAnswerRecordsResponse'] = _LISTANSWERRECORDSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateAnswerRecordRequest'] = _UPDATEANSWERRECORDREQUEST
DESCRIPTOR.message_types_by_name['AnswerFeedback'] = _ANSWERFEEDBACK
DESCRIPTOR.message_types_by_name['AgentAssistantFeedback'] = _AGENTASSISTANTFEEDBACK
DESCRIPTOR.message_types_by_name['AgentAssistantRecord'] = _AGENTASSISTANTRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnswerRecord = _reflection.GeneratedProtocolMessageType('AnswerRecord', (_message.Message,), {
  'DESCRIPTOR' : _ANSWERRECORD,
  '__module__' : 'google.cloud.dialogflow.v2.answer_record_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.AnswerRecord)
  })
_sym_db.RegisterMessage(AnswerRecord)

ListAnswerRecordsRequest = _reflection.GeneratedProtocolMessageType('ListAnswerRecordsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTANSWERRECORDSREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2.answer_record_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.ListAnswerRecordsRequest)
  })
_sym_db.RegisterMessage(ListAnswerRecordsRequest)

ListAnswerRecordsResponse = _reflection.GeneratedProtocolMessageType('ListAnswerRecordsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTANSWERRECORDSRESPONSE,
  '__module__' : 'google.cloud.dialogflow.v2.answer_record_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.ListAnswerRecordsResponse)
  })
_sym_db.RegisterMessage(ListAnswerRecordsResponse)

UpdateAnswerRecordRequest = _reflection.GeneratedProtocolMessageType('UpdateAnswerRecordRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEANSWERRECORDREQUEST,
  '__module__' : 'google.cloud.dialogflow.v2.answer_record_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.UpdateAnswerRecordRequest)
  })
_sym_db.RegisterMessage(UpdateAnswerRecordRequest)

AnswerFeedback = _reflection.GeneratedProtocolMessageType('AnswerFeedback', (_message.Message,), {
  'DESCRIPTOR' : _ANSWERFEEDBACK,
  '__module__' : 'google.cloud.dialogflow.v2.answer_record_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.AnswerFeedback)
  })
_sym_db.RegisterMessage(AnswerFeedback)

AgentAssistantFeedback = _reflection.GeneratedProtocolMessageType('AgentAssistantFeedback', (_message.Message,), {
  'DESCRIPTOR' : _AGENTASSISTANTFEEDBACK,
  '__module__' : 'google.cloud.dialogflow.v2.answer_record_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.AgentAssistantFeedback)
  })
_sym_db.RegisterMessage(AgentAssistantFeedback)

AgentAssistantRecord = _reflection.GeneratedProtocolMessageType('AgentAssistantRecord', (_message.Message,), {
  'DESCRIPTOR' : _AGENTASSISTANTRECORD,
  '__module__' : 'google.cloud.dialogflow.v2.answer_record_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.dialogflow.v2.AgentAssistantRecord)
  })
_sym_db.RegisterMessage(AgentAssistantRecord)


DESCRIPTOR._options = None
_ANSWERRECORD.fields_by_name['answer_feedback']._options = None
_ANSWERRECORD.fields_by_name['agent_assistant_record']._options = None
_ANSWERRECORD._options = None
_LISTANSWERRECORDSREQUEST.fields_by_name['parent']._options = None
_LISTANSWERRECORDSREQUEST.fields_by_name['filter']._options = None
_LISTANSWERRECORDSREQUEST.fields_by_name['page_size']._options = None
_LISTANSWERRECORDSREQUEST.fields_by_name['page_token']._options = None
_UPDATEANSWERRECORDREQUEST.fields_by_name['answer_record']._options = None
_UPDATEANSWERRECORDREQUEST.fields_by_name['update_mask']._options = None
_AGENTASSISTANTFEEDBACK.fields_by_name['answer_relevance']._options = None
_AGENTASSISTANTFEEDBACK.fields_by_name['document_correctness']._options = None
_AGENTASSISTANTFEEDBACK.fields_by_name['document_efficiency']._options = None
_AGENTASSISTANTRECORD.fields_by_name['article_suggestion_answer']._options = None
_AGENTASSISTANTRECORD.fields_by_name['faq_answer']._options = None

_ANSWERRECORDS = _descriptor.ServiceDescriptor(
  name='AnswerRecords',
  full_name='google.cloud.dialogflow.v2.AnswerRecords',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\031dialogflow.googleapis.com\322AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow',
  create_key=_descriptor._internal_create_key,
  serialized_start=2738,
  serialized_end=3423,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListAnswerRecords',
    full_name='google.cloud.dialogflow.v2.AnswerRecords.ListAnswerRecords',
    index=0,
    containing_service=None,
    input_type=_LISTANSWERRECORDSREQUEST,
    output_type=_LISTANSWERRECORDSRESPONSE,
    serialized_options=b'\332A\006parent\202\323\344\223\002\\\022%/v2/{parent=projects/*}/answerRecordsZ3\0221/v2/{parent=projects/*/locations/*}/answerRecords',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateAnswerRecord',
    full_name='google.cloud.dialogflow.v2.AnswerRecords.UpdateAnswerRecord',
    index=1,
    containing_service=None,
    input_type=_UPDATEANSWERRECORDREQUEST,
    output_type=_ANSWERRECORD,
    serialized_options=b'\332A\031answer_record,update_mask\202\323\344\223\002\226\00123/v2/{answer_record.name=projects/*/answerRecords/*}:\ranswer_recordZP2?/v2/{answer_record.name=projects/*/locations/*/answerRecords/*}:\ranswer_record',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ANSWERRECORDS)

DESCRIPTOR.services_by_name['AnswerRecords'] = _ANSWERRECORDS

# @@protoc_insertion_point(module_scope)
