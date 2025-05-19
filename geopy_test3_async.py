from geopy.adapters import BaseAsyncAdapter, _normalize_proxies
import json

try:
    import httpx

    httpx_available = True
except ImportError:
    httpx_available = False


class AsyncHttpxAdapter(BaseAsyncAdapter):
    is_available = httpx_available

    def __init__(self, *, proxies, ssl_context):
        if not httpx_available:
            raise ImportError(
                "`httpx` must be installed in order to use AsyncHttpxAdapter. "
                "If you have installed geopy via pip, you may use "
                "this command to install httpx: "
                "`pip install httpx`."
            )
        proxies = _normalize_proxies(proxies)
        super().__init__(proxies=proxies, ssl_context=ssl_context)

        self.proxies = proxies
        self.ssl_context = ssl_context

    @property
    def session(self):
        # Lazy session creation, which allows to avoid "unclosed socket"
        # warnings if a Geocoder instance is created without entering
        # async context and making any requests.
        session = self.__dict__.get("session")
        if session is None:
            session = httpx.AsyncClient(
                trust_env=False,  # don't use system proxies
            )
            self.__dict__["session"] = session
        return session

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.aclose()

    async def get_text(self, url, *, timeout, headers):
        response = await self.session.get(
            url, timeout=httpx.Timeout(timeout), headers=headers
        )
        return response.text

    async def get_json(self, *args, **kwargs):
        return json.loads(await self.get_text(*args, **kwargs))
