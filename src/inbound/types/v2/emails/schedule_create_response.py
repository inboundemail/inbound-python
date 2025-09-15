# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ScheduleCreateResponse"]


class ScheduleCreateResponse(BaseModel):
    id: str

    scheduled_at: str

    status: str

    timezone: str
