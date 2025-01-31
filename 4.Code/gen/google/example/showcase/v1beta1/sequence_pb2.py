# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/example/showcase/v1beta1/sequence.proto
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
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/example/showcase/v1beta1/sequence.proto',
  package='google.example.showcase.v1beta1',
  syntax='proto3',
  serialized_options=b'\n#com.google.example.showcase.v1beta1B\rSequenceProtoP\001Z4github.com/googleapis/gapic-showcase/server/genproto\352\002\031Google::Showcase::V1Beta1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.google/example/showcase/v1beta1/sequence.proto\x12\x1fgoogle.example.showcase.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\"\x9c\x02\n\x08Sequence\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12P\n\tresponses\x18\x02 \x03(\x0b\x32\x32.google.example.showcase.v1beta1.Sequence.ResponseR\tresponses\x1ag\n\x08Response\x12*\n\x06status\x18\x01 \x01(\x0b\x32\x12.google.rpc.StatusR\x06status\x12/\n\x05\x64\x65lay\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x05\x64\x65lay:;\xea\x41\x38\n showcase.googleapis.com/Sequence\x12\x14sequences/{sequence}\"\xf8\x03\n\x0eSequenceReport\x12\x18\n\x04name\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03R\x04name\x12S\n\x08\x61ttempts\x18\x02 \x03(\x0b\x32\x37.google.example.showcase.v1beta1.SequenceReport.AttemptR\x08\x61ttempts\x1a\xa4\x02\n\x07\x41ttempt\x12%\n\x0e\x61ttempt_number\x18\x01 \x01(\x05R\rattemptNumber\x12\x45\n\x10\x61ttempt_deadline\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0f\x61ttemptDeadline\x12?\n\rresponse_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cresponseTime\x12>\n\rattempt_delay\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0c\x61ttemptDelay\x12*\n\x06status\x18\x05 \x01(\x0b\x32\x12.google.rpc.StatusR\x06status:P\xea\x41M\n&showcase.googleapis.com/SequenceReport\x12#sequences/{sequence}/sequenceReport\"^\n\x15\x43reateSequenceRequest\x12\x45\n\x08sequence\x18\x01 \x01(\x0b\x32).google.example.showcase.v1beta1.SequenceR\x08sequence\"W\n\x16\x41ttemptSequenceRequest\x12=\n\x04name\x18\x01 \x01(\tB)\xe2\x41\x01\x02\xfa\x41\"\n showcase.googleapis.com/SequenceR\x04name\"_\n\x18GetSequenceReportRequest\x12\x43\n\x04name\x18\x01 \x01(\tB/\xe2\x41\x01\x02\xfa\x41(\n&showcase.googleapis.com/SequenceReportR\x04name2\xa5\x04\n\x0fSequenceService\x12\xa4\x01\n\x0e\x43reateSequence\x12\x36.google.example.showcase.v1beta1.CreateSequenceRequest\x1a).google.example.showcase.v1beta1.Sequence\"/\xda\x41\x08sequence\x82\xd3\xe4\x93\x02\x1e\"\x12/v1beta1/sequences:\x08sequence\x12\xba\x01\n\x11GetSequenceReport\x12\x39.google.example.showcase.v1beta1.GetSequenceReportRequest\x1a/.google.example.showcase.v1beta1.SequenceReport\"9\xda\x41\x04name\x82\xd3\xe4\x93\x02,\x12*/v1beta1/{name=sequences/*/sequenceReport}\x12\x91\x01\n\x0f\x41ttemptSequence\x12\x37.google.example.showcase.v1beta1.AttemptSequenceRequest\x1a\x16.google.protobuf.Empty\"-\xda\x41\x04name\x82\xd3\xe4\x93\x02 \"\x1b/v1beta1/{name=sequences/*}:\x01*\x1a\x1a\xca\x41\x17showcase.googleapis.comB\x88\x01\n#com.google.example.showcase.v1beta1B\rSequenceProtoP\x01Z4github.com/googleapis/gapic-showcase/server/genproto\xea\x02\x19Google::Showcase::V1Beta1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_api_dot_client__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_rpc_dot_status__pb2.DESCRIPTOR,])




