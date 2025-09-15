# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven, SequenceNotStr
from ...._utils import maybe_transform, async_maybe_transform
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
from ....types.v2.emails.schedule_list_response import ScheduleListResponse
from ....types.v2.emails.schedule_create_response import ScheduleCreateResponse
from ....types.v2.emails.schedule_delete_response import ScheduleDeleteResponse
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
        timezone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleCreateResponse:
        """
        POST /emails/schedule

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleRetrieveResponse:
        """
        GET /emails/schedule/{id}

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
        """
        GET /emails/schedule

        Args:
          limit: limit parameter

          offset: offset parameter

          status: status parameter

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
    ) -> ScheduleDeleteResponse:
        """
        DELETE /emails/schedule/{id}

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
            cast_to=ScheduleDeleteResponse,
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
        timezone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleCreateResponse:
        """
        POST /emails/schedule

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleRetrieveResponse:
        """
        GET /emails/schedule/{id}

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
        """
        GET /emails/schedule

        Args:
          limit: limit parameter

          offset: offset parameter

          status: status parameter

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
    ) -> ScheduleDeleteResponse:
        """
        DELETE /emails/schedule/{id}

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
            cast_to=ScheduleDeleteResponse,
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
        self.delete = to_raw_response_wrapper(
            schedule.delete,
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
        self.delete = async_to_raw_response_wrapper(
            schedule.delete,
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
        self.delete = to_streamed_response_wrapper(
            schedule.delete,
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
        self.delete = async_to_streamed_response_wrapper(
            schedule.delete,
        )
