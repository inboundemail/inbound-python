# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from inbound import Inbound, AsyncInbound
from tests.utils import assert_matches_type
from inbound.types.v2.emails import (
    ScheduleListResponse,
    ScheduleCancelResponse,
    ScheduleCreateResponse,
    ScheduleRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSchedule:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Inbound) -> None:
        schedule = client.v2.emails.schedule.create(
            from_="sender@yourdomain.com",
            scheduled_at="2025-10-01T09:00:00Z",
            subject="Scheduled Newsletter",
            to=["recipient@example.com"],
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Inbound) -> None:
        schedule = client.v2.emails.schedule.create(
            from_="sender@yourdomain.com",
            scheduled_at="2025-10-01T09:00:00Z",
            subject="Scheduled Newsletter",
            to=["recipient@example.com"],
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
            timezone="America/New_York",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Inbound) -> None:
        response = client.v2.emails.schedule.with_raw_response.create(
            from_="sender@yourdomain.com",
            scheduled_at="2025-10-01T09:00:00Z",
            subject="Scheduled Newsletter",
            to=["recipient@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Inbound) -> None:
        with client.v2.emails.schedule.with_streaming_response.create(
            from_="sender@yourdomain.com",
            scheduled_at="2025-10-01T09:00:00Z",
            subject="Scheduled Newsletter",
            to=["recipient@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Inbound) -> None:
        schedule = client.v2.emails.schedule.retrieve(
            "id",
        )
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Inbound) -> None:
        response = client.v2.emails.schedule.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Inbound) -> None:
        with client.v2.emails.schedule.with_streaming_response.retrieve(
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
            client.v2.emails.schedule.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Inbound) -> None:
        schedule = client.v2.emails.schedule.list()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Inbound) -> None:
        schedule = client.v2.emails.schedule.list(
            limit=0,
            offset=0,
            status="status",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Inbound) -> None:
        response = client.v2.emails.schedule.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Inbound) -> None:
        with client.v2.emails.schedule.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Inbound) -> None:
        schedule = client.v2.emails.schedule.cancel(
            "id",
        )
        assert_matches_type(ScheduleCancelResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Inbound) -> None:
        response = client.v2.emails.schedule.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = response.parse()
        assert_matches_type(ScheduleCancelResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Inbound) -> None:
        with client.v2.emails.schedule.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = response.parse()
            assert_matches_type(ScheduleCancelResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Inbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.v2.emails.schedule.with_raw_response.cancel(
                "",
            )


class TestAsyncSchedule:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncInbound) -> None:
        schedule = await async_client.v2.emails.schedule.create(
            from_="sender@yourdomain.com",
            scheduled_at="2025-10-01T09:00:00Z",
            subject="Scheduled Newsletter",
            to=["recipient@example.com"],
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncInbound) -> None:
        schedule = await async_client.v2.emails.schedule.create(
            from_="sender@yourdomain.com",
            scheduled_at="2025-10-01T09:00:00Z",
            subject="Scheduled Newsletter",
            to=["recipient@example.com"],
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
            timezone="America/New_York",
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.emails.schedule.with_raw_response.create(
            from_="sender@yourdomain.com",
            scheduled_at="2025-10-01T09:00:00Z",
            subject="Scheduled Newsletter",
            to=["recipient@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.emails.schedule.with_streaming_response.create(
            from_="sender@yourdomain.com",
            scheduled_at="2025-10-01T09:00:00Z",
            subject="Scheduled Newsletter",
            to=["recipient@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleCreateResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncInbound) -> None:
        schedule = await async_client.v2.emails.schedule.retrieve(
            "id",
        )
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.emails.schedule.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleRetrieveResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.emails.schedule.with_streaming_response.retrieve(
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
            await async_client.v2.emails.schedule.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncInbound) -> None:
        schedule = await async_client.v2.emails.schedule.list()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncInbound) -> None:
        schedule = await async_client.v2.emails.schedule.list(
            limit=0,
            offset=0,
            status="status",
        )
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.emails.schedule.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleListResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.emails.schedule.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleListResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncInbound) -> None:
        schedule = await async_client.v2.emails.schedule.cancel(
            "id",
        )
        assert_matches_type(ScheduleCancelResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncInbound) -> None:
        response = await async_client.v2.emails.schedule.with_raw_response.cancel(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule = await response.parse()
        assert_matches_type(ScheduleCancelResponse, schedule, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncInbound) -> None:
        async with async_client.v2.emails.schedule.with_streaming_response.cancel(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule = await response.parse()
            assert_matches_type(ScheduleCancelResponse, schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncInbound) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.v2.emails.schedule.with_raw_response.cancel(
                "",
            )
