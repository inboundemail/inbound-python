# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AuthVerifyResponse", "DNSRecord", "SesStatus", "Summary"]


class DNSRecord(BaseModel):
    description: Optional[str] = None

    error: Optional[str] = None

    is_required: Optional[bool] = FieldInfo(alias="isRequired", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    last_checked: Optional[str] = FieldInfo(alias="lastChecked", default=None)

    name: Optional[str] = None

    type: Optional[str] = None

    value: Optional[str] = None


class SesStatus(BaseModel):
    dkim_status: Optional[str] = FieldInfo(alias="dkimStatus", default=None)

    dkim_tokens: Optional[List[str]] = FieldInfo(alias="dkimTokens", default=None)

    dkim_verified: Optional[bool] = FieldInfo(alias="dkimVerified", default=None)

    identity_status: Optional[str] = FieldInfo(alias="identityStatus", default=None)

    identity_verified: Optional[bool] = FieldInfo(alias="identityVerified", default=None)

    mail_from_domain: Optional[str] = FieldInfo(alias="mailFromDomain", default=None)

    mail_from_status: Optional[str] = FieldInfo(alias="mailFromStatus", default=None)

    mail_from_verified: Optional[bool] = FieldInfo(alias="mailFromVerified", default=None)


class Summary(BaseModel):
    required_records: Optional[float] = FieldInfo(alias="requiredRecords", default=None)

    total_records: Optional[float] = FieldInfo(alias="totalRecords", default=None)

    verified_records: Optional[float] = FieldInfo(alias="verifiedRecords", default=None)

    verified_required_records: Optional[float] = FieldInfo(alias="verifiedRequiredRecords", default=None)


class AuthVerifyResponse(BaseModel):
    dns_records: Optional[List[DNSRecord]] = FieldInfo(alias="dnsRecords", default=None)

    domain: Optional[str] = None

    message: Optional[str] = None

    next_steps: Optional[List[str]] = FieldInfo(alias="nextSteps", default=None)

    overall_status: Optional[Literal["verified", "pending", "failed"]] = FieldInfo(alias="overallStatus", default=None)

    ses_status: Optional[SesStatus] = FieldInfo(alias="sesStatus", default=None)

    success: Optional[bool] = None

    summary: Optional[Summary] = None
