# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork.MediaObject import contentUrlProp, uploadDateProp, playerTypeProp, encodesCreativeWorkProp, productionCompanyProp, expiresProp, interactionCountProp, heightProp, encodingFormatProp, associatedArticleProp, offersProp, publicationProp, durationProp, requiresSubscriptionProp, embedUrlProp, regionsAllowedProp, bitrateProp, widthProp, contentSizeProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MusicVideoObjectSchema(SchemaObject):

    """Schema Mixin for MusicVideoObject
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A music video file.
    """

    def __init__(self):
        self.schema = 'MusicVideoObject'