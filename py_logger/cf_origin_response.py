from typing import Optional

from .cf_origin import CfOrigin


class CfOriginResponse(CfOrigin):
    def parse(self, cf_event) -> Optional[dict]:
        common = self._parse_common(cf_event)
        cf_req = self._parse_request(cf_event)
        return dict(common, **cf_req, **self._parse_response(cf_event))

    def _parse_response(self, cf_event):
        extra_dict = Dict(cf_event)
        cf_res = extra_dict.Records[0].cf.response
        return {
            'status': cf_res.status,
            'content_length': cf_res.headers.get('content-length', [])[0].get('value',''),
            'status_description': cf_res.get('statusDescription', '')
        }
