# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailAddressDeleteResponse", "Cleanup"]


class Cleanup(BaseModel):
    domain: Optional[str] = None

    email_address: Optional[str] = FieldInfo(alias="emailAddress", default=None)

    ses_rule_updated: Optional[bool] = FieldInfo(alias="sesRuleUpdated", default=None)

    warning: Optional[str] = None


class EmailAddressDeleteResponse(BaseModel):
    cleanup: Optional[Cleanup] = None

    message: Optional[str] = None
