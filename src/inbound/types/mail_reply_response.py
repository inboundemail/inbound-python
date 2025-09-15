# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MailReplyResponse", "ReplyData"]


class ReplyData(BaseModel):
    attachment_count: Optional[float] = FieldInfo(alias="attachmentCount", default=None)

    has_html_body: Optional[bool] = FieldInfo(alias="hasHtmlBody", default=None)

    has_text_body: Optional[bool] = FieldInfo(alias="hasTextBody", default=None)

    subject: Optional[str] = None

    to: Optional[str] = None


class MailReplyResponse(BaseModel):
    message: Optional[str] = None

    original_email_id: Optional[str] = FieldInfo(alias="originalEmailId", default=None)

    reply_data: Optional[ReplyData] = FieldInfo(alias="replyData", default=None)

    status: Optional[str] = None
