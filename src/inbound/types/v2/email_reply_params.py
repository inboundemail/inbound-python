# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["EmailReplyParams"]


class EmailReplyParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]

    attachments: SequenceNotStr[str]

    bcc: str

    cc: str

    from_name: str

    headers: str

    html: str

    body_include_original_1: Annotated[bool, PropertyInfo(alias="include_original")]

    body_include_original_2: Annotated[bool, PropertyInfo(alias="includeOriginal")]

    body_reply_to_1: Annotated[str, PropertyInfo(alias="reply_to")]

    body_reply_to_2: Annotated[str, PropertyInfo(alias="replyTo")]

    simple: bool

    subject: str

    tags: str

    text: str

    to: str
