# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EndpointRetrieveResponse"]


class EndpointRetrieveResponse(BaseModel):
    id: str

    associated_emails: List[str] = FieldInfo(alias="associatedEmails")

    catch_all_domains: List[str] = FieldInfo(alias="catchAllDomains")

    config: str

    created_at: str = FieldInfo(alias="createdAt")

    delivery_stats: str = FieldInfo(alias="deliveryStats")

    description: str

    group_emails: str = FieldInfo(alias="groupEmails")

    is_active: bool = FieldInfo(alias="isActive")

    name: str

    recent_deliveries: List[str] = FieldInfo(alias="recentDeliveries")

    type: Literal["webhook", "email", "email_group"]

    updated_at: str = FieldInfo(alias="updatedAt")

    user_id: str = FieldInfo(alias="userId")
