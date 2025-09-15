# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MailUpdateResponse"]


class MailUpdateResponse(BaseModel):
    id: Optional[str] = None

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    is_archived: Optional[bool] = FieldInfo(alias="isArchived", default=None)

    is_read: Optional[bool] = FieldInfo(alias="isRead", default=None)

    read_at: Optional[datetime] = FieldInfo(alias="readAt", default=None)
