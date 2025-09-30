# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailSendResponse"]


class EmailSendResponse(BaseModel):
    id: str
    """Unique email identifier in nanoid format"""

    message_id: str = FieldInfo(alias="messageId")
    """AWS SES Message ID for delivery tracking"""
