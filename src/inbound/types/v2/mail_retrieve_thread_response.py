# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MailRetrieveThreadResponse"]


class MailRetrieveThreadResponse(BaseModel):
    messages: List[str]

    thread_id: str = FieldInfo(alias="threadId")

    total_count: float = FieldInfo(alias="totalCount")
