# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inbound import Inbound, AsyncInbound
from tests.utils import assert_matches_type
from inbound.types import (
    MailListResponse,
    MailReplyResponse,
    MailUpdateResponse,
    MailRetrieveResponse,
    MailGetThreadResponse,
    MailBulkUpdateResponse,
    MailGetThreadCountsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMail:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inbound) -> None:
        mail = client.mail.retrieve(
            "id",
        )
        assert_matches_type(MailRetrieveResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inbound) -> None:
        response = client.mail.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailRetrieveResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inbound) -> None:
        with client.mail.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = response.parse()
            assert_matches_type(MailRetrieveResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mail.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Inbound) -> None:
        mail = client.mail.update(
            id="123",
        )
        assert_matches_type(MailUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Inbound) -> None:
        mail = client.mail.update(
            id="123",
            is_archived=True,
            is_read=True,
        )
        assert_matches_type(MailUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Inbound) -> None:
        response = client.mail.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Inbound) -> None:
        with client.mail.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = response.parse()
            assert_matches_type(MailUpdateResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mail.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Inbound) -> None:
        mail = client.mail.list()
        assert_matches_type(MailListResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Inbound) -> None:
        mail = client.mail.list(
            domain="domain",
            email_address="emailAddress",
            email_id="emailId",
            include_archived=True,
            limit=0,
            offset=0,
            search="search",
            status="all",
            time_range="24h",
        )
        assert_matches_type(MailListResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inbound) -> None:
        response = client.mail.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailListResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inbound) -> None:
        with client.mail.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = response.parse()
            assert_matches_type(MailListResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_update(self, client: Inbound) -> None:
        mail = client.mail.bulk_update()
        assert_matches_type(MailBulkUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_update_with_all_params(self, client: Inbound) -> None:
        mail = client.mail.bulk_update(
            email_ids=["string"],
            updates={
                "is_archived": True,
                "is_read": True,
            },
        )
        assert_matches_type(MailBulkUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_update(self, client: Inbound) -> None:
        response = client.mail.with_raw_response.bulk_update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailBulkUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_update(self, client: Inbound) -> None:
        with client.mail.with_streaming_response.bulk_update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = response.parse()
            assert_matches_type(MailBulkUpdateResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_thread(self, client: Inbound) -> None:
        mail = client.mail.get_thread(
            "id",
        )
        assert_matches_type(MailGetThreadResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_thread(self, client: Inbound) -> None:
        response = client.mail.with_raw_response.get_thread(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailGetThreadResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_thread(self, client: Inbound) -> None:
        with client.mail.with_streaming_response.get_thread(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = response.parse()
            assert_matches_type(MailGetThreadResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_thread(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mail.with_raw_response.get_thread(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_thread_counts(self, client: Inbound) -> None:
        mail = client.mail.get_thread_counts()
        assert_matches_type(MailGetThreadCountsResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_thread_counts_with_all_params(self, client: Inbound) -> None:
        mail = client.mail.get_thread_counts(
            email_ids=["string"],
        )
        assert_matches_type(MailGetThreadCountsResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_thread_counts(self, client: Inbound) -> None:
        response = client.mail.with_raw_response.get_thread_counts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailGetThreadCountsResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_thread_counts(self, client: Inbound) -> None:
        with client.mail.with_streaming_response.get_thread_counts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = response.parse()
            assert_matches_type(MailGetThreadCountsResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reply(self, client: Inbound) -> None:
        mail = client.mail.reply()
        assert_matches_type(MailReplyResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reply_with_all_params(self, client: Inbound) -> None:
        mail = client.mail.reply(
            attachments=[
                {
                    "content": "content",
                    "content_type": "contentType",
                    "filename": "filename",
                }
            ],
            email_id="emailId",
            html_body="htmlBody",
            subject="subject",
            text_body="textBody",
            to="to",
        )
        assert_matches_type(MailReplyResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reply(self, client: Inbound) -> None:
        response = client.mail.with_raw_response.reply()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailReplyResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reply(self, client: Inbound) -> None:
        with client.mail.with_streaming_response.reply() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = response.parse()
            assert_matches_type(MailReplyResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMail:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInbound) -> None:
        mail = await async_client.mail.retrieve(
            "id",
        )
        assert_matches_type(MailRetrieveResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInbound) -> None:
        response = await async_client.mail.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailRetrieveResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInbound) -> None:
        async with async_client.mail.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = await response.parse()
            assert_matches_type(MailRetrieveResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mail.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncInbound) -> None:
        mail = await async_client.mail.update(
            id="123",
        )
        assert_matches_type(MailUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncInbound) -> None:
        mail = await async_client.mail.update(
            id="123",
            is_archived=True,
            is_read=True,
        )
        assert_matches_type(MailUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncInbound) -> None:
        response = await async_client.mail.with_raw_response.update(
            id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncInbound) -> None:
        async with async_client.mail.with_streaming_response.update(
            id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = await response.parse()
            assert_matches_type(MailUpdateResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mail.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInbound) -> None:
        mail = await async_client.mail.list()
        assert_matches_type(MailListResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncInbound) -> None:
        mail = await async_client.mail.list(
            domain="domain",
            email_address="emailAddress",
            email_id="emailId",
            include_archived=True,
            limit=0,
            offset=0,
            search="search",
            status="all",
            time_range="24h",
        )
        assert_matches_type(MailListResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInbound) -> None:
        response = await async_client.mail.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailListResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInbound) -> None:
        async with async_client.mail.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = await response.parse()
            assert_matches_type(MailListResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncInbound) -> None:
        mail = await async_client.mail.bulk_update()
        assert_matches_type(MailBulkUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_update_with_all_params(self, async_client: AsyncInbound) -> None:
        mail = await async_client.mail.bulk_update(
            email_ids=["string"],
            updates={
                "is_archived": True,
                "is_read": True,
            },
        )
        assert_matches_type(MailBulkUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncInbound) -> None:
        response = await async_client.mail.with_raw_response.bulk_update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailBulkUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncInbound) -> None:
        async with async_client.mail.with_streaming_response.bulk_update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = await response.parse()
            assert_matches_type(MailBulkUpdateResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_thread(self, async_client: AsyncInbound) -> None:
        mail = await async_client.mail.get_thread(
            "id",
        )
        assert_matches_type(MailGetThreadResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_thread(self, async_client: AsyncInbound) -> None:
        response = await async_client.mail.with_raw_response.get_thread(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailGetThreadResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_thread(self, async_client: AsyncInbound) -> None:
        async with async_client.mail.with_streaming_response.get_thread(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = await response.parse()
            assert_matches_type(MailGetThreadResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_thread(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mail.with_raw_response.get_thread(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_thread_counts(self, async_client: AsyncInbound) -> None:
        mail = await async_client.mail.get_thread_counts()
        assert_matches_type(MailGetThreadCountsResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_thread_counts_with_all_params(self, async_client: AsyncInbound) -> None:
        mail = await async_client.mail.get_thread_counts(
            email_ids=["string"],
        )
        assert_matches_type(MailGetThreadCountsResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_thread_counts(self, async_client: AsyncInbound) -> None:
        response = await async_client.mail.with_raw_response.get_thread_counts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailGetThreadCountsResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_thread_counts(self, async_client: AsyncInbound) -> None:
        async with async_client.mail.with_streaming_response.get_thread_counts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = await response.parse()
            assert_matches_type(MailGetThreadCountsResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reply(self, async_client: AsyncInbound) -> None:
        mail = await async_client.mail.reply()
        assert_matches_type(MailReplyResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reply_with_all_params(self, async_client: AsyncInbound) -> None:
        mail = await async_client.mail.reply(
            attachments=[
                {
                    "content": "content",
                    "content_type": "contentType",
                    "filename": "filename",
                }
            ],
            email_id="emailId",
            html_body="htmlBody",
            subject="subject",
            text_body="textBody",
            to="to",
        )
        assert_matches_type(MailReplyResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reply(self, async_client: AsyncInbound) -> None:
        response = await async_client.mail.with_raw_response.reply()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailReplyResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reply(self, async_client: AsyncInbound) -> None:
        async with async_client.mail.with_streaming_response.reply() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = await response.parse()
            assert_matches_type(MailReplyResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True
