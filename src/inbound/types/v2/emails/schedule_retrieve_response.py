# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ScheduleRetrieveResponse"]


class ScheduleRetrieveResponse(BaseModel):
    id: str

    attempts: float

    created_at: str

    from_: str = FieldInfo(alias="from")

    max_attempts: float

    scheduled_at: str

    status: str

    subject: str

    timezone: str

    to: str

    updated_at: str

    attachments: Optional[List[str]] = None

    bcc: Optional[str] = None

    cc: Optional[str] = None

    headers: Optional[str] = None

    html: Optional[str] = None

    last_error: Optional[str] = None

    next_retry_at: Optional[str] = None

    reply_to: Optional[str] = FieldInfo(alias="replyTo", default=None)

    sent_at: Optional[str] = None

    sent_email_id: Optional[str] = None

    tags: Optional[str] = None

    text: Optional[str] = None
