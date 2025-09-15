# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MailListParams"]


class MailListParams(TypedDict, total=False):
    domain: str
    """domain parameter"""

    email_address: Annotated[str, PropertyInfo(alias="emailAddress")]
    """emailAddress parameter"""

    email_id: Annotated[str, PropertyInfo(alias="emailId")]
    """emailId parameter"""

    include_archived: Annotated[bool, PropertyInfo(alias="includeArchived")]
    """includeArchived parameter"""

    limit: float
    """limit parameter"""

    offset: float
    """offset parameter"""

    search: str
    """search parameter"""

    status: Literal["failed", "all", "processed", "undefined"]
    """status parameter"""

    time_range: Annotated[Literal["24h", "7d", "30d", "90d", "undefined"], PropertyInfo(alias="timeRange")]
    """timeRange parameter"""
