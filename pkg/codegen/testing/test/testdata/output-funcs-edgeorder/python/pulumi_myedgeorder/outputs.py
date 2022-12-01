# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from typing_extensions import NotRequired, Required, TypedDict
from . import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'AvailabilityInformationResponse',
    'BillingMeterDetailsResponse',
    'ConfigurationResponse',
    'CostInformationResponse',
    'DescriptionResponse',
    'DimensionsResponse',
    'FilterablePropertyResponse',
    'HierarchyInformationResponse',
    'ImageInformationResponse',
    'LinkResponse',
    'Pav2MeterDetailsResponse',
    'ProductFamilyResponse',
    'ProductLineResponse',
    'ProductResponse',
    'PurchaseMeterDetailsResponse',
    'SpecificationResponse',
]

@pulumi.output_type
class AvailabilityInformationResponse(dict):
    """
    Availability information of a product system.
    """
    def __init__(__self__, *,
                 availability_stage: str,
                 disabled_reason: str,
                 disabled_reason_message: str):
        """
        Availability information of a product system.
        :param str availability_stage: Current availability stage of the product. Availability stage
        :param str disabled_reason: Reason why the product is disabled.
        :param str disabled_reason_message: Message for why the product is disabled.
        """
        pulumi.set(__self__, "availability_stage", availability_stage)
        pulumi.set(__self__, "disabled_reason", disabled_reason)
        pulumi.set(__self__, "disabled_reason_message", disabled_reason_message)

    @property
    @pulumi.getter(name="availabilityStage")
    def availability_stage(self) -> str:
        """
        Current availability stage of the product. Availability stage
        """
        return pulumi.get(self, "availability_stage")

    @property
    @pulumi.getter(name="disabledReason")
    def disabled_reason(self) -> str:
        """
        Reason why the product is disabled.
        """
        return pulumi.get(self, "disabled_reason")

    @property
    @pulumi.getter(name="disabledReasonMessage")
    def disabled_reason_message(self) -> str:
        """
        Message for why the product is disabled.
        """
        return pulumi.get(self, "disabled_reason_message")


