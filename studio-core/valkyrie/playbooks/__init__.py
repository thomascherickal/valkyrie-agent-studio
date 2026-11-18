"""The playbook of every agent: its data fields, the sections of its deliverable, and its formulas. One module per role."""

from valkyrie.playbooks import (
    role01, role02, role03, role04, role05, role06, role07, role08, role09, role10, role11, role12,
)

PLAYBOOKS: dict[str, dict[str, list]] = {}
for _role in (role01, role02, role03, role04, role05, role06, role07, role08, role09, role10, role11, role12):
    PLAYBOOKS.update(_role.PLAYBOOKS)
