"""Playbooks for the C-Suite & Executives (CxOs) agents."""

from valkyrie.playbooks.role12.core import PLAYBOOKS as _CORE
from valkyrie.playbooks.role12.extra import PLAYBOOKS as _EXTRA

PLAYBOOKS = {**_CORE, **_EXTRA}
