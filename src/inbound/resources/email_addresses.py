# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import email_address_list_params, email_address_create_params, email_address_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.email_address_list_response import EmailAddressListResponse
from ..types.email_address_create_response import EmailAddressCreateResponse
from ..types.email_address_delete_response import EmailAddressDeleteResponse
from ..types.email_address_update_response import EmailAddressUpdateResponse
from ..types.email_address_retrieve_response import EmailAddressRetrieveResponse

__all__ = ["EmailAddressesResource", "AsyncEmailAddressesResource"]


class EmailAddressesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmailAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return EmailAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
        """
        return EmailAddressesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        address: str | NotGiven = NOT_GIVEN,
        domain_id: str | NotGiven = NOT_GIVEN,
        endpoint_id: Optional[str] | NotGiven = NOT_GIVEN,
        is_active: Optional[bool] | NotGiven = NOT_GIVEN,
        webhook_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailAddressCreateResponse:
        """
        Create a new email address for receiving emails and configure AWS SES receipt
        rules automatically.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/email-addresses",
            body=maybe_transform(
                {
                    "address": address,
                    "domain_id": domain_id,
                    "endpoint_id": endpoint_id,
                    "is_active": is_active,
                    "webhook_id": webhook_id,
                },
                email_address_create_params.EmailAddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailAddressCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailAddressRetrieveResponse:
        """
        Get detailed information about a specific email address including domain and
        routing configuration.

        Args:
          id: The ID of the email address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v2/email-addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailAddressRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        endpoint_id: Optional[str] | NotGiven = NOT_GIVEN,
        is_active: Optional[bool] | NotGiven = NOT_GIVEN,
        webhook_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailAddressUpdateResponse:
        """
        Update an email address's routing configuration (endpoint, webhook, or disable
        routing).

        Args:
          id: The ID of the email address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/v2/email-addresses/{id}",
            body=maybe_transform(
                {
                    "endpoint_id": endpoint_id,
                    "is_active": is_active,
                    "webhook_id": webhook_id,
                },
                email_address_update_params.EmailAddressUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailAddressUpdateResponse,
        )

    def list(
        self,
        *,
        domain_id: str | NotGiven = NOT_GIVEN,
        is_active: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        is_receipt_rule_configured: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailAddressListResponse:
        """
        Retrieve all email addresses for the authenticated user with filtering and
        pagination options.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/email-addresses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain_id": domain_id,
                        "is_active": is_active,
                        "is_receipt_rule_configured": is_receipt_rule_configured,
                        "limit": limit,
                        "offset": offset,
                    },
                    email_address_list_params.EmailAddressListParams,
                ),
            ),
            cast_to=EmailAddressListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailAddressDeleteResponse:
        """
        Permanently delete an email address and update AWS SES receipt rules
        accordingly.

        Args:
          id: The ID of the email address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v2/email-addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailAddressDeleteResponse,
        )


class AsyncEmailAddressesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmailAddressesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailAddressesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailAddressesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
        """
        return AsyncEmailAddressesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        address: str | NotGiven = NOT_GIVEN,
        domain_id: str | NotGiven = NOT_GIVEN,
        endpoint_id: Optional[str] | NotGiven = NOT_GIVEN,
        is_active: Optional[bool] | NotGiven = NOT_GIVEN,
        webhook_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailAddressCreateResponse:
        """
        Create a new email address for receiving emails and configure AWS SES receipt
        rules automatically.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/email-addresses",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "domain_id": domain_id,
                    "endpoint_id": endpoint_id,
                    "is_active": is_active,
                    "webhook_id": webhook_id,
                },
                email_address_create_params.EmailAddressCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailAddressCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailAddressRetrieveResponse:
        """
        Get detailed information about a specific email address including domain and
        routing configuration.

        Args:
          id: The ID of the email address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v2/email-addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailAddressRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        endpoint_id: Optional[str] | NotGiven = NOT_GIVEN,
        is_active: Optional[bool] | NotGiven = NOT_GIVEN,
        webhook_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailAddressUpdateResponse:
        """
        Update an email address's routing configuration (endpoint, webhook, or disable
        routing).

        Args:
          id: The ID of the email address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/v2/email-addresses/{id}",
            body=await async_maybe_transform(
                {
                    "endpoint_id": endpoint_id,
                    "is_active": is_active,
                    "webhook_id": webhook_id,
                },
                email_address_update_params.EmailAddressUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailAddressUpdateResponse,
        )

    async def list(
        self,
        *,
        domain_id: str | NotGiven = NOT_GIVEN,
        is_active: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        is_receipt_rule_configured: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailAddressListResponse:
        """
        Retrieve all email addresses for the authenticated user with filtering and
        pagination options.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/email-addresses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain_id": domain_id,
                        "is_active": is_active,
                        "is_receipt_rule_configured": is_receipt_rule_configured,
                        "limit": limit,
                        "offset": offset,
                    },
                    email_address_list_params.EmailAddressListParams,
                ),
            ),
            cast_to=EmailAddressListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailAddressDeleteResponse:
        """
        Permanently delete an email address and update AWS SES receipt rules
        accordingly.

        Args:
          id: The ID of the email address

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v2/email-addresses/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailAddressDeleteResponse,
        )


class EmailAddressesResourceWithRawResponse:
    def __init__(self, email_addresses: EmailAddressesResource) -> None:
        self._email_addresses = email_addresses

        self.create = to_raw_response_wrapper(
            email_addresses.create,
        )
        self.retrieve = to_raw_response_wrapper(
            email_addresses.retrieve,
        )
        self.update = to_raw_response_wrapper(
            email_addresses.update,
        )
        self.list = to_raw_response_wrapper(
            email_addresses.list,
        )
        self.delete = to_raw_response_wrapper(
            email_addresses.delete,
        )


class AsyncEmailAddressesResourceWithRawResponse:
    def __init__(self, email_addresses: AsyncEmailAddressesResource) -> None:
        self._email_addresses = email_addresses

        self.create = async_to_raw_response_wrapper(
            email_addresses.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            email_addresses.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            email_addresses.update,
        )
        self.list = async_to_raw_response_wrapper(
            email_addresses.list,
        )
        self.delete = async_to_raw_response_wrapper(
            email_addresses.delete,
        )


class EmailAddressesResourceWithStreamingResponse:
    def __init__(self, email_addresses: EmailAddressesResource) -> None:
        self._email_addresses = email_addresses

        self.create = to_streamed_response_wrapper(
            email_addresses.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            email_addresses.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            email_addresses.update,
        )
        self.list = to_streamed_response_wrapper(
            email_addresses.list,
        )
        self.delete = to_streamed_response_wrapper(
            email_addresses.delete,
        )


class AsyncEmailAddressesResourceWithStreamingResponse:
    def __init__(self, email_addresses: AsyncEmailAddressesResource) -> None:
        self._email_addresses = email_addresses

        self.create = async_to_streamed_response_wrapper(
            email_addresses.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            email_addresses.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            email_addresses.update,
        )
        self.list = async_to_streamed_response_wrapper(
            email_addresses.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            email_addresses.delete,
        )
