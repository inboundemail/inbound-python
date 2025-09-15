# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["OnboardingCheckReplyResponse", "Reply"]


class Reply(BaseModel):
    body: Optional[str] = None

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    received_at: Optional[str] = FieldInfo(alias="receivedAt", default=None)

    subject: Optional[str] = None


class OnboardingCheckReplyResponse(BaseModel):
    has_reply: Optional[bool] = FieldInfo(alias="hasReply", default=None)

    reply: Optional[Reply] = None
