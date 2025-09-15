# Domains

Types:

```python
from inbound.types import (
    DomainCreateResponse,
    DomainRetrieveResponse,
    DomainListResponse,
    DomainDeleteResponse,
    DomainListDNSRecordsResponse,
)
```

Methods:

- <code title="post /api/v2/domains">client.domains.<a href="./src/inbound/resources/domains/domains.py">create</a>(\*\*<a href="src/inbound/types/domain_create_params.py">params</a>) -> <a href="./src/inbound/types/domain_create_response.py">DomainCreateResponse</a></code>
- <code title="get /api/v2/domains/{id}">client.domains.<a href="./src/inbound/resources/domains/domains.py">retrieve</a>(path_id, \*\*<a href="src/inbound/types/domain_retrieve_params.py">params</a>) -> <a href="./src/inbound/types/domain_retrieve_response.py">DomainRetrieveResponse</a></code>
- <code title="patch /api/v2/domains/{id}">client.domains.<a href="./src/inbound/resources/domains/domains.py">update</a>(id) -> object</code>
- <code title="get /api/v2/domains">client.domains.<a href="./src/inbound/resources/domains/domains.py">list</a>(\*\*<a href="src/inbound/types/domain_list_params.py">params</a>) -> <a href="./src/inbound/types/domain_list_response.py">DomainListResponse</a></code>
- <code title="delete /api/v2/domains/{id}">client.domains.<a href="./src/inbound/resources/domains/domains.py">delete</a>(id) -> <a href="./src/inbound/types/domain_delete_response.py">DomainDeleteResponse</a></code>
- <code title="get /api/v2/domains/{id}/dns-records">client.domains.<a href="./src/inbound/resources/domains/domains.py">list_dns_records</a>(id) -> <a href="./src/inbound/types/domain_list_dns_records_response.py">DomainListDNSRecordsResponse</a></code>

## Auth

Types:

```python
from inbound.types.domains import AuthCreateResponse, AuthUpdateResponse
```

Methods:

- <code title="post /api/v2/domains/{id}/auth">client.domains.auth.<a href="./src/inbound/resources/domains/auth.py">create</a>(id, \*\*<a href="src/inbound/types/domains/auth_create_params.py">params</a>) -> <a href="./src/inbound/types/domains/auth_create_response.py">AuthCreateResponse</a></code>
- <code title="patch /api/v2/domains/{id}/auth">client.domains.auth.<a href="./src/inbound/resources/domains/auth.py">update</a>(id) -> <a href="./src/inbound/types/domains/auth_update_response.py">AuthUpdateResponse</a></code>

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

- <code title="post /api/v2/email-addresses">client.email_addresses.<a href="./src/inbound/resources/email_addresses.py">create</a>(\*\*<a href="src/inbound/types/email_address_create_params.py">params</a>) -> <a href="./src/inbound/types/email_address_create_response.py">EmailAddressCreateResponse</a></code>
- <code title="get /api/v2/email-addresses/{id}">client.email_addresses.<a href="./src/inbound/resources/email_addresses.py">retrieve</a>(id) -> <a href="./src/inbound/types/email_address_retrieve_response.py">EmailAddressRetrieveResponse</a></code>
- <code title="put /api/v2/email-addresses/{id}">client.email_addresses.<a href="./src/inbound/resources/email_addresses.py">update</a>(id, \*\*<a href="src/inbound/types/email_address_update_params.py">params</a>) -> <a href="./src/inbound/types/email_address_update_response.py">EmailAddressUpdateResponse</a></code>
- <code title="get /api/v2/email-addresses">client.email_addresses.<a href="./src/inbound/resources/email_addresses.py">list</a>(\*\*<a href="src/inbound/types/email_address_list_params.py">params</a>) -> <a href="./src/inbound/types/email_address_list_response.py">EmailAddressListResponse</a></code>
- <code title="delete /api/v2/email-addresses/{id}">client.email_addresses.<a href="./src/inbound/resources/email_addresses.py">delete</a>(id) -> <a href="./src/inbound/types/email_address_delete_response.py">EmailAddressDeleteResponse</a></code>

# Emails

Types:

```python
from inbound.types import EmailCreateResponse, EmailRetrieveResponse, EmailReplyResponse
```

Methods:

- <code title="post /api/v2/emails">client.emails.<a href="./src/inbound/resources/emails/emails.py">create</a>(\*\*<a href="src/inbound/types/email_create_params.py">params</a>) -> <a href="./src/inbound/types/email_create_response.py">EmailCreateResponse</a></code>
- <code title="get /api/v2/emails/{id}">client.emails.<a href="./src/inbound/resources/emails/emails.py">retrieve</a>(id) -> <a href="./src/inbound/types/email_retrieve_response.py">EmailRetrieveResponse</a></code>
- <code title="post /api/v2/emails/{id}/reply">client.emails.<a href="./src/inbound/resources/emails/emails.py">reply</a>(id, \*\*<a href="src/inbound/types/email_reply_params.py">params</a>) -> <a href="./src/inbound/types/email_reply_response.py">EmailReplyResponse</a></code>

## Schedule

Types:

```python
from inbound.types.emails import (
    ScheduleCreateResponse,
    ScheduleRetrieveResponse,
    ScheduleListResponse,
    ScheduleDeleteResponse,
)
```

