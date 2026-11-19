"""Playbooks for the Software Engineering agents."""

from valkyrie.playbooks.role02.core import PLAYBOOKS as _CORE
from valkyrie.playbooks.role02.extra import PLAYBOOKS as _EXTRA

PLAYBOOKS = {**_CORE, **_EXTRA}
