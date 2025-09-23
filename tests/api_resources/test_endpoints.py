# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inbound import Inbound, AsyncInbound
from tests.utils import assert_matches_type
from inbound.types import (
    EndpointListResponse,
    EndpointTestResponse,
    EndpointCreateResponse,
    EndpointDeleteResponse,
    EndpointUpdateResponse,
    EndpointRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEndpoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Inbound) -> None:
        endpoint = client.endpoints.create()
        assert_matches_type(EndpointCreateResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inbound) -> None:
        endpoint = client.endpoints.create(
            config={},
            description="description",
            name="name",
            type="webhook",
        )
        assert_matches_type(EndpointCreateResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inbound) -> None:
        response = client.endpoints.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert_matches_type(EndpointCreateResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inbound) -> None:
        with client.endpoints.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert_matches_type(EndpointCreateResponse, endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inbound) -> None:
        endpoint = client.endpoints.retrieve(
            "123",
        )
        assert_matches_type(EndpointRetrieveResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inbound) -> None:
        response = client.endpoints.with_raw_response.retrieve(
            "123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert_matches_type(EndpointRetrieveResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inbound) -> None:
        with client.endpoints.with_streaming_response.retrieve(
            "123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert_matches_type(EndpointRetrieveResponse, endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.endpoints.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Inbound) -> None:
        endpoint = client.endpoints.update(
            path_id="123",
        )
        assert_matches_type(EndpointUpdateResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Inbound) -> None:
        endpoint = client.endpoints.update(
            path_id="123",
            body_id="id",
            config={},
            description="description",
            is_active=True,
            name="name",
        )
        assert_matches_type(EndpointUpdateResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Inbound) -> None:
        response = client.endpoints.with_raw_response.update(
            path_id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert_matches_type(EndpointUpdateResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Inbound) -> None:
        with client.endpoints.with_streaming_response.update(
            path_id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert_matches_type(EndpointUpdateResponse, endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.endpoints.with_raw_response.update(
                path_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Inbound) -> None:
        endpoint = client.endpoints.list()
        assert_matches_type(EndpointListResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Inbound) -> None:
        endpoint = client.endpoints.list(
            active="true",
            limit=0,
            offset=0,
            sort_by="newest",
            type="webhook",
        )
        assert_matches_type(EndpointListResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inbound) -> None:
        response = client.endpoints.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert_matches_type(EndpointListResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inbound) -> None:
        with client.endpoints.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert_matches_type(EndpointListResponse, endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Inbound) -> None:
        endpoint = client.endpoints.delete(
            "123",
        )
        assert_matches_type(EndpointDeleteResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Inbound) -> None:
        response = client.endpoints.with_raw_response.delete(
            "123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert_matches_type(EndpointDeleteResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Inbound) -> None:
        with client.endpoints.with_streaming_response.delete(
            "123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert_matches_type(EndpointDeleteResponse, endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.endpoints.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test(self, client: Inbound) -> None:
        endpoint = client.endpoints.test(
            path_id="123",
        )
        assert_matches_type(EndpointTestResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_with_all_params(self, client: Inbound) -> None:
        endpoint = client.endpoints.test(
            path_id="123",
            body_id="id",
            webhook_format="inbound",
        )
        assert_matches_type(EndpointTestResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test(self, client: Inbound) -> None:
        response = client.endpoints.with_raw_response.test(
            path_id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = response.parse()
        assert_matches_type(EndpointTestResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test(self, client: Inbound) -> None:
        with client.endpoints.with_streaming_response.test(
            path_id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = response.parse()
            assert_matches_type(EndpointTestResponse, endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_test(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            client.endpoints.with_raw_response.test(
                path_id="",
            )


class TestAsyncEndpoints:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInbound) -> None:
        endpoint = await async_client.endpoints.create()
        assert_matches_type(EndpointCreateResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInbound) -> None:
        endpoint = await async_client.endpoints.create(
            config={},
            description="description",
            name="name",
            type="webhook",
        )
        assert_matches_type(EndpointCreateResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInbound) -> None:
        response = await async_client.endpoints.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert_matches_type(EndpointCreateResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInbound) -> None:
        async with async_client.endpoints.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert_matches_type(EndpointCreateResponse, endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInbound) -> None:
        endpoint = await async_client.endpoints.retrieve(
            "123",
        )
        assert_matches_type(EndpointRetrieveResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInbound) -> None:
        response = await async_client.endpoints.with_raw_response.retrieve(
            "123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert_matches_type(EndpointRetrieveResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInbound) -> None:
        async with async_client.endpoints.with_streaming_response.retrieve(
            "123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert_matches_type(EndpointRetrieveResponse, endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.endpoints.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncInbound) -> None:
        endpoint = await async_client.endpoints.update(
            path_id="123",
        )
        assert_matches_type(EndpointUpdateResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncInbound) -> None:
        endpoint = await async_client.endpoints.update(
            path_id="123",
            body_id="id",
            config={},
            description="description",
            is_active=True,
            name="name",
        )
        assert_matches_type(EndpointUpdateResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncInbound) -> None:
        response = await async_client.endpoints.with_raw_response.update(
            path_id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert_matches_type(EndpointUpdateResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncInbound) -> None:
        async with async_client.endpoints.with_streaming_response.update(
            path_id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert_matches_type(EndpointUpdateResponse, endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.endpoints.with_raw_response.update(
                path_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInbound) -> None:
        endpoint = await async_client.endpoints.list()
        assert_matches_type(EndpointListResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncInbound) -> None:
        endpoint = await async_client.endpoints.list(
            active="true",
            limit=0,
            offset=0,
            sort_by="newest",
            type="webhook",
        )
        assert_matches_type(EndpointListResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInbound) -> None:
        response = await async_client.endpoints.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert_matches_type(EndpointListResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInbound) -> None:
        async with async_client.endpoints.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert_matches_type(EndpointListResponse, endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncInbound) -> None:
        endpoint = await async_client.endpoints.delete(
            "123",
        )
        assert_matches_type(EndpointDeleteResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncInbound) -> None:
        response = await async_client.endpoints.with_raw_response.delete(
            "123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert_matches_type(EndpointDeleteResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncInbound) -> None:
        async with async_client.endpoints.with_streaming_response.delete(
            "123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert_matches_type(EndpointDeleteResponse, endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.endpoints.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test(self, async_client: AsyncInbound) -> None:
        endpoint = await async_client.endpoints.test(
            path_id="123",
        )
        assert_matches_type(EndpointTestResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_with_all_params(self, async_client: AsyncInbound) -> None:
        endpoint = await async_client.endpoints.test(
            path_id="123",
            body_id="id",
            webhook_format="inbound",
        )
        assert_matches_type(EndpointTestResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test(self, async_client: AsyncInbound) -> None:
        response = await async_client.endpoints.with_raw_response.test(
            path_id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        endpoint = await response.parse()
        assert_matches_type(EndpointTestResponse, endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test(self, async_client: AsyncInbound) -> None:
        async with async_client.endpoints.with_streaming_response.test(
            path_id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            endpoint = await response.parse()
            assert_matches_type(EndpointTestResponse, endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_test(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_id` but received ''"):
            await async_client.endpoints.with_raw_response.test(
                path_id="",
            )
