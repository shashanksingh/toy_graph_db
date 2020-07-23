# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: query_servicer.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='query_servicer.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14query_servicer.proto\"\xfd\x02\n\x11ToyGraphDBRequest\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .ToyGraphDBRequest.type_of_graph\x12\x11\n\x03\x64\x61g\x18\x02 \x01(\x0b\x32\x04.dag\x12\x1b\n\x08\x64irected\x18\x03 \x01(\x0b\x32\t.directed\x12\x15\n\x05graph\x18\x04 \x01(\x0b\x32\x06.graph\x12\x13\n\x04grid\x18\x05 \x01(\x0b\x32\x05.grid\x12\x13\n\x04tree\x18\x06 \x01(\x0b\x32\x05.tree\x12\x13\n\x04trie\x18\x07 \x01(\x0b\x32\x05.trie\x12\x1f\n\nundirected\x18\x08 \x01(\x0b\x32\x0b.undirected\x12\x0f\n\x07message\x18\t \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\n \x01(\t\x12\r\n\x05table\x18\x0b \x01(\t\"_\n\rtype_of_graph\x12\t\n\x05GRAPH\x10\x00\x12\x07\n\x03\x44\x41G\x10\x01\x12\x0c\n\x08\x44IRECTED\x10\x02\x12\x08\n\x04GRID\x10\x03\x12\x08\n\x04TREE\x10\x04\x12\x08\n\x04TRIE\x10\x05\x12\x0e\n\nUNDIRECTED\x10\x06\"\x05\n\x03\x64\x61g\"\n\n\x08\x64irected\"\x07\n\x05graph\"\x06\n\x04grid\"\x06\n\x04tree\"\x06\n\x04trie\"\x0c\n\nundirected\"o\n\x12ToyGraphDBResponse\x12\x17\n\x06status\x18\x02 \x01(\x0b\x32\x07.status\x12\x1d\n\rerror_message\x18\x03 \x01(\x0b\x32\x06.Error\x12!\n\x0fsuccess_message\x18\x04 \x01(\x0b\x32\x08.Success\"&\n\x05\x45rror\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\"(\n\x07Success\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\"8\n\x06status\".\n\x06status\x12\x0c\n\x08\x41LL_GOOD\x10\x00\x12\x16\n\x12\x45VERYTHING_IS_FINE\x10\x01\x32\xca\x01\n\nToyGraphDB\x12\x37\n\nread_graph\x12\x12.ToyGraphDBRequest\x1a\x13.ToyGraphDBResponse\"\x00\x12\x39\n\x0c\x63reate_graph\x12\x12.ToyGraphDBRequest\x1a\x13.ToyGraphDBResponse\"\x00\x12H\n\x1b\x63\x61ll_functionality_in_graph\x12\x12.ToyGraphDBRequest\x1a\x13.ToyGraphDBResponse\"\x00\x62\x06proto3'
)



_TOYGRAPHDBREQUEST_TYPE_OF_GRAPH = _descriptor.EnumDescriptor(
  name='type_of_graph',
  full_name='ToyGraphDBRequest.type_of_graph',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GRAPH', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DAG', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIRECTED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GRID', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TREE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRIE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNDIRECTED', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=311,
  serialized_end=406,
)
_sym_db.RegisterEnumDescriptor(_TOYGRAPHDBREQUEST_TYPE_OF_GRAPH)

_STATUS_STATUS = _descriptor.EnumDescriptor(
  name='status',
  full_name='status.status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALL_GOOD', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EVERYTHING_IS_FINE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=679,
  serialized_end=725,
)
_sym_db.RegisterEnumDescriptor(_STATUS_STATUS)


_TOYGRAPHDBREQUEST = _descriptor.Descriptor(
  name='ToyGraphDBRequest',
  full_name='ToyGraphDBRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ToyGraphDBRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dag', full_name='ToyGraphDBRequest.dag', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='directed', full_name='ToyGraphDBRequest.directed', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='graph', full_name='ToyGraphDBRequest.graph', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grid', full_name='ToyGraphDBRequest.grid', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tree', full_name='ToyGraphDBRequest.tree', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='trie', full_name='ToyGraphDBRequest.trie', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='undirected', full_name='ToyGraphDBRequest.undirected', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='ToyGraphDBRequest.message', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='database', full_name='ToyGraphDBRequest.database', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='table', full_name='ToyGraphDBRequest.table', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TOYGRAPHDBREQUEST_TYPE_OF_GRAPH,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=406,
)


