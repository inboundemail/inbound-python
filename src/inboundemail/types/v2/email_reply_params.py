# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .attachment_input_param import AttachmentInputParam

__all__ = ["EmailReplyParams", "Tag"]


class EmailReplyParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Sender email address.

    Supports plain or display name formats. Must be from verified domain
    (agent@inbnd.dev not allowed)
    """

    attachments: Iterable[AttachmentInputParam]
    """Email attachments (max 20 files, 25MB each, 40MB total)"""

    headers: Dict[str, str]
    """Custom email headers as key-value pairs"""

    html: str
    """HTML content of reply. Either html or text required"""

    reply_all: Annotated[bool, PropertyInfo(alias="replyAll")]
    """If true, includes original CC recipients in reply"""

    subject: str
    """Email subject. Defaults to Re prefix with original subject if not provided"""

    tags: Iterable[Tag]
    """Resend-compatible metadata tags"""

    text: str
    """Plain text content of reply. Either html or text required"""

    to: Union[str, SequenceNotStr[str]]
    """Recipient address(es). Defaults to original sender if not provided"""

    api_version: Annotated[str, PropertyInfo(alias="API-Version")]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class Tag(TypedDict, total=False):
    name: str

    value: str
