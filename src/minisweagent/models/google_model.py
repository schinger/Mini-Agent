import json
import logging
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from openai import OpenAI
from minisweagent.models import GLOBAL_MODEL_STATS

logger = logging.getLogger("google_model")


@dataclass
class GoogleModelConfig:
    model_name: str = "gemini-2.5-flash"
    model_kwargs: dict[str, Any] = field(default_factory=dict)


class GoogleModel:
    def __init__(self, **kwargs):
        self.config = GoogleModelConfig(**kwargs)
        self.cost = 0.0
        self.n_calls = 0
        self.client = OpenAI(api_key=self.config.model_kwargs.get("api_key", os.getenv("MSWEA_MODEL_API_KEY")),
                            base_url="https://generativelanguage.googleapis.com/v1beta/openai/")


    def query(self, messages: list[dict[str, str]], **kwargs) -> dict:
        response = self.client.chat.completions.create(
            model=self.config.model_name,
            messages=messages,
            **(self.config.model_kwargs | kwargs)
        )
        self.n_calls += 1
        self.cost += 1
        GLOBAL_MODEL_STATS.add(self.cost)
        return {
            "content": response.choices[0].message.content or "",  # type: ignore
        }
