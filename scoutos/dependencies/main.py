from types import SimpleNamespace

from .bool import BoolDependency
from .float import FloatDependency
from .int import IntDependency
from .str import StrDependency

Depends = SimpleNamespace(
    BoolType=BoolDependency,
    FloatType=FloatDependency,
    IntType=IntDependency,
    StrType=StrDependency,
)
