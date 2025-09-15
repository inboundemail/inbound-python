# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmailAddressCreateParams"]


class EmailAddressCreateParams(TypedDict, total=False):
    address: Required[str]

    domain_id: Required[Annotated[str, PropertyInfo(alias="domainId")]]

    endpoint_id: Annotated[str, PropertyInfo(alias="endpointId")]

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    webhook_id: Annotated[str, PropertyInfo(alias="webhookId")]