@pulumi.output_type
class BillingMeterDetailsResponse(dict):
    """
    Holds billing meter details for each type of billing
    """
    def __init__(__self__, *,
                 frequency: str,
                 meter_details: Any,
                 metering_type: str,
                 name: str):
        """
        Holds billing meter details for each type of billing
        :param str frequency: Frequency of recurrence
        :param Union['Pav2MeterDetailsResponse', 'PurchaseMeterDetailsResponse'] meter_details: Represents MeterDetails
        :param str metering_type: Represents Metering type (eg one-time or recurrent)
        :param str name: Represents Billing type name
        """
        pulumi.set(__self__, "frequency", frequency)
        pulumi.set(__self__, "meter_details", meter_details)
        pulumi.set(__self__, "metering_type", metering_type)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def frequency(self) -> str:
        """
        Frequency of recurrence
        """
        return pulumi.get(self, "frequency")

    @property
    @pulumi.getter(name="meterDetails")
    def meter_details(self) -> Any:
        """
        Represents MeterDetails
        """
        return pulumi.get(self, "meter_details")

    @property
    @pulumi.getter(name="meteringType")
    def metering_type(self) -> str:
        """
        Represents Metering type (eg one-time or recurrent)
        """
        return pulumi.get(self, "metering_type")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Represents Billing type name
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class ConfigurationResponse(dict):
    """
    Configuration object.
    """
    def __init__(__self__, *,
                 availability_information: 'outputs.AvailabilityInformationResponse',
                 cost_information: 'outputs.CostInformationResponse',
                 description: 'outputs.DescriptionResponse',
                 dimensions: 'outputs.DimensionsResponse',
                 display_name: str,
                 filterable_properties: Sequence['outputs.FilterablePropertyResponse'],
                 hierarchy_information: 'outputs.HierarchyInformationResponse',
                 image_information: Sequence['outputs.ImageInformationResponse'],
                 specifications: Sequence['outputs.SpecificationResponse']):
        """
        Configuration object.
        :param 'AvailabilityInformationResponse' availability_information: Availability information of the product system.
        :param 'CostInformationResponse' cost_information: Cost information for the product system.
        :param 'DescriptionResponse' description: Description related to the product system.
        :param 'DimensionsResponse' dimensions: Dimensions of the configuration
        :param str display_name: Display Name for the product system.
        :param Sequence['FilterablePropertyResponse'] filterable_properties: list of filters supported for a product
        :param 'HierarchyInformationResponse' hierarchy_information: Hierarchy information of a product.
        :param Sequence['ImageInformationResponse'] image_information: Image information for the product system.
        :param Sequence['SpecificationResponse'] specifications: Specifications of the configuration
        """
        pulumi.set(__self__, "availability_information", availability_information)
        pulumi.set(__self__, "cost_information", cost_information)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "dimensions", dimensions)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "filterable_properties", filterable_properties)
        pulumi.set(__self__, "hierarchy_information", hierarchy_information)
        pulumi.set(__self__, "image_information", image_information)
        pulumi.set(__self__, "specifications", specifications)

    @property
    @pulumi.getter(name="availabilityInformation")
    def availability_information(self) -> 'outputs.AvailabilityInformationResponse':
        """
        Availability information of the product system.
        """
        return pulumi.get(self, "availability_information")

    @property
    @pulumi.getter(name="costInformation")
    def cost_information(self) -> 'outputs.CostInformationResponse':
        """
        Cost information for the product system.
        """
        return pulumi.get(self, "cost_information")

    @property
    @pulumi.getter
    def description(self) -> 'outputs.DescriptionResponse':
        """
        Description related to the product system.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def dimensions(self) -> 'outputs.DimensionsResponse':
        """
        Dimensions of the configuration
        """
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display Name for the product system.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="filterableProperties")
    def filterable_properties(self) -> Sequence['outputs.FilterablePropertyResponse']:
        """
        list of filters supported for a product
        """
        return pulumi.get(self, "filterable_properties")

    @property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> 'outputs.HierarchyInformationResponse':
        """
        Hierarchy information of a product.
        """
        return pulumi.get(self, "hierarchy_information")

    @property
    @pulumi.getter(name="imageInformation")
    def image_information(self) -> Sequence['outputs.ImageInformationResponse']:
        """
        Image information for the product system.
        """
        return pulumi.get(self, "image_information")

    @property
    @pulumi.getter
    def specifications(self) -> Sequence['outputs.SpecificationResponse']:
        """
        Specifications of the configuration
        """
        return pulumi.get(self, "specifications")


@pulumi.output_type
class CostInformationResponse(dict):
    """
    Cost information for the product system
    """
    def __init__(__self__, *,
                 billing_info_url: str,
                 billing_meter_details: Sequence['outputs.BillingMeterDetailsResponse']):
        """
        Cost information for the product system
        :param str billing_info_url: Default url to display billing information
        :param Sequence['BillingMeterDetailsResponse'] billing_meter_details: Details on the various billing aspects for the product system.
        """
        pulumi.set(__self__, "billing_info_url", billing_info_url)
        pulumi.set(__self__, "billing_meter_details", billing_meter_details)

    @property
    @pulumi.getter(name="billingInfoUrl")
    def billing_info_url(self) -> str:
        """
        Default url to display billing information
        """
        return pulumi.get(self, "billing_info_url")

    @property
    @pulumi.getter(name="billingMeterDetails")
    def billing_meter_details(self) -> Sequence['outputs.BillingMeterDetailsResponse']:
        """
        Details on the various billing aspects for the product system.
        """
        return pulumi.get(self, "billing_meter_details")


@pulumi.output_type
class DescriptionResponse(dict):
    """
    Description related properties of a product system.
    """
    def __init__(__self__, *,
                 attributes: Sequence[str],
                 description_type: str,
                 keywords: Sequence[str],
                 links: Sequence['outputs.LinkResponse'],
                 long_description: str,
                 short_description: str):
        """
        Description related properties of a product system.
        :param Sequence[str] attributes: Attributes for the product system.
        :param str description_type: Type of description.
        :param Sequence[str] keywords: Keywords for the product system.
        :param Sequence['LinkResponse'] links: Links for the product system.
        :param str long_description: Long description of the product system.
        :param str short_description: Short description of the product system.
        """
        pulumi.set(__self__, "attributes", attributes)
        pulumi.set(__self__, "description_type", description_type)
        pulumi.set(__self__, "keywords", keywords)
        pulumi.set(__self__, "links", links)
        pulumi.set(__self__, "long_description", long_description)
        pulumi.set(__self__, "short_description", short_description)

    @property
    @pulumi.getter
    def attributes(self) -> Sequence[str]:
        """
        Attributes for the product system.
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="descriptionType")
    def description_type(self) -> str:
        """
        Type of description.
        """
        return pulumi.get(self, "description_type")

    @property
    @pulumi.getter
    def keywords(self) -> Sequence[str]:
        """
        Keywords for the product system.
        """
        return pulumi.get(self, "keywords")

    @property
    @pulumi.getter
    def links(self) -> Sequence['outputs.LinkResponse']:
        """
        Links for the product system.
        """
        return pulumi.get(self, "links")

    @property
    @pulumi.getter(name="longDescription")
    def long_description(self) -> str:
        """
        Long description of the product system.
        """
        return pulumi.get(self, "long_description")

    @property
    @pulumi.getter(name="shortDescription")
    def short_description(self) -> str:
        """
        Short description of the product system.
        """
        return pulumi.get(self, "short_description")


