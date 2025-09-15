# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EndpointListParams"]


class EndpointListParams(TypedDict, total=False):
    active: Literal["true", "false", "undefined"]
    """active parameter"""

    limit: float
    """limit parameter"""

    offset: float
    """offset parameter"""

    sort_by: Annotated[Literal["newest", "oldest", "undefined"], PropertyInfo(alias="sortBy")]
    """sortBy parameter"""

    type: Literal["webhook", "email", "email_group", "undefined"]
    """type parameter"""
