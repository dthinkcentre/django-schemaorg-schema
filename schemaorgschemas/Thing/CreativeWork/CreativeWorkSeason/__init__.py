# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CreativeWorkSeasonSchema(SchemaObject):

    """Schema Mixin for CreativeWorkSeason
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A media season e.g. tv, radio, video game etc.
    """

    def __init__(self):
        self.schema = 'CreativeWorkSeason'


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


class startDateProp(SchemaProperty):

    """
    SchemaField for startDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = startDateProp()  
    schema.org description:The start date and time of the item (in ISO 8601 date format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'startDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class episodeProp(SchemaProperty):

    """
    SchemaField for episode
    Usage: Include in SchemaObject SchemaFields as your_django_field = episodeProp()  
    schema.org description:An episode of a tv, radio or game media within a series or season. Supersedes episodes.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Episode"""

    _prop_schema = 'episode'
    _expected_schema = 'Episode'
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


class numberOfEpisodesProp(SchemaProperty):

    """
    SchemaField for numberOfEpisodes
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfEpisodesProp()  
    schema.org description:The number of episodes in this season or series.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'numberOfEpisodes'
    _expected_schema = 'Integer'
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


class endDateProp(SchemaProperty):

    """
    SchemaField for endDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = endDateProp()  
    schema.org description:The end date and time of the item (in ISO 8601 date format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'endDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class partOfSeriesProp(SchemaProperty):

    """
    SchemaField for partOfSeries
    Usage: Include in SchemaObject SchemaFields as your_django_field = partOfSeriesProp()  
    schema.org description:The series to which this episode or season belongs. Supersedes partOfTVSeries.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference CreativeWorkSeries"""

    _prop_schema = 'partOfSeries'
    _expected_schema = 'CreativeWorkSeries'
    _enum = False
    _format_as = "ForeignKey"


class seasonNumberProp(SchemaProperty):

    """
    SchemaField for seasonNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = seasonNumberProp()  
    schema.org description:Position of the season within an ordered group of seasons.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'seasonNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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
