# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ScheduleCreateResponse"]


class ScheduleCreateResponse(BaseModel):
    id: str
    """Unique identifier of scheduled email in nanoid format"""

    scheduled_at: datetime
    """Normalized ISO 8601 timestamp for scheduled send time"""

    status: Literal["scheduled"]
    """Current status (always "scheduled" for new emails)"""

    timezone: str
    """Timezone used for scheduling"""
