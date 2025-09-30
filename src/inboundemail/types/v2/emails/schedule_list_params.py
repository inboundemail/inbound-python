# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ScheduleListParams"]


class ScheduleListParams(TypedDict, total=False):
    limit: int
    """Maximum number of scheduled emails to return. Min: 1, Max: 100, Default: 50"""

    offset: int
    """Number of scheduled emails to skip for pagination. Min: 0, Default: 0"""

    status: str
    """Filter by email status. Values: 'scheduled', 'sent', 'failed', 'cancelled'"""
