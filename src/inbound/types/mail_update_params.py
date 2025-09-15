# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MailUpdateParams"]


class MailUpdateParams(TypedDict, total=False):
    is_archived: Annotated[bool, PropertyInfo(alias="isArchived")]

    is_read: Annotated[bool, PropertyInfo(alias="isRead")]
