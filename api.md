# V2

## Domains

Types:

```python
from inbound.types.v2 import (
    DomainCreateResponse,
    DomainRetrieveResponse,
    DomainListResponse,
    DomainDeleteResponse,
    DomainListDNSRecordsResponse,
)
```

Methods:

- <code title="post /api/v2/domains">client.v2.domains.<a href="./src/inbound/resources/v2/domains/domains.py">create</a>(\*\*<a href="src/inbound/types/v2/domain_create_params.py">params</a>) -> <a href="./src/inbound/types/v2/domain_create_response.py">DomainCreateResponse</a></code>
- <code title="get /api/v2/domains/{id}">client.v2.domains.<a href="./src/inbound/resources/v2/domains/domains.py">retrieve</a>(path_id, \*\*<a href="src/inbound/types/v2/domain_retrieve_params.py">params</a>) -> <a href="./src/inbound/types/v2/domain_retrieve_response.py">DomainRetrieveResponse</a></code>
- <code title="patch /api/v2/domains/{id}">client.v2.domains.<a href="./src/inbound/resources/v2/domains/domains.py">update</a>(id) -> object</code>
- <code title="get /api/v2/domains">client.v2.domains.<a href="./src/inbound/resources/v2/domains/domains.py">list</a>(\*\*<a href="src/inbound/types/v2/domain_list_params.py">params</a>) -> <a href="./src/inbound/types/v2/domain_list_response.py">DomainListResponse</a></code>
- <code title="delete /api/v2/domains/{id}">client.v2.domains.<a href="./src/inbound/resources/v2/domains/domains.py">delete</a>(id) -> <a href="./src/inbound/types/v2/domain_delete_response.py">DomainDeleteResponse</a></code>
- <code title="get /api/v2/domains/{id}/dns-records">client.v2.domains.<a href="./src/inbound/resources/v2/domains/domains.py">list_dns_records</a>(id) -> <a href="./src/inbound/types/v2/domain_list_dns_records_response.py">DomainListDNSRecordsResponse</a></code>

### Auth

Types:

```python
from inbound.types.v2.domains import AuthCreateResponse, AuthUpdateResponse
```

Methods:

- <code title="post /api/v2/domains/{id}/auth">client.v2.domains.auth.<a href="./src/inbound/resources/v2/domains/auth.py">create</a>(id, \*\*<a href="src/inbound/types/v2/domains/auth_create_params.py">params</a>) -> <a href="./src/inbound/types/v2/domains/auth_create_response.py">AuthCreateResponse</a></code>
- <code title="patch /api/v2/domains/{id}/auth">client.v2.domains.auth.<a href="./src/inbound/resources/v2/domains/auth.py">update</a>(id) -> <a href="./src/inbound/types/v2/domains/auth_update_response.py">AuthUpdateResponse</a></code>

## EmailAddresses

Types:

```python
from inbound.types.v2 import (
    EmailAddressCreateResponse,
    EmailAddressRetrieveResponse,
    EmailAddressUpdateResponse,
    EmailAddressListResponse,
    EmailAddressDeleteResponse,
)
```

Methods:

- <code title="post /api/v2/email-addresses">client.v2.email_addresses.<a href="./src/inbound/resources/v2/email_addresses.py">create</a>(\*\*<a href="src/inbound/types/v2/email_address_create_params.py">params</a>) -> <a href="./src/inbound/types/v2/email_address_create_response.py">EmailAddressCreateResponse</a></code>
- <code title="get /api/v2/email-addresses/{id}">client.v2.email_addresses.<a href="./src/inbound/resources/v2/email_addresses.py">retrieve</a>(id) -> <a href="./src/inbound/types/v2/email_address_retrieve_response.py">EmailAddressRetrieveResponse</a></code>
- <code title="put /api/v2/email-addresses/{id}">client.v2.email_addresses.<a href="./src/inbound/resources/v2/email_addresses.py">update</a>(id, \*\*<a href="src/inbound/types/v2/email_address_update_params.py">params</a>) -> <a href="./src/inbound/types/v2/email_address_update_response.py">EmailAddressUpdateResponse</a></code>
- <code title="get /api/v2/email-addresses">client.v2.email_addresses.<a href="./src/inbound/resources/v2/email_addresses.py">list</a>(\*\*<a href="src/inbound/types/v2/email_address_list_params.py">params</a>) -> <a href="./src/inbound/types/v2/email_address_list_response.py">EmailAddressListResponse</a></code>
- <code title="delete /api/v2/email-addresses/{id}">client.v2.email_addresses.<a href="./src/inbound/resources/v2/email_addresses.py">delete</a>(id) -> <a href="./src/inbound/types/v2/email_address_delete_response.py">EmailAddressDeleteResponse</a></code>

