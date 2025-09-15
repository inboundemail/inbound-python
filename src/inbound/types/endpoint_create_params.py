# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["EndpointCreateParams"]


class EndpointCreateParams(TypedDict, total=False):
    config: object

    description: Optional[str]

    name: str

    type: Literal["webhook", "email", "email_group"]
