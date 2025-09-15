# Domains

Types:

```python
from inbound.types import (
    DomainCreateResponse,
    DomainRetrieveResponse,
    DomainListResponse,
    DomainDeleteResponse,
    DomainRetrieveDNSRecordsResponse,
    DomainUpdateCatchAllResponse,
    DomainUpgradeMailFromResponse,
)
```

Methods:

- <code title="post /v2/domains">client.domains.<a href="./src/inbound/resources/domains/domains.py">create</a>(\*\*<a href="src/inbound/types/domain_create_params.py">params</a>) -> <a href="./src/inbound/types/domain_create_response.py">DomainCreateResponse</a></code>
- <code title="get /v2/domains/{id}">client.domains.<a href="./src/inbound/resources/domains/domains.py">retrieve</a>(path_id, \*\*<a href="src/inbound/types/domain_retrieve_params.py">params</a>) -> <a href="./src/inbound/types/domain_retrieve_response.py">DomainRetrieveResponse</a></code>
- <code title="get /v2/domains">client.domains.<a href="./src/inbound/resources/domains/domains.py">list</a>(\*\*<a href="src/inbound/types/domain_list_params.py">params</a>) -> <a href="./src/inbound/types/domain_list_response.py">DomainListResponse</a></code>
- <code title="delete /v2/domains/{id}">client.domains.<a href="./src/inbound/resources/domains/domains.py">delete</a>(id) -> <a href="./src/inbound/types/domain_delete_response.py">DomainDeleteResponse</a></code>
- <code title="get /v2/domains/{id}/dns-records">client.domains.<a href="./src/inbound/resources/domains/domains.py">retrieve_dns_records</a>(id) -> <a href="./src/inbound/types/domain_retrieve_dns_records_response.py">DomainRetrieveDNSRecordsResponse</a></code>
- <code title="put /v2/domains/{id}">client.domains.<a href="./src/inbound/resources/domains/domains.py">update_catch_all</a>(id, \*\*<a href="src/inbound/types/domain_update_catch_all_params.py">params</a>) -> <a href="./src/inbound/types/domain_update_catch_all_response.py">DomainUpdateCatchAllResponse</a></code>
- <code title="patch /v2/domains/{id}">client.domains.<a href="./src/inbound/resources/domains/domains.py">upgrade_mail_from</a>(id, \*\*<a href="src/inbound/types/domain_upgrade_mail_from_params.py">params</a>) -> <a href="./src/inbound/types/domain_upgrade_mail_from_response.py">DomainUpgradeMailFromResponse</a></code>

## Auth

Types:

```python
from inbound.types.domains import AuthInitializeResponse, AuthVerifyResponse
```

Methods:

- <code title="post /v2/domains/{id}/auth">client.domains.auth.<a href="./src/inbound/resources/domains/auth.py">initialize</a>(id, \*\*<a href="src/inbound/types/domains/auth_initialize_params.py">params</a>) -> <a href="./src/inbound/types/domains/auth_initialize_response.py">AuthInitializeResponse</a></code>
- <code title="patch /v2/domains/{id}/auth">client.domains.auth.<a href="./src/inbound/resources/domains/auth.py">verify</a>(id, \*\*<a href="src/inbound/types/domains/auth_verify_params.py">params</a>) -> <a href="./src/inbound/types/domains/auth_verify_response.py">AuthVerifyResponse</a></code>

# EmailAddresses

Types:

```python
from inbound.types import (
    EmailAddressCreateResponse,
    EmailAddressRetrieveResponse,
    EmailAddressUpdateResponse,
    EmailAddressListResponse,
    EmailAddressDeleteResponse,
)
```

Methods:

