# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MailBulkUpdateResponse", "Email"]


class Email(BaseModel):
    id: Optional[str] = None

    is_archived: Optional[bool] = FieldInfo(alias="isArchived", default=None)

    is_read: Optional[bool] = FieldInfo(alias="isRead", default=None)


class MailBulkUpdateResponse(BaseModel):
    emails: Optional[List[Email]] = None

    updated_count: Optional[float] = FieldInfo(alias="updatedCount", default=None)
