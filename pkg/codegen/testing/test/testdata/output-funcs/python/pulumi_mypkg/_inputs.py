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

__all__ = [
    'BastionShareableLink',
]

class BastionShareableLinkDict(TypedDict):
    """
    Bastion Shareable Link.
    """
    vm: str

@pulumi.input_type
class BastionShareableLink:
    def __init__(__self__, *,
                 vm: str):
        """
        Bastion Shareable Link.
        :param str vm: Reference of the virtual machine resource.
        """
        pulumi.set(__self__, "vm", vm)

    @property
    @pulumi.getter
    def vm(self) -> str:
        """
        Reference of the virtual machine resource.
        """
        return pulumi.get(self, "vm")

    @vm.setter
    def vm(self, value: str):
        pulumi.set(self, "vm", value)


