# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inbound import Inbound, AsyncInbound
from tests.utils import assert_matches_type
from inbound.types.v2 import (
    MailListResponse,
    MailCreateResponse,
    MailUpdateResponse,
    MailRetrieveResponse,
    MailBulkCreateResponse,
    MailRetrieveThreadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMail:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Inbound) -> None:
        mail = client.v2.mail.create(
            email_id="emailId",
            subject="subject",
            to="to",
        )
        assert_matches_type(MailCreateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inbound) -> None:
        mail = client.v2.mail.create(
            email_id="emailId",
            subject="subject",
            to="to",
            attachments="attachments",
            html_body="htmlBody",
            text_body="textBody",
        )
        assert_matches_type(MailCreateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inbound) -> None:
        response = client.v2.mail.with_raw_response.create(
            email_id="emailId",
            subject="subject",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailCreateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inbound) -> None:
        with client.v2.mail.with_streaming_response.create(
            email_id="emailId",
            subject="subject",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = response.parse()
            assert_matches_type(MailCreateResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inbound) -> None:
        mail = client.v2.mail.retrieve(
            "id",
        )
        assert_matches_type(MailRetrieveResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inbound) -> None:
        response = client.v2.mail.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailRetrieveResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inbound) -> None:
        with client.v2.mail.with_streaming_response.retrieve(
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
            client.v2.mail.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Inbound) -> None:
        mail = client.v2.mail.update(
            id="id",
        )
        assert_matches_type(MailUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Inbound) -> None:
        mail = client.v2.mail.update(
            id="id",
            is_archived=True,
            is_read=True,
        )
        assert_matches_type(MailUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Inbound) -> None:
        response = client.v2.mail.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Inbound) -> None:
        with client.v2.mail.with_streaming_response.update(
            id="id",
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
            client.v2.mail.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Inbound) -> None:
        mail = client.v2.mail.list()
        assert_matches_type(MailListResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Inbound) -> None:
        mail = client.v2.mail.list(
            domain="domain",
            email_address="emailAddress",
            email_id="emailId",
            include_archived=True,
            limit=0,
            offset=0,
            search="search",
            status="failed",
            time_range="24h",
        )
        assert_matches_type(MailListResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inbound) -> None:
        response = client.v2.mail.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailListResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inbound) -> None:
        with client.v2.mail.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = response.parse()
            assert_matches_type(MailListResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_bulk_create(self, client: Inbound) -> None:
        mail = client.v2.mail.bulk_create(
            email_ids="emailIds",
            updates=True,
        )
        assert_matches_type(MailBulkCreateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_bulk_create(self, client: Inbound) -> None:
        response = client.v2.mail.with_raw_response.bulk_create(
            email_ids="emailIds",
            updates=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailBulkCreateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_bulk_create(self, client: Inbound) -> None:
        with client.v2.mail.with_streaming_response.bulk_create(
            email_ids="emailIds",
            updates=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = response.parse()
            assert_matches_type(MailBulkCreateResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_thread(self, client: Inbound) -> None:
        mail = client.v2.mail.retrieve_thread(
            "id",
        )
        assert_matches_type(MailRetrieveThreadResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_thread(self, client: Inbound) -> None:
        response = client.v2.mail.with_raw_response.retrieve_thread(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(MailRetrieveThreadResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_thread(self, client: Inbound) -> None:
        with client.v2.mail.with_streaming_response.retrieve_thread(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = response.parse()
            assert_matches_type(MailRetrieveThreadResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_thread(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v2.mail.with_raw_response.retrieve_thread(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_thread_counts(self, client: Inbound) -> None:
        mail = client.v2.mail.thread_counts()
        assert_matches_type(object, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_thread_counts(self, client: Inbound) -> None:
        response = client.v2.mail.with_raw_response.thread_counts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = response.parse()
        assert_matches_type(object, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_thread_counts(self, client: Inbound) -> None:
        with client.v2.mail.with_streaming_response.thread_counts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = response.parse()
            assert_matches_type(object, mail, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMail:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInbound) -> None:
        mail = await async_client.v2.mail.create(
            email_id="emailId",
            subject="subject",
            to="to",
        )
        assert_matches_type(MailCreateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInbound) -> None:
        mail = await async_client.v2.mail.create(
            email_id="emailId",
            subject="subject",
            to="to",
            attachments="attachments",
            html_body="htmlBody",
            text_body="textBody",
        )
        assert_matches_type(MailCreateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.mail.with_raw_response.create(
            email_id="emailId",
            subject="subject",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailCreateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.mail.with_streaming_response.create(
            email_id="emailId",
            subject="subject",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = await response.parse()
            assert_matches_type(MailCreateResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInbound) -> None:
        mail = await async_client.v2.mail.retrieve(
            "id",
        )
        assert_matches_type(MailRetrieveResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.mail.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailRetrieveResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.mail.with_streaming_response.retrieve(
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
            await async_client.v2.mail.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncInbound) -> None:
        mail = await async_client.v2.mail.update(
            id="id",
        )
        assert_matches_type(MailUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncInbound) -> None:
        mail = await async_client.v2.mail.update(
            id="id",
            is_archived=True,
            is_read=True,
        )
        assert_matches_type(MailUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.mail.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailUpdateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.mail.with_streaming_response.update(
            id="id",
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
            await async_client.v2.mail.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInbound) -> None:
        mail = await async_client.v2.mail.list()
        assert_matches_type(MailListResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncInbound) -> None:
        mail = await async_client.v2.mail.list(
            domain="domain",
            email_address="emailAddress",
            email_id="emailId",
            include_archived=True,
            limit=0,
            offset=0,
            search="search",
            status="failed",
            time_range="24h",
        )
        assert_matches_type(MailListResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.mail.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailListResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.mail.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = await response.parse()
            assert_matches_type(MailListResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_bulk_create(self, async_client: AsyncInbound) -> None:
        mail = await async_client.v2.mail.bulk_create(
            email_ids="emailIds",
            updates=True,
        )
        assert_matches_type(MailBulkCreateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_bulk_create(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.mail.with_raw_response.bulk_create(
            email_ids="emailIds",
            updates=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailBulkCreateResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_bulk_create(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.mail.with_streaming_response.bulk_create(
            email_ids="emailIds",
            updates=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = await response.parse()
            assert_matches_type(MailBulkCreateResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_thread(self, async_client: AsyncInbound) -> None:
        mail = await async_client.v2.mail.retrieve_thread(
            "id",
        )
        assert_matches_type(MailRetrieveThreadResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_thread(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.mail.with_raw_response.retrieve_thread(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(MailRetrieveThreadResponse, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_thread(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.mail.with_streaming_response.retrieve_thread(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = await response.parse()
            assert_matches_type(MailRetrieveThreadResponse, mail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_thread(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v2.mail.with_raw_response.retrieve_thread(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_thread_counts(self, async_client: AsyncInbound) -> None:
        mail = await async_client.v2.mail.thread_counts()
        assert_matches_type(object, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_thread_counts(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.mail.with_raw_response.thread_counts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mail = await response.parse()
        assert_matches_type(object, mail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_thread_counts(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.mail.with_streaming_response.thread_counts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mail = await response.parse()
            assert_matches_type(object, mail, path=["response"])

        assert cast(Any, response.is_closed) is True
