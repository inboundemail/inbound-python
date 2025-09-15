# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DomainListParams"]


class DomainListParams(TypedDict, total=False):
    can_receive: Annotated[Literal["true", "false"], PropertyInfo(alias="canReceive")]

    check: Literal["true", "false"]

    limit: float

    offset: float

    status: Literal["pending", "verified", "failed"]
