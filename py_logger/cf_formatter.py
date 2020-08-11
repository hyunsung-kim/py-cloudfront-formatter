import logging
import pytz
from datetime import datetime

import json_log_formatter


from .cf_event_parser import CfEventParser


class CloudfrontJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message: str, extra: dict, record: logging.LogRecord) -> dict:
        extra['message'] = message
        extra['level'] = record.levelname

        if 'asctime' not in extra:
            extra['asctime'] = datetime.now(tz=pytz.utc).isoformat()

        cf_extra = self._parse(extra)
        if cf_extra:
            return cf_extra

        return extra


    def _parse(self, cf_event):
        return CfEventParser.loads(cf_event)
