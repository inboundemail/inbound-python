# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, strip_not_given, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.emails import schedule_list_params, schedule_create_params
from ....types.v2.attachment_input_param import AttachmentInputParam
from ....types.v2.emails.schedule_list_response import ScheduleListResponse
from ....types.v2.emails.schedule_cancel_response import ScheduleCancelResponse
from ....types.v2.emails.schedule_create_response import ScheduleCreateResponse
from ....types.v2.emails.schedule_retrieve_response import ScheduleRetrieveResponse

__all__ = ["ScheduleResource", "AsyncScheduleResource"]


class ScheduleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return ScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
        """
        return ScheduleResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        from_: str,
        scheduled_at: str,
        subject: str,
        to: Union[str, SequenceNotStr[str]],
        attachments: Iterable[AttachmentInputParam] | Omit = omit,
        bcc: Union[str, SequenceNotStr[str]] | Omit = omit,
        cc: Union[str, SequenceNotStr[str]] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        html: str | Omit = omit,
        body_reply_to_1: Union[str, SequenceNotStr[str]] | Omit = omit,
        body_reply_to_2: Union[str, SequenceNotStr[str]] | Omit = omit,
        tags: Iterable[schedule_create_params.Tag] | Omit = omit,
        text: str | Omit = omit,
        timezone: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleCreateResponse:
        """
        Schedules an email to be sent at a specified future time with Resend-compatible
        interface. Supports both ISO 8601 timestamps (e.g., "2025-10-01T09:00:00Z") and
        natural language date parsing (e.g., "in 1 hour", "tomorrow at 9am", "next
        Monday at 2pm"). Scheduled emails use the same delivery pipeline as immediate
        sends with full support for domain verification, attachments (up to 25MB each,
        40MB total), rate limiting, and idempotent operations. Includes automatic retry
        logic for failed sends.

        Args:
          from_: Sender email address. Supports "email@domain.com" and "Display Name
              <email@domain.com>" formats. Must be from verified domain or agent@inbnd.dev

          scheduled_at: When to send email. ISO 8601 format or natural language ("in 1 hour", "tomorrow
              at 9am")

          subject: Email subject line

          to: Recipient email address(es)

          attachments: Email attachments (max 20 files, 25MB each, 40MB total)

          bcc: Blind carbon copy recipient(s)

          cc: Carbon copy recipient(s)

          headers: Custom SMTP headers as key-value pairs

          html: HTML email body. Either html or text required

          body_reply_to_1: Reply-To address(es) in snake_case format (legacy)

          body_reply_to_2: Reply-To address(es) in camelCase format (Resend-compatible)

          tags: Resend-compatible metadata tags

          text: Plain text email body. Either html or text required

          timezone: User timezone for natural language parsing

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/api/v2/emails/schedule",
            body=maybe_transform(
                {
                    "from_": from_,
                    "scheduled_at": scheduled_at,
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
                    "timezone": timezone,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleRetrieveResponse:
        """
        Retrieves detailed information about a specific scheduled email by its ID.
        Returns complete email data including recipients, subject, HTML/text content,
        attachments, custom headers, scheduling information (scheduled time, timezone),
        retry attempts, max attempts, and current status (scheduled, sent, failed,
        cancelled). Only scheduled emails belonging to the authenticated user can be
        accessed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v2/emails/schedule/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleListResponse:
        """
        Retrieves a paginated list of scheduled emails for the authenticated user.
        Supports filtering by status (scheduled, sent, failed, cancelled) and standard
        pagination controls. Returns email metadata including recipients, schedule time,
        current status, retry attempts, and error information. Useful for monitoring
        upcoming sends and troubleshooting failed deliveries.

        Args:
          limit: Maximum number of scheduled emails to return. Min: 1, Max: 100, Default: 50

          offset: Number of scheduled emails to skip for pagination. Min: 0, Default: 0

          status: Filter by email status. Values: 'scheduled', 'sent', 'failed', 'cancelled'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/emails/schedule",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    schedule_list_params.ScheduleListParams,
                ),
            ),
            cast_to=ScheduleListResponse,
        )

    def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleCancelResponse:
        """Cancels a scheduled email before it is sent.

        Only emails with status 'scheduled'
        can be cancelled. Once an email is sent, failed, or already cancelled, it cannot
        be cancelled again. The cancellation is immediate and cannot be undone. Email
        will not be sent and delivery pipeline will skip it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v2/emails/schedule/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleCancelResponse,
        )


class AsyncScheduleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
        """
        return AsyncScheduleResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        from_: str,
        scheduled_at: str,
        subject: str,
        to: Union[str, SequenceNotStr[str]],
        attachments: Iterable[AttachmentInputParam] | Omit = omit,
        bcc: Union[str, SequenceNotStr[str]] | Omit = omit,
        cc: Union[str, SequenceNotStr[str]] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        html: str | Omit = omit,
        body_reply_to_1: Union[str, SequenceNotStr[str]] | Omit = omit,
        body_reply_to_2: Union[str, SequenceNotStr[str]] | Omit = omit,
        tags: Iterable[schedule_create_params.Tag] | Omit = omit,
        text: str | Omit = omit,
        timezone: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleCreateResponse:
        """
        Schedules an email to be sent at a specified future time with Resend-compatible
        interface. Supports both ISO 8601 timestamps (e.g., "2025-10-01T09:00:00Z") and
        natural language date parsing (e.g., "in 1 hour", "tomorrow at 9am", "next
        Monday at 2pm"). Scheduled emails use the same delivery pipeline as immediate
        sends with full support for domain verification, attachments (up to 25MB each,
        40MB total), rate limiting, and idempotent operations. Includes automatic retry
        logic for failed sends.

        Args:
          from_: Sender email address. Supports "email@domain.com" and "Display Name
              <email@domain.com>" formats. Must be from verified domain or agent@inbnd.dev

          scheduled_at: When to send email. ISO 8601 format or natural language ("in 1 hour", "tomorrow
              at 9am")

          subject: Email subject line

          to: Recipient email address(es)

          attachments: Email attachments (max 20 files, 25MB each, 40MB total)

          bcc: Blind carbon copy recipient(s)

          cc: Carbon copy recipient(s)

          headers: Custom SMTP headers as key-value pairs

          html: HTML email body. Either html or text required

          body_reply_to_1: Reply-To address(es) in snake_case format (legacy)

          body_reply_to_2: Reply-To address(es) in camelCase format (Resend-compatible)

          tags: Resend-compatible metadata tags

          text: Plain text email body. Either html or text required

          timezone: User timezone for natural language parsing

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/api/v2/emails/schedule",
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "scheduled_at": scheduled_at,
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
                    "timezone": timezone,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleRetrieveResponse:
        """
        Retrieves detailed information about a specific scheduled email by its ID.
        Returns complete email data including recipients, subject, HTML/text content,
        attachments, custom headers, scheduling information (scheduled time, timezone),
        retry attempts, max attempts, and current status (scheduled, sent, failed,
        cancelled). Only scheduled emails belonging to the authenticated user can be
        accessed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v2/emails/schedule/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleRetrieveResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleListResponse:
        """
        Retrieves a paginated list of scheduled emails for the authenticated user.
        Supports filtering by status (scheduled, sent, failed, cancelled) and standard
        pagination controls. Returns email metadata including recipients, schedule time,
        current status, retry attempts, and error information. Useful for monitoring
        upcoming sends and troubleshooting failed deliveries.

        Args:
          limit: Maximum number of scheduled emails to return. Min: 1, Max: 100, Default: 50

          offset: Number of scheduled emails to skip for pagination. Min: 0, Default: 0

          status: Filter by email status. Values: 'scheduled', 'sent', 'failed', 'cancelled'

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/emails/schedule",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    schedule_list_params.ScheduleListParams,
                ),
            ),
            cast_to=ScheduleListResponse,
        )

    async def cancel(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScheduleCancelResponse:
        """Cancels a scheduled email before it is sent.

        Only emails with status 'scheduled'
        can be cancelled. Once an email is sent, failed, or already cancelled, it cannot
        be cancelled again. The cancellation is immediate and cannot be undone. Email
        will not be sent and delivery pipeline will skip it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v2/emails/schedule/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleCancelResponse,
        )


