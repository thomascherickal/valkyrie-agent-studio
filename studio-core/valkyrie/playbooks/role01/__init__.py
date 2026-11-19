"""Playbooks for the Product Management agents."""

from valkyrie.playbooks.role01.core import PLAYBOOKS as _CORE
from valkyrie.playbooks.role01.extra import PLAYBOOKS as _EXTRA

PLAYBOOKS = {**_CORE, **_EXTRA}
