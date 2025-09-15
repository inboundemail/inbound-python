# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "DomainRetrieveResponse",
    "AuthRecommendations",
    "AuthRecommendationsDmarc",
    "AuthRecommendationsSpf",
    "CatchAllEndpoint",
    "Stats",
    "VerificationCheck",
    "VerificationCheckDNSRecord",
]


class AuthRecommendationsDmarc(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None

    value: Optional[str] = None


class AuthRecommendationsSpf(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None

    value: Optional[str] = None


class AuthRecommendations(BaseModel):
    dmarc: Optional[AuthRecommendationsDmarc] = None

    spf: Optional[AuthRecommendationsSpf] = None


class CatchAllEndpoint(BaseModel):
    id: Optional[str] = None

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    name: Optional[str] = None

    type: Optional[str] = None


class Stats(BaseModel):
    active_email_addresses: Optional[float] = FieldInfo(alias="activeEmailAddresses", default=None)

    emails_last24h: Optional[float] = FieldInfo(alias="emailsLast24h", default=None)

    emails_last30d: Optional[float] = FieldInfo(alias="emailsLast30d", default=None)

    emails_last7d: Optional[float] = FieldInfo(alias="emailsLast7d", default=None)

    total_email_addresses: Optional[float] = FieldInfo(alias="totalEmailAddresses", default=None)


class VerificationCheckDNSRecord(BaseModel):
    error: Optional[str] = None

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    name: Optional[str] = None

    type: Optional[str] = None

    value: Optional[str] = None


class VerificationCheck(BaseModel):
    dkim_status: Optional[str] = FieldInfo(alias="dkimStatus", default=None)

    dkim_tokens: Optional[List[str]] = FieldInfo(alias="dkimTokens", default=None)

    dkim_verified: Optional[bool] = FieldInfo(alias="dkimVerified", default=None)

    dns_records: Optional[List[VerificationCheckDNSRecord]] = FieldInfo(alias="dnsRecords", default=None)

    is_fully_verified: Optional[bool] = FieldInfo(alias="isFullyVerified", default=None)

    last_checked: Optional[datetime] = FieldInfo(alias="lastChecked", default=None)

    mail_from_domain: Optional[str] = FieldInfo(alias="mailFromDomain", default=None)

    mail_from_status: Optional[str] = FieldInfo(alias="mailFromStatus", default=None)

    mail_from_verified: Optional[bool] = FieldInfo(alias="mailFromVerified", default=None)

    ses_status: Optional[str] = FieldInfo(alias="sesStatus", default=None)


class DomainRetrieveResponse(BaseModel):
    id: Optional[str] = None

    auth_recommendations: Optional[AuthRecommendations] = FieldInfo(alias="authRecommendations", default=None)

    can_receive_emails: Optional[bool] = FieldInfo(alias="canReceiveEmails", default=None)

    catch_all_endpoint: Optional[CatchAllEndpoint] = FieldInfo(alias="catchAllEndpoint", default=None)
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

    stats: Optional[Stats] = None

    status: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    verification_check: Optional[VerificationCheck] = FieldInfo(alias="verificationCheck", default=None)
    """Recommendations when records are missing"""