@pulumi.output_type
class DimensionsResponse(dict):
    """
    Dimensions of a configuration.
    """
    def __init__(__self__, *,
                 depth: float,
                 height: float,
                 length: float,
                 length_height_unit: str,
                 weight: float,
                 weight_unit: str,
                 width: float):
        """
        Dimensions of a configuration.
        :param float depth: Depth of the device.
        :param float height: Height of the device.
        :param float length: Length of the device.
        :param str length_height_unit: Unit for the dimensions of length, height and width.
        :param float weight: Weight of the device.
        :param str weight_unit: Unit for the dimensions of weight.
        :param float width: Width of the device.
        """
        pulumi.set(__self__, "depth", depth)
        pulumi.set(__self__, "height", height)
        pulumi.set(__self__, "length", length)
        pulumi.set(__self__, "length_height_unit", length_height_unit)
        pulumi.set(__self__, "weight", weight)
        pulumi.set(__self__, "weight_unit", weight_unit)
        pulumi.set(__self__, "width", width)

    @property
    @pulumi.getter
    def depth(self) -> float:
        """
        Depth of the device.
        """
        return pulumi.get(self, "depth")

    @property
    @pulumi.getter
    def height(self) -> float:
        """
        Height of the device.
        """
        return pulumi.get(self, "height")

    @property
    @pulumi.getter
    def length(self) -> float:
        """
        Length of the device.
        """
        return pulumi.get(self, "length")

    @property
    @pulumi.getter(name="lengthHeightUnit")
    def length_height_unit(self) -> str:
        """
        Unit for the dimensions of length, height and width.
        """
        return pulumi.get(self, "length_height_unit")

    @property
    @pulumi.getter
    def weight(self) -> float:
        """
        Weight of the device.
        """
        return pulumi.get(self, "weight")

    @property
    @pulumi.getter(name="weightUnit")
    def weight_unit(self) -> str:
        """
        Unit for the dimensions of weight.
        """
        return pulumi.get(self, "weight_unit")

    @property
    @pulumi.getter
    def width(self) -> float:
        """
        Width of the device.
        """
        return pulumi.get(self, "width")


