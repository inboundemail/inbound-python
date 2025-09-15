# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailAddressCreateResponse"]


class EmailAddressCreateResponse(BaseModel):
    id: str

    address: str

    created_at: str = FieldInfo(alias="createdAt")

    domain: str

    domain_id: str = FieldInfo(alias="domainId")

    endpoint_id: str = FieldInfo(alias="endpointId")

    is_active: bool = FieldInfo(alias="isActive")

    is_receipt_rule_configured: bool = FieldInfo(alias="isReceiptRuleConfigured")

    receipt_rule_name: str = FieldInfo(alias="receiptRuleName")

    routing: str

    updated_at: str = FieldInfo(alias="updatedAt")

    user_id: str = FieldInfo(alias="userId")

    webhook_id: str = FieldInfo(alias="webhookId")

    warning: Optional[str] = None
