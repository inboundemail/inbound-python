# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DomainCreateResponse", "DNSRecord"]


class DNSRecord(BaseModel):
    description: Optional[str] = None

    is_required: Optional[bool] = FieldInfo(alias="isRequired", default=None)

    name: Optional[str] = None

    type: Optional[str] = None

    value: Optional[str] = None


class DomainCreateResponse(BaseModel):
    id: Optional[str] = None

    can_receive_emails: Optional[bool] = FieldInfo(alias="canReceiveEmails", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    dns_records: Optional[List[DNSRecord]] = FieldInfo(alias="dnsRecords", default=None)

    domain: Optional[str] = None

    domain_provider: Optional[str] = FieldInfo(alias="domainProvider", default=None)

    has_mx_records: Optional[bool] = FieldInfo(alias="hasMxRecords", default=None)

    mail_from_domain: Optional[str] = FieldInfo(alias="mailFromDomain", default=None)

    mail_from_domain_status: Optional[str] = FieldInfo(alias="mailFromDomainStatus", default=None)

    provider_confidence: Optional[str] = FieldInfo(alias="providerConfidence", default=None)

    status: Optional[Literal["pending", "verified", "failed"]] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
