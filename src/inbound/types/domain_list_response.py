# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "DomainListResponse",
    "Data",
    "DataCatchAllEndpoint",
    "DataStats",
    "DataVerificationCheck",
    "DataVerificationCheckDNSRecord",
    "Meta",
    "MetaStatusBreakdown",
    "Pagination",
]


class DataCatchAllEndpoint(BaseModel):
    id: Optional[str] = None

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    name: Optional[str] = None

    type: Optional[str] = None


class DataStats(BaseModel):
    active_email_addresses: Optional[float] = FieldInfo(alias="activeEmailAddresses", default=None)

    has_catch_all: Optional[bool] = FieldInfo(alias="hasCatchAll", default=None)

    total_email_addresses: Optional[float] = FieldInfo(alias="totalEmailAddresses", default=None)


class DataVerificationCheckDNSRecord(BaseModel):
    error: Optional[str] = None

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    name: Optional[str] = None

    type: Optional[str] = None

    value: Optional[str] = None


class DataVerificationCheck(BaseModel):
    dns_records: Optional[List[DataVerificationCheckDNSRecord]] = FieldInfo(alias="dnsRecords", default=None)

    is_fully_verified: Optional[bool] = FieldInfo(alias="isFullyVerified", default=None)

    last_checked: Optional[datetime] = FieldInfo(alias="lastChecked", default=None)

    ses_status: Optional[str] = FieldInfo(alias="sesStatus", default=None)


class Data(BaseModel):
    id: Optional[str] = None

    can_receive_emails: Optional[bool] = FieldInfo(alias="canReceiveEmails", default=None)

    catch_all_endpoint: Optional[DataCatchAllEndpoint] = FieldInfo(alias="catchAllEndpoint", default=None)
    """Additional fields when check=true"""

    catch_all_endpoint_id: Optional[str] = FieldInfo(alias="catchAllEndpointId", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    domain: Optional[str] = None

    domain_provider: Optional[str] = FieldInfo(alias="domainProvider", default=None)

    has_mx_records: Optional[bool] = FieldInfo(alias="hasMxRecords", default=None)

    is_catch_all_enabled: Optional[bool] = FieldInfo(alias="isCatchAllEnabled", default=None)

    last_dns_check: Optional[datetime] = FieldInfo(alias="lastDnsCheck", default=None)

    last_ses_check: Optional[datetime] = FieldInfo(alias="lastSesCheck", default=None)

    mail_from_domain: Optional[str] = FieldInfo(alias="mailFromDomain", default=None)

    mail_from_domain_status: Optional[str] = FieldInfo(alias="mailFromDomainStatus", default=None)

    mail_from_domain_verified_at: Optional[datetime] = FieldInfo(alias="mailFromDomainVerifiedAt", default=None)

    provider_confidence: Optional[str] = FieldInfo(alias="providerConfidence", default=None)

    receive_dmarc_emails: Optional[bool] = FieldInfo(alias="receiveDmarcEmails", default=None)

    stats: Optional[DataStats] = None

    status: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    verification_check: Optional[DataVerificationCheck] = FieldInfo(alias="verificationCheck", default=None)


class MetaStatusBreakdown(BaseModel):
    failed: Optional[float] = None

    pending: Optional[float] = None

    verified: Optional[float] = None


class Meta(BaseModel):
    status_breakdown: Optional[MetaStatusBreakdown] = FieldInfo(alias="statusBreakdown", default=None)

    total_count: Optional[float] = FieldInfo(alias="totalCount", default=None)

    verified_count: Optional[float] = FieldInfo(alias="verifiedCount", default=None)

    with_catch_all_count: Optional[float] = FieldInfo(alias="withCatchAllCount", default=None)


class Pagination(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    limit: Optional[float] = None

    offset: Optional[float] = None

    total: Optional[float] = None


class DomainListResponse(BaseModel):
    data: Optional[List[Data]] = None

    meta: Optional[Meta] = None

    pagination: Optional[Pagination] = None
