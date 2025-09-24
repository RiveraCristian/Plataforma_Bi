import json
from typing import Any, Optional

import redis

from app.core.config import get_settings

settings = get_settings()

_redis_client: Optional[redis.Redis] = None


def get_redis() -> redis.Redis:
    global _redis_client
    if _redis_client is None:
        _redis_client = redis.Redis.from_url(settings.redis_url)
    return _redis_client


def cache_result(key: str, value: Any, ttl: int = 300) -> None:
    client = get_redis()
    client.setex(name=key, time=ttl, value=json.dumps(value))


def get_cached_result(key: str) -> Any | None:
    client = get_redis()
    cached = client.get(key)
    if cached is None:
        return None
    return json.loads(cached)