Methods:

- <code title="post /api/v2/emails/schedule">client.emails.schedule.<a href="./src/inbound/resources/emails/schedule.py">create</a>(\*\*<a href="src/inbound/types/emails/schedule_create_params.py">params</a>) -> <a href="./src/inbound/types/emails/schedule_create_response.py">ScheduleCreateResponse</a></code>
- <code title="get /api/v2/emails/schedule/{id}">client.emails.schedule.<a href="./src/inbound/resources/emails/schedule.py">retrieve</a>(id) -> <a href="./src/inbound/types/emails/schedule_retrieve_response.py">ScheduleRetrieveResponse</a></code>
- <code title="get /api/v2/emails/schedule">client.emails.schedule.<a href="./src/inbound/resources/emails/schedule.py">list</a>(\*\*<a href="src/inbound/types/emails/schedule_list_params.py">params</a>) -> <a href="./src/inbound/types/emails/schedule_list_response.py">ScheduleListResponse</a></code>
- <code title="delete /api/v2/emails/schedule/{id}">client.emails.schedule.<a href="./src/inbound/resources/emails/schedule.py">delete</a>(id) -> <a href="./src/inbound/types/emails/schedule_delete_response.py">ScheduleDeleteResponse</a></code>

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

- <code title="post /api/v2/endpoints">client.endpoints.<a href="./src/inbound/resources/endpoints.py">create</a>(\*\*<a href="src/inbound/types/endpoint_create_params.py">params</a>) -> <a href="./src/inbound/types/endpoint_create_response.py">EndpointCreateResponse</a></code>
- <code title="get /api/v2/endpoints/{id}">client.endpoints.<a href="./src/inbound/resources/endpoints.py">retrieve</a>(path_id, \*\*<a href="src/inbound/types/endpoint_retrieve_params.py">params</a>) -> <a href="./src/inbound/types/endpoint_retrieve_response.py">EndpointRetrieveResponse</a></code>
- <code title="put /api/v2/endpoints/{id}">client.endpoints.<a href="./src/inbound/resources/endpoints.py">update</a>(path_id, \*\*<a href="src/inbound/types/endpoint_update_params.py">params</a>) -> <a href="./src/inbound/types/endpoint_update_response.py">EndpointUpdateResponse</a></code>
- <code title="get /api/v2/endpoints">client.endpoints.<a href="./src/inbound/resources/endpoints.py">list</a>(\*\*<a href="src/inbound/types/endpoint_list_params.py">params</a>) -> <a href="./src/inbound/types/endpoint_list_response.py">EndpointListResponse</a></code>
- <code title="delete /api/v2/endpoints/{id}">client.endpoints.<a href="./src/inbound/resources/endpoints.py">delete</a>(id) -> <a href="./src/inbound/types/endpoint_delete_response.py">EndpointDeleteResponse</a></code>
- <code title="post /api/v2/endpoints/{id}/test">client.endpoints.<a href="./src/inbound/resources/endpoints.py">test</a>(path_id, \*\*<a href="src/inbound/types/endpoint_test_params.py">params</a>) -> <a href="./src/inbound/types/endpoint_test_response.py">EndpointTestResponse</a></code>

# Mail

Types:

```python
from inbound.types import (
    MailCreateResponse,
    MailRetrieveResponse,
    MailUpdateResponse,
    MailListResponse,
    MailBulkCreateResponse,
    MailRetrieveThreadResponse,
)
```

Methods:

- <code title="post /api/v2/mail">client.mail.<a href="./src/inbound/resources/mail.py">create</a>(\*\*<a href="src/inbound/types/mail_create_params.py">params</a>) -> <a href="./src/inbound/types/mail_create_response.py">MailCreateResponse</a></code>
- <code title="get /api/v2/mail/{id}">client.mail.<a href="./src/inbound/resources/mail.py">retrieve</a>(id) -> <a href="./src/inbound/types/mail_retrieve_response.py">MailRetrieveResponse</a></code>
- <code title="patch /api/v2/mail/{id}">client.mail.<a href="./src/inbound/resources/mail.py">update</a>(id, \*\*<a href="src/inbound/types/mail_update_params.py">params</a>) -> <a href="./src/inbound/types/mail_update_response.py">MailUpdateResponse</a></code>
- <code title="get /api/v2/mail">client.mail.<a href="./src/inbound/resources/mail.py">list</a>(\*\*<a href="src/inbound/types/mail_list_params.py">params</a>) -> <a href="./src/inbound/types/mail_list_response.py">MailListResponse</a></code>
- <code title="post /api/v2/mail/bulk">client.mail.<a href="./src/inbound/resources/mail.py">bulk_create</a>(\*\*<a href="src/inbound/types/mail_bulk_create_params.py">params</a>) -> <a href="./src/inbound/types/mail_bulk_create_response.py">MailBulkCreateResponse</a></code>
- <code title="get /api/v2/mail/{id}/thread">client.mail.<a href="./src/inbound/resources/mail.py">retrieve_thread</a>(id) -> <a href="./src/inbound/types/mail_retrieve_thread_response.py">MailRetrieveThreadResponse</a></code>
- <code title="post /api/v2/mail/thread-counts">client.mail.<a href="./src/inbound/resources/mail.py">thread_counts</a>() -> object</code>