@pulumi.output_type
class FilterablePropertyResponse(dict):
    """
    Different types of filters supported and its values.
    """
    def __init__(__self__, *,
                 supported_values: Sequence[str],
                 type: str):
        """
        Different types of filters supported and its values.
        :param Sequence[str] supported_values: Values to be filtered.
        :param str type: Type of product filter.
        """
        pulumi.set(__self__, "supported_values", supported_values)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="supportedValues")
    def supported_values(self) -> Sequence[str]:
        """
        Values to be filtered.
        """
        return pulumi.get(self, "supported_values")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of product filter.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class HierarchyInformationResponse(dict):
    """
    Holds details about product hierarchy information
    """
    def __init__(__self__, *,
                 configuration_name: Optional[str] = None,
                 product_family_name: Optional[str] = None,
                 product_line_name: Optional[str] = None,
                 product_name: Optional[str] = None):
        """
        Holds details about product hierarchy information
        :param str configuration_name: Represents configuration name that uniquely identifies configuration
        :param str product_family_name: Represents product family name that uniquely identifies product family
        :param str product_line_name: Represents product line name that uniquely identifies product line
        :param str product_name: Represents product name that uniquely identifies product
        """
        if configuration_name is not None:
            pulumi.set(__self__, "configuration_name", configuration_name)
        if product_family_name is not None:
            pulumi.set(__self__, "product_family_name", product_family_name)
        if product_line_name is not None:
            pulumi.set(__self__, "product_line_name", product_line_name)
        if product_name is not None:
            pulumi.set(__self__, "product_name", product_name)

    @property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[str]:
        """
        Represents configuration name that uniquely identifies configuration
        """
        return pulumi.get(self, "configuration_name")

    @property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[str]:
        """
        Represents product family name that uniquely identifies product family
        """
        return pulumi.get(self, "product_family_name")

    @property
    @pulumi.getter(name="productLineName")
    def product_line_name(self) -> Optional[str]:
        """
        Represents product line name that uniquely identifies product line
        """
        return pulumi.get(self, "product_line_name")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[str]:
        """
        Represents product name that uniquely identifies product
        """
        return pulumi.get(self, "product_name")


@pulumi.output_type
class ImageInformationResponse(dict):
    """
    Image for the product
    """
    def __init__(__self__, *,
                 image_type: str,
                 image_url: str):
        """
        Image for the product
        :param str image_type: Type of the image
        :param str image_url: Url of the image
        """
        pulumi.set(__self__, "image_type", image_type)
        pulumi.set(__self__, "image_url", image_url)

    @property
    @pulumi.getter(name="imageType")
    def image_type(self) -> str:
        """
        Type of the image
        """
        return pulumi.get(self, "image_type")

    @property
    @pulumi.getter(name="imageUrl")
    def image_url(self) -> str:
        """
        Url of the image
        """
        return pulumi.get(self, "image_url")


@pulumi.output_type
class LinkResponse(dict):
    """
    Returns link related to the product
    """
    def __init__(__self__, *,
                 link_type: str,
                 link_url: str):
        """
        Returns link related to the product
        :param str link_type: Type of link
        :param str link_url: Url of the link
        """
        pulumi.set(__self__, "link_type", link_type)
        pulumi.set(__self__, "link_url", link_url)

    @property
    @pulumi.getter(name="linkType")
    def link_type(self) -> str:
        """
        Type of link
        """
        return pulumi.get(self, "link_type")

    @property
    @pulumi.getter(name="linkUrl")
    def link_url(self) -> str:
        """
        Url of the link
        """
        return pulumi.get(self, "link_url")


