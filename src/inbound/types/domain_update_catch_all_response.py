# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DomainUpdateCatchAllResponse", "CatchAllEndpoint"]


class CatchAllEndpoint(BaseModel):
    id: Optional[str] = None

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    name: Optional[str] = None

    type: Optional[str] = None


class DomainUpdateCatchAllResponse(BaseModel):
    id: Optional[str] = None

    aws_configuration_warning: Optional[str] = FieldInfo(alias="awsConfigurationWarning", default=None)

    catch_all_endpoint: Optional[CatchAllEndpoint] = FieldInfo(alias="catchAllEndpoint", default=None)

    catch_all_endpoint_id: Optional[str] = FieldInfo(alias="catchAllEndpointId", default=None)

    domain: Optional[str] = None

    is_catch_all_enabled: Optional[bool] = FieldInfo(alias="isCatchAllEnabled", default=None)

    receipt_rule_name: Optional[str] = FieldInfo(alias="receiptRuleName", default=None)

    status: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
