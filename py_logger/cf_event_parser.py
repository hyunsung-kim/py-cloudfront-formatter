from addict import Dict

from .cf_origin import CfOrigin
from .cf_origin_null import CfOriginNull
from .cf_origin_request import CfOriginRequest
from .cf_origin_response import CfOriginResponse


class CfEventParser():
    PARSER_MAPPER = {
        'origin-null': CfOriginNull(),
        'origin-request': CfOriginRequest(),
        'origin-response': CfOriginResponse(),
    }

    @staticmethod
    def loads(cf_event: dict) -> CfOrigin:
        try:
            event_type = cf_event['Records'][0]['cf']['config']['eventType'] or 'origin-null'
            mapper = CfEventParser.PARSER_MAPPER.get(event_type, None)
            if mapper:
                return mapper.parse(cf_event)
        except KeyError as e:
            raise LookupError from e
