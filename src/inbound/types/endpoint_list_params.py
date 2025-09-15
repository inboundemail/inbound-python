# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EndpointListParams"]


class EndpointListParams(TypedDict, total=False):
    active: Literal["true", "false"]

    limit: float

    offset: float

    sort_by: Annotated[Literal["newest", "oldest"], PropertyInfo(alias="sortBy")]

    type: Literal["webhook", "email", "email_group"]
