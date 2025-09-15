# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MailRetrieveResponse"]


class MailRetrieveResponse(BaseModel):
    id: str

    addresses: Literal[
        "{ from: import(/Users/ryanvogel/dev/inbound-org/inbound/app/api/v2/mail/[id]/route).ParsedEmailAddress",
        "null; to: import(/Users/ryanvogel/dev/inbound-org/inbound/app/api/v2/mail/[id]/route).ParsedEmailAddress",
        "null; cc: import(/Users/ryanvogel/dev/inbound-org/inbound/app/api/v2/mail/[id]/route).ParsedEmailAddress",
        "null; bcc: import(/Users/ryanvogel/dev/inbound-org/inbound/app/api/v2/mail/[id]/route).ParsedEmailAddress",
        "null; replyTo: import(/Users/ryanvogel/dev/inbound-org/inbound/app/api/v2/mail/[id]/route).ParsedEmailAddress",
        "null; }",
    ]

    bcc: str

    cc: str

    content: str

    created_at: Literal["Date", "null"] = FieldInfo(alias="createdAt")

    email_id: str = FieldInfo(alias="emailId")

    from_: str = FieldInfo(alias="from")

    from_name: str = FieldInfo(alias="fromName")

    is_read: bool = FieldInfo(alias="isRead")

    message_id: str = FieldInfo(alias="messageId")

    metadata: str

    processing: str

    read_at: Literal["Date", "null"] = FieldInfo(alias="readAt")

    received_at: Literal["Date", "null"] = FieldInfo(alias="receivedAt")

    recipient: str

    reply_to: str = FieldInfo(alias="replyTo")

    security: str

    subject: str

    to: str

    updated_at: Literal["Date", "null"] = FieldInfo(alias="updatedAt")
