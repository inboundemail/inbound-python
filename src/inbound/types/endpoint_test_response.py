# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EndpointTestResponse"]


class EndpointTestResponse(BaseModel):
    error: Optional[str] = None

    message: Optional[str] = None

    response_body: Optional[str] = FieldInfo(alias="responseBody", default=None)

    response_time: Optional[float] = FieldInfo(alias="responseTime", default=None)

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)

    success: Optional[bool] = None

    test_payload: Optional[object] = FieldInfo(alias="testPayload", default=None)

    webhook_format: Optional[Literal["inbound", "discord", "slack"]] = FieldInfo(alias="webhookFormat", default=None)
