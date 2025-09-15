# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MailCreateParams"]


class MailCreateParams(TypedDict, total=False):
    email_id: Required[Annotated[str, PropertyInfo(alias="emailId")]]

    subject: Required[str]

    to: Required[str]

    attachments: str

    html_body: Annotated[str, PropertyInfo(alias="htmlBody")]

    text_body: Annotated[str, PropertyInfo(alias="textBody")]
