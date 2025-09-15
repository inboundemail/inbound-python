# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EndpointCreateResponse", "DeliveryStats"]


class DeliveryStats(BaseModel):
    failed: Optional[float] = None

    last_delivery: Optional[str] = FieldInfo(alias="lastDelivery", default=None)

    successful: Optional[float] = None

    total: Optional[float] = None


class EndpointCreateResponse(BaseModel):
    id: Optional[str] = None

    config: Optional[object] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    delivery_stats: Optional[DeliveryStats] = FieldInfo(alias="deliveryStats", default=None)

    description: Optional[str] = None

    group_emails: Optional[List[str]] = FieldInfo(alias="groupEmails", default=None)

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    name: Optional[str] = None

    type: Optional[Literal["webhook", "email", "email_group"]] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
