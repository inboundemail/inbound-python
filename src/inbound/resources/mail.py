# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    mail_list_params,
    mail_reply_params,
    mail_update_params,
    mail_bulk_update_params,
    mail_get_thread_counts_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven, SequenceNotStr
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
from ..types.mail_list_response import MailListResponse
from ..types.mail_reply_response import MailReplyResponse
from ..types.mail_update_response import MailUpdateResponse
from ..types.mail_retrieve_response import MailRetrieveResponse
from ..types.mail_get_thread_response import MailGetThreadResponse
from ..types.mail_bulk_update_response import MailBulkUpdateResponse
from ..types.mail_get_thread_counts_response import MailGetThreadCountsResponse

__all__ = ["MailResource", "AsyncMailResource"]


class MailResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return MailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
        """
        return MailResourceWithStreamingResponse(self)

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
        Retrieve detailed information about a specific received email including content,
        attachments, headers, and security information.

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
            f"/v2/mail/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        is_archived: Optional[bool] | NotGiven = NOT_GIVEN,
        is_read: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailUpdateResponse:
        """
        Update an email's read status, archive status, or other properties.

        Args:
          id: The ID of the email to get the thread for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v2/mail/{id}",
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
        status: Literal["all", "processed", "failed"] | NotGiven = NOT_GIVEN,
        time_range: Literal["24h", "7d", "30d", "90d"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailListResponse:
        """
        Retrieve all received emails for the authenticated user with filtering, search,
        and pagination options.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/mail",
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

    def bulk_update(
        self,
        *,
        email_ids: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        updates: mail_bulk_update_params.Updates | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailBulkUpdateResponse:
        """Update multiple emails at once (mark as read, archive, etc.).

        Limited to 100
        emails per request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/mail/bulk",
            body=maybe_transform(
                {
                    "email_ids": email_ids,
                    "updates": updates,
                },
                mail_bulk_update_params.MailBulkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailBulkUpdateResponse,
        )

    def get_thread(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailGetThreadResponse:
        """Retrieve all emails in a conversation thread for a given email ID.

        Uses RFC 2822
        threading with subject-based fallback.

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
            f"/v2/mail/{id}/thread",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailGetThreadResponse,
        )

    def get_thread_counts(
        self,
        *,
        email_ids: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailGetThreadCountsResponse:
        """Calculate conversation thread sizes for multiple emails in batch.

        Useful for
        inbox listings to show conversation counts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/mail/thread-counts",
            body=maybe_transform({"email_ids": email_ids}, mail_get_thread_counts_params.MailGetThreadCountsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailGetThreadCountsResponse,
        )

    def reply(
        self,
        *,
        attachments: Optional[Iterable[mail_reply_params.Attachment]] | NotGiven = NOT_GIVEN,
        email_id: str | NotGiven = NOT_GIVEN,
        html_body: Optional[str] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text_body: Optional[str] | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailReplyResponse:
        """Create a reply to a received email.

        This is a convenience endpoint that calls
        the dedicated reply endpoint internally.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/mail",
            body=maybe_transform(
                {
                    "attachments": attachments,
                    "email_id": email_id,
                    "html_body": html_body,
                    "subject": subject,
                    "text_body": text_body,
                    "to": to,
                },
                mail_reply_params.MailReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailReplyResponse,
        )


class AsyncMailResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMailResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMailResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMailResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
        """
        return AsyncMailResourceWithStreamingResponse(self)

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
        Retrieve detailed information about a specific received email including content,
        attachments, headers, and security information.

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
            f"/v2/mail/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        is_archived: Optional[bool] | NotGiven = NOT_GIVEN,
        is_read: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailUpdateResponse:
        """
        Update an email's read status, archive status, or other properties.

        Args:
          id: The ID of the email to get the thread for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v2/mail/{id}",
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
        status: Literal["all", "processed", "failed"] | NotGiven = NOT_GIVEN,
        time_range: Literal["24h", "7d", "30d", "90d"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailListResponse:
        """
        Retrieve all received emails for the authenticated user with filtering, search,
        and pagination options.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/mail",
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

    async def bulk_update(
        self,
        *,
        email_ids: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        updates: mail_bulk_update_params.Updates | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailBulkUpdateResponse:
        """Update multiple emails at once (mark as read, archive, etc.).

        Limited to 100
        emails per request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/mail/bulk",
            body=await async_maybe_transform(
                {
                    "email_ids": email_ids,
                    "updates": updates,
                },
                mail_bulk_update_params.MailBulkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailBulkUpdateResponse,
        )

    async def get_thread(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailGetThreadResponse:
        """Retrieve all emails in a conversation thread for a given email ID.

        Uses RFC 2822
        threading with subject-based fallback.

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
            f"/v2/mail/{id}/thread",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailGetThreadResponse,
        )

    async def get_thread_counts(
        self,
        *,
        email_ids: SequenceNotStr[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailGetThreadCountsResponse:
        """Calculate conversation thread sizes for multiple emails in batch.

        Useful for
        inbox listings to show conversation counts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/mail/thread-counts",
            body=await async_maybe_transform(
                {"email_ids": email_ids}, mail_get_thread_counts_params.MailGetThreadCountsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailGetThreadCountsResponse,
        )

    async def reply(
        self,
        *,
        attachments: Optional[Iterable[mail_reply_params.Attachment]] | NotGiven = NOT_GIVEN,
        email_id: str | NotGiven = NOT_GIVEN,
        html_body: Optional[str] | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        text_body: Optional[str] | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MailReplyResponse:
        """Create a reply to a received email.

        This is a convenience endpoint that calls
        the dedicated reply endpoint internally.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/mail",
            body=await async_maybe_transform(
                {
                    "attachments": attachments,
                    "email_id": email_id,
                    "html_body": html_body,
                    "subject": subject,
                    "text_body": text_body,
                    "to": to,
                },
                mail_reply_params.MailReplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MailReplyResponse,
        )


class MailResourceWithRawResponse:
    def __init__(self, mail: MailResource) -> None:
        self._mail = mail

        self.retrieve = to_raw_response_wrapper(
            mail.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mail.update,
        )
        self.list = to_raw_response_wrapper(
            mail.list,
        )
        self.bulk_update = to_raw_response_wrapper(
            mail.bulk_update,
        )
        self.get_thread = to_raw_response_wrapper(
            mail.get_thread,
        )
        self.get_thread_counts = to_raw_response_wrapper(
            mail.get_thread_counts,
        )
        self.reply = to_raw_response_wrapper(
            mail.reply,
        )


class AsyncMailResourceWithRawResponse:
    def __init__(self, mail: AsyncMailResource) -> None:
        self._mail = mail

        self.retrieve = async_to_raw_response_wrapper(
            mail.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mail.update,
        )
        self.list = async_to_raw_response_wrapper(
            mail.list,
        )
        self.bulk_update = async_to_raw_response_wrapper(
            mail.bulk_update,
        )
        self.get_thread = async_to_raw_response_wrapper(
            mail.get_thread,
        )
        self.get_thread_counts = async_to_raw_response_wrapper(
            mail.get_thread_counts,
        )
        self.reply = async_to_raw_response_wrapper(
            mail.reply,
        )


class MailResourceWithStreamingResponse:
    def __init__(self, mail: MailResource) -> None:
        self._mail = mail

        self.retrieve = to_streamed_response_wrapper(
            mail.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mail.update,
        )
        self.list = to_streamed_response_wrapper(
            mail.list,
        )
        self.bulk_update = to_streamed_response_wrapper(
            mail.bulk_update,
        )
        self.get_thread = to_streamed_response_wrapper(
            mail.get_thread,
        )
        self.get_thread_counts = to_streamed_response_wrapper(
            mail.get_thread_counts,
        )
        self.reply = to_streamed_response_wrapper(
            mail.reply,
        )


class AsyncMailResourceWithStreamingResponse:
    def __init__(self, mail: AsyncMailResource) -> None:
        self._mail = mail

        self.retrieve = async_to_streamed_response_wrapper(
            mail.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mail.update,
        )
        self.list = async_to_streamed_response_wrapper(
            mail.list,
        )
        self.bulk_update = async_to_streamed_response_wrapper(
            mail.bulk_update,
        )
        self.get_thread = async_to_streamed_response_wrapper(
            mail.get_thread,
        )
        self.get_thread_counts = async_to_streamed_response_wrapper(
            mail.get_thread_counts,
        )
        self.reply = async_to_streamed_response_wrapper(
            mail.reply,
        )
