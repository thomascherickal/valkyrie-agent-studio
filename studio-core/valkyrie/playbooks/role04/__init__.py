"""Playbooks for the QA & Test Automation agents."""

from valkyrie.playbooks.role04.core import PLAYBOOKS as _CORE
from valkyrie.playbooks.role04.extra import PLAYBOOKS as _EXTRA

PLAYBOOKS = {**_CORE, **_EXTRA}
