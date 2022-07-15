# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stroeer/curation/v1/core_curation_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from stroeer.core.v1 import article_pb2 as stroeer_dot_core_dot_v1_dot_article__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/stroeer/curation/v1/core_curation_service.proto\x12\x13stroeer.curation.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dstroeer/core/v1/article.proto\" \n\x12GetCurationRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\x8d\x01\n\x13GetCurationResponse\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05label\x18\x02 \x01(\t\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12*\n\x08\x61rticles\x18\x04 \x03(\x0b\x32\x18.stroeer.core.v1.Article\"%\n\x17\x42\x61tchGetCurationRequest\x12\n\n\x02id\x18\x01 \x03(\x03\"W\n\x18\x42\x61tchGetCurationResponse\x12;\n\tcurations\x18\x01 \x03(\x0b\x32(.stroeer.curation.v1.GetCurationResponse2\xe8\x01\n\x0f\x43urationService\x12\x62\n\x0bGetCuration\x12\'.stroeer.curation.v1.GetCurationRequest\x1a(.stroeer.curation.v1.GetCurationResponse\"\x00\x12q\n\x10\x42\x61tchGetCuration\x12,.stroeer.curation.v1.BatchGetCurationRequest\x1a-.stroeer.curation.v1.BatchGetCurationResponse\"\x00\x42H\n\x16\x64\x65.stroeer.curation.v1P\x01Z,github.com/stroeer/go-tapir/curation/v1;coreb\x06proto3')



_GETCURATIONREQUEST = DESCRIPTOR.message_types_by_name['GetCurationRequest']
_GETCURATIONRESPONSE = DESCRIPTOR.message_types_by_name['GetCurationResponse']
_BATCHGETCURATIONREQUEST = DESCRIPTOR.message_types_by_name['BatchGetCurationRequest']
_BATCHGETCURATIONRESPONSE = DESCRIPTOR.message_types_by_name['BatchGetCurationResponse']
GetCurationRequest = _reflection.GeneratedProtocolMessageType('GetCurationRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCURATIONREQUEST,
  '__module__' : 'stroeer.curation.v1.core_curation_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.curation.v1.GetCurationRequest)
  })
_sym_db.RegisterMessage(GetCurationRequest)

GetCurationResponse = _reflection.GeneratedProtocolMessageType('GetCurationResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCURATIONRESPONSE,
  '__module__' : 'stroeer.curation.v1.core_curation_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.curation.v1.GetCurationResponse)
  })
_sym_db.RegisterMessage(GetCurationResponse)

BatchGetCurationRequest = _reflection.GeneratedProtocolMessageType('BatchGetCurationRequest', (_message.Message,), {
  'DESCRIPTOR' : _BATCHGETCURATIONREQUEST,
  '__module__' : 'stroeer.curation.v1.core_curation_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.curation.v1.BatchGetCurationRequest)
  })
_sym_db.RegisterMessage(BatchGetCurationRequest)

BatchGetCurationResponse = _reflection.GeneratedProtocolMessageType('BatchGetCurationResponse', (_message.Message,), {
  'DESCRIPTOR' : _BATCHGETCURATIONRESPONSE,
  '__module__' : 'stroeer.curation.v1.core_curation_service_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.curation.v1.BatchGetCurationResponse)
  })
_sym_db.RegisterMessage(BatchGetCurationResponse)

_CURATIONSERVICE = DESCRIPTOR.services_by_name['CurationService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026de.stroeer.curation.v1P\001Z,github.com/stroeer/go-tapir/curation/v1;core'
  _GETCURATIONREQUEST._serialized_start=136
  _GETCURATIONREQUEST._serialized_end=168
  _GETCURATIONRESPONSE._serialized_start=171
  _GETCURATIONRESPONSE._serialized_end=312
  _BATCHGETCURATIONREQUEST._serialized_start=314
  _BATCHGETCURATIONREQUEST._serialized_end=351
  _BATCHGETCURATIONRESPONSE._serialized_start=353
  _BATCHGETCURATIONRESPONSE._serialized_end=440
  _CURATIONSERVICE._serialized_start=443
  _CURATIONSERVICE._serialized_end=675
# @@protoc_insertion_point(module_scope)
