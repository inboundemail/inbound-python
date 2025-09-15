# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailAddressCreateParams"]


class EmailAddressCreateParams(TypedDict, total=False):
    address: str

    domain_id: Annotated[str, PropertyInfo(alias="domainId")]

    endpoint_id: Annotated[Optional[str], PropertyInfo(alias="endpointId")]

    is_active: Annotated[Optional[bool], PropertyInfo(alias="isActive")]

    webhook_id: Annotated[Optional[str], PropertyInfo(alias="webhookId")]
