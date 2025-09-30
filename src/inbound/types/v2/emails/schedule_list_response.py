# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ScheduleListResponse", "Data", "Pagination"]


class Data(BaseModel):
    id: str
    """Unique scheduled email identifier"""

    attempts: int
    """Number of send attempts made"""

    created_at: datetime
    """ISO 8601 timestamp when scheduled"""

    from_: str = FieldInfo(alias="from")
    """Sender email address"""

    scheduled_at: datetime
    """ISO 8601 timestamp for scheduled send"""

    status: Literal["scheduled", "sent", "failed", "cancelled"]
    """Current status of scheduled email"""

    subject: str
    """Email subject line"""

    timezone: str
    """Timezone for scheduled time"""

    to: List[str]
    """Recipient email addresses"""

    last_error: Optional[str] = None
    """Error message from last failed attempt"""


class Pagination(BaseModel):
    has_more: bool = FieldInfo(alias="hasMore")
    """Whether more pages exist"""

    limit: int
    """Number of items per page"""

    offset: int
    """Number of items skipped"""

    total: int
    """Total number of scheduled emails"""


class ScheduleListResponse(BaseModel):
    data: List[Data]
    """Array of scheduled email items"""

    pagination: Pagination
