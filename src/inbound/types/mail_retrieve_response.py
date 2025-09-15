# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MailRetrieveResponse",
    "Addresses",
    "AddressesBcc",
    "AddressesBccAddress",
    "AddressesCc",
    "AddressesCcAddress",
    "AddressesFrom",
    "AddressesFromAddress",
    "AddressesReplyTo",
    "AddressesReplyToAddress",
    "AddressesTo",
    "AddressesToAddress",
    "Content",
    "ContentAttachment",
    "Metadata",
    "Processing",
    "ProcessingS3Info",
    "Security",
]


class AddressesBccAddress(BaseModel):
    address: Optional[str] = None

    name: Optional[str] = None


class AddressesBcc(BaseModel):
    addresses: Optional[List[AddressesBccAddress]] = None

    text: Optional[str] = None


class AddressesCcAddress(BaseModel):
    address: Optional[str] = None

    name: Optional[str] = None


class AddressesCc(BaseModel):
    addresses: Optional[List[AddressesCcAddress]] = None

    text: Optional[str] = None


class AddressesFromAddress(BaseModel):
    address: Optional[str] = None

    name: Optional[str] = None


class AddressesFrom(BaseModel):
    addresses: Optional[List[AddressesFromAddress]] = None

    text: Optional[str] = None


class AddressesReplyToAddress(BaseModel):
    address: Optional[str] = None

    name: Optional[str] = None


class AddressesReplyTo(BaseModel):
    addresses: Optional[List[AddressesReplyToAddress]] = None

    text: Optional[str] = None


class AddressesToAddress(BaseModel):
    address: Optional[str] = None

    name: Optional[str] = None


class AddressesTo(BaseModel):
    addresses: Optional[List[AddressesToAddress]] = None

    text: Optional[str] = None


class Addresses(BaseModel):
    bcc: Optional[AddressesBcc] = None

    cc: Optional[AddressesCc] = None

    from_: Optional[AddressesFrom] = FieldInfo(alias="from", default=None)

    reply_to: Optional[AddressesReplyTo] = FieldInfo(alias="replyTo", default=None)

    to: Optional[AddressesTo] = None


class ContentAttachment(BaseModel):
    content_disposition: Optional[str] = FieldInfo(alias="contentDisposition", default=None)

    content_id: Optional[str] = FieldInfo(alias="contentId", default=None)

    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)

    filename: Optional[str] = None

    size: Optional[float] = None


class Content(BaseModel):
    attachments: Optional[List[ContentAttachment]] = None

    headers: Optional[Dict[str, object]] = None

    html_body: Optional[str] = FieldInfo(alias="htmlBody", default=None)

    raw_content: Optional[str] = FieldInfo(alias="rawContent", default=None)

    text_body: Optional[str] = FieldInfo(alias="textBody", default=None)


class Metadata(BaseModel):
    attachment_count: Optional[float] = FieldInfo(alias="attachmentCount", default=None)

    has_attachments: Optional[bool] = FieldInfo(alias="hasAttachments", default=None)

    has_html_body: Optional[bool] = FieldInfo(alias="hasHtmlBody", default=None)

    has_text_body: Optional[bool] = FieldInfo(alias="hasTextBody", default=None)

    in_reply_to: Optional[str] = FieldInfo(alias="inReplyTo", default=None)

    parse_error: Optional[str] = FieldInfo(alias="parseError", default=None)

    parse_success: Optional[bool] = FieldInfo(alias="parseSuccess", default=None)

    priority: Optional[str] = None

    references: Optional[List[str]] = None


class ProcessingS3Info(BaseModel):
    bucket_name: Optional[str] = FieldInfo(alias="bucketName", default=None)

    content_fetched: Optional[bool] = FieldInfo(alias="contentFetched", default=None)

    content_size: Optional[float] = FieldInfo(alias="contentSize", default=None)

    error: Optional[str] = None

    object_key: Optional[str] = FieldInfo(alias="objectKey", default=None)


class Processing(BaseModel):
    action_type: Optional[str] = FieldInfo(alias="actionType", default=None)

    common_headers: Optional[Dict[str, object]] = FieldInfo(alias="commonHeaders", default=None)

    processing_time_ms: Optional[float] = FieldInfo(alias="processingTimeMs", default=None)

    receipt_timestamp: Optional[datetime] = FieldInfo(alias="receiptTimestamp", default=None)

    s3_info: Optional[ProcessingS3Info] = FieldInfo(alias="s3Info", default=None)

    timestamp: Optional[datetime] = None


class Security(BaseModel):
    dkim: Optional[str] = None

    dmarc: Optional[str] = None

    spam: Optional[str] = None

    spf: Optional[str] = None

    virus: Optional[str] = None


class MailRetrieveResponse(BaseModel):
    id: Optional[str] = None

    addresses: Optional[Addresses] = None

    bcc: Optional[str] = None

    cc: Optional[str] = None

    content: Optional[Content] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    email_id: Optional[str] = FieldInfo(alias="emailId", default=None)

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    from_name: Optional[str] = FieldInfo(alias="fromName", default=None)

    is_read: Optional[bool] = FieldInfo(alias="isRead", default=None)

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)

    metadata: Optional[Metadata] = None

    processing: Optional[Processing] = None

    read_at: Optional[datetime] = FieldInfo(alias="readAt", default=None)

    received_at: Optional[datetime] = FieldInfo(alias="receivedAt", default=None)

    recipient: Optional[str] = None

    reply_to: Optional[str] = FieldInfo(alias="replyTo", default=None)

    security: Optional[Security] = None

    subject: Optional[str] = None

    to: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
