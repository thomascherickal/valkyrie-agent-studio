"""Per-agent facets and keywords that drive the generated Python implementations. One module per role."""

from valkyrie.profiles import (
    role01, role02, role03, role04, role05, role06, role07, role08, role09, role10, role11, role12,
)

PROFILES: dict[str, str] = {}
for _role in (role01, role02, role03, role04, role05, role06, role07, role08, role09, role10, role11, role12):
    PROFILES.update(_role.PROFILES)
