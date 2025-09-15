# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EmailReplyParams", "Attachment", "Tag"]


class EmailReplyParams(TypedDict, total=False):
    attachments: Optional[Iterable[Attachment]]

    bcc: Union[str, SequenceNotStr[str], None]

    cc: Union[str, SequenceNotStr[str], None]

    from_: Annotated[str, PropertyInfo(alias="from")]

    from_name: Optional[str]
    """Optional sender name for display"""

    headers: Optional[Dict[str, str]]

    html: Optional[str]

    body_include_original_1: Annotated[Optional[bool], PropertyInfo(alias="include_original")]
    """snake_case (legacy)"""

    body_include_original_2: Annotated[Optional[bool], PropertyInfo(alias="includeOriginal")]
    """camelCase (Resend-compatible)"""

    body_reply_to_1: Annotated[Union[str, SequenceNotStr[str], None], PropertyInfo(alias="reply_to")]
    """snake_case (legacy)"""

    body_reply_to_2: Annotated[Union[str, SequenceNotStr[str], None], PropertyInfo(alias="replyTo")]
    """camelCase (Resend-compatible)"""

    simple: Optional[bool]
    """Use simplified reply mode (faster, lighter)"""

    subject: Optional[str]
    """Optional - will add "Re: " to original subject if not provided"""

    tags: Optional[Iterable[Tag]]

    text: Optional[str]

    to: Union[str, SequenceNotStr[str], None]
    """Optional - will use original sender if not provided"""


class Attachment(TypedDict, total=False):
    content: Optional[str]
    """Base64 encoded content"""

    content_id: Optional[str]
    """Content ID for embedding (e.g., "logo" for <img src="cid:logo">)"""

    content_type: Optional[str]
    """snake_case (legacy)"""

    content_type: Annotated[Optional[str], PropertyInfo(alias="contentType")]
    """camelCase (Resend-compatible)"""

    filename: str
    """Required display name"""

    path: Optional[str]
    """Remote file URL"""


class Tag(TypedDict, total=False):
    name: str

    value: str
