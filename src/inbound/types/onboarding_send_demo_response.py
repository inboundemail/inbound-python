# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["OnboardingSendDemoResponse"]


class OnboardingSendDemoResponse(BaseModel):
    id: Optional[str] = None
    """The ID of the sent demo email"""
