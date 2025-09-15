# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DomainRetrieveDNSRecordsResponse", "Record"]


class Record(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    domain_id: Optional[str] = FieldInfo(alias="domainId", default=None)

    is_required: Optional[bool] = FieldInfo(alias="isRequired", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    last_checked: Optional[datetime] = FieldInfo(alias="lastChecked", default=None)

    name: Optional[str] = None

    priority: Optional[float] = None

    record_type: Optional[str] = FieldInfo(alias="recordType", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    value: Optional[str] = None


class DomainRetrieveDNSRecordsResponse(BaseModel):
    domain: Optional[str] = None

    domain_id: Optional[str] = FieldInfo(alias="domainId", default=None)

    records: Optional[List[Record]] = None
