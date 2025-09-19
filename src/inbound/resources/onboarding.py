# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import onboarding_send_demo_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.onboarding_send_demo_response import OnboardingSendDemoResponse
from ..types.onboarding_check_reply_response import OnboardingCheckReplyResponse
from ..types.onboarding_handle_webhook_response import OnboardingHandleWebhookResponse

__all__ = ["OnboardingResource", "AsyncOnboardingResource"]


class OnboardingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OnboardingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return OnboardingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnboardingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnboardingCheckReplyResponse:
        """Check if the user has received a reply to their onboarding demo email.

        Used for
        polling during the onboarding flow.
        """
        return self._get(
            "/v2/onboarding/check-reply",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnboardingCheckReplyResponse,
        )

    def handle_webhook(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnboardingHandleWebhookResponse:
        """Process webhook events for onboarding demo emails.

        Updates demo status when
        replies are received.
        """
        return self._post(
            "/v2/onboarding/webhook",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnboardingHandleWebhookResponse,
        )

    def send_demo(
        self,
        *,
        api_key: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnboardingSendDemoResponse:
        """Send a demo email to test the SDK integration during onboarding.

        The recipient
        can reply to complete the onboarding flow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/onboarding/demo",
            body=maybe_transform(
                {
                    "api_key": api_key,
                    "to": to,
                },
                onboarding_send_demo_params.OnboardingSendDemoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnboardingSendDemoResponse,
        )


class AsyncOnboardingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOnboardingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOnboardingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnboardingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnboardingCheckReplyResponse:
        """Check if the user has received a reply to their onboarding demo email.

        Used for
        polling during the onboarding flow.
        """
        return await self._get(
            "/v2/onboarding/check-reply",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnboardingCheckReplyResponse,
        )

    async def handle_webhook(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnboardingHandleWebhookResponse:
        """Process webhook events for onboarding demo emails.

        Updates demo status when
        replies are received.
        """
        return await self._post(
            "/v2/onboarding/webhook",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnboardingHandleWebhookResponse,
        )

    async def send_demo(
        self,
        *,
        api_key: str | Omit = omit,
        to: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OnboardingSendDemoResponse:
        """Send a demo email to test the SDK integration during onboarding.

        The recipient
        can reply to complete the onboarding flow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/onboarding/demo",
            body=await async_maybe_transform(
                {
                    "api_key": api_key,
                    "to": to,
                },
                onboarding_send_demo_params.OnboardingSendDemoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OnboardingSendDemoResponse,
        )


class OnboardingResourceWithRawResponse:
    def __init__(self, onboarding: OnboardingResource) -> None:
        self._onboarding = onboarding

        self.check_reply = to_raw_response_wrapper(
            onboarding.check_reply,
        )
        self.handle_webhook = to_raw_response_wrapper(
            onboarding.handle_webhook,
        )
        self.send_demo = to_raw_response_wrapper(
            onboarding.send_demo,
        )


class AsyncOnboardingResourceWithRawResponse:
    def __init__(self, onboarding: AsyncOnboardingResource) -> None:
        self._onboarding = onboarding

        self.check_reply = async_to_raw_response_wrapper(
            onboarding.check_reply,
        )
        self.handle_webhook = async_to_raw_response_wrapper(
            onboarding.handle_webhook,
        )
        self.send_demo = async_to_raw_response_wrapper(
            onboarding.send_demo,
        )


class OnboardingResourceWithStreamingResponse:
    def __init__(self, onboarding: OnboardingResource) -> None:
        self._onboarding = onboarding

        self.check_reply = to_streamed_response_wrapper(
            onboarding.check_reply,
        )
        self.handle_webhook = to_streamed_response_wrapper(
            onboarding.handle_webhook,
        )
        self.send_demo = to_streamed_response_wrapper(
            onboarding.send_demo,
        )


class AsyncOnboardingResourceWithStreamingResponse:
    def __init__(self, onboarding: AsyncOnboardingResource) -> None:
        self._onboarding = onboarding

        self.check_reply = async_to_streamed_response_wrapper(
            onboarding.check_reply,
        )
        self.handle_webhook = async_to_streamed_response_wrapper(
            onboarding.handle_webhook,
        )
        self.send_demo = async_to_streamed_response_wrapper(
            onboarding.send_demo,
        )