## Emails

Types:

```python
from inbound.types.v2 import EmailCreateResponse, EmailRetrieveResponse, EmailReplyResponse
```

Methods:

- <code title="post /api/v2/emails">client.v2.emails.<a href="./src/inbound/resources/v2/emails/emails.py">create</a>(\*\*<a href="src/inbound/types/v2/email_create_params.py">params</a>) -> <a href="./src/inbound/types/v2/email_create_response.py">EmailCreateResponse</a></code>
- <code title="get /api/v2/emails/{id}">client.v2.emails.<a href="./src/inbound/resources/v2/emails/emails.py">retrieve</a>(id) -> <a href="./src/inbound/types/v2/email_retrieve_response.py">EmailRetrieveResponse</a></code>
- <code title="post /api/v2/emails/{id}/reply">client.v2.emails.<a href="./src/inbound/resources/v2/emails/emails.py">reply</a>(id, \*\*<a href="src/inbound/types/v2/email_reply_params.py">params</a>) -> <a href="./src/inbound/types/v2/email_reply_response.py">EmailReplyResponse</a></code>

### Schedule

Types:

```python
from inbound.types.v2.emails import (
    ScheduleCreateResponse,
    ScheduleRetrieveResponse,
    ScheduleListResponse,
    ScheduleDeleteResponse,
)
```

Methods:

- <code title="post /api/v2/emails/schedule">client.v2.emails.schedule.<a href="./src/inbound/resources/v2/emails/schedule.py">create</a>(\*\*<a href="src/inbound/types/v2/emails/schedule_create_params.py">params</a>) -> <a href="./src/inbound/types/v2/emails/schedule_create_response.py">ScheduleCreateResponse</a></code>
- <code title="get /api/v2/emails/schedule/{id}">client.v2.emails.schedule.<a href="./src/inbound/resources/v2/emails/schedule.py">retrieve</a>(id) -> <a href="./src/inbound/types/v2/emails/schedule_retrieve_response.py">ScheduleRetrieveResponse</a></code>
- <code title="get /api/v2/emails/schedule">client.v2.emails.schedule.<a href="./src/inbound/resources/v2/emails/schedule.py">list</a>(\*\*<a href="src/inbound/types/v2/emails/schedule_list_params.py">params</a>) -> <a href="./src/inbound/types/v2/emails/schedule_list_response.py">ScheduleListResponse</a></code>
- <code title="delete /api/v2/emails/schedule/{id}">client.v2.emails.schedule.<a href="./src/inbound/resources/v2/emails/schedule.py">delete</a>(id) -> <a href="./src/inbound/types/v2/emails/schedule_delete_response.py">ScheduleDeleteResponse</a></code>

## Endpoints

Types:

```python
from inbound.types.v2 import (
    EndpointCreateResponse,
    EndpointRetrieveResponse,
    EndpointUpdateResponse,
    EndpointListResponse,
    EndpointDeleteResponse,
    EndpointTestResponse,
)
```

Methods:

