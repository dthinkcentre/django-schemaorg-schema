# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing.Action.ConsumeAction import expectsAcceptanceOfProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class WearActionSchema(SchemaObject):

    """Schema Mixin for WearAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of dressing oneself in clothing.
    """

    def __init__(self):
        self.schema = 'WearAction'


# schema.org version 2.0
