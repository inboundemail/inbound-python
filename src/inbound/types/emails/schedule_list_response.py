# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScheduleListResponse", "Data", "Pagination"]


class Data(BaseModel):
    id: Optional[str] = None

    attempts: Optional[float] = None

    created_at: Optional[str] = None

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    last_error: Optional[str] = None

    scheduled_at: Optional[str] = None

    status: Optional[str] = None

    subject: Optional[str] = None

    timezone: Optional[str] = None

    to: Optional[List[str]] = None


class Pagination(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    limit: Optional[float] = None

    offset: Optional[float] = None

    total: Optional[float] = None


class ScheduleListResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None
