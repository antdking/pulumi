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
    'func_with_const_input',
]

def func_with_const_input(plain_input: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None):
    """
    Codegen demo with const inputs
    """
    __args__ = dict()
    __args__['plainInput'] = plain_input
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mypkg::funcWithConstInput', __args__, opts=opts).value

