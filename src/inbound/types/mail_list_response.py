# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MailListResponse", "Email", "Filters", "Pagination"]


class Email(BaseModel):
    id: Optional[str] = None

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)

    attachment_count: Optional[float] = FieldInfo(alias="attachmentCount", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    email_id: Optional[str] = FieldInfo(alias="emailId", default=None)

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    from_name: Optional[str] = FieldInfo(alias="fromName", default=None)

    has_attachments: Optional[bool] = FieldInfo(alias="hasAttachments", default=None)

    is_archived: Optional[bool] = FieldInfo(alias="isArchived", default=None)

    is_read: Optional[bool] = FieldInfo(alias="isRead", default=None)

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)

    parse_error: Optional[str] = FieldInfo(alias="parseError", default=None)

    parse_success: Optional[bool] = FieldInfo(alias="parseSuccess", default=None)

    preview: Optional[str] = None

    read_at: Optional[datetime] = FieldInfo(alias="readAt", default=None)

    received_at: Optional[datetime] = FieldInfo(alias="receivedAt", default=None)

    recipient: Optional[str] = None

    subject: Optional[str] = None


class Filters(BaseModel):
    unique_domains: Optional[List[str]] = FieldInfo(alias="uniqueDomains", default=None)


class Pagination(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    limit: Optional[float] = None

    offset: Optional[float] = None

    total: Optional[float] = None


class MailListResponse(BaseModel):
    emails: Optional[List[Email]] = None

    filters: Optional[Filters] = None

    pagination: Optional[Pagination] = None
