# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stroeer/page/section/v1/section_page.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from stroeer.core.v1 import shared_pb2 as stroeer_dot_core_dot_v1_dot_shared__pb2
from stroeer.page.stage.v1 import stage_pb2 as stroeer_dot_page_dot_stage_dot_v1_dot_stage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*stroeer/page/section/v1/section_page.proto\x12\x17stroeer.page.section.v1\x1a\x1cstroeer/core/v1/shared.proto\x1a!stroeer/page/stage/v1/stage.proto\"\xb1\x02\n\x0bSectionPage\x12=\n\x07section\x18\x01 \x01(\x0b\x32,.stroeer.page.section.v1.SectionPage.Section\x12,\n\x06stages\x18\x02 \x03(\x0b\x32\x1c.stroeer.page.stage.v1.Stage\x1a\xb4\x01\n\x07Section\x12H\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x38.stroeer.page.section.v1.SectionPage.Section.FieldsEntry\x12\x30\n\x0csection_tree\x18\x02 \x01(\x0b\x32\x1a.stroeer.core.v1.Reference\x1a-\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42S\n\x1a\x64\x65.stroeer.page.section.v1P\x01Z3github.com/stroeer/go-tapir/page/section/v1;sectionb\x06proto3')



_SECTIONPAGE = DESCRIPTOR.message_types_by_name['SectionPage']
_SECTIONPAGE_SECTION = _SECTIONPAGE.nested_types_by_name['Section']
_SECTIONPAGE_SECTION_FIELDSENTRY = _SECTIONPAGE_SECTION.nested_types_by_name['FieldsEntry']
SectionPage = _reflection.GeneratedProtocolMessageType('SectionPage', (_message.Message,), {

  'Section' : _reflection.GeneratedProtocolMessageType('Section', (_message.Message,), {

    'FieldsEntry' : _reflection.GeneratedProtocolMessageType('FieldsEntry', (_message.Message,), {
      'DESCRIPTOR' : _SECTIONPAGE_SECTION_FIELDSENTRY,
      '__module__' : 'stroeer.page.section.v1.section_page_pb2'
      # @@protoc_insertion_point(class_scope:stroeer.page.section.v1.SectionPage.Section.FieldsEntry)
      })
    ,
    'DESCRIPTOR' : _SECTIONPAGE_SECTION,
    '__module__' : 'stroeer.page.section.v1.section_page_pb2'
    # @@protoc_insertion_point(class_scope:stroeer.page.section.v1.SectionPage.Section)
    })
  ,
  'DESCRIPTOR' : _SECTIONPAGE,
  '__module__' : 'stroeer.page.section.v1.section_page_pb2'
  # @@protoc_insertion_point(class_scope:stroeer.page.section.v1.SectionPage)
  })
_sym_db.RegisterMessage(SectionPage)
_sym_db.RegisterMessage(SectionPage.Section)
_sym_db.RegisterMessage(SectionPage.Section.FieldsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032de.stroeer.page.section.v1P\001Z3github.com/stroeer/go-tapir/page/section/v1;section'
  _SECTIONPAGE_SECTION_FIELDSENTRY._options = None
  _SECTIONPAGE_SECTION_FIELDSENTRY._serialized_options = b'8\001'
  _SECTIONPAGE._serialized_start=137
  _SECTIONPAGE._serialized_end=442
  _SECTIONPAGE_SECTION._serialized_start=262
  _SECTIONPAGE_SECTION._serialized_end=442
  _SECTIONPAGE_SECTION_FIELDSENTRY._serialized_start=397
  _SECTIONPAGE_SECTION_FIELDSENTRY._serialized_end=442
# @@protoc_insertion_point(module_scope)
