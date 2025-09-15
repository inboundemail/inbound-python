# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, SequenceNotStr
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
from ...types.emails import schedule_list_params, schedule_create_params
from ...types.emails.schedule_list_response import ScheduleListResponse
from ...types.emails.schedule_create_response import ScheduleCreateResponse

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
        attachments: Optional[Iterable[schedule_create_params.Attachment]] | NotGiven = NOT_GIVEN,
        bcc: Union[str, SequenceNotStr[str], None] | NotGiven = NOT_GIVEN,
        cc: Union[str, SequenceNotStr[str], None] | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        headers: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        html: Optional[str] | NotGiven = NOT_GIVEN,
        body_reply_to_1: Union[str, SequenceNotStr[str], None] | NotGiven = NOT_GIVEN,
        body_reply_to_2: Union[str, SequenceNotStr[str], None] | NotGiven = NOT_GIVEN,
        scheduled_at: str | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        tags: Optional[Iterable[schedule_create_params.Tag]] | NotGiven = NOT_GIVEN,
        text: Optional[str] | NotGiven = NOT_GIVEN,
        timezone: Optional[str] | NotGiven = NOT_GIVEN,
        to: Union[str, SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleCreateResponse:
        """Schedule an email to be sent at a future time.

        Supports natural language
        scheduling like "in 1 hour" or "tomorrow at 9am". Compatible with Resend API
        format.

        Args:
          from_: Supports both "email@domain.com" and "Display Name <email@domain.com>" formats

          body_reply_to_1: snake_case (legacy)

          body_reply_to_2: camelCase (Resend-compatible)

          scheduled_at: ISO 8601 or natural language ("in 1 hour", "tomorrow at 9am")

          timezone: User's timezone for natural language parsing (defaults to UTC)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/emails/schedule",
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
                    "scheduled_at": scheduled_at,
                    "subject": subject,
                    "tags": tags,
                    "text": text,
                    "timezone": timezone,
                    "to": to,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleCreateResponse,
        )

    def list(
        self,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleListResponse:
        """Retrieve a list of emails scheduled for future sending.

        Supports filtering by
        status and pagination.

        Args:
          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/emails/schedule",
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
        attachments: Optional[Iterable[schedule_create_params.Attachment]] | NotGiven = NOT_GIVEN,
        bcc: Union[str, SequenceNotStr[str], None] | NotGiven = NOT_GIVEN,
        cc: Union[str, SequenceNotStr[str], None] | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        headers: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        html: Optional[str] | NotGiven = NOT_GIVEN,
        body_reply_to_1: Union[str, SequenceNotStr[str], None] | NotGiven = NOT_GIVEN,
        body_reply_to_2: Union[str, SequenceNotStr[str], None] | NotGiven = NOT_GIVEN,
        scheduled_at: str | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        tags: Optional[Iterable[schedule_create_params.Tag]] | NotGiven = NOT_GIVEN,
        text: Optional[str] | NotGiven = NOT_GIVEN,
        timezone: Optional[str] | NotGiven = NOT_GIVEN,
        to: Union[str, SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleCreateResponse:
        """Schedule an email to be sent at a future time.

        Supports natural language
        scheduling like "in 1 hour" or "tomorrow at 9am". Compatible with Resend API
        format.

        Args:
          from_: Supports both "email@domain.com" and "Display Name <email@domain.com>" formats

          body_reply_to_1: snake_case (legacy)

          body_reply_to_2: camelCase (Resend-compatible)

          scheduled_at: ISO 8601 or natural language ("in 1 hour", "tomorrow at 9am")

          timezone: User's timezone for natural language parsing (defaults to UTC)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/emails/schedule",
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
                    "scheduled_at": scheduled_at,
                    "subject": subject,
                    "tags": tags,
                    "text": text,
                    "timezone": timezone,
                    "to": to,
                },
                schedule_create_params.ScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScheduleCreateResponse,
        )

    async def list(
        self,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleListResponse:
        """Retrieve a list of emails scheduled for future sending.

        Supports filtering by
        status and pagination.

        Args:
          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/emails/schedule",
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


class ScheduleResourceWithRawResponse:
    def __init__(self, schedule: ScheduleResource) -> None:
        self._schedule = schedule

        self.create = to_raw_response_wrapper(
            schedule.create,
        )
        self.list = to_raw_response_wrapper(
            schedule.list,
        )


class AsyncScheduleResourceWithRawResponse:
    def __init__(self, schedule: AsyncScheduleResource) -> None:
        self._schedule = schedule

        self.create = async_to_raw_response_wrapper(
            schedule.create,
        )
        self.list = async_to_raw_response_wrapper(
            schedule.list,
        )


class ScheduleResourceWithStreamingResponse:
    def __init__(self, schedule: ScheduleResource) -> None:
        self._schedule = schedule

        self.create = to_streamed_response_wrapper(
            schedule.create,
        )
        self.list = to_streamed_response_wrapper(
            schedule.list,
        )


class AsyncScheduleResourceWithStreamingResponse:
    def __init__(self, schedule: AsyncScheduleResource) -> None:
        self._schedule = schedule

        self.create = async_to_streamed_response_wrapper(
            schedule.create,
        )
        self.list = async_to_streamed_response_wrapper(
            schedule.list,
        )
