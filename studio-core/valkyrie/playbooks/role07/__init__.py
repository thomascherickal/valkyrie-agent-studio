"""Playbooks for the Technical Support agents."""

from valkyrie.playbooks.role07.core import PLAYBOOKS as _CORE
from valkyrie.playbooks.role07.extra import PLAYBOOKS as _EXTRA

PLAYBOOKS = {**_CORE, **_EXTRA}
