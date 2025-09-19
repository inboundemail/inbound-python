# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .auth import (
    AuthResource,
    AsyncAuthResource,
    AuthResourceWithRawResponse,
    AsyncAuthResourceWithRawResponse,
    AuthResourceWithStreamingResponse,
    AsyncAuthResourceWithStreamingResponse,
)
from ...types import (
    domain_list_params,
    domain_create_params,
    domain_retrieve_params,
    domain_update_catch_all_params,
    domain_upgrade_mail_from_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.domain_list_response import DomainListResponse
from ...types.domain_create_response import DomainCreateResponse
from ...types.domain_delete_response import DomainDeleteResponse
from ...types.domain_retrieve_response import DomainRetrieveResponse
from ...types.domain_update_catch_all_response import DomainUpdateCatchAllResponse
from ...types.domain_upgrade_mail_from_response import DomainUpgradeMailFromResponse
from ...types.domain_retrieve_dns_records_response import DomainRetrieveDNSRecordsResponse

__all__ = ["DomainsResource", "AsyncDomainsResource"]


class DomainsResource(SyncAPIResource):
    @cached_property
    def auth(self) -> AuthResource:
        return AuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> DomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return DomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
        """
        return DomainsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        domain: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainCreateResponse:
        """Add a new domain for email receiving.

        Validates domain ownership and sets up DNS
        verification records.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/domains",
            body=maybe_transform({"domain": domain}, domain_create_params.DomainCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainCreateResponse,
        )

    def retrieve(
        self,
        path_id: str,
        *,
        query_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainRetrieveResponse:
        """
        Get detailed information about a specific domain including verification status,
        statistics, and optional DNS/SES checks.

        Args:
          path_id: The ID of the domain

          query_id: from params

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return self._get(
            f"/v2/domains/{path_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query_id": query_id}, domain_retrieve_params.DomainRetrieveParams),
            ),
            cast_to=DomainRetrieveResponse,
        )

    def list(
        self,
        *,
        can_receive: Literal["true", "false"] | Omit = omit,
        check: Literal["true", "false"] | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        status: Literal["pending", "verified", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainListResponse:
        """
        Retrieve all domains for the authenticated user with filtering, pagination, and
        optional DNS/SES verification checks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "can_receive": can_receive,
                        "check": check,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    domain_list_params.DomainListParams,
                ),
            ),
            cast_to=DomainListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainDeleteResponse:
        """
        Permanently delete a domain and all its associated resources (email addresses,
        DNS records, AWS SES configuration).

        Args:
          id: The ID of the domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v2/domains/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainDeleteResponse,
        )

    def retrieve_dns_records(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainRetrieveDNSRecordsResponse:
        """
        Retrieve all DNS records associated with a domain, including verification status
        for each record.

        Args:
          id: The ID of the domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v2/domains/{id}/dns-records",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainRetrieveDNSRecordsResponse,
        )

    def update_catch_all(
        self,
        id: str,
        *,
        catch_all_endpoint_id: Optional[str] | Omit = omit,
        is_catch_all_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainUpdateCatchAllResponse:
        """Configure catch-all email routing for a domain.

        Enable or disable catch-all
        functionality with endpoint configuration.

        Args:
          id: The ID of the domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/v2/domains/{id}",
            body=maybe_transform(
                {
                    "catch_all_endpoint_id": catch_all_endpoint_id,
                    "is_catch_all_enabled": is_catch_all_enabled,
                },
                domain_update_catch_all_params.DomainUpdateCatchAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainUpdateCatchAllResponse,
        )

    def upgrade_mail_from(
        self,
        id: str,
        *,
        body: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainUpgradeMailFromResponse:
        """
        Upgrade an existing domain with MAIL FROM domain configuration to eliminate the
        "via amazonses.com" attribution in emails.

        Args:
          id: The ID of the domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v2/domains/{id}",
            body=maybe_transform(body, domain_upgrade_mail_from_params.DomainUpgradeMailFromParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainUpgradeMailFromResponse,
        )


class AsyncDomainsResource(AsyncAPIResource):
    @cached_property
    def auth(self) -> AsyncAuthResource:
        return AsyncAuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/inbound-python#with_streaming_response
        """
        return AsyncDomainsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        domain: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainCreateResponse:
        """Add a new domain for email receiving.

        Validates domain ownership and sets up DNS
        verification records.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/domains",
            body=await async_maybe_transform({"domain": domain}, domain_create_params.DomainCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainCreateResponse,
        )

    async def retrieve(
        self,
        path_id: str,
        *,
        query_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainRetrieveResponse:
        """
        Get detailed information about a specific domain including verification status,
        statistics, and optional DNS/SES checks.

        Args:
          path_id: The ID of the domain

          query_id: from params

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_id:
            raise ValueError(f"Expected a non-empty value for `path_id` but received {path_id!r}")
        return await self._get(
            f"/v2/domains/{path_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query_id": query_id}, domain_retrieve_params.DomainRetrieveParams),
            ),
            cast_to=DomainRetrieveResponse,
        )

    async def list(
        self,
        *,
        can_receive: Literal["true", "false"] | Omit = omit,
        check: Literal["true", "false"] | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        status: Literal["pending", "verified", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainListResponse:
        """
        Retrieve all domains for the authenticated user with filtering, pagination, and
        optional DNS/SES verification checks.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/domains",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "can_receive": can_receive,
                        "check": check,
                        "limit": limit,
                        "offset": offset,
                        "status": status,
                    },
                    domain_list_params.DomainListParams,
                ),
            ),
            cast_to=DomainListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainDeleteResponse:
        """
        Permanently delete a domain and all its associated resources (email addresses,
        DNS records, AWS SES configuration).

        Args:
          id: The ID of the domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v2/domains/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainDeleteResponse,
        )

    async def retrieve_dns_records(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainRetrieveDNSRecordsResponse:
        """
        Retrieve all DNS records associated with a domain, including verification status
        for each record.

        Args:
          id: The ID of the domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v2/domains/{id}/dns-records",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainRetrieveDNSRecordsResponse,
        )

    async def update_catch_all(
        self,
        id: str,
        *,
        catch_all_endpoint_id: Optional[str] | Omit = omit,
        is_catch_all_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainUpdateCatchAllResponse:
        """Configure catch-all email routing for a domain.

        Enable or disable catch-all
        functionality with endpoint configuration.

        Args:
          id: The ID of the domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/v2/domains/{id}",
            body=await async_maybe_transform(
                {
                    "catch_all_endpoint_id": catch_all_endpoint_id,
                    "is_catch_all_enabled": is_catch_all_enabled,
                },
                domain_update_catch_all_params.DomainUpdateCatchAllParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainUpdateCatchAllResponse,
        )

    async def upgrade_mail_from(
        self,
        id: str,
        *,
        body: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DomainUpgradeMailFromResponse:
        """
        Upgrade an existing domain with MAIL FROM domain configuration to eliminate the
        "via amazonses.com" attribution in emails.

        Args:
          id: The ID of the domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v2/domains/{id}",
            body=await async_maybe_transform(body, domain_upgrade_mail_from_params.DomainUpgradeMailFromParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainUpgradeMailFromResponse,
        )


class DomainsResourceWithRawResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.create = to_raw_response_wrapper(
            domains.create,
        )
        self.retrieve = to_raw_response_wrapper(
            domains.retrieve,
        )
        self.list = to_raw_response_wrapper(
            domains.list,
        )
        self.delete = to_raw_response_wrapper(
            domains.delete,
        )
        self.retrieve_dns_records = to_raw_response_wrapper(
            domains.retrieve_dns_records,
        )
        self.update_catch_all = to_raw_response_wrapper(
            domains.update_catch_all,
        )
        self.upgrade_mail_from = to_raw_response_wrapper(
            domains.upgrade_mail_from,
        )

    @cached_property
    def auth(self) -> AuthResourceWithRawResponse:
        return AuthResourceWithRawResponse(self._domains.auth)


class AsyncDomainsResourceWithRawResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.create = async_to_raw_response_wrapper(
            domains.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            domains.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            domains.list,
        )
        self.delete = async_to_raw_response_wrapper(
            domains.delete,
        )
        self.retrieve_dns_records = async_to_raw_response_wrapper(
            domains.retrieve_dns_records,
        )
        self.update_catch_all = async_to_raw_response_wrapper(
            domains.update_catch_all,
        )
        self.upgrade_mail_from = async_to_raw_response_wrapper(
            domains.upgrade_mail_from,
        )

    @cached_property
    def auth(self) -> AsyncAuthResourceWithRawResponse:
        return AsyncAuthResourceWithRawResponse(self._domains.auth)


class DomainsResourceWithStreamingResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

        self.create = to_streamed_response_wrapper(
            domains.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            domains.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            domains.list,
        )
        self.delete = to_streamed_response_wrapper(
            domains.delete,
        )
        self.retrieve_dns_records = to_streamed_response_wrapper(
            domains.retrieve_dns_records,
        )
        self.update_catch_all = to_streamed_response_wrapper(
            domains.update_catch_all,
        )
        self.upgrade_mail_from = to_streamed_response_wrapper(
            domains.upgrade_mail_from,
        )

    @cached_property
    def auth(self) -> AuthResourceWithStreamingResponse:
        return AuthResourceWithStreamingResponse(self._domains.auth)


class AsyncDomainsResourceWithStreamingResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

        self.create = async_to_streamed_response_wrapper(
            domains.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            domains.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            domains.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            domains.delete,
        )
        self.retrieve_dns_records = async_to_streamed_response_wrapper(
            domains.retrieve_dns_records,
        )
        self.update_catch_all = async_to_streamed_response_wrapper(
            domains.update_catch_all,
        )
        self.upgrade_mail_from = async_to_streamed_response_wrapper(
            domains.upgrade_mail_from,
        )

    @cached_property
    def auth(self) -> AsyncAuthResourceWithStreamingResponse:
        return AsyncAuthResourceWithStreamingResponse(self._domains.auth)
