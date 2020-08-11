from typing import Optional

from .cf_origin import CfOrigin


class CfOriginNull(CfOrigin):
    def parse(self, cf_event) -> Optional[dict]:
        return cf_event
