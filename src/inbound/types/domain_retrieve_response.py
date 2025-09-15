# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DomainRetrieveResponse"]


class DomainRetrieveResponse(BaseModel):
    id: str

    can_receive_emails: bool = FieldInfo(alias="canReceiveEmails")

    catch_all_endpoint_id: str = FieldInfo(alias="catchAllEndpointId")

    created_at: str = FieldInfo(alias="createdAt")

    domain: str

    domain_provider: str = FieldInfo(alias="domainProvider")

    has_mx_records: bool = FieldInfo(alias="hasMxRecords")

    is_catch_all_enabled: bool = FieldInfo(alias="isCatchAllEnabled")

    last_dns_check: Literal["Date", "null"] = FieldInfo(alias="lastDnsCheck")

    last_ses_check: Literal["Date", "null"] = FieldInfo(alias="lastSesCheck")

    mail_from_domain: str = FieldInfo(alias="mailFromDomain")

    mail_from_domain_status: str = FieldInfo(alias="mailFromDomainStatus")

    mail_from_domain_verified_at: Literal["Date", "null"] = FieldInfo(alias="mailFromDomainVerifiedAt")

    provider_confidence: str = FieldInfo(alias="providerConfidence")

    stats: str

    status: str

    updated_at: str = FieldInfo(alias="updatedAt")

    user_id: str = FieldInfo(alias="userId")

    auth_recommendations: Optional[str] = FieldInfo(alias="authRecommendations", default=None)

    catch_all_endpoint: Optional[str] = FieldInfo(alias="catchAllEndpoint", default=None)

    verification_check: Optional[str] = FieldInfo(alias="verificationCheck", default=None)
