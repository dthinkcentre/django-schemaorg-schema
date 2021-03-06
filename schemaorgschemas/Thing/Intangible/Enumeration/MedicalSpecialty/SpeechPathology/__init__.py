# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SpeechPathologySchema(SchemaObject):

    """Schema Mixin for SpeechPathology
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Speech pathology.
    """

    def __init__(self):
        self.schema = 'SpeechPathology'


# schema.org version 2.0
