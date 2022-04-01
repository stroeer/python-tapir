# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stroeer/page/article/v1/article_page_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stroeer.page.article.v1 import article_page_pb2 as stroeer_dot_page_dot_article_dot_v1_dot_article__page__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stroeer/page/article/v1/article_page_service.proto',
  package='stroeer.page.article.v1',
  syntax='proto3',
  serialized_options=b'\n\032de.stroeer.page.article.v1P\001Z3github.com/stroeer/go-tapir/page/article/v1;article',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2stroeer/page/article/v1/article_page_service.proto\x12\x17stroeer.page.article.v1\x1a*stroeer/page/article/v1/article_page.proto\"#\n\x15GetArticlePageRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"T\n\x16GetArticlePageResponse\x12:\n\x0c\x61rticle_page\x18\x01 \x01(\x0b\x32$.stroeer.page.article.v1.ArticlePage2\x89\x01\n\x12\x41rticlePageService\x12s\n\x0eGetArticlePage\x12..stroeer.page.article.v1.GetArticlePageRequest\x1a/.stroeer.page.article.v1.GetArticlePageResponse\"\x00\x42S\n\x1a\x64\x65.stroeer.page.article.v1P\x01Z3github.com/stroeer/go-tapir/page/article/v1;articleb\x06proto3'
  ,
  dependencies=[stroeer_dot_page_dot_article_dot_v1_dot_article__page__pb2.DESCRIPTOR,])




_GETARTICLEPAGEREQUEST = _descriptor.Descriptor(
  name='GetArticlePageRequest',
  full_name='stroeer.page.article.v1.GetArticlePageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='stroeer.page.article.v1.GetArticlePageRequest.id', index=0,
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
  serialized_start=123,
  serialized_end=158,
)


_GETARTICLEPAGERESPONSE = _descriptor.Descriptor(
  name='GetArticlePageResponse',
  full_name='stroeer.page.article.v1.GetArticlePageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='article_page', full_name='stroeer.page.article.v1.GetArticlePageResponse.article_page', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=160,
  serialized_end=244,
)

_GETARTICLEPAGERESPONSE.fields_by_name['article_page'].message_type = stroeer_dot_page_dot_article_dot_v1_dot_article__page__pb2._ARTICLEPAGE
DESCRIPTOR.message_types_by_name['GetArticlePageRequest'] = _GETARTICLEPAGEREQUEST
DESCRIPTOR.message_types_by_name['GetArticlePageResponse'] = _GETARTICLEPAGERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetArticlePageRequest = _reflection.GeneratedProtocolMessageType('GetArticlePageRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETARTICLEPAGEREQUEST,
  '__module__' : 'stroeer.page.article.v1.article_page_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.page.article.v1.GetArticlePageRequest)
  })
_sym_db.RegisterMessage(GetArticlePageRequest)

GetArticlePageResponse = _reflection.GeneratedProtocolMessageType('GetArticlePageResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETARTICLEPAGERESPONSE,
  '__module__' : 'stroeer.page.article.v1.article_page_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.page.article.v1.GetArticlePageResponse)
  })
_sym_db.RegisterMessage(GetArticlePageResponse)


DESCRIPTOR._options = None

_ARTICLEPAGESERVICE = _descriptor.ServiceDescriptor(
  name='ArticlePageService',
  full_name='stroeer.page.article.v1.ArticlePageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=247,
  serialized_end=384,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetArticlePage',
    full_name='stroeer.page.article.v1.ArticlePageService.GetArticlePage',
    index=0,
    containing_service=None,
    input_type=_GETARTICLEPAGEREQUEST,
    output_type=_GETARTICLEPAGERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ARTICLEPAGESERVICE)

DESCRIPTOR.services_by_name['ArticlePageService'] = _ARTICLEPAGESERVICE

# @@protoc_insertion_point(module_scope)