@pulumi.output_type
class Pav2MeterDetailsResponse(dict):
    """
    Billing type PAV2 meter details
    """
    def __init__(__self__, *,
                 billing_type: str,
                 charging_type: str,
                 meter_guid: str,
                 multiplier: float):
        """
        Billing type PAV2 meter details
        :param str billing_type: Represents billing type.
               Expected value is 'Pav2'.
        :param str charging_type: Charging type.
        :param str meter_guid: Validation status of requested data center and transport.
        :param float multiplier: Billing unit applicable for Pav2 billing
        """
        pulumi.set(__self__, "billing_type", 'Pav2')
        pulumi.set(__self__, "charging_type", charging_type)
        pulumi.set(__self__, "meter_guid", meter_guid)
        pulumi.set(__self__, "multiplier", multiplier)

    @property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> str:
        """
        Represents billing type.
        Expected value is 'Pav2'.
        """
        return pulumi.get(self, "billing_type")

    @property
    @pulumi.getter(name="chargingType")
    def charging_type(self) -> str:
        """
        Charging type.
        """
        return pulumi.get(self, "charging_type")

    @property
    @pulumi.getter(name="meterGuid")
    def meter_guid(self) -> str:
        """
        Validation status of requested data center and transport.
        """
        return pulumi.get(self, "meter_guid")

    @property
    @pulumi.getter
    def multiplier(self) -> float:
        """
        Billing unit applicable for Pav2 billing
        """
        return pulumi.get(self, "multiplier")


@pulumi.output_type
class ProductFamilyResponse(dict):
    """
    Product Family
    """
    def __init__(__self__, *,
                 availability_information: 'outputs.AvailabilityInformationResponse',
                 cost_information: 'outputs.CostInformationResponse',
                 description: 'outputs.DescriptionResponse',
                 display_name: str,
                 filterable_properties: Sequence['outputs.FilterablePropertyResponse'],
                 hierarchy_information: 'outputs.HierarchyInformationResponse',
                 image_information: Sequence['outputs.ImageInformationResponse'],
                 product_lines: Sequence['outputs.ProductLineResponse']):
        """
        Product Family
        :param 'AvailabilityInformationResponse' availability_information: Availability information of the product system.
        :param 'CostInformationResponse' cost_information: Cost information for the product system.
        :param 'DescriptionResponse' description: Description related to the product system.
        :param str display_name: Display Name for the product system.
        :param Sequence['FilterablePropertyResponse'] filterable_properties: list of filters supported for a product
        :param 'HierarchyInformationResponse' hierarchy_information: Hierarchy information of a product.
        :param Sequence['ImageInformationResponse'] image_information: Image information for the product system.
        :param Sequence['ProductLineResponse'] product_lines: List of product lines supported in the product family
        """
        pulumi.set(__self__, "availability_information", availability_information)
        pulumi.set(__self__, "cost_information", cost_information)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "filterable_properties", filterable_properties)
        pulumi.set(__self__, "hierarchy_information", hierarchy_information)
        pulumi.set(__self__, "image_information", image_information)
        pulumi.set(__self__, "product_lines", product_lines)

    @property
    @pulumi.getter(name="availabilityInformation")
    def availability_information(self) -> 'outputs.AvailabilityInformationResponse':
        """
        Availability information of the product system.
        """
        return pulumi.get(self, "availability_information")

    @property
    @pulumi.getter(name="costInformation")
    def cost_information(self) -> 'outputs.CostInformationResponse':
        """
        Cost information for the product system.
        """
        return pulumi.get(self, "cost_information")

    @property
    @pulumi.getter
    def description(self) -> 'outputs.DescriptionResponse':
        """
        Description related to the product system.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display Name for the product system.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="filterableProperties")
    def filterable_properties(self) -> Sequence['outputs.FilterablePropertyResponse']:
        """
        list of filters supported for a product
        """
        return pulumi.get(self, "filterable_properties")

    @property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> 'outputs.HierarchyInformationResponse':
        """
        Hierarchy information of a product.
        """
        return pulumi.get(self, "hierarchy_information")

    @property
    @pulumi.getter(name="imageInformation")
    def image_information(self) -> Sequence['outputs.ImageInformationResponse']:
        """
        Image information for the product system.
        """
        return pulumi.get(self, "image_information")

    @property
    @pulumi.getter(name="productLines")
    def product_lines(self) -> Sequence['outputs.ProductLineResponse']:
        """
        List of product lines supported in the product family
        """
        return pulumi.get(self, "product_lines")


@pulumi.output_type
class ProductLineResponse(dict):
    """
    Product line
    """
    def __init__(__self__, *,
                 availability_information: 'outputs.AvailabilityInformationResponse',
                 cost_information: 'outputs.CostInformationResponse',
                 description: 'outputs.DescriptionResponse',
                 display_name: str,
                 filterable_properties: Sequence['outputs.FilterablePropertyResponse'],
                 hierarchy_information: 'outputs.HierarchyInformationResponse',
                 image_information: Sequence['outputs.ImageInformationResponse'],
                 products: Sequence['outputs.ProductResponse']):
        """
        Product line
        :param 'AvailabilityInformationResponse' availability_information: Availability information of the product system.
        :param 'CostInformationResponse' cost_information: Cost information for the product system.
        :param 'DescriptionResponse' description: Description related to the product system.
        :param str display_name: Display Name for the product system.
        :param Sequence['FilterablePropertyResponse'] filterable_properties: list of filters supported for a product
        :param 'HierarchyInformationResponse' hierarchy_information: Hierarchy information of a product.
        :param Sequence['ImageInformationResponse'] image_information: Image information for the product system.
        :param Sequence['ProductResponse'] products: List of products in the product line
        """
        pulumi.set(__self__, "availability_information", availability_information)
        pulumi.set(__self__, "cost_information", cost_information)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "filterable_properties", filterable_properties)
        pulumi.set(__self__, "hierarchy_information", hierarchy_information)
        pulumi.set(__self__, "image_information", image_information)
        pulumi.set(__self__, "products", products)

    @property
    @pulumi.getter(name="availabilityInformation")
    def availability_information(self) -> 'outputs.AvailabilityInformationResponse':
        """
        Availability information of the product system.
        """
        return pulumi.get(self, "availability_information")

    @property
    @pulumi.getter(name="costInformation")
    def cost_information(self) -> 'outputs.CostInformationResponse':
        """
        Cost information for the product system.
        """
        return pulumi.get(self, "cost_information")

    @property
    @pulumi.getter
    def description(self) -> 'outputs.DescriptionResponse':
        """
        Description related to the product system.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display Name for the product system.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="filterableProperties")
    def filterable_properties(self) -> Sequence['outputs.FilterablePropertyResponse']:
        """
        list of filters supported for a product
        """
        return pulumi.get(self, "filterable_properties")

    @property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> 'outputs.HierarchyInformationResponse':
        """
        Hierarchy information of a product.
        """
        return pulumi.get(self, "hierarchy_information")

    @property
    @pulumi.getter(name="imageInformation")
    def image_information(self) -> Sequence['outputs.ImageInformationResponse']:
        """
        Image information for the product system.
        """
        return pulumi.get(self, "image_information")

    @property
    @pulumi.getter
    def products(self) -> Sequence['outputs.ProductResponse']:
        """
        List of products in the product line
        """
        return pulumi.get(self, "products")


