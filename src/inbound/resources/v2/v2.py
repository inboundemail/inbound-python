# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .mail import (
    MailResource,
    AsyncMailResource,
    MailResourceWithRawResponse,
    AsyncMailResourceWithRawResponse,
    MailResourceWithStreamingResponse,
    AsyncMailResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .endpoints import (
    EndpointsResource,
    AsyncEndpointsResource,
    EndpointsResourceWithRawResponse,
    AsyncEndpointsResourceWithRawResponse,
    EndpointsResourceWithStreamingResponse,
    AsyncEndpointsResourceWithStreamingResponse,
)
from .onboarding import (
    OnboardingResource,
    AsyncOnboardingResource,
    OnboardingResourceWithRawResponse,
    AsyncOnboardingResourceWithRawResponse,
    OnboardingResourceWithStreamingResponse,
    AsyncOnboardingResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .emails.emails import (
    EmailsResource,
    AsyncEmailsResource,
    EmailsResourceWithRawResponse,
    AsyncEmailsResourceWithRawResponse,
    EmailsResourceWithStreamingResponse,
    AsyncEmailsResourceWithStreamingResponse,
)
from .domains.domains import (
    DomainsResource,
    AsyncDomainsResource,
    DomainsResourceWithRawResponse,
    AsyncDomainsResourceWithRawResponse,
    DomainsResourceWithStreamingResponse,
    AsyncDomainsResourceWithStreamingResponse,
)
from .email_addresses import (
    EmailAddressesResource,
    AsyncEmailAddressesResource,
    EmailAddressesResourceWithRawResponse,
    AsyncEmailAddressesResourceWithRawResponse,
    EmailAddressesResourceWithStreamingResponse,
    AsyncEmailAddressesResourceWithStreamingResponse,
)

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    @cached_property
    def domains(self) -> DomainsResource:
        return DomainsResource(self._client)

    @cached_property
    def email_addresses(self) -> EmailAddressesResource:
        return EmailAddressesResource(self._client)

    @cached_property
    def emails(self) -> EmailsResource:
        return EmailsResource(self._client)

    @cached_property
    def endpoints(self) -> EndpointsResource:
        return EndpointsResource(self._client)

    @cached_property
    def mail(self) -> MailResource:
        return MailResource(self._client)

    @cached_property
    def onboarding(self) -> OnboardingResource:
        return OnboardingResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inboundemail/inbound-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inboundemail/inbound-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)


class AsyncV2Resource(AsyncAPIResource):
    @cached_property
    def domains(self) -> AsyncDomainsResource:
        return AsyncDomainsResource(self._client)

    @cached_property
    def email_addresses(self) -> AsyncEmailAddressesResource:
        return AsyncEmailAddressesResource(self._client)

    @cached_property
    def emails(self) -> AsyncEmailsResource:
        return AsyncEmailsResource(self._client)

    @cached_property
    def endpoints(self) -> AsyncEndpointsResource:
        return AsyncEndpointsResource(self._client)

    @cached_property
    def mail(self) -> AsyncMailResource:
        return AsyncMailResource(self._client)

    @cached_property
    def onboarding(self) -> AsyncOnboardingResource:
        return AsyncOnboardingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/inboundemail/inbound-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/inboundemail/inbound-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def domains(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self._v2.domains)

    @cached_property
    def email_addresses(self) -> EmailAddressesResourceWithRawResponse:
        return EmailAddressesResourceWithRawResponse(self._v2.email_addresses)

    @cached_property
    def emails(self) -> EmailsResourceWithRawResponse:
        return EmailsResourceWithRawResponse(self._v2.emails)

    @cached_property
    def endpoints(self) -> EndpointsResourceWithRawResponse:
        return EndpointsResourceWithRawResponse(self._v2.endpoints)

    @cached_property
    def mail(self) -> MailResourceWithRawResponse:
        return MailResourceWithRawResponse(self._v2.mail)

    @cached_property
    def onboarding(self) -> OnboardingResourceWithRawResponse:
        return OnboardingResourceWithRawResponse(self._v2.onboarding)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self._v2.domains)

    @cached_property
    def email_addresses(self) -> AsyncEmailAddressesResourceWithRawResponse:
        return AsyncEmailAddressesResourceWithRawResponse(self._v2.email_addresses)

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithRawResponse:
        return AsyncEmailsResourceWithRawResponse(self._v2.emails)

    @cached_property
    def endpoints(self) -> AsyncEndpointsResourceWithRawResponse:
        return AsyncEndpointsResourceWithRawResponse(self._v2.endpoints)

    @cached_property
    def mail(self) -> AsyncMailResourceWithRawResponse:
        return AsyncMailResourceWithRawResponse(self._v2.mail)

    @cached_property
    def onboarding(self) -> AsyncOnboardingResourceWithRawResponse:
        return AsyncOnboardingResourceWithRawResponse(self._v2.onboarding)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

    @cached_property
    def domains(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self._v2.domains)

    @cached_property
    def email_addresses(self) -> EmailAddressesResourceWithStreamingResponse:
        return EmailAddressesResourceWithStreamingResponse(self._v2.email_addresses)

    @cached_property
    def emails(self) -> EmailsResourceWithStreamingResponse:
        return EmailsResourceWithStreamingResponse(self._v2.emails)

    @cached_property
    def endpoints(self) -> EndpointsResourceWithStreamingResponse:
        return EndpointsResourceWithStreamingResponse(self._v2.endpoints)

    @cached_property
    def mail(self) -> MailResourceWithStreamingResponse:
        return MailResourceWithStreamingResponse(self._v2.mail)

    @cached_property
    def onboarding(self) -> OnboardingResourceWithStreamingResponse:
        return OnboardingResourceWithStreamingResponse(self._v2.onboarding)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

    @cached_property
    def domains(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self._v2.domains)

    @cached_property
    def email_addresses(self) -> AsyncEmailAddressesResourceWithStreamingResponse:
        return AsyncEmailAddressesResourceWithStreamingResponse(self._v2.email_addresses)

    @cached_property
    def emails(self) -> AsyncEmailsResourceWithStreamingResponse:
        return AsyncEmailsResourceWithStreamingResponse(self._v2.emails)

    @cached_property
    def endpoints(self) -> AsyncEndpointsResourceWithStreamingResponse:
        return AsyncEndpointsResourceWithStreamingResponse(self._v2.endpoints)

    @cached_property
    def mail(self) -> AsyncMailResourceWithStreamingResponse:
        return AsyncMailResourceWithStreamingResponse(self._v2.mail)

    @cached_property
    def onboarding(self) -> AsyncOnboardingResourceWithStreamingResponse:
        return AsyncOnboardingResourceWithStreamingResponse(self._v2.onboarding)
