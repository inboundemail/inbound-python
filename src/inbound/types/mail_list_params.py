# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MailListParams"]


class MailListParams(TypedDict, total=False):
    domain: str

    email_address: Annotated[str, PropertyInfo(alias="emailAddress")]

    email_id: Annotated[str, PropertyInfo(alias="emailId")]

    include_archived: Annotated[bool, PropertyInfo(alias="includeArchived")]

    limit: float

    offset: float

    search: str

    status: Literal["all", "processed", "failed"]

    time_range: Annotated[Literal["24h", "7d", "30d", "90d"], PropertyInfo(alias="timeRange")]
