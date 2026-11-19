"""Playbooks for the FinOps & Cloud Cost agents."""

from valkyrie.playbooks.role10.core import PLAYBOOKS as _CORE
from valkyrie.playbooks.role10.extra import PLAYBOOKS as _EXTRA

PLAYBOOKS = {**_CORE, **_EXTRA}
