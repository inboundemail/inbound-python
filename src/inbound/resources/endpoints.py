# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    endpoint_list_params,
    endpoint_test_params,
    endpoint_create_params,
    endpoint_update_params,
    endpoint_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.endpoint_list_response import EndpointListResponse
from ..types.endpoint_test_response import EndpointTestResponse
from ..types.endpoint_create_response import EndpointCreateResponse
from ..types.endpoint_delete_response import EndpointDeleteResponse
from ..types.endpoint_update_response import EndpointUpdateResponse
from ..types.endpoint_retrieve_response import EndpointRetrieveResponse

__all__ = ["EndpointsResource", "AsyncEndpointsResource"]


class EndpointsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EndpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inboundemail/inbound-python#accessing-raw-response-data-eg-headers
        """
        return EndpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EndpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inboundemail/inbound-python#with_streaming_response
        """
        return EndpointsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: str,
        name: str,
        type: Literal["webhook", "email", "email_group"],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndpointCreateResponse:
        """
        POST /endpoints

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/endpoints",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "type": type,
                    "description": description,
                },
                endpoint_create_params.EndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndpointCreateResponse,
        )

    def retrieve(
        self,
        path_id: str,
        *,
        query_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndpointRetrieveResponse:
        """
        GET /endpoints/{id}

        Args:
          query_id: id parameter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._get(
            f"/api/v2/endpoints/{path_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query_id": query_id}, endpoint_retrieve_params.EndpointRetrieveParams),
            ),
            cast_to=EndpointRetrieveResponse,
        )

    def update(
        self,
        path_id: str,
        *,
        body_id: str,
        config: Literal[
            "import(/Users/ryanvogel/dev/inbound-org/inbound/features/endpoints/types/index).EndpointConfig",
            "undefined",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndpointUpdateResponse:
        """
        PUT /endpoints/{id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._put(
            f"/api/v2/endpoints/{path_id}",
            body=maybe_transform(
                {
                    "body_id": body_id,
                    "config": config,
                    "description": description,
                    "is_active": is_active,
                    "name": name,
                },
                endpoint_update_params.EndpointUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndpointUpdateResponse,
        )

    def list(
        self,
        *,
        active: Literal["true", "false", "undefined"] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        sort_by: Literal["newest", "oldest", "undefined"] | NotGiven = NOT_GIVEN,
        type: Literal["webhook", "email", "email_group", "undefined"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndpointListResponse:
        """
        GET /endpoints

        Args:
          active: active parameter

          limit: limit parameter

          offset: offset parameter

          sort_by: sortBy parameter

          type: type parameter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "active": active,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                        "type": type,
                    },
                    endpoint_list_params.EndpointListParams,
                ),
            ),
            cast_to=EndpointListResponse,
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
    ) -> EndpointDeleteResponse:
        """
        DELETE /endpoints/{id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/api/v2/endpoints/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndpointDeleteResponse,
        )

    def test(
        self,
        path_id: str,
        *,
        body_id: str,
        webhook_format: Literal["inbound", "discord", "slack", "undefined"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndpointTestResponse:
        """
        POST /endpoints/{id}/test

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._post(
            f"/api/v2/endpoints/{path_id}/test",
            body=maybe_transform(
                {
                    "body_id": body_id,
                    "webhook_format": webhook_format,
                },
                endpoint_test_params.EndpointTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndpointTestResponse,
        )


class AsyncEndpointsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEndpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inboundemail/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEndpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEndpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inboundemail/inbound-python#with_streaming_response
        """
        return AsyncEndpointsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: str,
        name: str,
        type: Literal["webhook", "email", "email_group"],
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndpointCreateResponse:
        """
        POST /endpoints

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/endpoints",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "type": type,
                    "description": description,
                },
                endpoint_create_params.EndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndpointCreateResponse,
        )

    async def retrieve(
        self,
        path_id: str,
        *,
        query_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndpointRetrieveResponse:
        """
        GET /endpoints/{id}

        Args:
          query_id: id parameter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._get(
            f"/api/v2/endpoints/{path_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query_id": query_id}, endpoint_retrieve_params.EndpointRetrieveParams
                ),
            ),
            cast_to=EndpointRetrieveResponse,
        )

    async def update(
        self,
        path_id: str,
        *,
        body_id: str,
        config: Literal[
            "import(/Users/ryanvogel/dev/inbound-org/inbound/features/endpoints/types/index).EndpointConfig",
            "undefined",
        ]
        | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        is_active: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndpointUpdateResponse:
        """
        PUT /endpoints/{id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._put(
            f"/api/v2/endpoints/{path_id}",
            body=await async_maybe_transform(
                {
                    "body_id": body_id,
                    "config": config,
                    "description": description,
                    "is_active": is_active,
                    "name": name,
                },
                endpoint_update_params.EndpointUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndpointUpdateResponse,
        )

    async def list(
        self,
        *,
        active: Literal["true", "false", "undefined"] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        sort_by: Literal["newest", "oldest", "undefined"] | NotGiven = NOT_GIVEN,
        type: Literal["webhook", "email", "email_group", "undefined"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndpointListResponse:
        """
        GET /endpoints

        Args:
          active: active parameter

          limit: limit parameter

          offset: offset parameter

          sort_by: sortBy parameter

          type: type parameter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "active": active,
                        "limit": limit,
                        "offset": offset,
                        "sort_by": sort_by,
                        "type": type,
                    },
                    endpoint_list_params.EndpointListParams,
                ),
            ),
            cast_to=EndpointListResponse,
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
    ) -> EndpointDeleteResponse:
        """
        DELETE /endpoints/{id}

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/api/v2/endpoints/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndpointDeleteResponse,
        )

    async def test(
        self,
        path_id: str,
        *,
        body_id: str,
        webhook_format: Literal["inbound", "discord", "slack", "undefined"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EndpointTestResponse:
        """
        POST /endpoints/{id}/test

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._post(
            f"/api/v2/endpoints/{path_id}/test",
            body=await async_maybe_transform(
                {
                    "body_id": body_id,
                    "webhook_format": webhook_format,
                },
                endpoint_test_params.EndpointTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EndpointTestResponse,
        )


class EndpointsResourceWithRawResponse:
    def __init__(self, endpoints: EndpointsResource) -> None:
        self._endpoints = endpoints

        self.create = to_raw_response_wrapper(
            endpoints.create,
        )
        self.retrieve = to_raw_response_wrapper(
            endpoints.retrieve,
        )
        self.update = to_raw_response_wrapper(
            endpoints.update,
        )
        self.list = to_raw_response_wrapper(
            endpoints.list,
        )
        self.delete = to_raw_response_wrapper(
            endpoints.delete,
        )
        self.test = to_raw_response_wrapper(
            endpoints.test,
        )


class AsyncEndpointsResourceWithRawResponse:
    def __init__(self, endpoints: AsyncEndpointsResource) -> None:
        self._endpoints = endpoints

        self.create = async_to_raw_response_wrapper(
            endpoints.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            endpoints.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            endpoints.update,
        )
        self.list = async_to_raw_response_wrapper(
            endpoints.list,
        )
        self.delete = async_to_raw_response_wrapper(
            endpoints.delete,
        )
        self.test = async_to_raw_response_wrapper(
            endpoints.test,
        )


class EndpointsResourceWithStreamingResponse:
    def __init__(self, endpoints: EndpointsResource) -> None:
        self._endpoints = endpoints

        self.create = to_streamed_response_wrapper(
            endpoints.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            endpoints.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            endpoints.update,
        )
        self.list = to_streamed_response_wrapper(
            endpoints.list,
        )
        self.delete = to_streamed_response_wrapper(
            endpoints.delete,
        )
        self.test = to_streamed_response_wrapper(
            endpoints.test,
        )


class AsyncEndpointsResourceWithStreamingResponse:
    def __init__(self, endpoints: AsyncEndpointsResource) -> None:
        self._endpoints = endpoints

        self.create = async_to_streamed_response_wrapper(
            endpoints.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            endpoints.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            endpoints.update,
        )
        self.list = async_to_streamed_response_wrapper(
            endpoints.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            endpoints.delete,
        )
        self.test = async_to_streamed_response_wrapper(
            endpoints.test,
        )
