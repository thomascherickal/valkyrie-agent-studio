"""Playbooks for the Engineering & Product Management agents."""

from valkyrie.playbooks.role11.core import PLAYBOOKS as _CORE
from valkyrie.playbooks.role11.extra import PLAYBOOKS as _EXTRA

PLAYBOOKS = {**_CORE, **_EXTRA}
