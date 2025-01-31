# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/ads/googleads/v8/resources/conversion_value_rule.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.ads.googleads.v8.enums import conversion_value_rule_status_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_conversion__value__rule__status__pb2
from google.ads.googleads.v8.enums import value_rule_device_type_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_value__rule__device__type__pb2
from google.ads.googleads.v8.enums import value_rule_geo_location_match_type_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_value__rule__geo__location__match__type__pb2
from google.ads.googleads.v8.enums import value_rule_operation_pb2 as google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_value__rule__operation__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/ads/googleads/v8/resources/conversion_value_rule.proto',
  package='google.ads.googleads.v8.resources',
  syntax='proto3',
  serialized_options=b'\n%com.google.ads.googleads.v8.resourcesB\030ConversionValueRuleProtoP\001ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\242\002\003GAA\252\002!Google.Ads.GoogleAds.V8.Resources\312\002!Google\\Ads\\GoogleAds\\V8\\Resources\352\002%Google::Ads::GoogleAds::V8::Resources',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=google/ads/googleads/v8/resources/conversion_value_rule.proto\x12!google.ads.googleads.v8.resources\x1a@google/ads/googleads/v8/enums/conversion_value_rule_status.proto\x1a:google/ads/googleads/v8/enums/value_rule_device_type.proto\x1a\x46google/ads/googleads/v8/enums/value_rule_geo_location_match_type.proto\x1a\x38google/ads/googleads/v8/enums/value_rule_operation.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/api/annotations.proto\"\xa1\x0f\n\x13\x43onversionValueRule\x12Z\n\rresource_name\x18\x01 \x01(\tB5\xe2\x41\x01\x05\xfa\x41.\n,googleads.googleapis.com/ConversionValueRuleR\x0cresourceName\x12\x14\n\x02id\x18\x02 \x01(\x03\x42\x04\xe2\x41\x01\x03R\x02id\x12^\n\x06\x61\x63tion\x18\x03 \x01(\x0b\x32\x46.google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleActionR\x06\x61\x63tion\x12\x8a\x01\n\x16geo_location_condition\x18\x04 \x01(\x0b\x32T.google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleGeoLocationConditionR\x14geoLocationCondition\x12z\n\x10\x64\x65vice_condition\x18\x05 \x01(\x0b\x32O.google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleDeviceConditionR\x0f\x64\x65viceCondition\x12\x80\x01\n\x12\x61udience_condition\x18\x06 \x01(\x0b\x32Q.google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleAudienceConditionR\x11\x61udienceCondition\x12Q\n\x0eowner_customer\x18\x07 \x01(\tB*\xe2\x41\x01\x03\xfa\x41#\n!googleads.googleapis.com/CustomerR\rownerCustomer\x12n\n\x06status\x18\x08 \x01(\x0e\x32V.google.ads.googleads.v8.enums.ConversionValueRuleStatusEnum.ConversionValueRuleStatusR\x06status\x1a\x8f\x01\n\x0fValueRuleAction\x12\x66\n\toperation\x18\x01 \x01(\x0e\x32H.google.ads.googleads.v8.enums.ValueRuleOperationEnum.ValueRuleOperationR\toperation\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value\x1a\x95\x04\n\x1dValueRuleGeoLocationCondition\x12r\n\x1d\x65xcluded_geo_target_constants\x18\x01 \x03(\tB/\xfa\x41,\n*googleads.googleapis.com/GeoTargetConstantR\x1a\x65xcludedGeoTargetConstants\x12\x95\x01\n\x17\x65xcluded_geo_match_type\x18\x02 \x01(\x0e\x32^.google.ads.googleads.v8.enums.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchTypeR\x14\x65xcludedGeoMatchType\x12\x61\n\x14geo_target_constants\x18\x03 \x03(\tB/\xfa\x41,\n*googleads.googleapis.com/GeoTargetConstantR\x12geoTargetConstants\x12\x84\x01\n\x0egeo_match_type\x18\x04 \x01(\x0e\x32^.google.ads.googleads.v8.enums.ValueRuleGeoLocationMatchTypeEnum.ValueRuleGeoLocationMatchTypeR\x0cgeoMatchType\x1a\x89\x01\n\x18ValueRuleDeviceCondition\x12m\n\x0c\x64\x65vice_types\x18\x01 \x03(\x0e\x32J.google.ads.googleads.v8.enums.ValueRuleDeviceTypeEnum.ValueRuleDeviceTypeR\x0b\x64\x65viceTypes\x1a\xb6\x01\n\x1aValueRuleAudienceCondition\x12\x45\n\nuser_lists\x18\x01 \x03(\tB&\xfa\x41#\n!googleads.googleapis.com/UserListR\tuserLists\x12Q\n\x0euser_interests\x18\x02 \x03(\tB*\xfa\x41\'\n%googleads.googleapis.com/UserInterestR\ruserInterests:z\xea\x41w\n,googleads.googleapis.com/ConversionValueRule\x12Gcustomers/{customer_id}/conversionValueRules/{conversion_value_rule_id}B\x85\x02\n%com.google.ads.googleads.v8.resourcesB\x18\x43onversionValueRuleProtoP\x01ZJgoogle.golang.org/genproto/googleapis/ads/googleads/v8/resources;resources\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V8.Resources\xca\x02!Google\\Ads\\GoogleAds\\V8\\Resources\xea\x02%Google::Ads::GoogleAds::V8::Resourcesb\x06proto3'
  ,
  dependencies=[google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_conversion__value__rule__status__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_value__rule__device__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_value__rule__geo__location__match__type__pb2.DESCRIPTOR,google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_value__rule__operation__pb2.DESCRIPTOR,google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,google_dot_api_dot_resource__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_CONVERSIONVALUERULE_VALUERULEACTION = _descriptor.Descriptor(
  name='ValueRuleAction',
  full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleAction.operation', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='operation', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleAction.value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1272,
  serialized_end=1415,
)

_CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION = _descriptor.Descriptor(
  name='ValueRuleGeoLocationCondition',
  full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleGeoLocationCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='excluded_geo_target_constants', full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleGeoLocationCondition.excluded_geo_target_constants', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A,\n*googleads.googleapis.com/GeoTargetConstant', json_name='excludedGeoTargetConstants', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='excluded_geo_match_type', full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleGeoLocationCondition.excluded_geo_match_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='excludedGeoMatchType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geo_target_constants', full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleGeoLocationCondition.geo_target_constants', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A,\n*googleads.googleapis.com/GeoTargetConstant', json_name='geoTargetConstants', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geo_match_type', full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleGeoLocationCondition.geo_match_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='geoMatchType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1418,
  serialized_end=1951,
)

_CONVERSIONVALUERULE_VALUERULEDEVICECONDITION = _descriptor.Descriptor(
  name='ValueRuleDeviceCondition',
  full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleDeviceCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_types', full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleDeviceCondition.device_types', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='deviceTypes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1954,
  serialized_end=2091,
)

_CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION = _descriptor.Descriptor(
  name='ValueRuleAudienceCondition',
  full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleAudienceCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_lists', full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleAudienceCondition.user_lists', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A#\n!googleads.googleapis.com/UserList', json_name='userLists', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_interests', full_name='google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleAudienceCondition.user_interests', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372A\'\n%googleads.googleapis.com/UserInterest', json_name='userInterests', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=2094,
  serialized_end=2276,
)

_CONVERSIONVALUERULE = _descriptor.Descriptor(
  name='ConversionValueRule',
  full_name='google.ads.googleads.v8.resources.ConversionValueRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_name', full_name='google.ads.googleads.v8.resources.ConversionValueRule.resource_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\005\372A.\n,googleads.googleapis.com/ConversionValueRule', json_name='resourceName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='google.ads.googleads.v8.resources.ConversionValueRule.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003', json_name='id', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='google.ads.googleads.v8.resources.ConversionValueRule.action', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='action', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='geo_location_condition', full_name='google.ads.googleads.v8.resources.ConversionValueRule.geo_location_condition', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='geoLocationCondition', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_condition', full_name='google.ads.googleads.v8.resources.ConversionValueRule.device_condition', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='deviceCondition', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='audience_condition', full_name='google.ads.googleads.v8.resources.ConversionValueRule.audience_condition', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='audienceCondition', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner_customer', full_name='google.ads.googleads.v8.resources.ConversionValueRule.owner_customer', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\342A\001\003\372A#\n!googleads.googleapis.com/Customer', json_name='ownerCustomer', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='google.ads.googleads.v8.resources.ConversionValueRule.status', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CONVERSIONVALUERULE_VALUERULEACTION, _CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION, _CONVERSIONVALUERULE_VALUERULEDEVICECONDITION, _CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION, ],
  enum_types=[
  ],
  serialized_options=b'\352Aw\n,googleads.googleapis.com/ConversionValueRule\022Gcustomers/{customer_id}/conversionValueRules/{conversion_value_rule_id}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=2400,
)

