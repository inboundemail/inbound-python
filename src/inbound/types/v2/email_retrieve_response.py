# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailRetrieveResponse"]


class EmailRetrieveResponse(BaseModel):
    id: str

    bcc: str

    cc: str

    created_at: str

    from_: str = FieldInfo(alias="from")

    html: str

    last_event: str

    object: str

    reply_to: str

    subject: str

    text: str

    to: str
