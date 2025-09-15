# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DomainListParams"]


class DomainListParams(TypedDict, total=False):
    can_receive: Annotated[Literal["true", "false", "undefined"], PropertyInfo(alias="canReceive")]
    """canReceive parameter"""

    check: Literal["true", "false", "undefined"]
    """check parameter"""

    limit: float
    """limit parameter"""

    offset: float
    """offset parameter"""

    status: Literal["pending", "verified", "failed", "undefined"]
    """status parameter"""
