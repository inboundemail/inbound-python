# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inbound import Inbound, AsyncInbound
from tests.utils import assert_matches_type
from inbound.types.emails import (
    ScheduleListResponse,
    ScheduleCreateResponse,
    ScheduleDeleteResponse,
    ScheduleRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedule:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Inbound) -> None:
        schedule = client.emails.schedule.create(
            from_="from",
            scheduled_at="scheduled_at",
            subject="subject",
            to="to",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inbound) -> None:
        schedule = client.emails.schedule.create(
            from_="from",
            scheduled_at="scheduled_at",
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
            timezone="timezone",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inbound) -> None:
        response = client.emails.schedule.with_raw_response.create(
            from_="from",
            scheduled_at="scheduled_at",
            subject="subject",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inbound) -> None:
        with client.emails.schedule.with_streaming_response.create(
            from_="from",
            scheduled_at="scheduled_at",
            subject="subject",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inbound) -> None:
        schedule = client.emails.schedule.retrieve(
            "id",
        )
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inbound) -> None:
        response = client.emails.schedule.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inbound) -> None:
        with client.emails.schedule.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.emails.schedule.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Inbound) -> None:
        schedule = client.emails.schedule.list()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Inbound) -> None:
        schedule = client.emails.schedule.list(
            limit=0,
            offset=0,
            status="status",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inbound) -> None:
        response = client.emails.schedule.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inbound) -> None:
        with client.emails.schedule.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Inbound) -> None:
        schedule = client.emails.schedule.delete(
            "id",
        )
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Inbound) -> None:
        response = client.emails.schedule.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Inbound) -> None:
        with client.emails.schedule.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.emails.schedule.with_raw_response.delete(
                "",
            )


class TestAsyncSchedule:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInbound) -> None:
        schedule = await async_client.emails.schedule.create(
            from_="from",
            scheduled_at="scheduled_at",
            subject="subject",
            to="to",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInbound) -> None:
        schedule = await async_client.emails.schedule.create(
            from_="from",
            scheduled_at="scheduled_at",
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
            timezone="timezone",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInbound) -> None:
        response = await async_client.emails.schedule.with_raw_response.create(
            from_="from",
            scheduled_at="scheduled_at",
            subject="subject",
            to="to",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInbound) -> None:
        async with async_client.emails.schedule.with_streaming_response.create(
            from_="from",
            scheduled_at="scheduled_at",
            subject="subject",
            to="to",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInbound) -> None:
        schedule = await async_client.emails.schedule.retrieve(
            "id",
        )
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInbound) -> None:
        response = await async_client.emails.schedule.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInbound) -> None:
        async with async_client.emails.schedule.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.emails.schedule.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInbound) -> None:
        schedule = await async_client.emails.schedule.list()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncInbound) -> None:
        schedule = await async_client.emails.schedule.list(
            limit=0,
            offset=0,
            status="status",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInbound) -> None:
        response = await async_client.emails.schedule.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInbound) -> None:
        async with async_client.emails.schedule.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncInbound) -> None:
        schedule = await async_client.emails.schedule.delete(
            "id",
        )
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncInbound) -> None:
        response = await async_client.emails.schedule.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncInbound) -> None:
        async with async_client.emails.schedule.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleDeleteResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.emails.schedule.with_raw_response.delete(
                "",
            )
