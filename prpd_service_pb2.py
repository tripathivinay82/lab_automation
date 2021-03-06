# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prpd_service.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import prpd_common_pb2 as prpd__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='prpd_service.proto',
  package='routing',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x12prpd_service.proto\x12\x07routing\x1a\x11prpd_common.proto\"$\n\x14RtPurgeConfigRequest\x12\x0c\n\x04time\x18\x01 \x01(\r\"\x10\n\x0eRtEmptyRequest\"4\n\x0bRtOperReply\x12%\n\x08ret_code\x18\x01 \x01(\x0e\x32\x13.routing.ReturnCode\"J\n\x13RtPurgeTimeGetReply\x12%\n\x08ret_code\x18\x01 \x01(\x0e\x32\x13.routing.ReturnCode\x12\x0c\n\x04time\x18\x02 \x01(\r2\xee\x01\n\x04\x42\x61se\x12M\n\x14RoutePurgeTimeConfig\x12\x1d.routing.RtPurgeConfigRequest\x1a\x14.routing.RtOperReply\"\x00\x12I\n\x16RoutePurgeTimeUnconfig\x12\x17.routing.RtEmptyRequest\x1a\x14.routing.RtOperReply\"\x00\x12L\n\x11RoutePurgeTimeGet\x12\x17.routing.RtEmptyRequest\x1a\x1c.routing.RtPurgeTimeGetReply\"\x00\x62\x06proto3'
  ,
  dependencies=[prpd__common__pb2.DESCRIPTOR,])




_RTPURGECONFIGREQUEST = _descriptor.Descriptor(
  name='RtPurgeConfigRequest',
  full_name='routing.RtPurgeConfigRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time', full_name='routing.RtPurgeConfigRequest.time', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=50,
  serialized_end=86,
)


_RTEMPTYREQUEST = _descriptor.Descriptor(
  name='RtEmptyRequest',
  full_name='routing.RtEmptyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=88,
  serialized_end=104,
)


_RTOPERREPLY = _descriptor.Descriptor(
  name='RtOperReply',
  full_name='routing.RtOperReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='routing.RtOperReply.ret_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=106,
  serialized_end=158,
)


_RTPURGETIMEGETREPLY = _descriptor.Descriptor(
  name='RtPurgeTimeGetReply',
  full_name='routing.RtPurgeTimeGetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret_code', full_name='routing.RtPurgeTimeGetReply.ret_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='routing.RtPurgeTimeGetReply.time', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=160,
  serialized_end=234,
)

_RTOPERREPLY.fields_by_name['ret_code'].enum_type = prpd__common__pb2._RETURNCODE
_RTPURGETIMEGETREPLY.fields_by_name['ret_code'].enum_type = prpd__common__pb2._RETURNCODE
DESCRIPTOR.message_types_by_name['RtPurgeConfigRequest'] = _RTPURGECONFIGREQUEST
DESCRIPTOR.message_types_by_name['RtEmptyRequest'] = _RTEMPTYREQUEST
DESCRIPTOR.message_types_by_name['RtOperReply'] = _RTOPERREPLY
DESCRIPTOR.message_types_by_name['RtPurgeTimeGetReply'] = _RTPURGETIMEGETREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RtPurgeConfigRequest = _reflection.GeneratedProtocolMessageType('RtPurgeConfigRequest', (_message.Message,), {
  'DESCRIPTOR' : _RTPURGECONFIGREQUEST,
  '__module__' : 'prpd_service_pb2'
  # @@protoc_insertion_point(class_scope:routing.RtPurgeConfigRequest)
  })
_sym_db.RegisterMessage(RtPurgeConfigRequest)

RtEmptyRequest = _reflection.GeneratedProtocolMessageType('RtEmptyRequest', (_message.Message,), {
  'DESCRIPTOR' : _RTEMPTYREQUEST,
  '__module__' : 'prpd_service_pb2'
  # @@protoc_insertion_point(class_scope:routing.RtEmptyRequest)
  })
_sym_db.RegisterMessage(RtEmptyRequest)

RtOperReply = _reflection.GeneratedProtocolMessageType('RtOperReply', (_message.Message,), {
  'DESCRIPTOR' : _RTOPERREPLY,
  '__module__' : 'prpd_service_pb2'
  # @@protoc_insertion_point(class_scope:routing.RtOperReply)
  })
_sym_db.RegisterMessage(RtOperReply)

RtPurgeTimeGetReply = _reflection.GeneratedProtocolMessageType('RtPurgeTimeGetReply', (_message.Message,), {
  'DESCRIPTOR' : _RTPURGETIMEGETREPLY,
  '__module__' : 'prpd_service_pb2'
  # @@protoc_insertion_point(class_scope:routing.RtPurgeTimeGetReply)
  })
_sym_db.RegisterMessage(RtPurgeTimeGetReply)



_BASE = _descriptor.ServiceDescriptor(
  name='Base',
  full_name='routing.Base',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=237,
  serialized_end=475,
  methods=[
  _descriptor.MethodDescriptor(
    name='RoutePurgeTimeConfig',
    full_name='routing.Base.RoutePurgeTimeConfig',
    index=0,
    containing_service=None,
    input_type=_RTPURGECONFIGREQUEST,
    output_type=_RTOPERREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RoutePurgeTimeUnconfig',
    full_name='routing.Base.RoutePurgeTimeUnconfig',
    index=1,
    containing_service=None,
    input_type=_RTEMPTYREQUEST,
    output_type=_RTOPERREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RoutePurgeTimeGet',
    full_name='routing.Base.RoutePurgeTimeGet',
    index=2,
    containing_service=None,
    input_type=_RTEMPTYREQUEST,
    output_type=_RTPURGETIMEGETREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_BASE)

DESCRIPTOR.services_by_name['Base'] = _BASE

# @@protoc_insertion_point(module_scope)
