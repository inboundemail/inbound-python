# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailAddressUpdateParams"]


class EmailAddressUpdateParams(TypedDict, total=False):
    endpoint_id: Annotated[str, PropertyInfo(alias="endpointId")]

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    webhook_id: Annotated[str, PropertyInfo(alias="webhookId")]
