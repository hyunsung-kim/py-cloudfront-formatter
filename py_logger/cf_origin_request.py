from typing import Optional

from .cf_origin import CfOrigin


class CfOriginRequest(CfOrigin):

    def parse(self, cf_event) -> Optional[dict]:
        common = self._parse_common(cf_event)
        cf_req = self._parse_request(cf_event)
        return dict(common, **cf_req)
