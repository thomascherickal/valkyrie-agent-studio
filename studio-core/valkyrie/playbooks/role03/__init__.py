"""Playbooks for the DevOps & SRE agents."""

from valkyrie.playbooks.role03.core import PLAYBOOKS as _CORE
from valkyrie.playbooks.role03.extra import PLAYBOOKS as _EXTRA

PLAYBOOKS = {**_CORE, **_EXTRA}
