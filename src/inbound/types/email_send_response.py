# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailSendResponse"]


class EmailSendResponse(BaseModel):
    id: Optional[str] = None

    message_id: Optional[str] = FieldInfo(alias="messageId", default=None)
    """AWS SES Message ID"""
