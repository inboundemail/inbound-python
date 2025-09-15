# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MailGetThreadCountsResponse", "Data"]


class Data(BaseModel):
    email_id: Optional[str] = FieldInfo(alias="emailId", default=None)

    has_thread: Optional[bool] = FieldInfo(alias="hasThread", default=None)
    """true if thread count > 1"""

    thread_count: Optional[float] = FieldInfo(alias="threadCount", default=None)


class MailGetThreadCountsResponse(BaseModel):
    data: Optional[List[Data]] = None

    error: Optional[str] = None

    success: Optional[bool] = None
