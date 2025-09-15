# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["ScheduleListResponse"]


class ScheduleListResponse(BaseModel):
    data: List[str]

    pagination: float
