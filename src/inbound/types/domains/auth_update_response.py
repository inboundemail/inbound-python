# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AuthUpdateResponse"]


class AuthUpdateResponse(BaseModel):
    dns_records: List[str] = FieldInfo(alias="dnsRecords")

    domain: str

    message: str

    overall_status: Literal["pending", "verified", "failed"] = FieldInfo(alias="overallStatus")

    ses_status: str = FieldInfo(alias="sesStatus")

    success: bool

    summary: float

    next_steps: Optional[str] = FieldInfo(alias="nextSteps", default=None)
