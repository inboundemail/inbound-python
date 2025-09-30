# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmailRetryDeliveryParams"]


class EmailRetryDeliveryParams(TypedDict, total=False):
    delivery_id: Required[Annotated[str, PropertyInfo(alias="deliveryId")]]
    """The ID of the delivery record to retry (nanoid format).

    Must belong to the specified email
    """
