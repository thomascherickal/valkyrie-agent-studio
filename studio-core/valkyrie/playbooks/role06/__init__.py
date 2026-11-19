"""Playbooks for the Security & AppSec agents."""

from valkyrie.playbooks.role06.core import PLAYBOOKS as _CORE
from valkyrie.playbooks.role06.extra import PLAYBOOKS as _EXTRA

PLAYBOOKS = {**_CORE, **_EXTRA}
