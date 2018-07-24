""" This file is licensed under GPLv3, see https://www.gnu.org/licenses/ """

from typing import TYPE_CHECKING, List, Optional

from .core import DataType

if TYPE_CHECKING:
    # pylint: disable=unused-import
    from .build import PackageBuild  # noqa
    from .version import VersionMatcher  # noqa
    from .core import InteractiveSpawn  # noqa


class PackagesNotFound(Exception):
    packages: List[str]
    wanted_by: Optional[List[str]]

    def __init__(self, packages: List[str], wanted_by: Optional[List[str]] = None) -> None:
        message = ', '.join(packages)
        if wanted_by:
            message += f" wanted by {', '.join(wanted_by)}"
        super().__init__(message)


class PackagesNotFoundInRepo(PackagesNotFound):
    pass


class PackagesNotFoundInAUR(PackagesNotFound):
    pass


class BuildError(Exception):
    pass


class CloneError(DataType, Exception):
    build: 'PackageBuild'
    result: 'InteractiveSpawn'


class DependencyError(Exception):
    pass


class DependencyVersionMismatch(DataType, Exception):
    version_found: str
    dependency_line: str
    who_depends: str
    depends_on: str
    location: str

    version_matcher: Optional['VersionMatcher'] = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.version_matcher:
            self.dependency_line = self.version_matcher.line


class DependencyNotBuiltYet(Exception):
    pass


class AURError(Exception):
    pass


class SysExit(Exception):
    code: int

    def __init__(self, code: int) -> None:
        self.code = code
        super().__init__(f"Exit code: {code}")
