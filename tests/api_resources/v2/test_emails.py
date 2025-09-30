# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inbound import Inbound, AsyncInbound
from tests.utils import assert_matches_type
from inbound.types.v2 import (
    EmailSendResponse,
    EmailReplyResponse,
    EmailResendResponse,
    EmailRetrieveResponse,
    EmailRetryDeliveryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inbound) -> None:
        email = client.v2.emails.retrieve(
            "id",
        )
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inbound) -> None:
        response = client.v2.emails.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inbound) -> None:
        with client.v2.emails.with_streaming_response.retrieve(
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
            client.v2.emails.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reply(self, client: Inbound) -> None:
        email = client.v2.emails.reply(
            id="id",
            from_="support@yourdomain.com",
        )
        assert_matches_type(EmailReplyResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reply_with_all_params(self, client: Inbound) -> None:
        email = client.v2.emails.reply(
            id="id",
            from_="support@yourdomain.com",
            attachments=[
                {
                    "filename": "invoice.pdf",
                    "content": "U3RhaW5sZXNzIHJvY2tz",
                    "content_id": "company-logo",
                    "content_type": "application/pdf",
                    "content_type": "application/pdf",
                    "path": "https://example.com/document.pdf",
                }
            ],
            headers={"foo": "string"},
            html="html",
            reply_all=True,
            subject="subject",
            tags=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            text="text",
            to="string",
            api_version="API-Version",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(EmailReplyResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reply(self, client: Inbound) -> None:
        response = client.v2.emails.with_raw_response.reply(
            id="id",
            from_="support@yourdomain.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailReplyResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reply(self, client: Inbound) -> None:
        with client.v2.emails.with_streaming_response.reply(
            id="id",
            from_="support@yourdomain.com",
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
            client.v2.emails.with_raw_response.reply(
                id="",
                from_="support@yourdomain.com",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_resend(self, client: Inbound) -> None:
        email = client.v2.emails.resend(
            id="id",
            endpoint_id="endpoint_abc123xyz",
        )
        assert_matches_type(EmailResendResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_resend(self, client: Inbound) -> None:
        response = client.v2.emails.with_raw_response.resend(
            id="id",
            endpoint_id="endpoint_abc123xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailResendResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_resend(self, client: Inbound) -> None:
        with client.v2.emails.with_streaming_response.resend(
            id="id",
            endpoint_id="endpoint_abc123xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailResendResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_resend(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v2.emails.with_raw_response.resend(
                id="",
                endpoint_id="endpoint_abc123xyz",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retry_delivery(self, client: Inbound) -> None:
        email = client.v2.emails.retry_delivery(
            id="id",
            delivery_id="delivery_xyz456",
        )
        assert_matches_type(EmailRetryDeliveryResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retry_delivery(self, client: Inbound) -> None:
        response = client.v2.emails.with_raw_response.retry_delivery(
            id="id",
            delivery_id="delivery_xyz456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailRetryDeliveryResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retry_delivery(self, client: Inbound) -> None:
        with client.v2.emails.with_streaming_response.retry_delivery(
            id="id",
            delivery_id="delivery_xyz456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailRetryDeliveryResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retry_delivery(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v2.emails.with_raw_response.retry_delivery(
                id="",
                delivery_id="delivery_xyz456",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: Inbound) -> None:
        email = client.v2.emails.send(
            from_="Support Team <support@yourdomain.com>",
            subject="Welcome to Inbound",
            to=["customer@example.com"],
        )
        assert_matches_type(EmailSendResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: Inbound) -> None:
        email = client.v2.emails.send(
            from_="Support Team <support@yourdomain.com>",
            subject="Welcome to Inbound",
            to=["customer@example.com"],
            attachments=[
                {
                    "filename": "invoice.pdf",
                    "content": "U3RhaW5sZXNzIHJvY2tz",
                    "content_id": "company-logo",
                    "content_type": "application/pdf",
                    "content_type": "application/pdf",
                    "path": "https://example.com/document.pdf",
                }
            ],
            bcc="string",
            cc="string",
            headers={"foo": "string"},
            html="html",
            body_reply_to_1="string",
            body_reply_to_2="string",
            tags=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            text="text",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(EmailSendResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Inbound) -> None:
        response = client.v2.emails.with_raw_response.send(
            from_="Support Team <support@yourdomain.com>",
            subject="Welcome to Inbound",
            to=["customer@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = response.parse()
        assert_matches_type(EmailSendResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Inbound) -> None:
        with client.v2.emails.with_streaming_response.send(
            from_="Support Team <support@yourdomain.com>",
            subject="Welcome to Inbound",
            to=["customer@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = response.parse()
            assert_matches_type(EmailSendResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInbound) -> None:
        email = await async_client.v2.emails.retrieve(
            "id",
        )
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.emails.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailRetrieveResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.emails.with_streaming_response.retrieve(
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
            await async_client.v2.emails.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reply(self, async_client: AsyncInbound) -> None:
        email = await async_client.v2.emails.reply(
            id="id",
            from_="support@yourdomain.com",
        )
        assert_matches_type(EmailReplyResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reply_with_all_params(self, async_client: AsyncInbound) -> None:
        email = await async_client.v2.emails.reply(
            id="id",
            from_="support@yourdomain.com",
            attachments=[
                {
                    "filename": "invoice.pdf",
                    "content": "U3RhaW5sZXNzIHJvY2tz",
                    "content_id": "company-logo",
                    "content_type": "application/pdf",
                    "content_type": "application/pdf",
                    "path": "https://example.com/document.pdf",
                }
            ],
            headers={"foo": "string"},
            html="html",
            reply_all=True,
            subject="subject",
            tags=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            text="text",
            to="string",
            api_version="API-Version",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(EmailReplyResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reply(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.emails.with_raw_response.reply(
            id="id",
            from_="support@yourdomain.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailReplyResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reply(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.emails.with_streaming_response.reply(
            id="id",
            from_="support@yourdomain.com",
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
            await async_client.v2.emails.with_raw_response.reply(
                id="",
                from_="support@yourdomain.com",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_resend(self, async_client: AsyncInbound) -> None:
        email = await async_client.v2.emails.resend(
            id="id",
            endpoint_id="endpoint_abc123xyz",
        )
        assert_matches_type(EmailResendResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_resend(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.emails.with_raw_response.resend(
            id="id",
            endpoint_id="endpoint_abc123xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailResendResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_resend(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.emails.with_streaming_response.resend(
            id="id",
            endpoint_id="endpoint_abc123xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailResendResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_resend(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v2.emails.with_raw_response.resend(
                id="",
                endpoint_id="endpoint_abc123xyz",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retry_delivery(self, async_client: AsyncInbound) -> None:
        email = await async_client.v2.emails.retry_delivery(
            id="id",
            delivery_id="delivery_xyz456",
        )
        assert_matches_type(EmailRetryDeliveryResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retry_delivery(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.emails.with_raw_response.retry_delivery(
            id="id",
            delivery_id="delivery_xyz456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailRetryDeliveryResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retry_delivery(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.emails.with_streaming_response.retry_delivery(
            id="id",
            delivery_id="delivery_xyz456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailRetryDeliveryResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retry_delivery(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v2.emails.with_raw_response.retry_delivery(
                id="",
                delivery_id="delivery_xyz456",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncInbound) -> None:
        email = await async_client.v2.emails.send(
            from_="Support Team <support@yourdomain.com>",
            subject="Welcome to Inbound",
            to=["customer@example.com"],
        )
        assert_matches_type(EmailSendResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncInbound) -> None:
        email = await async_client.v2.emails.send(
            from_="Support Team <support@yourdomain.com>",
            subject="Welcome to Inbound",
            to=["customer@example.com"],
            attachments=[
                {
                    "filename": "invoice.pdf",
                    "content": "U3RhaW5sZXNzIHJvY2tz",
                    "content_id": "company-logo",
                    "content_type": "application/pdf",
                    "content_type": "application/pdf",
                    "path": "https://example.com/document.pdf",
                }
            ],
            bcc="string",
            cc="string",
            headers={"foo": "string"},
            html="html",
            body_reply_to_1="string",
            body_reply_to_2="string",
            tags=[
                {
                    "name": "name",
                    "value": "value",
                }
            ],
            text="text",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(EmailSendResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.emails.with_raw_response.send(
            from_="Support Team <support@yourdomain.com>",
            subject="Welcome to Inbound",
            to=["customer@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email = await response.parse()
        assert_matches_type(EmailSendResponse, email, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.emails.with_streaming_response.send(
            from_="Support Team <support@yourdomain.com>",
            subject="Welcome to Inbound",
            to=["customer@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email = await response.parse()
            assert_matches_type(EmailSendResponse, email, path=["response"])

        assert cast(Any, response.is_closed) is True
