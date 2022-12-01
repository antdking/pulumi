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
from ._inputs import *

__all__ = [
    'ListProductFamiliesResult',
    'AwaitableListProductFamiliesResult',
    'list_product_families',
    'list_product_families_output',
]

@pulumi.output_type
class ListProductFamiliesResult:
    """
    The list of product families.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        Link for the next set of product families.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.ProductFamilyResponse']:
        """
        List of product families.
        """
        return pulumi.get(self, "value")


class AwaitableListProductFamiliesResult(ListProductFamiliesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListProductFamiliesResult(
            next_link=self.next_link,
            value=self.value)


def list_product_families(customer_subscription_details: Optional[Union['CustomerSubscriptionDetails', 'CustomerSubscriptionDetailsDict']] = None,
                          expand: Optional[str] = None,
                          filterable_properties: Optional[Mapping[str, Sequence[Union['FilterableProperty', 'FilterablePropertyDict']]]] = None,
                          skip_token: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListProductFamiliesResult:
    """
    The list of product families.
    API Version: 2020-12-01-preview.


    :param Union['CustomerSubscriptionDetails', 'CustomerSubscriptionDetailsDict'] customer_subscription_details: Customer subscription properties. Clients can display available products to unregistered customers by explicitly passing subscription details
    :param str expand: $expand is supported on configurations parameter for product, which provides details on the configurations for the product.
    :param Mapping[str, Sequence[Union['FilterableProperty', 'FilterablePropertyDict']]] filterable_properties: Dictionary of filterable properties on product family.
    :param str skip_token: $skipToken is supported on list of product families, which provides the next page in the list of product families.
    """
    __args__ = dict()
    __args__['customerSubscriptionDetails'] = customer_subscription_details
    __args__['expand'] = expand
    __args__['filterableProperties'] = filterable_properties
    __args__['skipToken'] = skip_token
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('myedgeorder::listProductFamilies', __args__, opts=opts, typ=ListProductFamiliesResult).value

    return AwaitableListProductFamiliesResult(
        next_link=__ret__.next_link,
        value=__ret__.value)


@_utilities.lift_output_func(list_product_families)
def list_product_families_output(customer_subscription_details: Optional[pulumi.Input[Optional[Union['CustomerSubscriptionDetails', 'CustomerSubscriptionDetailsDict']]]] = None,
                                 expand: Optional[pulumi.Input[Optional[str]]] = None,
                                 filterable_properties: Optional[pulumi.Input[Mapping[str, Sequence[Union['FilterableProperty', 'FilterablePropertyDict']]]]] = None,
                                 skip_token: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListProductFamiliesResult]:
    """
    The list of product families.
    API Version: 2020-12-01-preview.


    :param Union['CustomerSubscriptionDetails', 'CustomerSubscriptionDetailsDict'] customer_subscription_details: Customer subscription properties. Clients can display available products to unregistered customers by explicitly passing subscription details
    :param str expand: $expand is supported on configurations parameter for product, which provides details on the configurations for the product.
    :param Mapping[str, Sequence[Union['FilterableProperty', 'FilterablePropertyDict']]] filterable_properties: Dictionary of filterable properties on product family.
    :param str skip_token: $skipToken is supported on list of product families, which provides the next page in the list of product families.
    """
    ...