_CONVERSIONVALUERULE_VALUERULEACTION.fields_by_name['operation'].enum_type = google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_value__rule__operation__pb2._VALUERULEOPERATIONENUM_VALUERULEOPERATION
_CONVERSIONVALUERULE_VALUERULEACTION.containing_type = _CONVERSIONVALUERULE
_CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION.fields_by_name['excluded_geo_match_type'].enum_type = google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_value__rule__geo__location__match__type__pb2._VALUERULEGEOLOCATIONMATCHTYPEENUM_VALUERULEGEOLOCATIONMATCHTYPE
_CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION.fields_by_name['geo_match_type'].enum_type = google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_value__rule__geo__location__match__type__pb2._VALUERULEGEOLOCATIONMATCHTYPEENUM_VALUERULEGEOLOCATIONMATCHTYPE
_CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION.containing_type = _CONVERSIONVALUERULE
_CONVERSIONVALUERULE_VALUERULEDEVICECONDITION.fields_by_name['device_types'].enum_type = google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_value__rule__device__type__pb2._VALUERULEDEVICETYPEENUM_VALUERULEDEVICETYPE
_CONVERSIONVALUERULE_VALUERULEDEVICECONDITION.containing_type = _CONVERSIONVALUERULE
_CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION.containing_type = _CONVERSIONVALUERULE
_CONVERSIONVALUERULE.fields_by_name['action'].message_type = _CONVERSIONVALUERULE_VALUERULEACTION
_CONVERSIONVALUERULE.fields_by_name['geo_location_condition'].message_type = _CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION
_CONVERSIONVALUERULE.fields_by_name['device_condition'].message_type = _CONVERSIONVALUERULE_VALUERULEDEVICECONDITION
_CONVERSIONVALUERULE.fields_by_name['audience_condition'].message_type = _CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION
_CONVERSIONVALUERULE.fields_by_name['status'].enum_type = google_dot_ads_dot_googleads_dot_v8_dot_enums_dot_conversion__value__rule__status__pb2._CONVERSIONVALUERULESTATUSENUM_CONVERSIONVALUERULESTATUS
DESCRIPTOR.message_types_by_name['ConversionValueRule'] = _CONVERSIONVALUERULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConversionValueRule = _reflection.GeneratedProtocolMessageType('ConversionValueRule', (_message.Message,), {

  'ValueRuleAction' : _reflection.GeneratedProtocolMessageType('ValueRuleAction', (_message.Message,), {
    'DESCRIPTOR' : _CONVERSIONVALUERULE_VALUERULEACTION,
    '__module__' : 'google.ads.googleads.v8.resources.conversion_value_rule_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleAction)
    })
  ,

  'ValueRuleGeoLocationCondition' : _reflection.GeneratedProtocolMessageType('ValueRuleGeoLocationCondition', (_message.Message,), {
    'DESCRIPTOR' : _CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION,
    '__module__' : 'google.ads.googleads.v8.resources.conversion_value_rule_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleGeoLocationCondition)
    })
  ,

  'ValueRuleDeviceCondition' : _reflection.GeneratedProtocolMessageType('ValueRuleDeviceCondition', (_message.Message,), {
    'DESCRIPTOR' : _CONVERSIONVALUERULE_VALUERULEDEVICECONDITION,
    '__module__' : 'google.ads.googleads.v8.resources.conversion_value_rule_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleDeviceCondition)
    })
  ,

  'ValueRuleAudienceCondition' : _reflection.GeneratedProtocolMessageType('ValueRuleAudienceCondition', (_message.Message,), {
    'DESCRIPTOR' : _CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION,
    '__module__' : 'google.ads.googleads.v8.resources.conversion_value_rule_pb2'
    # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.ConversionValueRule.ValueRuleAudienceCondition)
    })
  ,
  'DESCRIPTOR' : _CONVERSIONVALUERULE,
  '__module__' : 'google.ads.googleads.v8.resources.conversion_value_rule_pb2'
  # @@protoc_insertion_point(class_scope:google.ads.googleads.v8.resources.ConversionValueRule)
  })
_sym_db.RegisterMessage(ConversionValueRule)
_sym_db.RegisterMessage(ConversionValueRule.ValueRuleAction)
_sym_db.RegisterMessage(ConversionValueRule.ValueRuleGeoLocationCondition)
_sym_db.RegisterMessage(ConversionValueRule.ValueRuleDeviceCondition)
_sym_db.RegisterMessage(ConversionValueRule.ValueRuleAudienceCondition)


DESCRIPTOR._options = None
_CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION.fields_by_name['excluded_geo_target_constants']._options = None
_CONVERSIONVALUERULE_VALUERULEGEOLOCATIONCONDITION.fields_by_name['geo_target_constants']._options = None
_CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION.fields_by_name['user_lists']._options = None
_CONVERSIONVALUERULE_VALUERULEAUDIENCECONDITION.fields_by_name['user_interests']._options = None
_CONVERSIONVALUERULE.fields_by_name['resource_name']._options = None
_CONVERSIONVALUERULE.fields_by_name['id']._options = None
_CONVERSIONVALUERULE.fields_by_name['owner_customer']._options = None
_CONVERSIONVALUERULE._options = None
# @@protoc_insertion_point(module_scope)
