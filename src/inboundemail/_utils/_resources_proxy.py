from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `inboundemail.resources` module.

    This is used so that we can lazily import `inboundemail.resources` only when
    needed *and* so that users can just import `inboundemail` and reference `inboundemail.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("inboundemail.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
