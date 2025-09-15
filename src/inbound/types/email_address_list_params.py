# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailAddressListParams"]


class EmailAddressListParams(TypedDict, total=False):
    domain_id: Annotated[str, PropertyInfo(alias="domainId")]

    is_active: Annotated[Literal["true", "false"], PropertyInfo(alias="isActive")]

    is_receipt_rule_configured: Annotated[Literal["true", "false"], PropertyInfo(alias="isReceiptRuleConfigured")]

    limit: float

    offset: float
