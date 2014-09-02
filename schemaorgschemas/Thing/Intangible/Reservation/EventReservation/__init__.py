# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Reservation import reservationForProp, totalPriceProp, modifiedTimeProp, priceCurrencyProp, reservationStatusProp, programMembershipUsedProp, bookingAgentProp, reservedTicketProp, providerProp, reservationIdProp, bookingTimeProp, underNameProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EventReservationSchema(SchemaObject):

    """Schema Mixin for EventReservation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A reservation for an event like a concert, sporting event, or lecture.
    """

    def __init__(self):
        self.schema = 'EventReservation'