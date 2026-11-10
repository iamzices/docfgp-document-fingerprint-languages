"""Check pinned model metadata, packaged model bytes, and verified downloads."""

import hashlib
import json
from pathlib import Path

import pytest

from docfgp_languages import REVISION, TESSDATA
from scripts.fetch_models import _digest, _fetch

MODELS = json.loads((TESSDATA / "models.json").read_text(encoding="utf-8"))["models"]


def test_manifest_pins_english_and_every_non_latin_language() -> None:
    """Pin English and every language written in another script to one upstream revision."""
    assert len(REVISION) == 40
    assert next(iter(MODELS)) == "eng"
    assert len(MODELS) == 61
    assert {"ara", "chi_sim", "hin", "jpn", "kor", "rus", "tha"} <= MODELS.keys()
    assert not {"deu", "fra", "spa"} & MODELS.keys()
    assert all(len(model["sha256"]) == 64 and model["bytes"] > 0 for model in MODELS.values())


def test_packaged_models_match_their_pinned_digests() -> None:
    """Ship exactly the model bytes that the manifest pins."""
    for name, model in MODELS.items():
        path = TESSDATA / f"{name}.traineddata"
        assert path.stat().st_size == model["bytes"]
        assert _digest(path) == model["sha256"]


def test_downloads_are_kept_only_when_their_digest_matches(tmp_path: Path) -> None:
    """Publish a verified download and discard one that does not match."""
    source = tmp_path / "source.traineddata"
    source.write_bytes(b"model")
    target = tmp_path / "tessdata" / "test.traineddata"
    with pytest.raises(SystemExit, match="SHA-256"):
        _fetch(source.as_uri(), target, "0" * 64)
    assert list(target.parent.iterdir()) == []
    _fetch(source.as_uri(), target, hashlib.sha256(b"model").hexdigest())
    assert target.read_bytes() == b"model"
    assert target.stat().st_mode & 0o777 == 0o644
