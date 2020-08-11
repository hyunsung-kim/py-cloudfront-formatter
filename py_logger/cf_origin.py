import abc
from typing import Optional

from addict import Dict


class CfOrigin(metaclass=abc.ABCMeta):
    def _parse_common(self, cf_event):
        extra_dict = Dict(cf_event)
        cf = extra_dict.Records[0].cf
        return {
            "level": extra_dict.level,
            "timestamp": extra_dict.asctime,
            "event_type": cf.config.eventType,
            "request_id": cf.config.requestId,
            "message": extra_dict.message
        }


    def _parse_request(self, cf_event):
        extra_dict = Dict(cf_event)
        cf_req = extra_dict.Records[0].cf.request
        return {
            "client_ip": cf_req.clientIp,
            "x_forwarded_for": cf_req.headers['x-forwarded-for'][0].get('value', ''),
            "authorization": cf_req.headers['authorization'][0].get('value', ''),
            "user_agent": cf_req.headers['user-agent'][0].get('value', ''),
            "host": cf_req.headers['host'][0].get('value', ''),
            "method": cf_req.method,
            "domain_name": cf_req.origin.custom.get('domainName', ''),
            "protocol": cf_req.origin.custom.protocol,
            "path": cf_req.origin.custom.get('path', ''),
            "querystring": cf_req.get('querystring',''),
            "uri": cf_req.uri
        }


    @abc.abstractmethod
    def parse(self, cf_event) -> Optional[dict]:
        pass