- <code title="post /v2/email-addresses">client.email_addresses.<a href="./src/inbound/resources/email_addresses.py">create</a>(\*\*<a href="src/inbound/types/email_address_create_params.py">params</a>) -> <a href="./src/inbound/types/email_address_create_response.py">EmailAddressCreateResponse</a></code>
- <code title="get /v2/email-addresses/{id}">client.email_addresses.<a href="./src/inbound/resources/email_addresses.py">retrieve</a>(id) -> <a href="./src/inbound/types/email_address_retrieve_response.py">EmailAddressRetrieveResponse</a></code>
- <code title="put /v2/email-addresses/{id}">client.email_addresses.<a href="./src/inbound/resources/email_addresses.py">update</a>(id, \*\*<a href="src/inbound/types/email_address_update_params.py">params</a>) -> <a href="./src/inbound/types/email_address_update_response.py">EmailAddressUpdateResponse</a></code>
- <code title="get /v2/email-addresses">client.email_addresses.<a href="./src/inbound/resources/email_addresses.py">list</a>(\*\*<a href="src/inbound/types/email_address_list_params.py">params</a>) -> <a href="./src/inbound/types/email_address_list_response.py">EmailAddressListResponse</a></code>
- <code title="delete /v2/email-addresses/{id}">client.email_addresses.<a href="./src/inbound/resources/email_addresses.py">delete</a>(id) -> <a href="./src/inbound/types/email_address_delete_response.py">EmailAddressDeleteResponse</a></code>

# Emails

Types:

```python
from inbound.types import EmailRetrieveResponse, EmailReplyResponse, EmailSendResponse
```

Methods:

- <code title="get /v2/emails/{id}">client.emails.<a href="./src/inbound/resources/emails/emails.py">retrieve</a>(id) -> <a href="./src/inbound/types/email_retrieve_response.py">EmailRetrieveResponse</a></code>
- <code title="post /v2/emails/{id}/reply">client.emails.<a href="./src/inbound/resources/emails/emails.py">reply</a>(id, \*\*<a href="src/inbound/types/email_reply_params.py">params</a>) -> <a href="./src/inbound/types/email_reply_response.py">EmailReplyResponse</a></code>
- <code title="post /v2/emails">client.emails.<a href="./src/inbound/resources/emails/emails.py">send</a>(\*\*<a href="src/inbound/types/email_send_params.py">params</a>) -> <a href="./src/inbound/types/email_send_response.py">EmailSendResponse</a></code>

## Schedule

Types:

```python
from inbound.types.emails import ScheduleCreateResponse, ScheduleListResponse
```

Methods:

- <code title="post /v2/emails/schedule">client.emails.schedule.<a href="./src/inbound/resources/emails/schedule.py">create</a>(\*\*<a href="src/inbound/types/emails/schedule_create_params.py">params</a>) -> <a href="./src/inbound/types/emails/schedule_create_response.py">ScheduleCreateResponse</a></code>
- <code title="get /v2/emails/schedule">client.emails.schedule.<a href="./src/inbound/resources/emails/schedule.py">list</a>(\*\*<a href="src/inbound/types/emails/schedule_list_params.py">params</a>) -> <a href="./src/inbound/types/emails/schedule_list_response.py">ScheduleListResponse</a></code>

# Endpoints

Types:

```python
from inbound.types import (
    EndpointCreateResponse,
    EndpointRetrieveResponse,
    EndpointUpdateResponse,
    EndpointListResponse,
    EndpointDeleteResponse,
    EndpointTestResponse,
)
```

Methods:

- <code title="post /v2/endpoints">client.endpoints.<a href="./src/inbound/resources/endpoints.py">create</a>(\*\*<a href="src/inbound/types/endpoint_create_params.py">params</a>) -> <a href="./src/inbound/types/endpoint_create_response.py">EndpointCreateResponse</a></code>
- <code title="get /v2/endpoints/{id}">client.endpoints.<a href="./src/inbound/resources/endpoints.py">retrieve</a>(id) -> <a href="./src/inbound/types/endpoint_retrieve_response.py">EndpointRetrieveResponse</a></code>
- <code title="put /v2/endpoints/{id}">client.endpoints.<a href="./src/inbound/resources/endpoints.py">update</a>(path_id, \*\*<a href="src/inbound/types/endpoint_update_params.py">params</a>) -> <a href="./src/inbound/types/endpoint_update_response.py">EndpointUpdateResponse</a></code>
- <code title="get /v2/endpoints">client.endpoints.<a href="./src/inbound/resources/endpoints.py">list</a>(\*\*<a href="src/inbound/types/endpoint_list_params.py">params</a>) -> <a href="./src/inbound/types/endpoint_list_response.py">EndpointListResponse</a></code>
- <code title="delete /v2/endpoints/{id}">client.endpoints.<a href="./src/inbound/resources/endpoints.py">delete</a>(id) -> <a href="./src/inbound/types/endpoint_delete_response.py">EndpointDeleteResponse</a></code>
- <code title="post /v2/endpoints/{id}/test">client.endpoints.<a href="./src/inbound/resources/endpoints.py">test</a>(path_id, \*\*<a href="src/inbound/types/endpoint_test_params.py">params</a>) -> <a href="./src/inbound/types/endpoint_test_response.py">EndpointTestResponse</a></code>