_DAG = _descriptor.Descriptor(
  name='dag',
  full_name='dag',
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
  serialized_start=94,
  serialized_end=99,
)


_DIRECTED = _descriptor.Descriptor(
  name='directed',
  full_name='directed',
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
  serialized_start=113,
  serialized_end=123,
)


_GRAPH = _descriptor.Descriptor(
  name='graph',
  full_name='graph',
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
  serialized_start=142,
  serialized_end=149,
)


_GRID = _descriptor.Descriptor(
  name='grid',
  full_name='grid',
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
  serialized_start=165,
  serialized_end=171,
)


_TREE = _descriptor.Descriptor(
  name='tree',
  full_name='tree',
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
  serialized_start=186,
  serialized_end=192,
)


_TRIE = _descriptor.Descriptor(
  name='trie',
  full_name='trie',
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
  serialized_start=207,
  serialized_end=213,
)


_UNDIRECTED = _descriptor.Descriptor(
  name='undirected',
  full_name='undirected',
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
  serialized_start=228,
  serialized_end=240,
)


_TOYGRAPHDBRESPONSE = _descriptor.Descriptor(
  name='ToyGraphDBResponse',
  full_name='ToyGraphDBResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ToyGraphDBResponse.status', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='ToyGraphDBResponse.error_message', index=1,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='success_message', full_name='ToyGraphDBResponse.success_message', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=474,
  serialized_end=585,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='Error.code', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='Error.message', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=587,
  serialized_end=625,
)


_SUCCESS = _descriptor.Descriptor(
  name='Success',
  full_name='Success',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='Success.code', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='Success.message', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=627,
  serialized_end=667,
)


_STATUS = _descriptor.Descriptor(
  name='status',
  full_name='status',
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
    _STATUS_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=669,
  serialized_end=725,
)

_TOYGRAPHDBREQUEST.fields_by_name['type'].enum_type = _TOYGRAPHDBREQUEST_TYPE_OF_GRAPH
_TOYGRAPHDBREQUEST.fields_by_name['dag'].message_type = _DAG
_TOYGRAPHDBREQUEST.fields_by_name['directed'].message_type = _DIRECTED
_TOYGRAPHDBREQUEST.fields_by_name['graph'].message_type = _GRAPH
_TOYGRAPHDBREQUEST.fields_by_name['grid'].message_type = _GRID
_TOYGRAPHDBREQUEST.fields_by_name['tree'].message_type = _TREE
_TOYGRAPHDBREQUEST.fields_by_name['trie'].message_type = _TRIE
_TOYGRAPHDBREQUEST.fields_by_name['undirected'].message_type = _UNDIRECTED
_TOYGRAPHDBREQUEST_TYPE_OF_GRAPH.containing_type = _TOYGRAPHDBREQUEST
_TOYGRAPHDBRESPONSE.fields_by_name['status'].message_type = _STATUS
_TOYGRAPHDBRESPONSE.fields_by_name['error_message'].message_type = _ERROR
_TOYGRAPHDBRESPONSE.fields_by_name['success_message'].message_type = _SUCCESS
_STATUS_STATUS.containing_type = _STATUS
DESCRIPTOR.message_types_by_name['ToyGraphDBRequest'] = _TOYGRAPHDBREQUEST
DESCRIPTOR.message_types_by_name['dag'] = _DAG
DESCRIPTOR.message_types_by_name['directed'] = _DIRECTED
DESCRIPTOR.message_types_by_name['graph'] = _GRAPH
DESCRIPTOR.message_types_by_name['grid'] = _GRID
DESCRIPTOR.message_types_by_name['tree'] = _TREE
DESCRIPTOR.message_types_by_name['trie'] = _TRIE
DESCRIPTOR.message_types_by_name['undirected'] = _UNDIRECTED
DESCRIPTOR.message_types_by_name['ToyGraphDBResponse'] = _TOYGRAPHDBRESPONSE
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['Success'] = _SUCCESS
DESCRIPTOR.message_types_by_name['status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ToyGraphDBRequest = _reflection.GeneratedProtocolMessageType('ToyGraphDBRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOYGRAPHDBREQUEST,
  '__module__' : 'query_servicer_pb2'
  # @@protoc_insertion_point(class_scope:ToyGraphDBRequest)
  })
