# V2

## Emails

Types:

```python
from inboundemail.types.v2 import (
    AttachmentInput,
    EmailRetrieveResponse,
    EmailReplyResponse,
    EmailResendResponse,
    EmailRetryDeliveryResponse,
    EmailSendResponse,
)
```

Methods:

- <code title="get /api/v2/emails/{id}">client.v2.emails.<a href="./src/inboundemail/resources/v2/emails/emails.py">retrieve</a>(id) -> <a href="./src/inboundemail/types/v2/email_retrieve_response.py">EmailRetrieveResponse</a></code>
- <code title="post /api/v2/emails/{id}/reply">client.v2.emails.<a href="./src/inboundemail/resources/v2/emails/emails.py">reply</a>(id, \*\*<a href="src/inboundemail/types/v2/email_reply_params.py">params</a>) -> <a href="./src/inboundemail/types/v2/email_reply_response.py">EmailReplyResponse</a></code>
- <code title="post /api/v2/emails/{id}/resend">client.v2.emails.<a href="./src/inboundemail/resources/v2/emails/emails.py">resend</a>(id, \*\*<a href="src/inboundemail/types/v2/email_resend_params.py">params</a>) -> <a href="./src/inboundemail/types/v2/email_resend_response.py">EmailResendResponse</a></code>
- <code title="post /api/v2/emails/{id}/retry-delivery">client.v2.emails.<a href="./src/inboundemail/resources/v2/emails/emails.py">retry_delivery</a>(id, \*\*<a href="src/inboundemail/types/v2/email_retry_delivery_params.py">params</a>) -> <a href="./src/inboundemail/types/v2/email_retry_delivery_response.py">EmailRetryDeliveryResponse</a></code>
- <code title="post /api/v2/emails">client.v2.emails.<a href="./src/inboundemail/resources/v2/emails/emails.py">send</a>(\*\*<a href="src/inboundemail/types/v2/email_send_params.py">params</a>) -> <a href="./src/inboundemail/types/v2/email_send_response.py">EmailSendResponse</a></code>

### Schedule

Types:

```python
from inboundemail.types.v2.emails import (
    ScheduleCreateResponse,
    ScheduleRetrieveResponse,
    ScheduleListResponse,
    ScheduleCancelResponse,
)
```

Methods:

- <code title="post /api/v2/emails/schedule">client.v2.emails.schedule.<a href="./src/inboundemail/resources/v2/emails/schedule.py">create</a>(\*\*<a href="src/inboundemail/types/v2/emails/schedule_create_params.py">params</a>) -> <a href="./src/inboundemail/types/v2/emails/schedule_create_response.py">ScheduleCreateResponse</a></code>
- <code title="get /api/v2/emails/schedule/{id}">client.v2.emails.schedule.<a href="./src/inboundemail/resources/v2/emails/schedule.py">retrieve</a>(id) -> <a href="./src/inboundemail/types/v2/emails/schedule_retrieve_response.py">ScheduleRetrieveResponse</a></code>
- <code title="get /api/v2/emails/schedule">client.v2.emails.schedule.<a href="./src/inboundemail/resources/v2/emails/schedule.py">list</a>(\*\*<a href="src/inboundemail/types/v2/emails/schedule_list_params.py">params</a>) -> <a href="./src/inboundemail/types/v2/emails/schedule_list_response.py">ScheduleListResponse</a></code>
- <code title="delete /api/v2/emails/schedule/{id}">client.v2.emails.schedule.<a href="./src/inboundemail/resources/v2/emails/schedule.py">cancel</a>(id) -> <a href="./src/inboundemail/types/v2/emails/schedule_cancel_response.py">ScheduleCancelResponse</a></code>
