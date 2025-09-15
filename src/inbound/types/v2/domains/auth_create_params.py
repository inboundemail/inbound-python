# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AuthCreateParams"]


class AuthCreateParams(TypedDict, total=False):
    generate_dmarc: Annotated[bool, PropertyInfo(alias="generateDmarc")]

    generate_spf: Annotated[bool, PropertyInfo(alias="generateSpf")]

    mail_from_domain: Annotated[str, PropertyInfo(alias="mailFromDomain")]