_sym_db.RegisterMessage(ToyGraphDBRequest)

dag = _reflection.GeneratedProtocolMessageType('dag', (_message.Message,), {
  'DESCRIPTOR' : _DAG,
  '__module__' : 'query_servicer_pb2'
  # @@protoc_insertion_point(class_scope:dag)
  })
_sym_db.RegisterMessage(dag)

directed = _reflection.GeneratedProtocolMessageType('directed', (_message.Message,), {
  'DESCRIPTOR' : _DIRECTED,
  '__module__' : 'query_servicer_pb2'
  # @@protoc_insertion_point(class_scope:directed)
  })
_sym_db.RegisterMessage(directed)

graph = _reflection.GeneratedProtocolMessageType('graph', (_message.Message,), {
  'DESCRIPTOR' : _GRAPH,
  '__module__' : 'query_servicer_pb2'
  # @@protoc_insertion_point(class_scope:graph)
  })
_sym_db.RegisterMessage(graph)

grid = _reflection.GeneratedProtocolMessageType('grid', (_message.Message,), {
  'DESCRIPTOR' : _GRID,
  '__module__' : 'query_servicer_pb2'
  # @@protoc_insertion_point(class_scope:grid)
  })
_sym_db.RegisterMessage(grid)

tree = _reflection.GeneratedProtocolMessageType('tree', (_message.Message,), {
  'DESCRIPTOR' : _TREE,
  '__module__' : 'query_servicer_pb2'
  # @@protoc_insertion_point(class_scope:tree)
  })
_sym_db.RegisterMessage(tree)

trie = _reflection.GeneratedProtocolMessageType('trie', (_message.Message,), {
  'DESCRIPTOR' : _TRIE,
  '__module__' : 'query_servicer_pb2'
  # @@protoc_insertion_point(class_scope:trie)
  })
_sym_db.RegisterMessage(trie)

undirected = _reflection.GeneratedProtocolMessageType('undirected', (_message.Message,), {
  'DESCRIPTOR' : _UNDIRECTED,
  '__module__' : 'query_servicer_pb2'
  # @@protoc_insertion_point(class_scope:undirected)
  })
_sym_db.RegisterMessage(undirected)

ToyGraphDBResponse = _reflection.GeneratedProtocolMessageType('ToyGraphDBResponse', (_message.Message,), {
  'DESCRIPTOR' : _TOYGRAPHDBRESPONSE,
  '__module__' : 'query_servicer_pb2'
  # @@protoc_insertion_point(class_scope:ToyGraphDBResponse)
  })
_sym_db.RegisterMessage(ToyGraphDBResponse)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'query_servicer_pb2'
  # @@protoc_insertion_point(class_scope:Error)
  })
_sym_db.RegisterMessage(Error)

Success = _reflection.GeneratedProtocolMessageType('Success', (_message.Message,), {
  'DESCRIPTOR' : _SUCCESS,
  '__module__' : 'query_servicer_pb2'
  # @@protoc_insertion_point(class_scope:Success)
  })
_sym_db.RegisterMessage(Success)

status = _reflection.GeneratedProtocolMessageType('status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'query_servicer_pb2'
  # @@protoc_insertion_point(class_scope:status)
  })
_sym_db.RegisterMessage(status)



_TOYGRAPHDB = _descriptor.ServiceDescriptor(
  name='ToyGraphDB',
  full_name='ToyGraphDB',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=728,
  serialized_end=930,
  methods=[
  _descriptor.MethodDescriptor(
    name='read_graph',
    full_name='ToyGraphDB.read_graph',
    index=0,
    containing_service=None,
    input_type=_TOYGRAPHDBREQUEST,
    output_type=_TOYGRAPHDBRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='create_graph',
    full_name='ToyGraphDB.create_graph',
    index=1,
    containing_service=None,
    input_type=_TOYGRAPHDBREQUEST,
    output_type=_TOYGRAPHDBRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='call_functionality_in_graph',
    full_name='ToyGraphDB.call_functionality_in_graph',
    index=2,
    containing_service=None,
    input_type=_TOYGRAPHDBREQUEST,
    output_type=_TOYGRAPHDBRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TOYGRAPHDB)

DESCRIPTOR.services_by_name['ToyGraphDB'] = _TOYGRAPHDB

# @@protoc_insertion_point(module_scope)
