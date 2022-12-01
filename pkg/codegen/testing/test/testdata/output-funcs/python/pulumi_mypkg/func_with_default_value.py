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
    'FuncWithDefaultValueResult',
    'AwaitableFuncWithDefaultValueResult',
    'func_with_default_value',
    'func_with_default_value_output',
]

@pulumi.output_type
class FuncWithDefaultValueResult:
    def __init__(__self__, r=None):
        if r and not isinstance(r, str):
            raise TypeError("Expected argument 'r' to be a str")
        pulumi.set(__self__, "r", r)

    @property
    @pulumi.getter
    def r(self) -> str:
        return pulumi.get(self, "r")


class AwaitableFuncWithDefaultValueResult(FuncWithDefaultValueResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return FuncWithDefaultValueResult(
            r=self.r)


def func_with_default_value(a: Optional[str] = None,
                            b: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableFuncWithDefaultValueResult:
    """
    Check codegen of functions with default values.
    """
    __args__ = dict()
    __args__['a'] = a
    __args__['b'] = b
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('mypkg::funcWithDefaultValue', __args__, opts=opts, typ=FuncWithDefaultValueResult).value

    return AwaitableFuncWithDefaultValueResult(
        r=__ret__.r)


@_utilities.lift_output_func(func_with_default_value)
def func_with_default_value_output(a: Optional[pulumi.Input[str]] = None,
                                   b: Optional[pulumi.Input[Optional[str]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[FuncWithDefaultValueResult]:
    """
    Check codegen of functions with default values.
    """
    ...
