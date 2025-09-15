# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AuthCreateResponse"]


class AuthCreateResponse(BaseModel):
    dkim_enabled: bool = FieldInfo(alias="dkimEnabled")

    dkim_tokens: str = FieldInfo(alias="dkimTokens")

    domain: str

    mail_from_domain: str = FieldInfo(alias="mailFromDomain")

    mail_from_status: str = FieldInfo(alias="mailFromStatus")

    message: str

    records: List[str]

    ses_identity_status: str = FieldInfo(alias="sesIdentityStatus")

    success: bool
