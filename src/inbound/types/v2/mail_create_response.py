# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MailCreateResponse"]


class MailCreateResponse(BaseModel):
    message: str

    original_email_id: str = FieldInfo(alias="originalEmailId")

    reply_data: str = FieldInfo(alias="replyData")

    status: str
