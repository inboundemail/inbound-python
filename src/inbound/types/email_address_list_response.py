# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailAddressListResponse", "Data", "DataDomain", "DataRouting", "Pagination"]


class DataDomain(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    status: Optional[str] = None


class DataRouting(BaseModel):
    id: Optional[str] = None

    config: Optional[object] = None

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    name: Optional[str] = None

    type: Optional[Literal["webhook", "endpoint", "none"]] = None


class Data(BaseModel):
    id: Optional[str] = None

    address: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    domain: Optional[DataDomain] = None

    domain_id: Optional[str] = FieldInfo(alias="domainId", default=None)

    endpoint_id: Optional[str] = FieldInfo(alias="endpointId", default=None)

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_receipt_rule_configured: Optional[bool] = FieldInfo(alias="isReceiptRuleConfigured", default=None)

    receipt_rule_name: Optional[str] = FieldInfo(alias="receiptRuleName", default=None)

    routing: Optional[DataRouting] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    webhook_id: Optional[str] = FieldInfo(alias="webhookId", default=None)


class Pagination(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    limit: Optional[float] = None

    offset: Optional[float] = None

    total: Optional[float] = None


class EmailAddressListResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None
