# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ScheduleListParams"]


class ScheduleListParams(TypedDict, total=False):
    limit: float
    """limit parameter"""

    offset: float
    """offset parameter"""

    status: str
    """status parameter"""
