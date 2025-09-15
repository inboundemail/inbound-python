# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.domains import auth_verify_params, auth_initialize_params
from ...types.domains.auth_verify_response import AuthVerifyResponse
from ...types.domains.auth_initialize_response import AuthInitializeResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def initialize(
        self,
        id: str,
        *,
        generate_dmarc: Optional[bool] | NotGiven = NOT_GIVEN,
        generate_spf: Optional[bool] | NotGiven = NOT_GIVEN,
        mail_from_domain: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthInitializeResponse:
        """
        Initialize AWS SES authentication for a domain including DKIM, MAIL FROM domain,
        and optional SPF/DMARC records.

        Args:
          id: The ID of the domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v2/domains/{id}/auth",
            body=maybe_transform(
                {
                    "generate_dmarc": generate_dmarc,
                    "generate_spf": generate_spf,
                    "mail_from_domain": mail_from_domain,
                },
                auth_initialize_params.AuthInitializeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthInitializeResponse,
        )

    def verify(
        self,
        id: str,
        *,
        body: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthVerifyResponse:
        """Verify DNS records and check AWS SES authentication status for a domain.

        Updates
        verification status in the database.

        Args:
          id: The ID of the domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v2/domains/{id}/auth",
            body=maybe_transform(body, auth_verify_params.AuthVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthVerifyResponse,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def initialize(
        self,
        id: str,
        *,
        generate_dmarc: Optional[bool] | NotGiven = NOT_GIVEN,
        generate_spf: Optional[bool] | NotGiven = NOT_GIVEN,
        mail_from_domain: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthInitializeResponse:
        """
        Initialize AWS SES authentication for a domain including DKIM, MAIL FROM domain,
        and optional SPF/DMARC records.

        Args:
          id: The ID of the domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v2/domains/{id}/auth",
            body=await async_maybe_transform(
                {
                    "generate_dmarc": generate_dmarc,
                    "generate_spf": generate_spf,
                    "mail_from_domain": mail_from_domain,
                },
                auth_initialize_params.AuthInitializeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthInitializeResponse,
        )

    async def verify(
        self,
        id: str,
        *,
        body: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthVerifyResponse:
        """Verify DNS records and check AWS SES authentication status for a domain.

        Updates
        verification status in the database.

        Args:
          id: The ID of the domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v2/domains/{id}/auth",
            body=await async_maybe_transform(body, auth_verify_params.AuthVerifyParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthVerifyResponse,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.initialize = to_raw_response_wrapper(
            auth.initialize,
        )
        self.verify = to_raw_response_wrapper(
            auth.verify,
        )


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.initialize = async_to_raw_response_wrapper(
            auth.initialize,
        )
        self.verify = async_to_raw_response_wrapper(
            auth.verify,
        )


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.initialize = to_streamed_response_wrapper(
            auth.initialize,
        )
        self.verify = to_streamed_response_wrapper(
            auth.verify,
        )


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.initialize = async_to_streamed_response_wrapper(
            auth.initialize,
        )
        self.verify = async_to_streamed_response_wrapper(
            auth.verify,
        )
