# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from .schedule import (
    ScheduleResource,
    AsyncScheduleResource,
    ScheduleResourceWithRawResponse,
    AsyncScheduleResourceWithRawResponse,
    ScheduleResourceWithStreamingResponse,
    AsyncScheduleResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ....types.v2 import email_send_params, email_reply_params, email_resend_params, email_retry_delivery_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.email_send_response import EmailSendResponse
from ....types.v2.email_reply_response import EmailReplyResponse
from ....types.v2.email_resend_response import EmailResendResponse
from ....types.v2.attachment_input_param import AttachmentInputParam
from ....types.v2.email_retrieve_response import EmailRetrieveResponse
from ....types.v2.email_retry_delivery_response import EmailRetryDeliveryResponse

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

        For more information, see https://www.github.com/inboundemail/inbound-python#accessing-raw-response-data-eg-headers
        """
        return EmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inboundemail/inbound-python#with_streaming_response
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
        """Retrieves a single sent email by its ID.

        Returns email metadata including
        recipients, subject, content, and delivery status. Only emails belonging to the
        authenticated user can be accessed. Response format is Resend-compatible for
        easy migration from other email services.

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
        attachments: Iterable[AttachmentInputParam] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        html: str | Omit = omit,
        reply_all: bool | Omit = omit,
        subject: str | Omit = omit,
        tags: Iterable[email_reply_params.Tag] | Omit = omit,
        text: str | Omit = omit,
        to: Union[str, SequenceNotStr[str]] | Omit = omit,
        api_version: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailReplyResponse:
        """
        Sends a reply to an inbound email or email thread with proper RFC 5322 email
        threading headers (In-Reply-To, References). Supports both direct email IDs and
        thread IDs - when given a thread ID, automatically replies to the latest message
        in the thread. Includes Reply All functionality, automatic thread association,
        attachment support (up to 25MB each, 40MB total), and idempotent operations.
        Sender domain must be verified (agent@inbnd.dev not allowed for replies).
        Compatible with Resend API format.

        Args:
          from_: Sender email address. Supports plain or display name formats. Must be from
              verified domain (agent@inbnd.dev not allowed)

          attachments: Email attachments (max 20 files, 25MB each, 40MB total)

          headers: Custom email headers as key-value pairs

          html: HTML content of reply. Either html or text required

          reply_all: If true, includes original CC recipients in reply

          subject: Email subject. Defaults to Re prefix with original subject if not provided

          tags: Resend-compatible metadata tags

          text: Plain text content of reply. Either html or text required

          to: Recipient address(es). Defaults to original sender if not provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "API-Version": api_version,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            f"/api/v2/emails/{id}/reply",
            body=maybe_transform(
                {
                    "from_": from_,
                    "attachments": attachments,
                    "headers": headers,
                    "html": html,
                    "reply_all": reply_all,
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

    def resend(
        self,
        id: str,
        *,
        endpoint_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailResendResponse:
        """Resends a previously received inbound email to a specific endpoint.

        Useful for
        re-delivering emails to webhooks or forwarding addresses after initial delivery.
        Creates a new delivery record and tracks the attempt. Supports both webhook and
        email forwarding endpoints. Endpoint must be active and belong to the
        authenticated user. Note: Requires session authentication (API keys not
        supported for this endpoint).

        Args:
          endpoint_id: The ID of the endpoint to deliver the email to (nanoid format). Endpoint must be
              active and belong to user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v2/emails/{id}/resend",
            body=maybe_transform({"endpoint_id": endpoint_id}, email_resend_params.EmailResendParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailResendResponse,
        )

    def retry_delivery(
        self,
        id: str,
        *,
        delivery_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailRetryDeliveryResponse:
        """Retries endpoint delivery for a previously failed or successful delivery.

        Allows
        re-attempting delivery to webhooks or forwarding addresses regardless of current
        status. Uses the email router to re-process the email and create new delivery
        records. Increments attempt counter and updates delivery timestamps. Endpoint
        must still exist and be active. Note: Requires session authentication (API keys
        not supported).

        Args:
          delivery_id: The ID of the delivery record to retry (nanoid format). Must belong to the
              specified email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/api/v2/emails/{id}/retry-delivery",
            body=maybe_transform({"delivery_id": delivery_id}, email_retry_delivery_params.EmailRetryDeliveryParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailRetryDeliveryResponse,
        )

    def send(
        self,
        *,
        from_: str,
        subject: str,
        to: Union[str, SequenceNotStr[str]],
        attachments: Iterable[AttachmentInputParam] | Omit = omit,
        bcc: Union[str, SequenceNotStr[str]] | Omit = omit,
        cc: Union[str, SequenceNotStr[str]] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        html: str | Omit = omit,
        body_reply_to_1: Union[str, SequenceNotStr[str]] | Omit = omit,
        body_reply_to_2: Union[str, SequenceNotStr[str]] | Omit = omit,
        tags: Iterable[email_send_params.Tag] | Omit = omit,
        text: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendResponse:
        """
        Send an email through the Inbound API with comprehensive support for HTML/text
        content, file attachments (up to 25MB each, 40MB total), custom SMTP headers,
        CC/BCC recipients, and idempotent operations. Sender domain must be verified
        unless using the special agent@inbnd.dev address (available to all users).
        Includes usage tracking and rate limiting via Autumn. Email delivery powered by
        AWS SES with full RFC 5322 compliance. Compatible with Resend API format for
        easy migration.

        Args:
          from_: Sender email address. Supports both "email@domain.com" and "Display Name
              <email@domain.com>" formats. Must be from a verified domain or agent@inbnd.dev

          subject: Email subject line (max 998 characters)

          to: Recipient email address(es). Can be a single string or array of strings

          attachments: Email attachments (max 20 files, 25MB each, 40MB total)

          bcc: Blind carbon copy recipient(s)

          cc: Carbon copy recipient(s)

          headers: Custom SMTP headers as key-value pairs

          html: HTML email body. Either html or text must be provided

          body_reply_to_1: Reply-To address(es) in snake_case format (legacy)

          body_reply_to_2: Reply-To address(es) in camelCase format (Resend-compatible)

          tags: Resend-compatible metadata tags

          text: Plain text email body. Either html or text must be provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
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

        For more information, see https://www.github.com/inboundemail/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inboundemail/inbound-python#with_streaming_response
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
        """Retrieves a single sent email by its ID.

        Returns email metadata including
        recipients, subject, content, and delivery status. Only emails belonging to the
        authenticated user can be accessed. Response format is Resend-compatible for
        easy migration from other email services.

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
        attachments: Iterable[AttachmentInputParam] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        html: str | Omit = omit,
        reply_all: bool | Omit = omit,
        subject: str | Omit = omit,
        tags: Iterable[email_reply_params.Tag] | Omit = omit,
        text: str | Omit = omit,
        to: Union[str, SequenceNotStr[str]] | Omit = omit,
        api_version: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailReplyResponse:
        """
        Sends a reply to an inbound email or email thread with proper RFC 5322 email
        threading headers (In-Reply-To, References). Supports both direct email IDs and
        thread IDs - when given a thread ID, automatically replies to the latest message
        in the thread. Includes Reply All functionality, automatic thread association,
        attachment support (up to 25MB each, 40MB total), and idempotent operations.
        Sender domain must be verified (agent@inbnd.dev not allowed for replies).
        Compatible with Resend API format.

        Args:
          from_: Sender email address. Supports plain or display name formats. Must be from
              verified domain (agent@inbnd.dev not allowed)

          attachments: Email attachments (max 20 files, 25MB each, 40MB total)

          headers: Custom email headers as key-value pairs

          html: HTML content of reply. Either html or text required

          reply_all: If true, includes original CC recipients in reply

          subject: Email subject. Defaults to Re prefix with original subject if not provided

          tags: Resend-compatible metadata tags

          text: Plain text content of reply. Either html or text required

          to: Recipient address(es). Defaults to original sender if not provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "API-Version": api_version,
                    "Idempotency-Key": idempotency_key,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            f"/api/v2/emails/{id}/reply",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "attachments": attachments,
                    "headers": headers,
                    "html": html,
                    "reply_all": reply_all,
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

    async def resend(
        self,
        id: str,
        *,
        endpoint_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailResendResponse:
        """Resends a previously received inbound email to a specific endpoint.

        Useful for
        re-delivering emails to webhooks or forwarding addresses after initial delivery.
        Creates a new delivery record and tracks the attempt. Supports both webhook and
        email forwarding endpoints. Endpoint must be active and belong to the
        authenticated user. Note: Requires session authentication (API keys not
        supported for this endpoint).

        Args:
          endpoint_id: The ID of the endpoint to deliver the email to (nanoid format). Endpoint must be
              active and belong to user

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v2/emails/{id}/resend",
            body=await async_maybe_transform({"endpoint_id": endpoint_id}, email_resend_params.EmailResendParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailResendResponse,
        )

    async def retry_delivery(
        self,
        id: str,
        *,
        delivery_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailRetryDeliveryResponse:
        """Retries endpoint delivery for a previously failed or successful delivery.

        Allows
        re-attempting delivery to webhooks or forwarding addresses regardless of current
        status. Uses the email router to re-process the email and create new delivery
        records. Increments attempt counter and updates delivery timestamps. Endpoint
        must still exist and be active. Note: Requires session authentication (API keys
        not supported).

        Args:
          delivery_id: The ID of the delivery record to retry (nanoid format). Must belong to the
              specified email

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/api/v2/emails/{id}/retry-delivery",
            body=await async_maybe_transform(
                {"delivery_id": delivery_id}, email_retry_delivery_params.EmailRetryDeliveryParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmailRetryDeliveryResponse,
        )

    async def send(
        self,
        *,
        from_: str,
        subject: str,
        to: Union[str, SequenceNotStr[str]],
        attachments: Iterable[AttachmentInputParam] | Omit = omit,
        bcc: Union[str, SequenceNotStr[str]] | Omit = omit,
        cc: Union[str, SequenceNotStr[str]] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        html: str | Omit = omit,
        body_reply_to_1: Union[str, SequenceNotStr[str]] | Omit = omit,
        body_reply_to_2: Union[str, SequenceNotStr[str]] | Omit = omit,
        tags: Iterable[email_send_params.Tag] | Omit = omit,
        text: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendResponse:
        """
        Send an email through the Inbound API with comprehensive support for HTML/text
        content, file attachments (up to 25MB each, 40MB total), custom SMTP headers,
        CC/BCC recipients, and idempotent operations. Sender domain must be verified
        unless using the special agent@inbnd.dev address (available to all users).
        Includes usage tracking and rate limiting via Autumn. Email delivery powered by
        AWS SES with full RFC 5322 compliance. Compatible with Resend API format for
        easy migration.

        Args:
          from_: Sender email address. Supports both "email@domain.com" and "Display Name
              <email@domain.com>" formats. Must be from a verified domain or agent@inbnd.dev

          subject: Email subject line (max 998 characters)

          to: Recipient email address(es). Can be a single string or array of strings

          attachments: Email attachments (max 20 files, 25MB each, 40MB total)

          bcc: Blind carbon copy recipient(s)

          cc: Carbon copy recipient(s)

          headers: Custom SMTP headers as key-value pairs

          html: HTML email body. Either html or text must be provided

          body_reply_to_1: Reply-To address(es) in snake_case format (legacy)

          body_reply_to_2: Reply-To address(es) in camelCase format (Resend-compatible)

          tags: Resend-compatible metadata tags

          text: Plain text email body. Either html or text must be provided

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
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
        self.resend = to_raw_response_wrapper(
            emails.resend,
        )
        self.retry_delivery = to_raw_response_wrapper(
            emails.retry_delivery,
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
        self.resend = async_to_raw_response_wrapper(
            emails.resend,
        )
        self.retry_delivery = async_to_raw_response_wrapper(
            emails.retry_delivery,
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
        self.resend = to_streamed_response_wrapper(
            emails.resend,
        )
        self.retry_delivery = to_streamed_response_wrapper(
            emails.retry_delivery,
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
        self.resend = async_to_streamed_response_wrapper(
            emails.resend,
        )
        self.retry_delivery = async_to_streamed_response_wrapper(
            emails.retry_delivery,
        )
        self.send = async_to_streamed_response_wrapper(
            emails.send,
        )

    @cached_property
    def schedule(self) -> AsyncScheduleResourceWithStreamingResponse:
        return AsyncScheduleResourceWithStreamingResponse(self._emails.schedule)