- <code title="post /api/v2/endpoints">client.v2.endpoints.<a href="./src/inbound/resources/v2/endpoints.py">create</a>(\*\*<a href="src/inbound/types/v2/endpoint_create_params.py">params</a>) -> <a href="./src/inbound/types/v2/endpoint_create_response.py">EndpointCreateResponse</a></code>
- <code title="get /api/v2/endpoints/{id}">client.v2.endpoints.<a href="./src/inbound/resources/v2/endpoints.py">retrieve</a>(path_id, \*\*<a href="src/inbound/types/v2/endpoint_retrieve_params.py">params</a>) -> <a href="./src/inbound/types/v2/endpoint_retrieve_response.py">EndpointRetrieveResponse</a></code>
- <code title="put /api/v2/endpoints/{id}">client.v2.endpoints.<a href="./src/inbound/resources/v2/endpoints.py">update</a>(path_id, \*\*<a href="src/inbound/types/v2/endpoint_update_params.py">params</a>) -> <a href="./src/inbound/types/v2/endpoint_update_response.py">EndpointUpdateResponse</a></code>
- <code title="get /api/v2/endpoints">client.v2.endpoints.<a href="./src/inbound/resources/v2/endpoints.py">list</a>(\*\*<a href="src/inbound/types/v2/endpoint_list_params.py">params</a>) -> <a href="./src/inbound/types/v2/endpoint_list_response.py">EndpointListResponse</a></code>
- <code title="delete /api/v2/endpoints/{id}">client.v2.endpoints.<a href="./src/inbound/resources/v2/endpoints.py">delete</a>(id) -> <a href="./src/inbound/types/v2/endpoint_delete_response.py">EndpointDeleteResponse</a></code>
- <code title="post /api/v2/endpoints/{id}/test">client.v2.endpoints.<a href="./src/inbound/resources/v2/endpoints.py">test</a>(path_id, \*\*<a href="src/inbound/types/v2/endpoint_test_params.py">params</a>) -> <a href="./src/inbound/types/v2/endpoint_test_response.py">EndpointTestResponse</a></code>

## Mail

Types:

```python
from inbound.types.v2 import (
    MailCreateResponse,
    MailRetrieveResponse,
    MailUpdateResponse,
    MailListResponse,
    MailBulkCreateResponse,
    MailRetrieveThreadResponse,
)
```

Methods:

- <code title="post /api/v2/mail">client.v2.mail.<a href="./src/inbound/resources/v2/mail.py">create</a>(\*\*<a href="src/inbound/types/v2/mail_create_params.py">params</a>) -> <a href="./src/inbound/types/v2/mail_create_response.py">MailCreateResponse</a></code>
- <code title="get /api/v2/mail/{id}">client.v2.mail.<a href="./src/inbound/resources/v2/mail.py">retrieve</a>(id) -> <a href="./src/inbound/types/v2/mail_retrieve_response.py">MailRetrieveResponse</a></code>
- <code title="patch /api/v2/mail/{id}">client.v2.mail.<a href="./src/inbound/resources/v2/mail.py">update</a>(id, \*\*<a href="src/inbound/types/v2/mail_update_params.py">params</a>) -> <a href="./src/inbound/types/v2/mail_update_response.py">MailUpdateResponse</a></code>
- <code title="get /api/v2/mail">client.v2.mail.<a href="./src/inbound/resources/v2/mail.py">list</a>(\*\*<a href="src/inbound/types/v2/mail_list_params.py">params</a>) -> <a href="./src/inbound/types/v2/mail_list_response.py">MailListResponse</a></code>
- <code title="post /api/v2/mail/bulk">client.v2.mail.<a href="./src/inbound/resources/v2/mail.py">bulk_create</a>(\*\*<a href="src/inbound/types/v2/mail_bulk_create_params.py">params</a>) -> <a href="./src/inbound/types/v2/mail_bulk_create_response.py">MailBulkCreateResponse</a></code>
- <code title="get /api/v2/mail/{id}/thread">client.v2.mail.<a href="./src/inbound/resources/v2/mail.py">retrieve_thread</a>(id) -> <a href="./src/inbound/types/v2/mail_retrieve_thread_response.py">MailRetrieveThreadResponse</a></code>
- <code title="post /api/v2/mail/thread-counts">client.v2.mail.<a href="./src/inbound/resources/v2/mail.py">thread_counts</a>() -> object</code>

## Onboarding

Methods:

- <code title="get /api/v2/onboarding/check-reply">client.v2.onboarding.<a href="./src/inbound/resources/v2/onboarding.py">check_reply</a>() -> object</code>
- <code title="post /api/v2/onboarding/demo">client.v2.onboarding.<a href="./src/inbound/resources/v2/onboarding.py">demo</a>() -> object</code>
- <code title="post /api/v2/onboarding/webhook">client.v2.onboarding.<a href="./src/inbound/resources/v2/onboarding.py">webhook</a>() -> object</code>
