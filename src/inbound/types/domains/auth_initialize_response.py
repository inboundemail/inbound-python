# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AuthInitializeResponse", "Record"]


class Record(BaseModel):
    description: Optional[str] = None

    is_required: Optional[bool] = FieldInfo(alias="isRequired", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    name: Optional[str] = None

    priority: Optional[float] = None

    type: Optional[Literal["TXT", "CNAME", "MX"]] = None

    value: Optional[str] = None


class AuthInitializeResponse(BaseModel):
    dkim_enabled: Optional[bool] = FieldInfo(alias="dkimEnabled", default=None)

    dkim_tokens: Optional[List[str]] = FieldInfo(alias="dkimTokens", default=None)

    domain: Optional[str] = None

    mail_from_domain: Optional[str] = FieldInfo(alias="mailFromDomain", default=None)

    mail_from_status: Optional[str] = FieldInfo(alias="mailFromStatus", default=None)

    message: Optional[str] = None

    records: Optional[List[Record]] = None

    ses_identity_status: Optional[str] = FieldInfo(alias="sesIdentityStatus", default=None)

    success: Optional[bool] = None
