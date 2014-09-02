# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Place import isicV4Prop, mapProp, openingHoursSpecificationProp, photoProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, telephoneProp, addressProp, interactionCountProp, logoProp, geoProp, eventProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GatedResidenceCommunitySchema(SchemaObject):

    """Schema Mixin for GatedResidenceCommunity
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Residence type: Gated community.
    """

    def __init__(self):
        self.schema = 'GatedResidenceCommunity'