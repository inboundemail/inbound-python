# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DomainUpgradeMailFromResponse", "AdditionalDNSRecord"]


class AdditionalDNSRecord(BaseModel):
    description: Optional[str] = None

    is_required: Optional[bool] = FieldInfo(alias="isRequired", default=None)

    name: Optional[str] = None

    type: Optional[str] = None

    value: Optional[str] = None


class DomainUpgradeMailFromResponse(BaseModel):
    additional_dns_records: Optional[List[AdditionalDNSRecord]] = FieldInfo(alias="additionalDnsRecords", default=None)

    mail_from_domain: Optional[str] = FieldInfo(alias="mailFromDomain", default=None)

    mail_from_domain_status: Optional[str] = FieldInfo(alias="mailFromDomainStatus", default=None)

    message: Optional[str] = None

    success: Optional[bool] = None
