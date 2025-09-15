# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inbound import Inbound, AsyncInbound
from tests.utils import assert_matches_type
from inbound.types import (
    OnboardingSendDemoResponse,
    OnboardingCheckReplyResponse,
    OnboardingHandleWebhookResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOnboarding:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_check_reply(self, client: Inbound) -> None:
        onboarding = client.onboarding.check_reply()
        assert_matches_type(OnboardingCheckReplyResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_check_reply(self, client: Inbound) -> None:
        response = client.onboarding.with_raw_response.check_reply()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onboarding = response.parse()
        assert_matches_type(OnboardingCheckReplyResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_check_reply(self, client: Inbound) -> None:
        with client.onboarding.with_streaming_response.check_reply() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onboarding = response.parse()
            assert_matches_type(OnboardingCheckReplyResponse, onboarding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_handle_webhook(self, client: Inbound) -> None:
        onboarding = client.onboarding.handle_webhook()
        assert_matches_type(OnboardingHandleWebhookResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_handle_webhook(self, client: Inbound) -> None:
        response = client.onboarding.with_raw_response.handle_webhook()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onboarding = response.parse()
        assert_matches_type(OnboardingHandleWebhookResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_handle_webhook(self, client: Inbound) -> None:
        with client.onboarding.with_streaming_response.handle_webhook() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onboarding = response.parse()
            assert_matches_type(OnboardingHandleWebhookResponse, onboarding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_demo(self, client: Inbound) -> None:
        onboarding = client.onboarding.send_demo()
        assert_matches_type(OnboardingSendDemoResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_demo_with_all_params(self, client: Inbound) -> None:
        onboarding = client.onboarding.send_demo(
            api_key="apiKey",
            to="to",
        )
        assert_matches_type(OnboardingSendDemoResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_demo(self, client: Inbound) -> None:
        response = client.onboarding.with_raw_response.send_demo()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onboarding = response.parse()
        assert_matches_type(OnboardingSendDemoResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_demo(self, client: Inbound) -> None:
        with client.onboarding.with_streaming_response.send_demo() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onboarding = response.parse()
            assert_matches_type(OnboardingSendDemoResponse, onboarding, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOnboarding:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_check_reply(self, async_client: AsyncInbound) -> None:
        onboarding = await async_client.onboarding.check_reply()
        assert_matches_type(OnboardingCheckReplyResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_check_reply(self, async_client: AsyncInbound) -> None:
        response = await async_client.onboarding.with_raw_response.check_reply()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onboarding = await response.parse()
        assert_matches_type(OnboardingCheckReplyResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_check_reply(self, async_client: AsyncInbound) -> None:
        async with async_client.onboarding.with_streaming_response.check_reply() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onboarding = await response.parse()
            assert_matches_type(OnboardingCheckReplyResponse, onboarding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_handle_webhook(self, async_client: AsyncInbound) -> None:
        onboarding = await async_client.onboarding.handle_webhook()
        assert_matches_type(OnboardingHandleWebhookResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_handle_webhook(self, async_client: AsyncInbound) -> None:
        response = await async_client.onboarding.with_raw_response.handle_webhook()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onboarding = await response.parse()
        assert_matches_type(OnboardingHandleWebhookResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_handle_webhook(self, async_client: AsyncInbound) -> None:
        async with async_client.onboarding.with_streaming_response.handle_webhook() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onboarding = await response.parse()
            assert_matches_type(OnboardingHandleWebhookResponse, onboarding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_demo(self, async_client: AsyncInbound) -> None:
        onboarding = await async_client.onboarding.send_demo()
        assert_matches_type(OnboardingSendDemoResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_demo_with_all_params(self, async_client: AsyncInbound) -> None:
        onboarding = await async_client.onboarding.send_demo(
            api_key="apiKey",
            to="to",
        )
        assert_matches_type(OnboardingSendDemoResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_demo(self, async_client: AsyncInbound) -> None:
        response = await async_client.onboarding.with_raw_response.send_demo()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        onboarding = await response.parse()
        assert_matches_type(OnboardingSendDemoResponse, onboarding, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_demo(self, async_client: AsyncInbound) -> None:
        async with async_client.onboarding.with_streaming_response.send_demo() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            onboarding = await response.parse()
            assert_matches_type(OnboardingSendDemoResponse, onboarding, path=["response"])

        assert cast(Any, response.is_closed) is True
