# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MovieSchema(SchemaObject):

    """Schema Mixin for Movie
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A movie.
    """

    def __init__(self):
        self.schema = 'Movie'


class directorProp(SchemaProperty):

    """
    SchemaField for director
    Usage: Include in SchemaObject SchemaFields as your_django_field = directorProp()  
    schema.org description:A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip. Supersedes directors.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'director'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class trailerProp(SchemaProperty):

    """
    SchemaField for trailer
    Usage: Include in SchemaObject SchemaFields as your_django_field = trailerProp()  
    schema.org description:The trailer of a movie or tv/radio series, season, episode, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference VideoObject"""

    _prop_schema = 'trailer'
    _expected_schema = 'VideoObject'
    _enum = False
    _format_as = "ForeignKey"


class productionCompanyProp(SchemaProperty):

    """
    SchemaField for productionCompany
    Usage: Include in SchemaObject SchemaFields as your_django_field = productionCompanyProp()  
    schema.org description:The production company or studio responsible for the item e.g. series, video game, episode etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'productionCompany'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class durationProp(SchemaProperty):

    """
    SchemaField for duration
    Usage: Include in SchemaObject SchemaFields as your_django_field = durationProp()  
    schema.org description:The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Duration"""

    _prop_schema = 'duration'
    _expected_schema = 'Duration'
    _enum = False
    _format_as = "TimeField"


class subtitleLanguageProp(SchemaProperty):

    """
    SchemaField for subtitleLanguage
    Usage: Include in SchemaObject SchemaFields as your_django_field = subtitleLanguageProp()  
    schema.org description:Languages in which subtitles/captions are available, in IETF BCP 47 standard format.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'subtitleLanguage'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class musicByProp(SchemaProperty):

    """
    SchemaField for musicBy
    Usage: Include in SchemaObject SchemaFields as your_django_field = musicByProp()  
    schema.org description:The composer of the soundtrack.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'musicBy'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class actorProp(SchemaProperty):

    """
    SchemaField for actor
    Usage: Include in SchemaObject SchemaFields as your_django_field = actorProp()  
    schema.org description:An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip. Supersedes actors.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'actor'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