class ScheduleResourceWithRawResponse:
    def __init__(self, schedule: ScheduleResource) -> None:
        self._schedule = schedule

        self.create = to_raw_response_wrapper(
            schedule.create,
        )
        self.retrieve = to_raw_response_wrapper(
            schedule.retrieve,
        )
        self.list = to_raw_response_wrapper(
            schedule.list,
        )
        self.cancel = to_raw_response_wrapper(
            schedule.cancel,
        )


class AsyncScheduleResourceWithRawResponse:
    def __init__(self, schedule: AsyncScheduleResource) -> None:
        self._schedule = schedule

        self.create = async_to_raw_response_wrapper(
            schedule.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            schedule.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            schedule.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            schedule.cancel,
        )


class ScheduleResourceWithStreamingResponse:
    def __init__(self, schedule: ScheduleResource) -> None:
        self._schedule = schedule

        self.create = to_streamed_response_wrapper(
            schedule.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            schedule.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            schedule.list,
        )
        self.cancel = to_streamed_response_wrapper(
            schedule.cancel,
        )


class AsyncScheduleResourceWithStreamingResponse:
    def __init__(self, schedule: AsyncScheduleResource) -> None:
        self._schedule = schedule

        self.create = async_to_streamed_response_wrapper(
            schedule.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            schedule.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            schedule.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            schedule.cancel,
        )
