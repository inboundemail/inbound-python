# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DomainDeleteResponse", "DeletedResources"]


class DeletedResources(BaseModel):
    blocked_emails: Optional[float] = FieldInfo(alias="blockedEmails", default=None)

    dns_records: Optional[float] = FieldInfo(alias="dnsRecords", default=None)

    domain: Optional[str] = None

    email_addresses: Optional[float] = FieldInfo(alias="emailAddresses", default=None)

    ses_identity: Optional[bool] = FieldInfo(alias="sesIdentity", default=None)

    ses_receipt_rules: Optional[bool] = FieldInfo(alias="sesReceiptRules", default=None)


class DomainDeleteResponse(BaseModel):
    deleted_resources: Optional[DeletedResources] = FieldInfo(alias="deletedResources", default=None)

    message: Optional[str] = None

    success: Optional[bool] = None
