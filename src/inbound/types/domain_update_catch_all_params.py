# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DomainUpdateCatchAllParams"]


class DomainUpdateCatchAllParams(TypedDict, total=False):
    catch_all_endpoint_id: Annotated[Optional[str], PropertyInfo(alias="catchAllEndpointId")]

    is_catch_all_enabled: Annotated[bool, PropertyInfo(alias="isCatchAllEnabled")]