_SEQUENCE_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='google.example.showcase.v1beta1.Sequence.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='google.example.showcase.v1beta1.Sequence.Response.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='delay', full_name='google.example.showcase.v1beta1.Sequence.Response.delay', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='delay', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=438,
  serialized_end=541,
)

_SEQUENCE = _descriptor.Descriptor(
  name='Sequence',
  full_name='google.example.showcase.v1beta1.Sequence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.showcase.v1beta1.Sequence.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='responses', full_name='google.example.showcase.v1beta1.Sequence.responses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='responses', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SEQUENCE_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=b'\352A8\n showcase.googleapis.com/Sequence\022\024sequences/{sequence}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=318,
  serialized_end=602,
)


_SEQUENCEREPORT_ATTEMPT = _descriptor.Descriptor(
  name='Attempt',
  full_name='google.example.showcase.v1beta1.SequenceReport.Attempt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='attempt_number', full_name='google.example.showcase.v1beta1.SequenceReport.Attempt.attempt_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='attemptNumber', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attempt_deadline', full_name='google.example.showcase.v1beta1.SequenceReport.Attempt.attempt_deadline', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='attemptDeadline', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='response_time', full_name='google.example.showcase.v1beta1.SequenceReport.Attempt.response_time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='responseTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attempt_delay', full_name='google.example.showcase.v1beta1.SequenceReport.Attempt.attempt_delay', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='attemptDelay', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.example.showcase.v1beta1.SequenceReport.Attempt.status', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=735,
  serialized_end=1027,
)

_SEQUENCEREPORT = _descriptor.Descriptor(
  name='SequenceReport',
  full_name='google.example.showcase.v1beta1.SequenceReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.showcase.v1beta1.SequenceReport.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attempts', full_name='google.example.showcase.v1beta1.SequenceReport.attempts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='attempts', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SEQUENCEREPORT_ATTEMPT, ],
  enum_types=[
  ],
  serialized_options=b'\352AM\n&showcase.googleapis.com/SequenceReport\022#sequences/{sequence}/sequenceReport',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=605,
  serialized_end=1109,
)


_CREATESEQUENCEREQUEST = _descriptor.Descriptor(
  name='CreateSequenceRequest',
  full_name='google.example.showcase.v1beta1.CreateSequenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequence', full_name='google.example.showcase.v1beta1.CreateSequenceRequest.sequence', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sequence', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1111,
  serialized_end=1205,
)


_ATTEMPTSEQUENCEREQUEST = _descriptor.Descriptor(
  name='AttemptSequenceRequest',
  full_name='google.example.showcase.v1beta1.AttemptSequenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.showcase.v1beta1.AttemptSequenceRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A\"\n showcase.googleapis.com/Sequence', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1207,
  serialized_end=1294,
)


_GETSEQUENCEREPORTREQUEST = _descriptor.Descriptor(
  name='GetSequenceReportRequest',
  full_name='google.example.showcase.v1beta1.GetSequenceReportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.example.showcase.v1beta1.GetSequenceReportRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002\372A(\n&showcase.googleapis.com/SequenceReport', json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1296,
  serialized_end=1391,
)

