# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmailResendParams"]


class EmailResendParams(TypedDict, total=False):
    endpoint_id: Required[Annotated[str, PropertyInfo(alias="endpointId")]]
    """The ID of the endpoint to deliver the email to (nanoid format).

    Endpoint must be active and belong to user
    """
