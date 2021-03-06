# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gribi_ywrapper.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='gribi_ywrapper.proto',
  package='ywrapper',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x14gribi_ywrapper.proto\x12\x08ywrapper\"\x1b\n\nBytesValue\x12\r\n\x05value\x18\x01 \x01(\x0c\"\x1a\n\tBoolValue\x12\r\n\x05value\x18\x01 \x01(\x08\"3\n\x0e\x44\x65\x63imal64Value\x12\x0e\n\x06\x64igits\x18\x01 \x01(\x03\x12\x11\n\tprecision\x18\x02 \x01(\r\"\x19\n\x08IntValue\x12\r\n\x05value\x18\x01 \x01(\x12\"\x1c\n\x0bStringValue\x12\r\n\x05value\x18\x01 \x01(\t\"\x1a\n\tUintValue\x12\r\n\x05value\x18\x01 \x01(\x04\x62\x06proto3'
)




_BYTESVALUE = _descriptor.Descriptor(
  name='BytesValue',
  full_name='ywrapper.BytesValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='ywrapper.BytesValue.value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=34,
  serialized_end=61,
)


_BOOLVALUE = _descriptor.Descriptor(
  name='BoolValue',
  full_name='ywrapper.BoolValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='ywrapper.BoolValue.value', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=63,
  serialized_end=89,
)


_DECIMAL64VALUE = _descriptor.Descriptor(
  name='Decimal64Value',
  full_name='ywrapper.Decimal64Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='digits', full_name='ywrapper.Decimal64Value.digits', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='precision', full_name='ywrapper.Decimal64Value.precision', index=1,
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
  serialized_start=91,
  serialized_end=142,
)


_INTVALUE = _descriptor.Descriptor(
  name='IntValue',
  full_name='ywrapper.IntValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='ywrapper.IntValue.value', index=0,
      number=1, type=18, cpp_type=2, label=1,
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
  serialized_start=144,
  serialized_end=169,
)


_STRINGVALUE = _descriptor.Descriptor(
  name='StringValue',
  full_name='ywrapper.StringValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='ywrapper.StringValue.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=171,
  serialized_end=199,
)


_UINTVALUE = _descriptor.Descriptor(
  name='UintValue',
  full_name='ywrapper.UintValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='ywrapper.UintValue.value', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  serialized_start=201,
  serialized_end=227,
)

DESCRIPTOR.message_types_by_name['BytesValue'] = _BYTESVALUE
DESCRIPTOR.message_types_by_name['BoolValue'] = _BOOLVALUE
DESCRIPTOR.message_types_by_name['Decimal64Value'] = _DECIMAL64VALUE
DESCRIPTOR.message_types_by_name['IntValue'] = _INTVALUE
DESCRIPTOR.message_types_by_name['StringValue'] = _STRINGVALUE
DESCRIPTOR.message_types_by_name['UintValue'] = _UINTVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BytesValue = _reflection.GeneratedProtocolMessageType('BytesValue', (_message.Message,), {
  'DESCRIPTOR' : _BYTESVALUE,
  '__module__' : 'gribi_ywrapper_pb2'
  # @@protoc_insertion_point(class_scope:ywrapper.BytesValue)
  })
_sym_db.RegisterMessage(BytesValue)

BoolValue = _reflection.GeneratedProtocolMessageType('BoolValue', (_message.Message,), {
  'DESCRIPTOR' : _BOOLVALUE,
  '__module__' : 'gribi_ywrapper_pb2'
  # @@protoc_insertion_point(class_scope:ywrapper.BoolValue)
  })
_sym_db.RegisterMessage(BoolValue)

Decimal64Value = _reflection.GeneratedProtocolMessageType('Decimal64Value', (_message.Message,), {
  'DESCRIPTOR' : _DECIMAL64VALUE,
  '__module__' : 'gribi_ywrapper_pb2'
  # @@protoc_insertion_point(class_scope:ywrapper.Decimal64Value)
  })
_sym_db.RegisterMessage(Decimal64Value)

IntValue = _reflection.GeneratedProtocolMessageType('IntValue', (_message.Message,), {
  'DESCRIPTOR' : _INTVALUE,
  '__module__' : 'gribi_ywrapper_pb2'
  # @@protoc_insertion_point(class_scope:ywrapper.IntValue)
  })
_sym_db.RegisterMessage(IntValue)

StringValue = _reflection.GeneratedProtocolMessageType('StringValue', (_message.Message,), {
  'DESCRIPTOR' : _STRINGVALUE,
  '__module__' : 'gribi_ywrapper_pb2'
  # @@protoc_insertion_point(class_scope:ywrapper.StringValue)
  })
_sym_db.RegisterMessage(StringValue)

UintValue = _reflection.GeneratedProtocolMessageType('UintValue', (_message.Message,), {
  'DESCRIPTOR' : _UINTVALUE,
  '__module__' : 'gribi_ywrapper_pb2'
  # @@protoc_insertion_point(class_scope:ywrapper.UintValue)
  })
_sym_db.RegisterMessage(UintValue)


# @@protoc_insertion_point(module_scope)