_SEQUENCE_RESPONSE.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_SEQUENCE_RESPONSE.fields_by_name['delay'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_SEQUENCE_RESPONSE.containing_type = _SEQUENCE
_SEQUENCE.fields_by_name['responses'].message_type = _SEQUENCE_RESPONSE
_SEQUENCEREPORT_ATTEMPT.fields_by_name['attempt_deadline'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SEQUENCEREPORT_ATTEMPT.fields_by_name['response_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SEQUENCEREPORT_ATTEMPT.fields_by_name['attempt_delay'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_SEQUENCEREPORT_ATTEMPT.fields_by_name['status'].message_type = google_dot_rpc_dot_status__pb2._STATUS
_SEQUENCEREPORT_ATTEMPT.containing_type = _SEQUENCEREPORT
_SEQUENCEREPORT.fields_by_name['attempts'].message_type = _SEQUENCEREPORT_ATTEMPT
_CREATESEQUENCEREQUEST.fields_by_name['sequence'].message_type = _SEQUENCE
DESCRIPTOR.message_types_by_name['Sequence'] = _SEQUENCE
DESCRIPTOR.message_types_by_name['SequenceReport'] = _SEQUENCEREPORT
DESCRIPTOR.message_types_by_name['CreateSequenceRequest'] = _CREATESEQUENCEREQUEST
DESCRIPTOR.message_types_by_name['AttemptSequenceRequest'] = _ATTEMPTSEQUENCEREQUEST
DESCRIPTOR.message_types_by_name['GetSequenceReportRequest'] = _GETSEQUENCEREPORTREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Sequence = _reflection.GeneratedProtocolMessageType('Sequence', (_message.Message,), {

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _SEQUENCE_RESPONSE,
    '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
    # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.Sequence.Response)
    })
  ,
  'DESCRIPTOR' : _SEQUENCE,
  '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.Sequence)
  })
_sym_db.RegisterMessage(Sequence)
_sym_db.RegisterMessage(Sequence.Response)

SequenceReport = _reflection.GeneratedProtocolMessageType('SequenceReport', (_message.Message,), {

  'Attempt' : _reflection.GeneratedProtocolMessageType('Attempt', (_message.Message,), {
    'DESCRIPTOR' : _SEQUENCEREPORT_ATTEMPT,
    '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
    # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.SequenceReport.Attempt)
    })
  ,
  'DESCRIPTOR' : _SEQUENCEREPORT,
  '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.SequenceReport)
  })
_sym_db.RegisterMessage(SequenceReport)
_sym_db.RegisterMessage(SequenceReport.Attempt)

CreateSequenceRequest = _reflection.GeneratedProtocolMessageType('CreateSequenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATESEQUENCEREQUEST,
  '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.CreateSequenceRequest)
  })
_sym_db.RegisterMessage(CreateSequenceRequest)

AttemptSequenceRequest = _reflection.GeneratedProtocolMessageType('AttemptSequenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _ATTEMPTSEQUENCEREQUEST,
  '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.AttemptSequenceRequest)
  })
_sym_db.RegisterMessage(AttemptSequenceRequest)

GetSequenceReportRequest = _reflection.GeneratedProtocolMessageType('GetSequenceReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSEQUENCEREPORTREQUEST,
  '__module__' : 'google.example.showcase.v1beta1.sequence_pb2'
  # @@protoc_insertion_point(class_scope:google.example.showcase.v1beta1.GetSequenceReportRequest)
  })
_sym_db.RegisterMessage(GetSequenceReportRequest)


DESCRIPTOR._options = None
_SEQUENCE.fields_by_name['name']._options = None
_SEQUENCE._options = None
_SEQUENCEREPORT.fields_by_name['name']._options = None
_SEQUENCEREPORT._options = None
_ATTEMPTSEQUENCEREQUEST.fields_by_name['name']._options = None
_GETSEQUENCEREPORTREQUEST.fields_by_name['name']._options = None

_SEQUENCESERVICE = _descriptor.ServiceDescriptor(
  name='SequenceService',
  full_name='google.example.showcase.v1beta1.SequenceService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312A\027showcase.googleapis.com',
  create_key=_descriptor._internal_create_key,
  serialized_start=1394,
  serialized_end=1943,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateSequence',
    full_name='google.example.showcase.v1beta1.SequenceService.CreateSequence',
    index=0,
    containing_service=None,
    input_type=_CREATESEQUENCEREQUEST,
    output_type=_SEQUENCE,
    serialized_options=b'\332A\010sequence\202\323\344\223\002\036\"\022/v1beta1/sequences:\010sequence',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetSequenceReport',
    full_name='google.example.showcase.v1beta1.SequenceService.GetSequenceReport',
    index=1,
    containing_service=None,
    input_type=_GETSEQUENCEREPORTREQUEST,
    output_type=_SEQUENCEREPORT,
    serialized_options=b'\332A\004name\202\323\344\223\002,\022*/v1beta1/{name=sequences/*/sequenceReport}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AttemptSequence',
    full_name='google.example.showcase.v1beta1.SequenceService.AttemptSequence',
    index=2,
    containing_service=None,
    input_type=_ATTEMPTSEQUENCEREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=b'\332A\004name\202\323\344\223\002 \"\033/v1beta1/{name=sequences/*}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEQUENCESERVICE)

DESCRIPTOR.services_by_name['SequenceService'] = _SEQUENCESERVICE

# @@protoc_insertion_point(module_scope)
