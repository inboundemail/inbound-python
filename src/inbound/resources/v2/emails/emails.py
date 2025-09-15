# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .schedule import (
    ScheduleResource,
    AsyncScheduleResource,
    ScheduleResourceWithRawResponse,
    AsyncScheduleResourceWithRawResponse,
    ScheduleResourceWithStreamingResponse,
    AsyncScheduleResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, SequenceNotStr
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v2 import email_reply_params, email_create_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.email_reply_response import EmailReplyResponse
from ....types.v2.email_create_response import EmailCreateResponse
from ....types.v2.email_retrieve_response import EmailRetrieveResponse

__all__ = ["EmailsResource", "AsyncEmailsResource"]


class EmailsResource(SyncAPIResource):
    @cached_property
    def schedule(self) -> ScheduleResource:
        return ScheduleResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return EmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
        """
        return EmailsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        from_: str,
        subject: str,
        to: str,
        attachments: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        bcc: str | NotGiven = NOT_GIVEN,
        cc: str | NotGiven = NOT_GIVEN,
        headers: str | NotGiven = NOT_GIVEN,
        html: str | NotGiven = NOT_GIVEN,
        body_reply_to_1: str | NotGiven = NOT_GIVEN,
        body_reply_to_2: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailCreateResponse:
        """
        POST /emails

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/emails",
            body=maybe_transform(
                {
                    "from_": from_,
                    "subject": subject,
                    "to": to,
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "headers": headers,
                    "html": html,
                    "body_reply_to_1": body_reply_to_1,
                    "body_reply_to_2": body_reply_to_2,
                    "tags": tags,
                    "text": text,
                },
                email_create_params.EmailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailCreateResponse,
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
    ) -> EmailRetrieveResponse:
        """
        GET /emails/{id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v2/emails/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailRetrieveResponse,
        )

    def reply(
        self,
        id: str,
        *,
        from_: str,
        attachments: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        bcc: str | NotGiven = NOT_GIVEN,
        cc: str | NotGiven = NOT_GIVEN,
        from_name: str | NotGiven = NOT_GIVEN,
        headers: str | NotGiven = NOT_GIVEN,
        html: str | NotGiven = NOT_GIVEN,
        body_include_original_1: bool | NotGiven = NOT_GIVEN,
        body_include_original_2: bool | NotGiven = NOT_GIVEN,
        body_reply_to_1: str | NotGiven = NOT_GIVEN,
        body_reply_to_2: str | NotGiven = NOT_GIVEN,
        simple: bool | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailReplyResponse:
        """
        POST /emails/{id}/reply

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v2/emails/{id}/reply",
            body=maybe_transform(
                {
                    "from_": from_,
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "from_name": from_name,
                    "headers": headers,
                    "html": html,
                    "body_include_original_1": body_include_original_1,
                    "body_include_original_2": body_include_original_2,
                    "body_reply_to_1": body_reply_to_1,
                    "body_reply_to_2": body_reply_to_2,
                    "simple": simple,
                    "subject": subject,
                    "tags": tags,
                    "text": text,
                    "to": to,
                },
                email_reply_params.EmailReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailReplyResponse,
        )


class AsyncEmailsResource(AsyncAPIResource):
    @cached_property
    def schedule(self) -> AsyncScheduleResource:
        return AsyncScheduleResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
        """
        return AsyncEmailsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        from_: str,
        subject: str,
        to: str,
        attachments: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        bcc: str | NotGiven = NOT_GIVEN,
        cc: str | NotGiven = NOT_GIVEN,
        headers: str | NotGiven = NOT_GIVEN,
        html: str | NotGiven = NOT_GIVEN,
        body_reply_to_1: str | NotGiven = NOT_GIVEN,
        body_reply_to_2: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailCreateResponse:
        """
        POST /emails

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/emails",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "subject": subject,
                    "to": to,
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "headers": headers,
                    "html": html,
                    "body_reply_to_1": body_reply_to_1,
                    "body_reply_to_2": body_reply_to_2,
                    "tags": tags,
                    "text": text,
                },
                email_create_params.EmailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailCreateResponse,
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
    ) -> EmailRetrieveResponse:
        """
        GET /emails/{id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v2/emails/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailRetrieveResponse,
        )

    async def reply(
        self,
        id: str,
        *,
        from_: str,
        attachments: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        bcc: str | NotGiven = NOT_GIVEN,
        cc: str | NotGiven = NOT_GIVEN,
        from_name: str | NotGiven = NOT_GIVEN,
        headers: str | NotGiven = NOT_GIVEN,
        html: str | NotGiven = NOT_GIVEN,
        body_include_original_1: bool | NotGiven = NOT_GIVEN,
        body_include_original_2: bool | NotGiven = NOT_GIVEN,
        body_reply_to_1: str | NotGiven = NOT_GIVEN,
        body_reply_to_2: str | NotGiven = NOT_GIVEN,
        simple: bool | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmailReplyResponse:
        """
        POST /emails/{id}/reply

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v2/emails/{id}/reply",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "from_name": from_name,
                    "headers": headers,
                    "html": html,
                    "body_include_original_1": body_include_original_1,
                    "body_include_original_2": body_include_original_2,
                    "body_reply_to_1": body_reply_to_1,
                    "body_reply_to_2": body_reply_to_2,
                    "simple": simple,
                    "subject": subject,
                    "tags": tags,
                    "text": text,
                    "to": to,
                },
                email_reply_params.EmailReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailReplyResponse,
        )


class EmailsResourceWithRawResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.create = to_raw_response_wrapper(
            emails.create,
        )
        self.retrieve = to_raw_response_wrapper(
            emails.retrieve,
        )
        self.reply = to_raw_response_wrapper(
            emails.reply,
        )

    @cached_property
    def schedule(self) -> ScheduleResourceWithRawResponse:
        return ScheduleResourceWithRawResponse(self._emails.schedule)


class AsyncEmailsResourceWithRawResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.create = async_to_raw_response_wrapper(
            emails.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            emails.retrieve,
        )
        self.reply = async_to_raw_response_wrapper(
            emails.reply,
        )

    @cached_property
    def schedule(self) -> AsyncScheduleResourceWithRawResponse:
        return AsyncScheduleResourceWithRawResponse(self._emails.schedule)


class EmailsResourceWithStreamingResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.create = to_streamed_response_wrapper(
            emails.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            emails.retrieve,
        )
        self.reply = to_streamed_response_wrapper(
            emails.reply,
        )

    @cached_property
    def schedule(self) -> ScheduleResourceWithStreamingResponse:
        return ScheduleResourceWithStreamingResponse(self._emails.schedule)


class AsyncEmailsResourceWithStreamingResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.create = async_to_streamed_response_wrapper(
            emails.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            emails.retrieve,
        )
        self.reply = async_to_streamed_response_wrapper(
            emails.reply,
        )

    @cached_property
    def schedule(self) -> AsyncScheduleResourceWithStreamingResponse:
        return AsyncScheduleResourceWithStreamingResponse(self._emails.schedule)
