# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .attachment_input_param import AttachmentInputParam

__all__ = ["EmailSendParams", "Tag"]


class EmailSendParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Sender email address.

    Supports both "email@domain.com" and "Display Name <email@domain.com>" formats.
    Must be from a verified domain or agent@inbnd.dev
    """

    subject: Required[str]
    """Email subject line (max 998 characters)"""

    to: Required[Union[str, SequenceNotStr[str]]]
    """Recipient email address(es). Can be a single string or array of strings"""

    attachments: Iterable[AttachmentInputParam]
    """Email attachments (max 20 files, 25MB each, 40MB total)"""

    bcc: Union[str, SequenceNotStr[str]]
    """Blind carbon copy recipient(s)"""

    cc: Union[str, SequenceNotStr[str]]
    """Carbon copy recipient(s)"""

    headers: Dict[str, str]
    """Custom SMTP headers as key-value pairs"""

    html: str
    """HTML email body. Either html or text must be provided"""

    body_reply_to_1: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="reply_to")]
    """Reply-To address(es) in snake_case format (legacy)"""

    body_reply_to_2: Annotated[Union[str, SequenceNotStr[str]], PropertyInfo(alias="replyTo")]
    """Reply-To address(es) in camelCase format (Resend-compatible)"""

    tags: Iterable[Tag]
    """Resend-compatible metadata tags"""

    text: str
    """Plain text email body. Either html or text must be provided"""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Tag(TypedDict, total=False):
    name: str

    value: str
