# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EndpointCreateParams"]


class EndpointCreateParams(TypedDict, total=False):
    config: Required[str]

    name: Required[str]

    type: Required[Literal["webhook", "email", "email_group"]]

    description: str
