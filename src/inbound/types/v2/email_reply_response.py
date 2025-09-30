# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailReplyResponse"]


class EmailReplyResponse(BaseModel):
    id: str
    """Unique identifier of the reply email in nanoid format"""

    aws_message_id: str = FieldInfo(alias="awsMessageId")
    """AWS SES Message ID for delivery tracking"""

    is_thread_reply: bool = FieldInfo(alias="isThreadReply")
    """Whether this was a reply to a thread ID vs direct email ID"""

    message_id: str = FieldInfo(alias="messageId")
    """Inbound Message-ID used for email threading (RFC 5322)"""

    replied_to_email_id: str = FieldInfo(alias="repliedToEmailId")
    """The actual email ID that was replied to"""

    replied_to_thread_id: Optional[str] = FieldInfo(alias="repliedToThreadId", default=None)
    """The thread ID if replying to a thread (optional)"""
