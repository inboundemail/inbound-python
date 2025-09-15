# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EndpointUpdateParams"]


class EndpointUpdateParams(TypedDict, total=False):
    body_id: Annotated[str, PropertyInfo(alias="id")]
    """from params"""

    config: object

    description: Optional[str]

    is_active: Annotated[Optional[bool], PropertyInfo(alias="isActive")]

    name: Optional[str]
