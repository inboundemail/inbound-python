# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EndpointTestParams"]


class EndpointTestParams(TypedDict, total=False):
    body_id: Annotated[str, PropertyInfo(alias="id")]
    """from params"""

    webhook_format: Annotated[Optional[Literal["inbound", "discord", "slack"]], PropertyInfo(alias="webhookFormat")]
    """optional, defaults to 'inbound'"""
