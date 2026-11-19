"""Playbooks for the Growth & Product Analytics agents."""

from valkyrie.playbooks.role09.core import PLAYBOOKS as _CORE
from valkyrie.playbooks.role09.extra import PLAYBOOKS as _EXTRA

PLAYBOOKS = {**_CORE, **_EXTRA}
