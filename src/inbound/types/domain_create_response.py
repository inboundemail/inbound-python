# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DomainCreateResponse"]


class DomainCreateResponse(BaseModel):
    id: str

    can_receive_emails: bool = FieldInfo(alias="canReceiveEmails")

    created_at: str = FieldInfo(alias="createdAt")

    dns_records: str = FieldInfo(alias="dnsRecords")

    domain: str

    domain_provider: str = FieldInfo(alias="domainProvider")

    has_mx_records: bool = FieldInfo(alias="hasMxRecords")

    provider_confidence: str = FieldInfo(alias="providerConfidence")

    status: Literal["pending", "verified", "failed"]

    updated_at: str = FieldInfo(alias="updatedAt")

    mail_from_domain: Optional[str] = FieldInfo(alias="mailFromDomain", default=None)

    mail_from_domain_status: Optional[str] = FieldInfo(alias="mailFromDomainStatus", default=None)
