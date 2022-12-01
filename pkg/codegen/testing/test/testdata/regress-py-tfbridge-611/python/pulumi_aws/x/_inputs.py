# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from typing_extensions import NotRequired, Required, TypedDict
from .. import _utilities

__all__ = [
    'GetPolicyDocumentStatementArgs',
]

class GetPolicyDocumentStatementArgsDict(TypedDict):
    actions: NotRequired[Optional[Sequence[str]]]

@pulumi.input_type
class GetPolicyDocumentStatementArgs:
    def __init__(__self__, *,
                 actions: Optional[Sequence[str]] = None):
        if actions is not None:
            pulumi.set(__self__, "actions", actions)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[Sequence[str]]):
        pulumi.set(self, "actions", value)


