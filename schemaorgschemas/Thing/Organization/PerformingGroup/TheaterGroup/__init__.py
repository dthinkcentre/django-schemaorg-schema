# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, interactionCountProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, locationProp, employeeProp, emailProp, seeksProp, subOrganizationProp, brandProp, ownsProp, telephoneProp, departmentProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, legalNameProp, vatIDProp, globalLocationNumberProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TheaterGroupSchema(SchemaObject):

    """Schema Mixin for TheaterGroup
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A theater group or company-for example, the Royal Shakespeare Company or Druid Theatre.
    """

    def __init__(self):
        self.schema = 'TheaterGroup'