# Mail

Types:

```python
from inbound.types import (
    MailRetrieveResponse,
    MailUpdateResponse,
    MailListResponse,
    MailBulkUpdateResponse,
    MailGetThreadResponse,
    MailGetThreadCountsResponse,
    MailReplyResponse,
)
```

Methods:

- <code title="get /v2/mail/{id}">client.mail.<a href="./src/inbound/resources/mail.py">retrieve</a>(id) -> <a href="./src/inbound/types/mail_retrieve_response.py">MailRetrieveResponse</a></code>
- <code title="patch /v2/mail/{id}">client.mail.<a href="./src/inbound/resources/mail.py">update</a>(id, \*\*<a href="src/inbound/types/mail_update_params.py">params</a>) -> <a href="./src/inbound/types/mail_update_response.py">MailUpdateResponse</a></code>
- <code title="get /v2/mail">client.mail.<a href="./src/inbound/resources/mail.py">list</a>(\*\*<a href="src/inbound/types/mail_list_params.py">params</a>) -> <a href="./src/inbound/types/mail_list_response.py">MailListResponse</a></code>
- <code title="post /v2/mail/bulk">client.mail.<a href="./src/inbound/resources/mail.py">bulk_update</a>(\*\*<a href="src/inbound/types/mail_bulk_update_params.py">params</a>) -> <a href="./src/inbound/types/mail_bulk_update_response.py">MailBulkUpdateResponse</a></code>
- <code title="get /v2/mail/{id}/thread">client.mail.<a href="./src/inbound/resources/mail.py">get_thread</a>(id) -> <a href="./src/inbound/types/mail_get_thread_response.py">MailGetThreadResponse</a></code>
- <code title="post /v2/mail/thread-counts">client.mail.<a href="./src/inbound/resources/mail.py">get_thread_counts</a>(\*\*<a href="src/inbound/types/mail_get_thread_counts_params.py">params</a>) -> <a href="./src/inbound/types/mail_get_thread_counts_response.py">MailGetThreadCountsResponse</a></code>
- <code title="post /v2/mail">client.mail.<a href="./src/inbound/resources/mail.py">reply</a>(\*\*<a href="src/inbound/types/mail_reply_params.py">params</a>) -> <a href="./src/inbound/types/mail_reply_response.py">MailReplyResponse</a></code>

# Onboarding

Types:

```python
from inbound.types import (
    OnboardingCheckReplyResponse,
    OnboardingHandleWebhookResponse,
    OnboardingSendDemoResponse,
)
```

Methods:

- <code title="get /v2/onboarding/check-reply">client.onboarding.<a href="./src/inbound/resources/onboarding.py">check_reply</a>() -> <a href="./src/inbound/types/onboarding_check_reply_response.py">OnboardingCheckReplyResponse</a></code>
- <code title="post /v2/onboarding/webhook">client.onboarding.<a href="./src/inbound/resources/onboarding.py">handle_webhook</a>() -> <a href="./src/inbound/types/onboarding_handle_webhook_response.py">OnboardingHandleWebhookResponse</a></code>
- <code title="post /v2/onboarding/demo">client.onboarding.<a href="./src/inbound/resources/onboarding.py">send_demo</a>(\*\*<a href="src/inbound/types/onboarding_send_demo_params.py">params</a>) -> <a href="./src/inbound/types/onboarding_send_demo_response.py">OnboardingSendDemoResponse</a></code>
