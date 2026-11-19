"""Playbooks for the Data Engineering agents."""

from valkyrie.playbooks.role05.core import PLAYBOOKS as _CORE
from valkyrie.playbooks.role05.extra import PLAYBOOKS as _EXTRA

PLAYBOOKS = {**_CORE, **_EXTRA}
