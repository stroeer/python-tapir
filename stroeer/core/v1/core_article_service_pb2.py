# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stroeer/core/v1/core_article_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stroeer.core.v1 import article_pb2 as stroeer_dot_core_dot_v1_dot_article__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stroeer/core/v1/core_article_service.proto',
  package='stroeer.core.v1',
  syntax='proto3',
  serialized_options=b'\n\022de.stroeer.core.v1P\001Z(github.com/stroeer/go-tapir/core/v1;core',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*stroeer/core/v1/core_article_service.proto\x12\x0fstroeer.core.v1\x1a\x1dstroeer/core/v1/article.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x1f\n\x11GetArticleRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\xa7\x07\n\x13ListArticlesRequest\x12\x39\n\x05query\x18\x01 \x01(\x0b\x32*.stroeer.core.v1.ListArticlesRequest.Query\x12=\n\x07\x66ilters\x18\x02 \x01(\x0b\x32,.stroeer.core.v1.ListArticlesRequest.Filters\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x1a\xfc\x03\n\x05Query\x12\x0c\n\x04path\x18\x01 \x01(\t\x12=\n\x04type\x18\x02 \x01(\x0e\x32/.stroeer.core.v1.ListArticlesRequest.Query.Type\x12\x42\n\x07sort_by\x18\x03 \x01(\x0e\x32\x31.stroeer.core.v1.ListArticlesRequest.Query.SortBy\x12?\n\x05order\x18\x04 \x01(\x0e\x32\x30.stroeer.core.v1.ListArticlesRequest.Query.Order\x12-\n\tfrom_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07to_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"@\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x10\n\x0cHOME_SECTION\x10\x01\x12\x10\n\x0cROOT_SECTION\x10\x02\"D\n\x06SortBy\x12\x17\n\x13SORT_BY_UNSPECIFIED\x10\x00\x12\x0f\n\x0bUPDATE_TIME\x10\x01\x12\x10\n\x0cPUBLISH_TIME\x10\x02\"=\n\x05Order\x12\x15\n\x11ORDER_UNSPECIFIED\x10\x00\x12\r\n\tASCENDING\x10\x01\x12\x0e\n\nDESCENDING\x10\x02\x1a\xef\x01\n\x07\x46ilters\x12\x34\n\rtype_includes\x18\x01 \x03(\x0e\x32\x1d.stroeer.core.v1.Article.Type\x12\x34\n\rtype_excludes\x18\x02 \x03(\x0e\x32\x1d.stroeer.core.v1.Article.Type\x12;\n\x11sub_type_includes\x18\x03 \x03(\x0e\x32 .stroeer.core.v1.Article.SubType\x12;\n\x11sub_type_excludes\x18\x04 \x03(\x0e\x32 .stroeer.core.v1.Article.SubType\"[\n\x14ListArticlesResponse\x12*\n\x08\x61rticles\x18\x01 \x03(\x0b\x32\x18.stroeer.core.v1.Article\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"(\n\x14ListSectionsResponse\x12\x10\n\x08sections\x18\x01 \x03(\t2\x8e\x02\n\x0e\x41rticleService\x12L\n\nGetArticle\x12\".stroeer.core.v1.GetArticleRequest\x1a\x18.stroeer.core.v1.Article\"\x00\x12]\n\x0cListArticles\x12$.stroeer.core.v1.ListArticlesRequest\x1a%.stroeer.core.v1.ListArticlesResponse\"\x00\x12O\n\x0cListSections\x12\x16.google.protobuf.Empty\x1a%.stroeer.core.v1.ListSectionsResponse\"\x00\x42@\n\x12\x64\x65.stroeer.core.v1P\x01Z(github.com/stroeer/go-tapir/core/v1;coreb\x06proto3'
  ,
  dependencies=[stroeer_dot_core_dot_v1_dot_article__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])



_LISTARTICLESREQUEST_QUERY_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='stroeer.core.v1.ListArticlesRequest.Query.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HOME_SECTION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROOT_SECTION', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=686,
  serialized_end=750,
)
_sym_db.RegisterEnumDescriptor(_LISTARTICLESREQUEST_QUERY_TYPE)

_LISTARTICLESREQUEST_QUERY_SORTBY = _descriptor.EnumDescriptor(
  name='SortBy',
  full_name='stroeer.core.v1.ListArticlesRequest.Query.SortBy',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SORT_BY_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UPDATE_TIME', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUBLISH_TIME', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=752,
  serialized_end=820,
)
_sym_db.RegisterEnumDescriptor(_LISTARTICLESREQUEST_QUERY_SORTBY)

_LISTARTICLESREQUEST_QUERY_ORDER = _descriptor.EnumDescriptor(
  name='Order',
  full_name='stroeer.core.v1.ListArticlesRequest.Query.Order',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ORDER_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ASCENDING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DESCENDING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=822,
  serialized_end=883,
)
_sym_db.RegisterEnumDescriptor(_LISTARTICLESREQUEST_QUERY_ORDER)


_GETARTICLEREQUEST = _descriptor.Descriptor(
  name='GetArticleRequest',
  full_name='stroeer.core.v1.GetArticleRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='stroeer.core.v1.GetArticleRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=156,
  serialized_end=187,
)


_LISTARTICLESREQUEST_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='stroeer.core.v1.ListArticlesRequest.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='stroeer.core.v1.ListArticlesRequest.Query.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='stroeer.core.v1.ListArticlesRequest.Query.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sort_by', full_name='stroeer.core.v1.ListArticlesRequest.Query.sort_by', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='order', full_name='stroeer.core.v1.ListArticlesRequest.Query.order', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='from_time', full_name='stroeer.core.v1.ListArticlesRequest.Query.from_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_time', full_name='stroeer.core.v1.ListArticlesRequest.Query.to_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LISTARTICLESREQUEST_QUERY_TYPE,
    _LISTARTICLESREQUEST_QUERY_SORTBY,
    _LISTARTICLESREQUEST_QUERY_ORDER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=375,
  serialized_end=883,
)

_LISTARTICLESREQUEST_FILTERS = _descriptor.Descriptor(
  name='Filters',
  full_name='stroeer.core.v1.ListArticlesRequest.Filters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_includes', full_name='stroeer.core.v1.ListArticlesRequest.Filters.type_includes', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type_excludes', full_name='stroeer.core.v1.ListArticlesRequest.Filters.type_excludes', index=1,
      number=2, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sub_type_includes', full_name='stroeer.core.v1.ListArticlesRequest.Filters.sub_type_includes', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sub_type_excludes', full_name='stroeer.core.v1.ListArticlesRequest.Filters.sub_type_excludes', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=886,
  serialized_end=1125,
)

_LISTARTICLESREQUEST = _descriptor.Descriptor(
  name='ListArticlesRequest',
  full_name='stroeer.core.v1.ListArticlesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='stroeer.core.v1.ListArticlesRequest.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filters', full_name='stroeer.core.v1.ListArticlesRequest.filters', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='stroeer.core.v1.ListArticlesRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page_token', full_name='stroeer.core.v1.ListArticlesRequest.page_token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LISTARTICLESREQUEST_QUERY, _LISTARTICLESREQUEST_FILTERS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=1125,
)


_LISTARTICLESRESPONSE = _descriptor.Descriptor(
  name='ListArticlesResponse',
  full_name='stroeer.core.v1.ListArticlesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='articles', full_name='stroeer.core.v1.ListArticlesResponse.articles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_page_token', full_name='stroeer.core.v1.ListArticlesResponse.next_page_token', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1127,
  serialized_end=1218,
)


_LISTSECTIONSRESPONSE = _descriptor.Descriptor(
  name='ListSectionsResponse',
  full_name='stroeer.core.v1.ListSectionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sections', full_name='stroeer.core.v1.ListSectionsResponse.sections', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1220,
  serialized_end=1260,
)

_LISTARTICLESREQUEST_QUERY.fields_by_name['type'].enum_type = _LISTARTICLESREQUEST_QUERY_TYPE
_LISTARTICLESREQUEST_QUERY.fields_by_name['sort_by'].enum_type = _LISTARTICLESREQUEST_QUERY_SORTBY
_LISTARTICLESREQUEST_QUERY.fields_by_name['order'].enum_type = _LISTARTICLESREQUEST_QUERY_ORDER
_LISTARTICLESREQUEST_QUERY.fields_by_name['from_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTARTICLESREQUEST_QUERY.fields_by_name['to_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_LISTARTICLESREQUEST_QUERY.containing_type = _LISTARTICLESREQUEST
_LISTARTICLESREQUEST_QUERY_TYPE.containing_type = _LISTARTICLESREQUEST_QUERY
_LISTARTICLESREQUEST_QUERY_SORTBY.containing_type = _LISTARTICLESREQUEST_QUERY
_LISTARTICLESREQUEST_QUERY_ORDER.containing_type = _LISTARTICLESREQUEST_QUERY
_LISTARTICLESREQUEST_FILTERS.fields_by_name['type_includes'].enum_type = stroeer_dot_core_dot_v1_dot_article__pb2._ARTICLE_TYPE
_LISTARTICLESREQUEST_FILTERS.fields_by_name['type_excludes'].enum_type = stroeer_dot_core_dot_v1_dot_article__pb2._ARTICLE_TYPE
_LISTARTICLESREQUEST_FILTERS.fields_by_name['sub_type_includes'].enum_type = stroeer_dot_core_dot_v1_dot_article__pb2._ARTICLE_SUBTYPE
_LISTARTICLESREQUEST_FILTERS.fields_by_name['sub_type_excludes'].enum_type = stroeer_dot_core_dot_v1_dot_article__pb2._ARTICLE_SUBTYPE
_LISTARTICLESREQUEST_FILTERS.containing_type = _LISTARTICLESREQUEST
_LISTARTICLESREQUEST.fields_by_name['query'].message_type = _LISTARTICLESREQUEST_QUERY
_LISTARTICLESREQUEST.fields_by_name['filters'].message_type = _LISTARTICLESREQUEST_FILTERS
_LISTARTICLESRESPONSE.fields_by_name['articles'].message_type = stroeer_dot_core_dot_v1_dot_article__pb2._ARTICLE
DESCRIPTOR.message_types_by_name['GetArticleRequest'] = _GETARTICLEREQUEST
DESCRIPTOR.message_types_by_name['ListArticlesRequest'] = _LISTARTICLESREQUEST
DESCRIPTOR.message_types_by_name['ListArticlesResponse'] = _LISTARTICLESRESPONSE
DESCRIPTOR.message_types_by_name['ListSectionsResponse'] = _LISTSECTIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetArticleRequest = _reflection.GeneratedProtocolMessageType('GetArticleRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETARTICLEREQUEST,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.GetArticleRequest)
  })
_sym_db.RegisterMessage(GetArticleRequest)

ListArticlesRequest = _reflection.GeneratedProtocolMessageType('ListArticlesRequest', (_message.Message,), {

  'Query' : _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
    'DESCRIPTOR' : _LISTARTICLESREQUEST_QUERY,
    '__module__' : 'stroeer.core.v1.core_article_service_pb2'
    # @@protoc_insertion_point(class_scope:stroeer.core.v1.ListArticlesRequest.Query)
    })
  ,

  'Filters' : _reflection.GeneratedProtocolMessageType('Filters', (_message.Message,), {
    'DESCRIPTOR' : _LISTARTICLESREQUEST_FILTERS,
    '__module__' : 'stroeer.core.v1.core_article_service_pb2'
    # @@protoc_insertion_point(class_scope:stroeer.core.v1.ListArticlesRequest.Filters)
    })
  ,
  'DESCRIPTOR' : _LISTARTICLESREQUEST,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.ListArticlesRequest)
  })
_sym_db.RegisterMessage(ListArticlesRequest)
_sym_db.RegisterMessage(ListArticlesRequest.Query)
_sym_db.RegisterMessage(ListArticlesRequest.Filters)

ListArticlesResponse = _reflection.GeneratedProtocolMessageType('ListArticlesResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTARTICLESRESPONSE,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.ListArticlesResponse)
  })
_sym_db.RegisterMessage(ListArticlesResponse)

ListSectionsResponse = _reflection.GeneratedProtocolMessageType('ListSectionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTSECTIONSRESPONSE,
  '__module__' : 'stroeer.core.v1.core_article_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.core.v1.ListSectionsResponse)
  })
_sym_db.RegisterMessage(ListSectionsResponse)


DESCRIPTOR._options = None

_ARTICLESERVICE = _descriptor.ServiceDescriptor(
  name='ArticleService',
  full_name='stroeer.core.v1.ArticleService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1263,
  serialized_end=1533,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetArticle',
    full_name='stroeer.core.v1.ArticleService.GetArticle',
    index=0,
    containing_service=None,
    input_type=_GETARTICLEREQUEST,
    output_type=stroeer_dot_core_dot_v1_dot_article__pb2._ARTICLE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListArticles',
    full_name='stroeer.core.v1.ArticleService.ListArticles',
    index=1,
    containing_service=None,
    input_type=_LISTARTICLESREQUEST,
    output_type=_LISTARTICLESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListSections',
    full_name='stroeer.core.v1.ArticleService.ListSections',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_LISTSECTIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ARTICLESERVICE)

DESCRIPTOR.services_by_name['ArticleService'] = _ARTICLESERVICE

# @@protoc_insertion_point(module_scope)
