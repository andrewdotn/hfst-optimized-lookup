# typings for cython module _hfst_optimized_lookup.pyx
import os
from typing import Union, List, Set, Dict, Iterable

from ._types import Analysis

class PyTransducerFile:
    def __init__(self, path: Union[str, os.PathLike[str]]) -> None: ...
    def lookup(self, string: str) -> List[str]: ...
    def lookup_symbols(self, string: str) -> List[List[str]]: ...
    def lookup_lemma_with_affixes(self, string: str) -> List[Analysis]: ...
    def bulk_lookup(self, strings: Iterable[str]) -> Dict[str, Set[str]]: ...
    def symbol_count(self) -> int: ...
