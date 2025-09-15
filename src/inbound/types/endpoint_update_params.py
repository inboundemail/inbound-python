# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EndpointUpdateParams"]


class EndpointUpdateParams(TypedDict, total=False):
    body_id: Required[Annotated[str, PropertyInfo(alias="id")]]

    config: Literal[
        "import(/Users/ryanvogel/dev/inbound-org/inbound/features/endpoints/types/index).EndpointConfig", "undefined"
    ]

    description: str

    is_active: Annotated[bool, PropertyInfo(alias="isActive")]

    name: str
