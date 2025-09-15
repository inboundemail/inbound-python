# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailRetrieveResponse"]


class EmailRetrieveResponse(BaseModel):
    id: Optional[str] = None

    bcc: Optional[List[object]] = None

    cc: Optional[List[object]] = None

    created_at: Optional[str] = None

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    html: Optional[str] = None

    last_event: Optional[str] = None

    object: Optional[Literal["email"]] = None

    reply_to: Optional[List[builtins.object]] = None

    subject: Optional[str] = None

    text: Optional[str] = None

    to: Optional[List[str]] = None
