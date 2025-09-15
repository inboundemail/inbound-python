# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AuthInitializeParams"]


class AuthInitializeParams(TypedDict, total=False):
    generate_dmarc: Annotated[Optional[bool], PropertyInfo(alias="generateDmarc")]

    generate_spf: Annotated[Optional[bool], PropertyInfo(alias="generateSpf")]

    mail_from_domain: Annotated[Optional[str], PropertyInfo(alias="mailFromDomain")]
