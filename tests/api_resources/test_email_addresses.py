# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inbound import Inbound, AsyncInbound
from tests.utils import assert_matches_type
from inbound.types import (
    EmailAddressListResponse,
    EmailAddressCreateResponse,
    EmailAddressDeleteResponse,
    EmailAddressUpdateResponse,
    EmailAddressRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailAddresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Inbound) -> None:
        email_address = client.email_addresses.create(
            address="address",
            domain_id="domainId",
        )
        assert_matches_type(EmailAddressCreateResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inbound) -> None:
        email_address = client.email_addresses.create(
            address="address",
            domain_id="domainId",
            endpoint_id="endpointId",
            is_active=True,
            webhook_id="webhookId",
        )
        assert_matches_type(EmailAddressCreateResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inbound) -> None:
        response = client.email_addresses.with_raw_response.create(
            address="address",
            domain_id="domainId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_address = response.parse()
        assert_matches_type(EmailAddressCreateResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inbound) -> None:
        with client.email_addresses.with_streaming_response.create(
            address="address",
            domain_id="domainId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_address = response.parse()
            assert_matches_type(EmailAddressCreateResponse, email_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inbound) -> None:
        email_address = client.email_addresses.retrieve(
            "id",
        )
        assert_matches_type(EmailAddressRetrieveResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inbound) -> None:
        response = client.email_addresses.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_address = response.parse()
        assert_matches_type(EmailAddressRetrieveResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inbound) -> None:
        with client.email_addresses.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_address = response.parse()
            assert_matches_type(EmailAddressRetrieveResponse, email_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_addresses.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Inbound) -> None:
        email_address = client.email_addresses.update(
            id="id",
        )
        assert_matches_type(EmailAddressUpdateResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Inbound) -> None:
        email_address = client.email_addresses.update(
            id="id",
            endpoint_id="endpointId",
            is_active=True,
            webhook_id="webhookId",
        )
        assert_matches_type(EmailAddressUpdateResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Inbound) -> None:
        response = client.email_addresses.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_address = response.parse()
        assert_matches_type(EmailAddressUpdateResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Inbound) -> None:
        with client.email_addresses.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_address = response.parse()
            assert_matches_type(EmailAddressUpdateResponse, email_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_addresses.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Inbound) -> None:
        email_address = client.email_addresses.list()
        assert_matches_type(EmailAddressListResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Inbound) -> None:
        email_address = client.email_addresses.list(
            domain_id="domainId",
            is_active="true",
            is_receipt_rule_configured="true",
            limit=0,
            offset=0,
        )
        assert_matches_type(EmailAddressListResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inbound) -> None:
        response = client.email_addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_address = response.parse()
        assert_matches_type(EmailAddressListResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inbound) -> None:
        with client.email_addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_address = response.parse()
            assert_matches_type(EmailAddressListResponse, email_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Inbound) -> None:
        email_address = client.email_addresses.delete(
            "id",
        )
        assert_matches_type(EmailAddressDeleteResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Inbound) -> None:
        response = client.email_addresses.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_address = response.parse()
        assert_matches_type(EmailAddressDeleteResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Inbound) -> None:
        with client.email_addresses.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_address = response.parse()
            assert_matches_type(EmailAddressDeleteResponse, email_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.email_addresses.with_raw_response.delete(
                "",
            )


class TestAsyncEmailAddresses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInbound) -> None:
        email_address = await async_client.email_addresses.create(
            address="address",
            domain_id="domainId",
        )
        assert_matches_type(EmailAddressCreateResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInbound) -> None:
        email_address = await async_client.email_addresses.create(
            address="address",
            domain_id="domainId",
            endpoint_id="endpointId",
            is_active=True,
            webhook_id="webhookId",
        )
        assert_matches_type(EmailAddressCreateResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInbound) -> None:
        response = await async_client.email_addresses.with_raw_response.create(
            address="address",
            domain_id="domainId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_address = await response.parse()
        assert_matches_type(EmailAddressCreateResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInbound) -> None:
        async with async_client.email_addresses.with_streaming_response.create(
            address="address",
            domain_id="domainId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_address = await response.parse()
            assert_matches_type(EmailAddressCreateResponse, email_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInbound) -> None:
        email_address = await async_client.email_addresses.retrieve(
            "id",
        )
        assert_matches_type(EmailAddressRetrieveResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInbound) -> None:
        response = await async_client.email_addresses.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_address = await response.parse()
        assert_matches_type(EmailAddressRetrieveResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInbound) -> None:
        async with async_client.email_addresses.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_address = await response.parse()
            assert_matches_type(EmailAddressRetrieveResponse, email_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_addresses.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncInbound) -> None:
        email_address = await async_client.email_addresses.update(
            id="id",
        )
        assert_matches_type(EmailAddressUpdateResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncInbound) -> None:
        email_address = await async_client.email_addresses.update(
            id="id",
            endpoint_id="endpointId",
            is_active=True,
            webhook_id="webhookId",
        )
        assert_matches_type(EmailAddressUpdateResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncInbound) -> None:
        response = await async_client.email_addresses.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_address = await response.parse()
        assert_matches_type(EmailAddressUpdateResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncInbound) -> None:
        async with async_client.email_addresses.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_address = await response.parse()
            assert_matches_type(EmailAddressUpdateResponse, email_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_addresses.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInbound) -> None:
        email_address = await async_client.email_addresses.list()
        assert_matches_type(EmailAddressListResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncInbound) -> None:
        email_address = await async_client.email_addresses.list(
            domain_id="domainId",
            is_active="true",
            is_receipt_rule_configured="true",
            limit=0,
            offset=0,
        )
        assert_matches_type(EmailAddressListResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInbound) -> None:
        response = await async_client.email_addresses.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_address = await response.parse()
        assert_matches_type(EmailAddressListResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInbound) -> None:
        async with async_client.email_addresses.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_address = await response.parse()
            assert_matches_type(EmailAddressListResponse, email_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncInbound) -> None:
        email_address = await async_client.email_addresses.delete(
            "id",
        )
        assert_matches_type(EmailAddressDeleteResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncInbound) -> None:
        response = await async_client.email_addresses.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_address = await response.parse()
        assert_matches_type(EmailAddressDeleteResponse, email_address, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncInbound) -> None:
        async with async_client.email_addresses.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_address = await response.parse()
            assert_matches_type(EmailAddressDeleteResponse, email_address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.email_addresses.with_raw_response.delete(
                "",
            )
