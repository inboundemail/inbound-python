# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EmailRetrieveResponse"]


class EmailRetrieveResponse(BaseModel):
    id: str
    """Unique email identifier in nanoid format"""

    created_at: datetime
    """ISO 8601 timestamp when email was created"""

    from_: str = FieldInfo(alias="from")
    """Sender email address (may include display name)"""

    last_event: Literal["created", "pending", "delivered", "failed"]
    """Last delivery event status"""

    object: Literal["email"]
    """Object type identifier (always "email")"""

    subject: str
    """Email subject line"""

    to: List[str]
    """Recipient email addresses"""

    bcc: Optional[List[Optional[str]]] = None
    """Blind carbon copy recipients (contains null if none)"""

    cc: Optional[List[Optional[str]]] = None
    """Carbon copy recipients (contains null if none)"""

    html: Optional[str] = None
    """HTML email body content"""

    reply_to: Optional[List[Optional[str]]] = None
    """Reply-To addresses (contains null if none)"""

    text: Optional[str] = None
    """Plain text email body content"""
