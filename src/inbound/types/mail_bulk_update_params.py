# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MailBulkUpdateParams", "Updates"]


class MailBulkUpdateParams(TypedDict, total=False):
    email_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="emailIds")]

    updates: Updates


class Updates(TypedDict, total=False):
    is_archived: Annotated[bool, PropertyInfo(alias="isArchived")]

    is_read: Annotated[bool, PropertyInfo(alias="isRead")]