@pulumi.output_type
class ProductResponse(dict):
    """
    List of Products
    """
    def __init__(__self__, *,
                 availability_information: 'outputs.AvailabilityInformationResponse',
                 configurations: Sequence['outputs.ConfigurationResponse'],
                 cost_information: 'outputs.CostInformationResponse',
                 description: 'outputs.DescriptionResponse',
                 display_name: str,
                 filterable_properties: Sequence['outputs.FilterablePropertyResponse'],
                 hierarchy_information: 'outputs.HierarchyInformationResponse',
                 image_information: Sequence['outputs.ImageInformationResponse']):
        """
        List of Products
        :param 'AvailabilityInformationResponse' availability_information: Availability information of the product system.
        :param Sequence['ConfigurationResponse'] configurations: List of configurations for the product
        :param 'CostInformationResponse' cost_information: Cost information for the product system.
        :param 'DescriptionResponse' description: Description related to the product system.
        :param str display_name: Display Name for the product system.
        :param Sequence['FilterablePropertyResponse'] filterable_properties: list of filters supported for a product
        :param 'HierarchyInformationResponse' hierarchy_information: Hierarchy information of a product.
        :param Sequence['ImageInformationResponse'] image_information: Image information for the product system.
        """
        pulumi.set(__self__, "availability_information", availability_information)
        pulumi.set(__self__, "configurations", configurations)
        pulumi.set(__self__, "cost_information", cost_information)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "filterable_properties", filterable_properties)
        pulumi.set(__self__, "hierarchy_information", hierarchy_information)
        pulumi.set(__self__, "image_information", image_information)

    @property
    @pulumi.getter(name="availabilityInformation")
    def availability_information(self) -> 'outputs.AvailabilityInformationResponse':
        """
        Availability information of the product system.
        """
        return pulumi.get(self, "availability_information")

    @property
    @pulumi.getter
    def configurations(self) -> Sequence['outputs.ConfigurationResponse']:
        """
        List of configurations for the product
        """
        return pulumi.get(self, "configurations")

    @property
    @pulumi.getter(name="costInformation")
    def cost_information(self) -> 'outputs.CostInformationResponse':
        """
        Cost information for the product system.
        """
        return pulumi.get(self, "cost_information")

    @property
    @pulumi.getter
    def description(self) -> 'outputs.DescriptionResponse':
        """
        Description related to the product system.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display Name for the product system.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="filterableProperties")
    def filterable_properties(self) -> Sequence['outputs.FilterablePropertyResponse']:
        """
        list of filters supported for a product
        """
        return pulumi.get(self, "filterable_properties")

    @property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> 'outputs.HierarchyInformationResponse':
        """
        Hierarchy information of a product.
        """
        return pulumi.get(self, "hierarchy_information")

    @property
    @pulumi.getter(name="imageInformation")
    def image_information(self) -> Sequence['outputs.ImageInformationResponse']:
        """
        Image information for the product system.
        """
        return pulumi.get(self, "image_information")


@pulumi.output_type
class PurchaseMeterDetailsResponse(dict):
    """
    Billing type Purchase meter details
    """
    def __init__(__self__, *,
                 billing_type: str,
                 charging_type: str,
                 multiplier: float,
                 product_id: str,
                 sku_id: str,
                 term_id: str):
        """
        Billing type Purchase meter details
        :param str billing_type: Represents billing type.
               Expected value is 'Purchase'.
        :param str charging_type: Charging type.
        :param float multiplier: Billing unit applicable for Pav2 billing
        :param str product_id: Product Id
        :param str sku_id: Sku Id
        :param str term_id: Term Id
        """
        pulumi.set(__self__, "billing_type", 'Purchase')
        pulumi.set(__self__, "charging_type", charging_type)
        pulumi.set(__self__, "multiplier", multiplier)
        pulumi.set(__self__, "product_id", product_id)
        pulumi.set(__self__, "sku_id", sku_id)
        pulumi.set(__self__, "term_id", term_id)

    @property
    @pulumi.getter(name="billingType")
    def billing_type(self) -> str:
        """
        Represents billing type.
        Expected value is 'Purchase'.
        """
        return pulumi.get(self, "billing_type")

    @property
    @pulumi.getter(name="chargingType")
    def charging_type(self) -> str:
        """
        Charging type.
        """
        return pulumi.get(self, "charging_type")

    @property
    @pulumi.getter
    def multiplier(self) -> float:
        """
        Billing unit applicable for Pav2 billing
        """
        return pulumi.get(self, "multiplier")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        """
        Product Id
        """
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter(name="skuId")
    def sku_id(self) -> str:
        """
        Sku Id
        """
        return pulumi.get(self, "sku_id")

    @property
    @pulumi.getter(name="termId")
    def term_id(self) -> str:
        """
        Term Id
        """
        return pulumi.get(self, "term_id")


@pulumi.output_type
class SpecificationResponse(dict):
    """
    Specifications of the configurations
    """
    def __init__(__self__, *,
                 name: str,
                 value: str):
        """
        Specifications of the configurations
        :param str name: Name of the specification
        :param str value: Value of the specification
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the specification
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Value of the specification
        """
        return pulumi.get(self, "value")


