# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OnboardingSendDemoParams"]


class OnboardingSendDemoParams(TypedDict, total=False):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]

    to: str
