# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import mail_list_params, mail_create_params, mail_update_params, mail_bulk_create_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.mail_list_response import MailListResponse
from ...types.v2.mail_create_response import MailCreateResponse
from ...types.v2.mail_update_response import MailUpdateResponse
from ...types.v2.mail_retrieve_response import MailRetrieveResponse
from ...types.v2.mail_bulk_create_response import MailBulkCreateResponse
from ...types.v2.mail_retrieve_thread_response import MailRetrieveThreadResponse

__all__ = ["MailResource", "AsyncMailResource"]


class MailResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inboundemail/inbound-python#accessing-raw-response-data-eg-headers
        """
        return MailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inboundemail/inbound-python#with_streaming_response
        """
        return MailResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        email_id: str,
        subject: str,
        to: str,
        attachments: str | NotGiven = NOT_GIVEN,
        html_body: str | NotGiven = NOT_GIVEN,
        text_body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailCreateResponse:
        """
        POST /mail

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/mail",
            body=maybe_transform(
                {
                    "email_id": email_id,
                    "subject": subject,
                    "to": to,
                    "attachments": attachments,
                    "html_body": html_body,
                    "text_body": text_body,
                },
                mail_create_params.MailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailCreateResponse,
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
    ) -> MailRetrieveResponse:
        """
        GET /mail/{id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v2/mail/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        is_archived: bool | NotGiven = NOT_GIVEN,
        is_read: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailUpdateResponse:
        """
        PATCH /mail/{id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/api/v2/mail/{id}",
            body=maybe_transform(
                {
                    "is_archived": is_archived,
                    "is_read": is_read,
                },
                mail_update_params.MailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailUpdateResponse,
        )

    def list(
        self,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        email_address: str | NotGiven = NOT_GIVEN,
        email_id: str | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        status: Literal["failed", "all", "processed", "undefined"] | NotGiven = NOT_GIVEN,
        time_range: Literal["24h", "7d", "30d", "90d", "undefined"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailListResponse:
        """
        GET /mail

        Args:
          domain: domain parameter

          email_address: emailAddress parameter

          email_id: emailId parameter

          include_archived: includeArchived parameter

          limit: limit parameter

          offset: offset parameter

          search: search parameter

          status: status parameter

          time_range: timeRange parameter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/mail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "email_address": email_address,
                        "email_id": email_id,
                        "include_archived": include_archived,
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                        "status": status,
                        "time_range": time_range,
                    },
                    mail_list_params.MailListParams,
                ),
            ),
            cast_to=MailListResponse,
        )

    def bulk_create(
        self,
        *,
        email_ids: str,
        updates: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailBulkCreateResponse:
        """
        POST /mail/bulk

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/mail/bulk",
            body=maybe_transform(
                {
                    "email_ids": email_ids,
                    "updates": updates,
                },
                mail_bulk_create_params.MailBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailBulkCreateResponse,
        )

    def retrieve_thread(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailRetrieveThreadResponse:
        """
        GET /mail/{id}/thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/api/v2/mail/{id}/thread",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailRetrieveThreadResponse,
        )

    def thread_counts(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """POST /mail/thread-counts"""
        return self._post(
            "/api/v2/mail/thread-counts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncMailResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inboundemail/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inboundemail/inbound-python#with_streaming_response
        """
        return AsyncMailResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        email_id: str,
        subject: str,
        to: str,
        attachments: str | NotGiven = NOT_GIVEN,
        html_body: str | NotGiven = NOT_GIVEN,
        text_body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailCreateResponse:
        """
        POST /mail

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/mail",
            body=await async_maybe_transform(
                {
                    "email_id": email_id,
                    "subject": subject,
                    "to": to,
                    "attachments": attachments,
                    "html_body": html_body,
                    "text_body": text_body,
                },
                mail_create_params.MailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailCreateResponse,
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
    ) -> MailRetrieveResponse:
        """
        GET /mail/{id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v2/mail/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        is_archived: bool | NotGiven = NOT_GIVEN,
        is_read: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailUpdateResponse:
        """
        PATCH /mail/{id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/api/v2/mail/{id}",
            body=await async_maybe_transform(
                {
                    "is_archived": is_archived,
                    "is_read": is_read,
                },
                mail_update_params.MailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailUpdateResponse,
        )

    async def list(
        self,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        email_address: str | NotGiven = NOT_GIVEN,
        email_id: str | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        status: Literal["failed", "all", "processed", "undefined"] | NotGiven = NOT_GIVEN,
        time_range: Literal["24h", "7d", "30d", "90d", "undefined"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailListResponse:
        """
        GET /mail

        Args:
          domain: domain parameter

          email_address: emailAddress parameter

          email_id: emailId parameter

          include_archived: includeArchived parameter

          limit: limit parameter

          offset: offset parameter

          search: search parameter

          status: status parameter

          time_range: timeRange parameter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/mail",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "email_address": email_address,
                        "email_id": email_id,
                        "include_archived": include_archived,
                        "limit": limit,
                        "offset": offset,
                        "search": search,
                        "status": status,
                        "time_range": time_range,
                    },
                    mail_list_params.MailListParams,
                ),
            ),
            cast_to=MailListResponse,
        )

    async def bulk_create(
        self,
        *,
        email_ids: str,
        updates: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailBulkCreateResponse:
        """
        POST /mail/bulk

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/mail/bulk",
            body=await async_maybe_transform(
                {
                    "email_ids": email_ids,
                    "updates": updates,
                },
                mail_bulk_create_params.MailBulkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailBulkCreateResponse,
        )

    async def retrieve_thread(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailRetrieveThreadResponse:
        """
        GET /mail/{id}/thread

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/api/v2/mail/{id}/thread",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailRetrieveThreadResponse,
        )

    async def thread_counts(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """POST /mail/thread-counts"""
        return await self._post(
            "/api/v2/mail/thread-counts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class MailResourceWithRawResponse:
    def __init__(self, mail: MailResource) -> None:
        self._mail = mail

        self.create = to_raw_response_wrapper(
            mail.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mail.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mail.update,
        )
        self.list = to_raw_response_wrapper(
            mail.list,
        )
        self.bulk_create = to_raw_response_wrapper(
            mail.bulk_create,
        )
        self.retrieve_thread = to_raw_response_wrapper(
            mail.retrieve_thread,
        )
        self.thread_counts = to_raw_response_wrapper(
            mail.thread_counts,
        )


class AsyncMailResourceWithRawResponse:
    def __init__(self, mail: AsyncMailResource) -> None:
        self._mail = mail

        self.create = async_to_raw_response_wrapper(
            mail.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mail.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mail.update,
        )
        self.list = async_to_raw_response_wrapper(
            mail.list,
        )
        self.bulk_create = async_to_raw_response_wrapper(
            mail.bulk_create,
        )
        self.retrieve_thread = async_to_raw_response_wrapper(
            mail.retrieve_thread,
        )
        self.thread_counts = async_to_raw_response_wrapper(
            mail.thread_counts,
        )


class MailResourceWithStreamingResponse:
    def __init__(self, mail: MailResource) -> None:
        self._mail = mail

        self.create = to_streamed_response_wrapper(
            mail.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mail.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mail.update,
        )
        self.list = to_streamed_response_wrapper(
            mail.list,
        )
        self.bulk_create = to_streamed_response_wrapper(
            mail.bulk_create,
        )
        self.retrieve_thread = to_streamed_response_wrapper(
            mail.retrieve_thread,
        )
        self.thread_counts = to_streamed_response_wrapper(
            mail.thread_counts,
        )


class AsyncMailResourceWithStreamingResponse:
    def __init__(self, mail: AsyncMailResource) -> None:
        self._mail = mail

        self.create = async_to_streamed_response_wrapper(
            mail.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mail.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mail.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mail.list,
        )
        self.bulk_create = async_to_streamed_response_wrapper(
            mail.bulk_create,
        )
        self.retrieve_thread = async_to_streamed_response_wrapper(
            mail.retrieve_thread,
        )
        self.thread_counts = async_to_streamed_response_wrapper(
            mail.thread_counts,
        )
