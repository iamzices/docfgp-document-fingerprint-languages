"""Provide pinned Tesseract language models for DocFGP OCR."""

import json
from pathlib import Path

TESSDATA = Path(__file__).with_name("tessdata")
REVISION = json.loads((TESSDATA / "models.json").read_text(encoding="utf-8"))["revision"]

__all__ = ["REVISION", "TESSDATA"]
