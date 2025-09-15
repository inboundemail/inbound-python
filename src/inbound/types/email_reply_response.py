# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailReplyResponse"]


class EmailReplyResponse(BaseModel):
    id: Optional[str] = None

    aws_message_id: Optional[str] = FieldInfo(alias="awsMessageId", default=None)
    """AWS SES Message ID"""

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)
    """Inbound message ID (used for threading)"""
