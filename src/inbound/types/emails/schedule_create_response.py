# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ScheduleCreateResponse"]


class ScheduleCreateResponse(BaseModel):
    id: Optional[str] = None

    scheduled_at: Optional[str] = None
    """Normalized ISO 8601 timestamp"""

    status: Optional[Literal["scheduled"]] = None

    timezone: Optional[str] = None
