# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inbound import Inbound, AsyncInbound
from tests.utils import assert_matches_type
from inbound.types import (
    DomainListResponse,
    DomainCreateResponse,
    DomainDeleteResponse,
    DomainRetrieveResponse,
    DomainUpdateCatchAllResponse,
    DomainUpgradeMailFromResponse,
    DomainRetrieveDNSRecordsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Inbound) -> None:
        domain = client.domains.create()
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inbound) -> None:
        domain = client.domains.create(
            domain="domain",
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inbound) -> None:
        response = client.domains.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inbound) -> None:
        with client.domains.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainCreateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inbound) -> None:
        domain = client.domains.retrieve(
            path_id="123",
        )
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Inbound) -> None:
        domain = client.domains.retrieve(
            path_id="123",
            query_id="id",
        )
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inbound) -> None:
        response = client.domains.with_raw_response.retrieve(
            path_id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inbound) -> None:
        with client.domains.with_streaming_response.retrieve(
            path_id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.domains.with_raw_response.retrieve(
                path_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Inbound) -> None:
        domain = client.domains.list()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Inbound) -> None:
        domain = client.domains.list(
            can_receive="true",
            check="true",
            limit=0,
            offset=0,
            status="pending",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inbound) -> None:
        response = client.domains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inbound) -> None:
        with client.domains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Inbound) -> None:
        domain = client.domains.delete(
            "id",
        )
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Inbound) -> None:
        response = client.domains.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Inbound) -> None:
        with client.domains.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainDeleteResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.domains.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_dns_records(self, client: Inbound) -> None:
        domain = client.domains.retrieve_dns_records(
            "id",
        )
        assert_matches_type(DomainRetrieveDNSRecordsResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_dns_records(self, client: Inbound) -> None:
        response = client.domains.with_raw_response.retrieve_dns_records(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainRetrieveDNSRecordsResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_dns_records(self, client: Inbound) -> None:
        with client.domains.with_streaming_response.retrieve_dns_records(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainRetrieveDNSRecordsResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_dns_records(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.domains.with_raw_response.retrieve_dns_records(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_catch_all(self, client: Inbound) -> None:
        domain = client.domains.update_catch_all(
            id="123",
        )
        assert_matches_type(DomainUpdateCatchAllResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_catch_all_with_all_params(self, client: Inbound) -> None:
        domain = client.domains.update_catch_all(
            id="123",
            catch_all_endpoint_id="catchAllEndpointId",
            is_catch_all_enabled=True,
        )
        assert_matches_type(DomainUpdateCatchAllResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_catch_all(self, client: Inbound) -> None:
        response = client.domains.with_raw_response.update_catch_all(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainUpdateCatchAllResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_catch_all(self, client: Inbound) -> None:
        with client.domains.with_streaming_response.update_catch_all(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainUpdateCatchAllResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_catch_all(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.domains.with_raw_response.update_catch_all(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upgrade_mail_from(self, client: Inbound) -> None:
        domain = client.domains.upgrade_mail_from(
            id="123",
        )
        assert_matches_type(DomainUpgradeMailFromResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upgrade_mail_from_with_all_params(self, client: Inbound) -> None:
        domain = client.domains.upgrade_mail_from(
            id="123",
            body={},
        )
        assert_matches_type(DomainUpgradeMailFromResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upgrade_mail_from(self, client: Inbound) -> None:
        response = client.domains.with_raw_response.upgrade_mail_from(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainUpgradeMailFromResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upgrade_mail_from(self, client: Inbound) -> None:
        with client.domains.with_streaming_response.upgrade_mail_from(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainUpgradeMailFromResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_upgrade_mail_from(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.domains.with_raw_response.upgrade_mail_from(
                id="",
            )


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInbound) -> None:
        domain = await async_client.domains.create()
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInbound) -> None:
        domain = await async_client.domains.create(
            domain="domain",
        )
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInbound) -> None:
        response = await async_client.domains.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainCreateResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInbound) -> None:
        async with async_client.domains.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainCreateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInbound) -> None:
        domain = await async_client.domains.retrieve(
            path_id="123",
        )
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncInbound) -> None:
        domain = await async_client.domains.retrieve(
            path_id="123",
            query_id="id",
        )
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInbound) -> None:
        response = await async_client.domains.with_raw_response.retrieve(
            path_id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInbound) -> None:
        async with async_client.domains.with_streaming_response.retrieve(
            path_id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainRetrieveResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.domains.with_raw_response.retrieve(
                path_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInbound) -> None:
        domain = await async_client.domains.list()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncInbound) -> None:
        domain = await async_client.domains.list(
            can_receive="true",
            check="true",
            limit=0,
            offset=0,
            status="pending",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInbound) -> None:
        response = await async_client.domains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInbound) -> None:
        async with async_client.domains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncInbound) -> None:
        domain = await async_client.domains.delete(
            "id",
        )
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncInbound) -> None:
        response = await async_client.domains.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainDeleteResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncInbound) -> None:
        async with async_client.domains.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainDeleteResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.domains.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_dns_records(self, async_client: AsyncInbound) -> None:
        domain = await async_client.domains.retrieve_dns_records(
            "id",
        )
        assert_matches_type(DomainRetrieveDNSRecordsResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_dns_records(self, async_client: AsyncInbound) -> None:
        response = await async_client.domains.with_raw_response.retrieve_dns_records(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainRetrieveDNSRecordsResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_dns_records(self, async_client: AsyncInbound) -> None:
        async with async_client.domains.with_streaming_response.retrieve_dns_records(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainRetrieveDNSRecordsResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_dns_records(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.domains.with_raw_response.retrieve_dns_records(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_catch_all(self, async_client: AsyncInbound) -> None:
        domain = await async_client.domains.update_catch_all(
            id="123",
        )
        assert_matches_type(DomainUpdateCatchAllResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_catch_all_with_all_params(self, async_client: AsyncInbound) -> None:
        domain = await async_client.domains.update_catch_all(
            id="123",
            catch_all_endpoint_id="catchAllEndpointId",
            is_catch_all_enabled=True,
        )
        assert_matches_type(DomainUpdateCatchAllResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_catch_all(self, async_client: AsyncInbound) -> None:
        response = await async_client.domains.with_raw_response.update_catch_all(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainUpdateCatchAllResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_catch_all(self, async_client: AsyncInbound) -> None:
        async with async_client.domains.with_streaming_response.update_catch_all(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainUpdateCatchAllResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_catch_all(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.domains.with_raw_response.update_catch_all(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upgrade_mail_from(self, async_client: AsyncInbound) -> None:
        domain = await async_client.domains.upgrade_mail_from(
            id="123",
        )
        assert_matches_type(DomainUpgradeMailFromResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upgrade_mail_from_with_all_params(self, async_client: AsyncInbound) -> None:
        domain = await async_client.domains.upgrade_mail_from(
            id="123",
            body={},
        )
        assert_matches_type(DomainUpgradeMailFromResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upgrade_mail_from(self, async_client: AsyncInbound) -> None:
        response = await async_client.domains.with_raw_response.upgrade_mail_from(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainUpgradeMailFromResponse, domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upgrade_mail_from(self, async_client: AsyncInbound) -> None:
        async with async_client.domains.with_streaming_response.upgrade_mail_from(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainUpgradeMailFromResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_upgrade_mail_from(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.domains.with_raw_response.upgrade_mail_from(
                id="",
            )
