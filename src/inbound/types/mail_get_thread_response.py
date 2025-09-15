# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MailGetThreadResponse",
    "Message",
    "MessageAddresses",
    "MessageAddressesFrom",
    "MessageAddressesFromAddress",
    "MessageAddressesTo",
    "MessageAddressesToAddress",
    "MessageContent",
    "MessageContentAttachment",
    "MessageMetadata",
]


class MessageAddressesFromAddress(BaseModel):
    address: Optional[str] = None

    name: Optional[str] = None


class MessageAddressesFrom(BaseModel):
    addresses: Optional[List[MessageAddressesFromAddress]] = None

    text: Optional[str] = None


class MessageAddressesToAddress(BaseModel):
    address: Optional[str] = None

    name: Optional[str] = None


class MessageAddressesTo(BaseModel):
    addresses: Optional[List[MessageAddressesToAddress]] = None

    text: Optional[str] = None


class MessageAddresses(BaseModel):
    from_: Optional[MessageAddressesFrom] = FieldInfo(alias="from", default=None)

    to: Optional[MessageAddressesTo] = None


class MessageContentAttachment(BaseModel):
    content_disposition: Optional[str] = FieldInfo(alias="contentDisposition", default=None)

    content_id: Optional[str] = FieldInfo(alias="contentId", default=None)

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)

    filename: Optional[str] = None

    size: Optional[float] = None


class MessageContent(BaseModel):
    attachments: Optional[List[MessageContentAttachment]] = None

    html_body: Optional[str] = FieldInfo(alias="htmlBody", default=None)

    text_body: Optional[str] = FieldInfo(alias="textBody", default=None)


class MessageMetadata(BaseModel):
    in_reply_to: Optional[str] = FieldInfo(alias="inReplyTo", default=None)

    parse_error: Optional[str] = FieldInfo(alias="parseError", default=None)

    parse_success: Optional[bool] = FieldInfo(alias="parseSuccess", default=None)

    references: Optional[List[str]] = None


class Message(BaseModel):
    id: Optional[str] = None

    addresses: Optional[MessageAddresses] = None

    content: Optional[MessageContent] = None

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    from_name: Optional[str] = FieldInfo(alias="fromName", default=None)

    is_read: Optional[bool] = FieldInfo(alias="isRead", default=None)

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)

    metadata: Optional[MessageMetadata] = None

    read_at: Optional[datetime] = FieldInfo(alias="readAt", default=None)

    received_at: Optional[datetime] = FieldInfo(alias="receivedAt", default=None)

    sent_at: Optional[datetime] = FieldInfo(alias="sentAt", default=None)

    subject: Optional[str] = None

    to: Optional[str] = None

    type: Optional[Literal["inbound", "outbound"]] = None


class MailGetThreadResponse(BaseModel):
    messages: Optional[List[Message]] = None

    thread_id: Optional[str] = FieldInfo(alias="threadId", default=None)
    """The root message ID of the thread"""

    total_count: Optional[float] = FieldInfo(alias="totalCount", default=None)
