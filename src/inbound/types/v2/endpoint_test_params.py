# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EndpointTestParams"]


class EndpointTestParams(TypedDict, total=False):
    body_id: Required[Annotated[str, PropertyInfo(alias="id")]]

    webhook_format: Annotated[Literal["inbound", "discord", "slack", "undefined"], PropertyInfo(alias="webhookFormat")]
