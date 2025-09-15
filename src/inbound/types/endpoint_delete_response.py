# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EndpointDeleteResponse", "Cleanup"]


class Cleanup(BaseModel):
    deliveries_deleted: Optional[float] = FieldInfo(alias="deliveriesDeleted", default=None)

    domains: Optional[List[str]] = None

    domains_updated: Optional[float] = FieldInfo(alias="domainsUpdated", default=None)

    email_addresses: Optional[List[str]] = FieldInfo(alias="emailAddresses", default=None)

    email_addresses_updated: Optional[float] = FieldInfo(alias="emailAddressesUpdated", default=None)

    group_emails_deleted: Optional[float] = FieldInfo(alias="groupEmailsDeleted", default=None)


class EndpointDeleteResponse(BaseModel):
    cleanup: Optional[Cleanup] = None

    message: Optional[str] = None
