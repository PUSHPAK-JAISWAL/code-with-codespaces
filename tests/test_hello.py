from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hello import build_greeting


def test_build_greeting_uses_name_and_activity():
    assert build_greeting("Ava", "building") == (
        "Hello, Ava! Ready for some building today? "
        "This repo just got a little more interactive."
    )
