# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["EndpointDeleteResponse"]


class EndpointDeleteResponse(BaseModel):
    cleanup: str

    message: str
