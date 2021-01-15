import os
from typing import Union, List, Set, Dict, Iterable


class TransducerFile:
    def __init__(self, path: Union[str, os.PathLike[str]]) -> None: ...
    def lookup(self, string: str) -> List[str]: ...
    def bulk_lookup(self, strings: Iterable[str]) -> Dict[str, Set[str]]: ...
    def symbol_count(self) -> int: ...