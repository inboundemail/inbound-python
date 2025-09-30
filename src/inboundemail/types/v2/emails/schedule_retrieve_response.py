# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ScheduleRetrieveResponse", "Tag"]


class Tag(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None


class ScheduleRetrieveResponse(BaseModel):
    id: str
    """Unique scheduled email identifier"""

    attempts: int
    """Send attempts made"""

    created_at: datetime
    """Creation timestamp"""

    from_: str = FieldInfo(alias="from")
    """Sender email address"""

    max_attempts: int
    """Maximum retry attempts"""

    scheduled_at: datetime
    """ISO 8601 scheduled send time"""

    status: Literal["scheduled", "sent", "failed", "cancelled"]
    """Current status"""

    subject: str
    """Email subject line"""

    timezone: str
    """Timezone for scheduled time"""

    to: List[str]
    """Recipient email addresses"""

    updated_at: datetime
    """Last update timestamp"""

    attachments: Optional[List[object]] = None
    """Email attachments"""

    bcc: Optional[List[str]] = None
    """Blind carbon copy recipients"""

    cc: Optional[List[str]] = None
    """Carbon copy recipients"""

    headers: Optional[Dict[str, str]] = None
    """Custom headers"""

    html: Optional[str] = None
    """HTML content"""

    last_error: Optional[str] = None
    """Last error message"""

    next_retry_at: Optional[datetime] = None
    """Next retry time (if failed)"""

    reply_to: Optional[List[str]] = FieldInfo(alias="replyTo", default=None)
    """Reply-To addresses"""

    sent_at: Optional[datetime] = None
    """Actual send timestamp"""

    sent_email_id: Optional[str] = None
    """ID of sent email record"""

    tags: Optional[List[Tag]] = None
    """Metadata tags"""

    text: Optional[str] = None
    """Plain text content"""
