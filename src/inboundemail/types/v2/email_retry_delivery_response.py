# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailRetryDeliveryResponse"]


class EmailRetryDeliveryResponse(BaseModel):
    message: str
    """Human-readable status message"""

    success: bool
    """Whether the retry operation was initiated successfully"""

    delivery_id: Optional[str] = FieldInfo(alias="deliveryId", default=None)
    """The delivery record ID that was retried"""

    error: Optional[str] = None
    """Error message if operation failed"""
