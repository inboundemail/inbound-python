# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["OnboardingResource", "AsyncOnboardingResource"]


class OnboardingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OnboardingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inboundemail/inbound-python#accessing-raw-response-data-eg-headers
        """
        return OnboardingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnboardingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inboundemail/inbound-python#with_streaming_response
        """
        return OnboardingResourceWithStreamingResponse(self)

    def check_reply(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """GET /onboarding/check-reply"""
        return self._get(
            "/api/v2/onboarding/check-reply",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def demo(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """POST /onboarding/demo"""
        return self._post(
            "/api/v2/onboarding/demo",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def webhook(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """POST /onboarding/webhook"""
        return self._post(
            "/api/v2/onboarding/webhook",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOnboardingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOnboardingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inboundemail/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOnboardingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnboardingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inboundemail/inbound-python#with_streaming_response
        """
        return AsyncOnboardingResourceWithStreamingResponse(self)

    async def check_reply(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """GET /onboarding/check-reply"""
        return await self._get(
            "/api/v2/onboarding/check-reply",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def demo(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """POST /onboarding/demo"""
        return await self._post(
            "/api/v2/onboarding/demo",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def webhook(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """POST /onboarding/webhook"""
        return await self._post(
            "/api/v2/onboarding/webhook",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OnboardingResourceWithRawResponse:
    def __init__(self, onboarding: OnboardingResource) -> None:
        self._onboarding = onboarding

        self.check_reply = to_raw_response_wrapper(
            onboarding.check_reply,
        )
        self.demo = to_raw_response_wrapper(
            onboarding.demo,
        )
        self.webhook = to_raw_response_wrapper(
            onboarding.webhook,
        )


class AsyncOnboardingResourceWithRawResponse:
    def __init__(self, onboarding: AsyncOnboardingResource) -> None:
        self._onboarding = onboarding

        self.check_reply = async_to_raw_response_wrapper(
            onboarding.check_reply,
        )
        self.demo = async_to_raw_response_wrapper(
            onboarding.demo,
        )
        self.webhook = async_to_raw_response_wrapper(
            onboarding.webhook,
        )


class OnboardingResourceWithStreamingResponse:
    def __init__(self, onboarding: OnboardingResource) -> None:
        self._onboarding = onboarding

        self.check_reply = to_streamed_response_wrapper(
            onboarding.check_reply,
        )
        self.demo = to_streamed_response_wrapper(
            onboarding.demo,
        )
        self.webhook = to_streamed_response_wrapper(
            onboarding.webhook,
        )


class AsyncOnboardingResourceWithStreamingResponse:
    def __init__(self, onboarding: AsyncOnboardingResource) -> None:
        self._onboarding = onboarding

        self.check_reply = async_to_streamed_response_wrapper(
            onboarding.check_reply,
        )
        self.demo = async_to_streamed_response_wrapper(
            onboarding.demo,
        )
        self.webhook = async_to_streamed_response_wrapper(
            onboarding.webhook,
        )
