# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EndpointTestResponse"]


class EndpointTestResponse(BaseModel):
    message: str

    response_time: float = FieldInfo(alias="responseTime")

    success: bool

    error: Optional[str] = None

    response_body: Optional[str] = FieldInfo(alias="responseBody", default=None)

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    test_payload: Optional[str] = FieldInfo(alias="testPayload", default=None)

    webhook_format: Optional[Literal["inbound", "discord", "slack", "undefined"]] = FieldInfo(
        alias="webhookFormat", default=None
    )
