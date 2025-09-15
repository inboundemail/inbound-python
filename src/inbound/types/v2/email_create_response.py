# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailCreateResponse"]


class EmailCreateResponse(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageId")
