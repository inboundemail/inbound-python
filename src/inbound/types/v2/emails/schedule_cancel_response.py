# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ScheduleCancelResponse"]


class ScheduleCancelResponse(BaseModel):
    id: str
    """Unique scheduled email identifier"""

    cancelled_at: datetime
    """ISO 8601 timestamp when cancelled"""

    status: Literal["cancelled"]
    """Status after cancellation (always "cancelled")"""
