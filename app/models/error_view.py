from typing import Optional
from dataclasses import dataclass

@dataclass
class ErrorViewModel:
    request_id: Optional[str] = None

    @property
    def show_request_id(self) -> bool:
        return bool(self.request_id)
