# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: modules/v2x/proto/v2x_carstatus.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from modules.localization.proto import localization_pb2 as modules_dot_localization_dot_proto_dot_localization__pb2
from modules.canbus.proto import chassis_detail_pb2 as modules_dot_canbus_dot_proto_dot_chassis__detail__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='modules/v2x/proto/v2x_carstatus.proto',
  package='apollo.v2x',
  syntax='proto2',
  serialized_pb=_b('\n%modules/v2x/proto/v2x_carstatus.proto\x12\napollo.v2x\x1a-modules/localization/proto/localization.proto\x1a)modules/canbus/proto/chassis_detail.proto\"\x82\x01\n\tCarStatus\x12?\n\x0clocalization\x18\x01 \x01(\x0b\x32).apollo.localization.LocalizationEstimate\x12\x34\n\x0e\x63hassis_detail\x18\x02 \x01(\x0b\x32\x1c.apollo.canbus.ChassisDetail')
  ,
  dependencies=[modules_dot_localization_dot_proto_dot_localization__pb2.DESCRIPTOR,modules_dot_canbus_dot_proto_dot_chassis__detail__pb2.DESCRIPTOR,])




_CARSTATUS = _descriptor.Descriptor(
  name='CarStatus',
  full_name='apollo.v2x.CarStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='localization', full_name='apollo.v2x.CarStatus.localization', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chassis_detail', full_name='apollo.v2x.CarStatus.chassis_detail', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=274,
)

_CARSTATUS.fields_by_name['localization'].message_type = modules_dot_localization_dot_proto_dot_localization__pb2._LOCALIZATIONESTIMATE
_CARSTATUS.fields_by_name['chassis_detail'].message_type = modules_dot_canbus_dot_proto_dot_chassis__detail__pb2._CHASSISDETAIL
DESCRIPTOR.message_types_by_name['CarStatus'] = _CARSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CarStatus = _reflection.GeneratedProtocolMessageType('CarStatus', (_message.Message,), dict(
  DESCRIPTOR = _CARSTATUS,
  __module__ = 'modules.v2x.proto.v2x_carstatus_pb2'
  # @@protoc_insertion_point(class_scope:apollo.v2x.CarStatus)
  ))
_sym_db.RegisterMessage(CarStatus)


# @@protoc_insertion_point(module_scope)
