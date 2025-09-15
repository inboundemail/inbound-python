# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EndpointUpdateResponse"]


class EndpointUpdateResponse(BaseModel):
    id: Optional[str] = None

    config: Optional[object] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    description: Optional[str] = None

    group_emails: Optional[List[str]] = FieldInfo(alias="groupEmails", default=None)

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    name: Optional[str] = None

    type: Optional[Literal["webhook", "email", "email_group"]] = None

    updated_at: Optional[str] = FieldInfo(alias="updatedAt", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
