# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/websecurityscanner/v1beta/scan_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.cloud.websecurityscanner.v1beta import scan_run_pb2 as google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/websecurityscanner/v1beta/scan_config.proto',
  package='google.cloud.websecurityscanner.v1beta',
  syntax='proto3',
  serialized_options=b'\n*com.google.cloud.websecurityscanner.v1betaB\017ScanConfigProtoP\001ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\252\002&Google.Cloud.WebSecurityScanner.V1Beta\312\002&Google\\Cloud\\WebSecurityScanner\\V1beta\352\002)Google::Cloud::WebSecurityScanner::V1beta',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8google/cloud/websecurityscanner/v1beta/scan_config.proto\x12&google.cloud.websecurityscanner.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x35google/cloud/websecurityscanner/v1beta/scan_run.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc7\x0f\n\nScanConfig\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\'\n\x0c\x64isplay_name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02R\x0b\x64isplayName\x12\x17\n\x07max_qps\x18\x03 \x01(\x05R\x06maxQps\x12)\n\rstarting_urls\x18\x04 \x03(\tB\x04\xe2\x41\x01\x02R\x0cstartingUrls\x12i\n\x0e\x61uthentication\x18\x05 \x01(\x0b\x32\x41.google.cloud.websecurityscanner.v1beta.ScanConfig.AuthenticationR\x0e\x61uthentication\x12[\n\nuser_agent\x18\x06 \x01(\x0e\x32<.google.cloud.websecurityscanner.v1beta.ScanConfig.UserAgentR\tuserAgent\x12-\n\x12\x62lacklist_patterns\x18\x07 \x03(\tR\x11\x62lacklistPatterns\x12W\n\x08schedule\x18\x08 \x01(\x0b\x32;.google.cloud.websecurityscanner.v1beta.ScanConfig.ScheduleR\x08schedule\x12l\n\x10target_platforms\x18\t \x03(\x0e\x32\x41.google.cloud.websecurityscanner.v1beta.ScanConfig.TargetPlatformR\x0ftargetPlatforms\x12\x9a\x01\n!export_to_security_command_center\x18\n \x01(\x0e\x32P.google.cloud.websecurityscanner.v1beta.ScanConfig.ExportToSecurityCommandCenterR\x1d\x65xportToSecurityCommandCenter\x12N\n\nlatest_run\x18\x0b \x01(\x0b\x32/.google.cloud.websecurityscanner.v1beta.ScanRunR\tlatestRun\x12[\n\nrisk_level\x18\x0c \x01(\x0e\x32<.google.cloud.websecurityscanner.v1beta.ScanConfig.RiskLevelR\triskLevel\x1a\xe5\x03\n\x0e\x41uthentication\x12x\n\x0egoogle_account\x18\x01 \x01(\x0b\x32O.google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.GoogleAccountH\x00R\rgoogleAccount\x12x\n\x0e\x63ustom_account\x18\x02 \x01(\x0b\x32O.google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.CustomAccountH\x00R\rcustomAccount\x1aT\n\rGoogleAccount\x12 \n\x08username\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08username\x12!\n\x08password\x18\x02 \x01(\tB\x05\xe2\x41\x02\x02\x04R\x08password\x1aw\n\rCustomAccount\x12 \n\x08username\x18\x01 \x01(\tB\x04\xe2\x41\x01\x02R\x08username\x12!\n\x08password\x18\x02 \x01(\tB\x05\xe2\x41\x02\x02\x04R\x08password\x12!\n\tlogin_url\x18\x03 \x01(\tB\x04\xe2\x41\x01\x02R\x08loginUrlB\x10\n\x0e\x61uthentication\x1a\x87\x01\n\x08Schedule\x12?\n\rschedule_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cscheduleTime\x12:\n\x16interval_duration_days\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x02R\x14intervalDurationDays\"`\n\tUserAgent\x12\x1a\n\x16USER_AGENT_UNSPECIFIED\x10\x00\x12\x10\n\x0c\x43HROME_LINUX\x10\x01\x12\x12\n\x0e\x43HROME_ANDROID\x10\x02\x12\x11\n\rSAFARI_IPHONE\x10\x03\"N\n\x0eTargetPlatform\x12\x1f\n\x1bTARGET_PLATFORM_UNSPECIFIED\x10\x00\x12\x0e\n\nAPP_ENGINE\x10\x01\x12\x0b\n\x07\x43OMPUTE\x10\x02\"<\n\tRiskLevel\x12\x1a\n\x16RISK_LEVEL_UNSPECIFIED\x10\x00\x12\n\n\x06NORMAL\x10\x01\x12\x07\n\x03LOW\x10\x02\"m\n\x1d\x45xportToSecurityCommandCenter\x12\x31\n-EXPORT_TO_SECURITY_COMMAND_CENTER_UNSPECIFIED\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02:_\xea\x41\\\n,websecurityscanner.googleapis.com/ScanConfig\x12,projects/{project}/scanConfigs/{scan_config}B\x97\x02\n*com.google.cloud.websecurityscanner.v1betaB\x0fScanConfigProtoP\x01ZXgoogle.golang.org/genproto/googleapis/cloud/websecurityscanner/v1beta;websecurityscanner\xaa\x02&Google.Cloud.WebSecurityScanner.V1Beta\xca\x02&Google\\Cloud\\WebSecurityScanner\\V1beta\xea\x02)Google::Cloud::WebSecurityScanner::V1betab\x06proto3'
  ,
  dependencies=[google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_SCANCONFIG_USERAGENT = _descriptor.EnumDescriptor(
  name='UserAgent',
  full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.UserAgent',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='USER_AGENT_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHROME_LINUX', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHROME_ANDROID', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SAFARI_IPHONE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1794,
  serialized_end=1890,
)
_sym_db.RegisterEnumDescriptor(_SCANCONFIG_USERAGENT)

_SCANCONFIG_TARGETPLATFORM = _descriptor.EnumDescriptor(
  name='TargetPlatform',
  full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.TargetPlatform',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TARGET_PLATFORM_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APP_ENGINE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPUTE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1892,
  serialized_end=1970,
)
_sym_db.RegisterEnumDescriptor(_SCANCONFIG_TARGETPLATFORM)

_SCANCONFIG_RISKLEVEL = _descriptor.EnumDescriptor(
  name='RiskLevel',
  full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.RiskLevel',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RISK_LEVEL_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NORMAL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOW', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1972,
  serialized_end=2032,
)
_sym_db.RegisterEnumDescriptor(_SCANCONFIG_RISKLEVEL)

_SCANCONFIG_EXPORTTOSECURITYCOMMANDCENTER = _descriptor.EnumDescriptor(
  name='ExportToSecurityCommandCenter',
  full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.ExportToSecurityCommandCenter',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EXPORT_TO_SECURITY_COMMAND_CENTER_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ENABLED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DISABLED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2034,
  serialized_end=2143,
)
_sym_db.RegisterEnumDescriptor(_SCANCONFIG_EXPORTTOSECURITYCOMMANDCENTER)


_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT = _descriptor.Descriptor(
  name='GoogleAccount',
  full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.GoogleAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.GoogleAccount.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='username', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.GoogleAccount.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\002\002\004', json_name='password', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1431,
  serialized_end=1515,
)

_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT = _descriptor.Descriptor(
  name='CustomAccount',
  full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.CustomAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.CustomAccount.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='username', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.CustomAccount.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\002\002\004', json_name='password', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='login_url', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.CustomAccount.login_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='loginUrl', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1517,
  serialized_end=1636,
)

_SCANCONFIG_AUTHENTICATION = _descriptor.Descriptor(
  name='Authentication',
  full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='google_account', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.google_account', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='googleAccount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='custom_account', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.custom_account', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='customAccount', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT, _SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='authentication', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.authentication',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1169,
  serialized_end=1654,
)

_SCANCONFIG_SCHEDULE = _descriptor.Descriptor(
  name='Schedule',
  full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Schedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedule_time', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Schedule.schedule_time', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='scheduleTime', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interval_duration_days', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.Schedule.interval_duration_days', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='intervalDurationDays', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1657,
  serialized_end=1792,
)

_SCANCONFIG = _descriptor.Descriptor(
  name='ScanConfig',
  full_name='google.cloud.websecurityscanner.v1beta.ScanConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='name', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='displayName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_qps', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.max_qps', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='maxQps', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='starting_urls', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.starting_urls', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\002', json_name='startingUrls', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authentication', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.authentication', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='authentication', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_agent', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.user_agent', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='userAgent', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blacklist_patterns', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.blacklist_patterns', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='blacklistPatterns', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schedule', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.schedule', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='schedule', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_platforms', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.target_platforms', index=8,
      number=9, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='targetPlatforms', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='export_to_security_command_center', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.export_to_security_command_center', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='exportToSecurityCommandCenter', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latest_run', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.latest_run', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='latestRun', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='risk_level', full_name='google.cloud.websecurityscanner.v1beta.ScanConfig.risk_level', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='riskLevel', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SCANCONFIG_AUTHENTICATION, _SCANCONFIG_SCHEDULE, ],
  enum_types=[
    _SCANCONFIG_USERAGENT,
    _SCANCONFIG_TARGETPLATFORM,
    _SCANCONFIG_RISKLEVEL,
    _SCANCONFIG_EXPORTTOSECURITYCOMMANDCENTER,
  ],
  serialized_options=b'\352A\\\n,websecurityscanner.googleapis.com/ScanConfig\022,projects/{project}/scanConfigs/{scan_config}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=249,
  serialized_end=2240,
)

_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT.containing_type = _SCANCONFIG_AUTHENTICATION
_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT.containing_type = _SCANCONFIG_AUTHENTICATION
_SCANCONFIG_AUTHENTICATION.fields_by_name['google_account'].message_type = _SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT
_SCANCONFIG_AUTHENTICATION.fields_by_name['custom_account'].message_type = _SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT
_SCANCONFIG_AUTHENTICATION.containing_type = _SCANCONFIG
_SCANCONFIG_AUTHENTICATION.oneofs_by_name['authentication'].fields.append(
  _SCANCONFIG_AUTHENTICATION.fields_by_name['google_account'])
_SCANCONFIG_AUTHENTICATION.fields_by_name['google_account'].containing_oneof = _SCANCONFIG_AUTHENTICATION.oneofs_by_name['authentication']
_SCANCONFIG_AUTHENTICATION.oneofs_by_name['authentication'].fields.append(
  _SCANCONFIG_AUTHENTICATION.fields_by_name['custom_account'])
_SCANCONFIG_AUTHENTICATION.fields_by_name['custom_account'].containing_oneof = _SCANCONFIG_AUTHENTICATION.oneofs_by_name['authentication']
_SCANCONFIG_SCHEDULE.fields_by_name['schedule_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SCANCONFIG_SCHEDULE.containing_type = _SCANCONFIG
_SCANCONFIG.fields_by_name['authentication'].message_type = _SCANCONFIG_AUTHENTICATION
_SCANCONFIG.fields_by_name['user_agent'].enum_type = _SCANCONFIG_USERAGENT
_SCANCONFIG.fields_by_name['schedule'].message_type = _SCANCONFIG_SCHEDULE
_SCANCONFIG.fields_by_name['target_platforms'].enum_type = _SCANCONFIG_TARGETPLATFORM
_SCANCONFIG.fields_by_name['export_to_security_command_center'].enum_type = _SCANCONFIG_EXPORTTOSECURITYCOMMANDCENTER
_SCANCONFIG.fields_by_name['latest_run'].message_type = google_dot_cloud_dot_websecurityscanner_dot_v1beta_dot_scan__run__pb2._SCANRUN
_SCANCONFIG.fields_by_name['risk_level'].enum_type = _SCANCONFIG_RISKLEVEL
_SCANCONFIG_USERAGENT.containing_type = _SCANCONFIG
_SCANCONFIG_TARGETPLATFORM.containing_type = _SCANCONFIG
_SCANCONFIG_RISKLEVEL.containing_type = _SCANCONFIG
_SCANCONFIG_EXPORTTOSECURITYCOMMANDCENTER.containing_type = _SCANCONFIG
DESCRIPTOR.message_types_by_name['ScanConfig'] = _SCANCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScanConfig = _reflection.GeneratedProtocolMessageType('ScanConfig', (_message.Message,), {

  'Authentication' : _reflection.GeneratedProtocolMessageType('Authentication', (_message.Message,), {

    'GoogleAccount' : _reflection.GeneratedProtocolMessageType('GoogleAccount', (_message.Message,), {
      'DESCRIPTOR' : _SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT,
      '__module__' : 'google.cloud.websecurityscanner.v1beta.scan_config_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.GoogleAccount)
      })
    ,

    'CustomAccount' : _reflection.GeneratedProtocolMessageType('CustomAccount', (_message.Message,), {
      'DESCRIPTOR' : _SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT,
      '__module__' : 'google.cloud.websecurityscanner.v1beta.scan_config_pb2'
      # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication.CustomAccount)
      })
    ,
    'DESCRIPTOR' : _SCANCONFIG_AUTHENTICATION,
    '__module__' : 'google.cloud.websecurityscanner.v1beta.scan_config_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ScanConfig.Authentication)
    })
  ,

  'Schedule' : _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), {
    'DESCRIPTOR' : _SCANCONFIG_SCHEDULE,
    '__module__' : 'google.cloud.websecurityscanner.v1beta.scan_config_pb2'
    # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ScanConfig.Schedule)
    })
  ,
  'DESCRIPTOR' : _SCANCONFIG,
  '__module__' : 'google.cloud.websecurityscanner.v1beta.scan_config_pb2'
  # @@protoc_insertion_point(class_scope:google.cloud.websecurityscanner.v1beta.ScanConfig)
  })
_sym_db.RegisterMessage(ScanConfig)
_sym_db.RegisterMessage(ScanConfig.Authentication)
_sym_db.RegisterMessage(ScanConfig.Authentication.GoogleAccount)
_sym_db.RegisterMessage(ScanConfig.Authentication.CustomAccount)
_sym_db.RegisterMessage(ScanConfig.Schedule)


DESCRIPTOR._options = None
_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT.fields_by_name['username']._options = None
_SCANCONFIG_AUTHENTICATION_GOOGLEACCOUNT.fields_by_name['password']._options = None
_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT.fields_by_name['username']._options = None
_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT.fields_by_name['password']._options = None
_SCANCONFIG_AUTHENTICATION_CUSTOMACCOUNT.fields_by_name['login_url']._options = None
_SCANCONFIG_SCHEDULE.fields_by_name['interval_duration_days']._options = None
_SCANCONFIG.fields_by_name['display_name']._options = None
_SCANCONFIG.fields_by_name['starting_urls']._options = None
_SCANCONFIG._options = None
# @@protoc_insertion_point(module_scope)
