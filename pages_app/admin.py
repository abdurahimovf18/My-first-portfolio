from django.contrib import admin
from typing import Any


def register_models(*, globals_: dict[str, Any]):
    [admin.site.register(val) for key, val in globals_.items() if key.lower().endswith('model')]
