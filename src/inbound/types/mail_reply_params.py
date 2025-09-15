# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MailReplyParams", "Attachment"]


class MailReplyParams(TypedDict, total=False):
    attachments: Optional[Iterable[Attachment]]

    email_id: Annotated[str, PropertyInfo(alias="emailId")]

    html_body: Annotated[Optional[str], PropertyInfo(alias="htmlBody")]

    subject: str

    text_body: Annotated[Optional[str], PropertyInfo(alias="textBody")]

    to: str


class Attachment(TypedDict, total=False):
    content: str

    content_type: Annotated[str, PropertyInfo(alias="contentType")]

    filename: str
