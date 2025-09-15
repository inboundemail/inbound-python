# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["EmailCreateParams"]


class EmailCreateParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="from")]]

    subject: Required[str]

    to: Required[str]

    attachments: SequenceNotStr[str]

    bcc: str

    cc: str

    headers: str

    html: str

    body_reply_to_1: Annotated[str, PropertyInfo(alias="reply_to")]

    body_reply_to_2: Annotated[str, PropertyInfo(alias="replyTo")]

    tags: str

    text: str
