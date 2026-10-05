"""Path bootstrap for the lightweight notebooks in submission/notebooks/.
"""
from __future__ import annotations

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_DOCKER = Path("/workspace/scripts")
_LOCAL = _HERE.parent.parent / "scripts"

_TARGET = _DOCKER if _DOCKER.exists() else _LOCAL
sys.path.insert(0, str(_TARGET))
