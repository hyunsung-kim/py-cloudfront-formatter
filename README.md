<p align="center">
    <img src="log.jpg" width="1000" />
</p>

# py-cloudfront-formatter
[Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-event-structure.html) 에서 사용하는 복잡한 내용을 json 형태로 포맷하기 위한 `Formatter`를 제공한다.

## Terminology
- Logger: 사용자에게 로그 기능을 사용하기 위한 인터페이스
- Handler: 원하는 목적지(Destination)에 로그 레코드(log record)를 출력하기 위한 함수
- Filter: 어떤 로그를 출력할지 결정하는 함수
- Formatter: 로그 레코드의 레이아웃(형태)


## Usage
```
import logging

from py_logger.cf_formatter import CloudfrontJSONFormatter

# cf handler
cf_handler = logging.StreamHandler()
cf_handler.setFormatter(CloudfrontJSONFormatter())

# setting up cf logger
logger = logging.getLogger('cf_logger')
logger.addHandler(cf_handler)
logger.setLevel(logging.INFO)
logger.propagate = False

logger.info('good', extra=cf_event)
```

## TODO
- [ ] 테스트 코드 작성
- [ ] log record 중에 필요한 부분으 추가하기 e.g) exc_info=True


## Reference
- [logging-cookbook](https://docs.python.org/ko/3/howto/logging-cookbook.html#)
- [python-json-logger](https://github.com/madzak/python-json-logger)
- [json-log-formatter](https://github.com/marselester/json-log-formatter)
