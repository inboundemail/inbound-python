# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailAddressCreateResponse", "Domain", "Routing"]


class Domain(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    status: Optional[str] = None


class Routing(BaseModel):
    id: Optional[str] = None

    config: Optional[object] = None

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    name: Optional[str] = None

    type: Optional[Literal["webhook", "endpoint", "none"]] = None


class EmailAddressCreateResponse(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    domain: Optional[Domain] = None

    domain_id: Optional[str] = FieldInfo(alias="domainId", default=None)

    endpoint_id: Optional[str] = FieldInfo(alias="endpointId", default=None)

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_receipt_rule_configured: Optional[bool] = FieldInfo(alias="isReceiptRuleConfigured", default=None)

    receipt_rule_name: Optional[str] = FieldInfo(alias="receiptRuleName", default=None)

    routing: Optional[Routing] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    warning: Optional[str] = None

    webhook_id: Optional[str] = FieldInfo(alias="webhookId", default=None)
