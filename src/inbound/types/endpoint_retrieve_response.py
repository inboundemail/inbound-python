# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EndpointRetrieveResponse", "AssociatedEmail", "CatchAllDomain", "DeliveryStats", "RecentDelivery"]


class AssociatedEmail(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)


class CatchAllDomain(BaseModel):
    id: Optional[str] = None

    domain: Optional[str] = None

    status: Optional[str] = None


class DeliveryStats(BaseModel):
    failed: Optional[float] = None

    last_delivery: Optional[str] = FieldInfo(alias="lastDelivery", default=None)

    successful: Optional[float] = None

    total: Optional[float] = None


class RecentDelivery(BaseModel):
    id: Optional[str] = None

    attempts: Optional[float] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    delivery_type: Optional[str] = FieldInfo(alias="deliveryType", default=None)

    email_id: Optional[str] = FieldInfo(alias="emailId", default=None)

    last_attempt_at: Optional[str] = FieldInfo(alias="lastAttemptAt", default=None)

    response_data: Optional[object] = FieldInfo(alias="responseData", default=None)

    status: Optional[str] = None


class EndpointRetrieveResponse(BaseModel):
    id: Optional[str] = None

    associated_emails: Optional[List[AssociatedEmail]] = FieldInfo(alias="associatedEmails", default=None)

    catch_all_domains: Optional[List[CatchAllDomain]] = FieldInfo(alias="catchAllDomains", default=None)

    config: Optional[object] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    delivery_stats: Optional[DeliveryStats] = FieldInfo(alias="deliveryStats", default=None)

    description: Optional[str] = None

    group_emails: Optional[List[str]] = FieldInfo(alias="groupEmails", default=None)

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    name: Optional[str] = None

    recent_deliveries: Optional[List[RecentDelivery]] = FieldInfo(alias="recentDeliveries", default=None)

    type: Optional[Literal["webhook", "email", "email_group"]] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
