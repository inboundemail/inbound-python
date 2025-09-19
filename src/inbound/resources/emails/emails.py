# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from ...types import email_send_params, email_reply_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .schedule import (
    ScheduleResource,
    AsyncScheduleResource,
    ScheduleResourceWithRawResponse,
    AsyncScheduleResourceWithRawResponse,
    ScheduleResourceWithStreamingResponse,
    AsyncScheduleResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.email_send_response import EmailSendResponse
from ...types.email_reply_response import EmailReplyResponse
from ...types.email_retrieve_response import EmailRetrieveResponse

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

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailRetrieveResponse:
        """Retrieve details of a specific sent email by its ID.

        Compatible with Resend API
        format.

        Args:
          id: The ID of the email to get the thread for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v2/emails/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailRetrieveResponse,
        )

    def reply(
        self,
        id: str,
        *,
        attachments: Optional[Iterable[email_reply_params.Attachment]] | Omit = omit,
        bcc: Union[str, SequenceNotStr[str], None] | Omit = omit,
        cc: Union[str, SequenceNotStr[str], None] | Omit = omit,
        from_: str | Omit = omit,
        from_name: Optional[str] | Omit = omit,
        headers: Optional[Dict[str, str]] | Omit = omit,
        html: Optional[str] | Omit = omit,
        body_include_original_1: Optional[bool] | Omit = omit,
        body_include_original_2: Optional[bool] | Omit = omit,
        body_reply_to_1: Union[str, SequenceNotStr[str], None] | Omit = omit,
        body_reply_to_2: Union[str, SequenceNotStr[str], None] | Omit = omit,
        simple: Optional[bool] | Omit = omit,
        subject: Optional[str] | Omit = omit,
        tags: Optional[Iterable[email_reply_params.Tag]] | Omit = omit,
        text: Optional[str] | Omit = omit,
        to: Union[str, SequenceNotStr[str], None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailReplyResponse:
        """Reply to an inbound email with proper threading support.

        Supports both simple
        mode (faster) and full mode (with attachments and original message quoting).

        Args:
          id: The ID of the email to get the thread for

          from_name: Optional sender name for display

          body_include_original_1: snake_case (legacy)

          body_include_original_2: camelCase (Resend-compatible)

          body_reply_to_1: snake_case (legacy)

          body_reply_to_2: camelCase (Resend-compatible)

          simple: Use simplified reply mode (faster, lighter)

          subject: Optional - will add "Re: " to original subject if not provided

          to: Optional - will use original sender if not provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v2/emails/{id}/reply",
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "from_": from_,
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

    def send(
        self,
        *,
        attachments: Optional[Iterable[email_send_params.Attachment]] | Omit = omit,
        bcc: Union[str, SequenceNotStr[str], None] | Omit = omit,
        cc: Union[str, SequenceNotStr[str], None] | Omit = omit,
        from_: str | Omit = omit,
        headers: Optional[Dict[str, str]] | Omit = omit,
        html: Optional[str] | Omit = omit,
        body_reply_to_1: Union[str, SequenceNotStr[str], None] | Omit = omit,
        body_reply_to_2: Union[str, SequenceNotStr[str], None] | Omit = omit,
        subject: str | Omit = omit,
        tags: Optional[Iterable[email_send_params.Tag]] | Omit = omit,
        text: Optional[str] | Omit = omit,
        to: Union[str, SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendResponse:
        """Send a single email through the Inbound API.

        Supports both simple text/HTML
        emails and emails with attachments. Compatible with Resend API format for easy
        migration.

        Args:
          from_: Now supports both "email@domain.com" and "Display Name <email@domain.com>"
              formats

          body_reply_to_1: snake_case (legacy)

          body_reply_to_2: camelCase (Resend-compatible)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/emails",
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "from_": from_,
                    "headers": headers,
                    "html": html,
                    "body_reply_to_1": body_reply_to_1,
                    "body_reply_to_2": body_reply_to_2,
                    "subject": subject,
                    "tags": tags,
                    "text": text,
                    "to": to,
                },
                email_send_params.EmailSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSendResponse,
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

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailRetrieveResponse:
        """Retrieve details of a specific sent email by its ID.

        Compatible with Resend API
        format.

        Args:
          id: The ID of the email to get the thread for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v2/emails/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailRetrieveResponse,
        )

    async def reply(
        self,
        id: str,
        *,
        attachments: Optional[Iterable[email_reply_params.Attachment]] | Omit = omit,
        bcc: Union[str, SequenceNotStr[str], None] | Omit = omit,
        cc: Union[str, SequenceNotStr[str], None] | Omit = omit,
        from_: str | Omit = omit,
        from_name: Optional[str] | Omit = omit,
        headers: Optional[Dict[str, str]] | Omit = omit,
        html: Optional[str] | Omit = omit,
        body_include_original_1: Optional[bool] | Omit = omit,
        body_include_original_2: Optional[bool] | Omit = omit,
        body_reply_to_1: Union[str, SequenceNotStr[str], None] | Omit = omit,
        body_reply_to_2: Union[str, SequenceNotStr[str], None] | Omit = omit,
        simple: Optional[bool] | Omit = omit,
        subject: Optional[str] | Omit = omit,
        tags: Optional[Iterable[email_reply_params.Tag]] | Omit = omit,
        text: Optional[str] | Omit = omit,
        to: Union[str, SequenceNotStr[str], None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailReplyResponse:
        """Reply to an inbound email with proper threading support.

        Supports both simple
        mode (faster) and full mode (with attachments and original message quoting).

        Args:
          id: The ID of the email to get the thread for

          from_name: Optional sender name for display

          body_include_original_1: snake_case (legacy)

          body_include_original_2: camelCase (Resend-compatible)

          body_reply_to_1: snake_case (legacy)

          body_reply_to_2: camelCase (Resend-compatible)

          simple: Use simplified reply mode (faster, lighter)

          subject: Optional - will add "Re: " to original subject if not provided

          to: Optional - will use original sender if not provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v2/emails/{id}/reply",
            body=await async_maybe_transform(
                {
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "from_": from_,
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

    async def send(
        self,
        *,
        attachments: Optional[Iterable[email_send_params.Attachment]] | Omit = omit,
        bcc: Union[str, SequenceNotStr[str], None] | Omit = omit,
        cc: Union[str, SequenceNotStr[str], None] | Omit = omit,
        from_: str | Omit = omit,
        headers: Optional[Dict[str, str]] | Omit = omit,
        html: Optional[str] | Omit = omit,
        body_reply_to_1: Union[str, SequenceNotStr[str], None] | Omit = omit,
        body_reply_to_2: Union[str, SequenceNotStr[str], None] | Omit = omit,
        subject: str | Omit = omit,
        tags: Optional[Iterable[email_send_params.Tag]] | Omit = omit,
        text: Optional[str] | Omit = omit,
        to: Union[str, SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendResponse:
        """Send a single email through the Inbound API.

        Supports both simple text/HTML
        emails and emails with attachments. Compatible with Resend API format for easy
        migration.

        Args:
          from_: Now supports both "email@domain.com" and "Display Name <email@domain.com>"
              formats

          body_reply_to_1: snake_case (legacy)

          body_reply_to_2: camelCase (Resend-compatible)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/emails",
            body=await async_maybe_transform(
                {
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "from_": from_,
                    "headers": headers,
                    "html": html,
                    "body_reply_to_1": body_reply_to_1,
                    "body_reply_to_2": body_reply_to_2,
                    "subject": subject,
                    "tags": tags,
                    "text": text,
                    "to": to,
                },
                email_send_params.EmailSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailSendResponse,
        )


class EmailsResourceWithRawResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.retrieve = to_raw_response_wrapper(
            emails.retrieve,
        )
        self.reply = to_raw_response_wrapper(
            emails.reply,
        )
        self.send = to_raw_response_wrapper(
            emails.send,
        )

    @cached_property
    def schedule(self) -> ScheduleResourceWithRawResponse:
        return ScheduleResourceWithRawResponse(self._emails.schedule)


class AsyncEmailsResourceWithRawResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.retrieve = async_to_raw_response_wrapper(
            emails.retrieve,
        )
        self.reply = async_to_raw_response_wrapper(
            emails.reply,
        )
        self.send = async_to_raw_response_wrapper(
            emails.send,
        )

    @cached_property
    def schedule(self) -> AsyncScheduleResourceWithRawResponse:
        return AsyncScheduleResourceWithRawResponse(self._emails.schedule)


class EmailsResourceWithStreamingResponse:
    def __init__(self, emails: EmailsResource) -> None:
        self._emails = emails

        self.retrieve = to_streamed_response_wrapper(
            emails.retrieve,
        )
        self.reply = to_streamed_response_wrapper(
            emails.reply,
        )
        self.send = to_streamed_response_wrapper(
            emails.send,
        )

    @cached_property
    def schedule(self) -> ScheduleResourceWithStreamingResponse:
        return ScheduleResourceWithStreamingResponse(self._emails.schedule)


class AsyncEmailsResourceWithStreamingResponse:
    def __init__(self, emails: AsyncEmailsResource) -> None:
        self._emails = emails

        self.retrieve = async_to_streamed_response_wrapper(
            emails.retrieve,
        )
        self.reply = async_to_streamed_response_wrapper(
            emails.reply,
        )
        self.send = async_to_streamed_response_wrapper(
            emails.send,
        )

    @cached_property
    def schedule(self) -> AsyncScheduleResourceWithStreamingResponse:
        return AsyncScheduleResourceWithStreamingResponse(self._emails.schedule)
