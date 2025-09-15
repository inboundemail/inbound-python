# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MailUpdateResponse"]


class MailUpdateResponse(BaseModel):
    id: str

    archived_at: Literal["Date", "null"] = FieldInfo(alias="archivedAt")

    is_archived: bool = FieldInfo(alias="isArchived")

    is_read: bool = FieldInfo(alias="isRead")

    read_at: Literal["Date", "null"] = FieldInfo(alias="readAt")
