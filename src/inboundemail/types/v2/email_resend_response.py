# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailResendResponse"]


class EmailResendResponse(BaseModel):
    message: str
    """Human-readable status message"""

    success: bool
    """Whether the resend operation succeeded"""

    delivery_id: Optional[str] = FieldInfo(alias="deliveryId", default=None)
    """Unique identifier of the delivery record (nanoid format)"""

    error: Optional[str] = None
    """Error message if operation failed"""
