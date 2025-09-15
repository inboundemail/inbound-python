# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EmailSendParams", "Attachment", "Tag"]


class EmailSendParams(TypedDict, total=False):
    attachments: Optional[Iterable[Attachment]]

    bcc: Union[str, SequenceNotStr[str], None]

    cc: Union[str, SequenceNotStr[str], None]

    from_: Annotated[str, PropertyInfo(alias="from")]
    """
    Now supports both "email@domain.com" and "Display Name <email@domain.com>"
    formats
    """

    headers: Optional[Dict[str, str]]

    html: Optional[str]

    body_reply_to_1: Annotated[Union[str, SequenceNotStr[str], None], PropertyInfo(alias="reply_to")]
    """snake_case (legacy)"""

    body_reply_to_2: Annotated[Union[str, SequenceNotStr[str], None], PropertyInfo(alias="replyTo")]
    """camelCase (Resend-compatible)"""

    subject: str

    tags: Optional[Iterable[Tag]]

    text: Optional[str]

    to: Union[str, SequenceNotStr[str]]


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
