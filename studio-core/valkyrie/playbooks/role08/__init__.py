"""Playbooks for the Developer Relations & Docs agents."""

from valkyrie.playbooks.role08.core import PLAYBOOKS as _CORE
from valkyrie.playbooks.role08.extra import PLAYBOOKS as _EXTRA

PLAYBOOKS = {**_CORE, **_EXTRA}
