# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo
from ..._models import set_pydantic_config

__all__ = ["AttachmentInputParam"]


class AttachmentInputParam(TypedDict, total=False):
    filename: Required[str]
    """Display name for the attachment (required)"""

    content: Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]
    """Base64-encoded file content (mutually exclusive with path)"""

    content_id: str
    """Content-ID for embedding images in HTML (used with cid URLs)"""

    content_type: str
    """MIME type in snake_case format (legacy support)"""

    content_type: Annotated[str, PropertyInfo(alias="contentType")]
    """MIME type in camelCase format (Resend-compatible)"""

    path: str
    """Remote file URL to fetch attachment from (mutually exclusive with content)"""


set_pydantic_config(AttachmentInputParam, {"arbitrary_types_allowed": True})
