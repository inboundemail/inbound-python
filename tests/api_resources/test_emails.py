# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inbound import Inbound, AsyncInbound
from tests.utils import assert_matches_type
from inbound.types import (
    EmailReplyResponse,
    EmailCreateResponse,
    EmailRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Inbound) -> None:
        email = client.emails.create(
            from_="from",
            subject="subject",
            to="to",
        )
        assert_matches_type(EmailCreateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inbound) -> None:
        email = client.emails.create(
            from_="from",
            subject="subject",
            to="to",
            attachments=["string"],
            bcc="bcc",
            cc="cc",
            headers="headers",
            html="html",
            body_reply_to_1="reply_to",
            body_reply_to_2="replyTo",
            tags="tags",
            text="text",
        )
        assert_matches_type(EmailCreateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inbound) -> None:
        response = client.emails.with_raw_response.create(
            from_="from",
            subject="subject",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailCreateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inbound) -> None:
        with client.emails.with_streaming_response.create(
            from_="from",
            subject="subject",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailCreateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inbound) -> None:
        email = client.emails.retrieve(
            "id",
        )
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inbound) -> None:
        response = client.emails.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inbound) -> None:
        with client.emails.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailRetrieveResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.emails.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reply(self, client: Inbound) -> None:
        email = client.emails.reply(
            id="id",
            from_="from",
        )
        assert_matches_type(EmailReplyResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reply_with_all_params(self, client: Inbound) -> None:
        email = client.emails.reply(
            id="id",
            from_="from",
            attachments=["string"],
            bcc="bcc",
            cc="cc",
            from_name="from_name",
            headers="headers",
            html="html",
            body_include_original_1=True,
            body_include_original_2=True,
            body_reply_to_1="reply_to",
            body_reply_to_2="replyTo",
            simple=True,
            subject="subject",
            tags="tags",
            text="text",
            to="to",
        )
        assert_matches_type(EmailReplyResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reply(self, client: Inbound) -> None:
        response = client.emails.with_raw_response.reply(
            id="id",
            from_="from",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailReplyResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reply(self, client: Inbound) -> None:
        with client.emails.with_streaming_response.reply(
            id="id",
            from_="from",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailReplyResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reply(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.emails.with_raw_response.reply(
                id="",
                from_="from",
            )


class TestAsyncEmails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInbound) -> None:
        email = await async_client.emails.create(
            from_="from",
            subject="subject",
            to="to",
        )
        assert_matches_type(EmailCreateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInbound) -> None:
        email = await async_client.emails.create(
            from_="from",
            subject="subject",
            to="to",
            attachments=["string"],
            bcc="bcc",
            cc="cc",
            headers="headers",
            html="html",
            body_reply_to_1="reply_to",
            body_reply_to_2="replyTo",
            tags="tags",
            text="text",
        )
        assert_matches_type(EmailCreateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInbound) -> None:
        response = await async_client.emails.with_raw_response.create(
            from_="from",
            subject="subject",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailCreateResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInbound) -> None:
        async with async_client.emails.with_streaming_response.create(
            from_="from",
            subject="subject",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailCreateResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInbound) -> None:
        email = await async_client.emails.retrieve(
            "id",
        )
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInbound) -> None:
        response = await async_client.emails.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInbound) -> None:
        async with async_client.emails.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailRetrieveResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.emails.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reply(self, async_client: AsyncInbound) -> None:
        email = await async_client.emails.reply(
            id="id",
            from_="from",
        )
        assert_matches_type(EmailReplyResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reply_with_all_params(self, async_client: AsyncInbound) -> None:
        email = await async_client.emails.reply(
            id="id",
            from_="from",
            attachments=["string"],
            bcc="bcc",
            cc="cc",
            from_name="from_name",
            headers="headers",
            html="html",
            body_include_original_1=True,
            body_include_original_2=True,
            body_reply_to_1="reply_to",
            body_reply_to_2="replyTo",
            simple=True,
            subject="subject",
            tags="tags",
            text="text",
            to="to",
        )
        assert_matches_type(EmailReplyResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reply(self, async_client: AsyncInbound) -> None:
        response = await async_client.emails.with_raw_response.reply(
            id="id",
            from_="from",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailReplyResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reply(self, async_client: AsyncInbound) -> None:
        async with async_client.emails.with_streaming_response.reply(
            id="id",
            from_="from",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailReplyResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reply(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.emails.with_raw_response.reply(
                id="",
                from_="from",
            )
