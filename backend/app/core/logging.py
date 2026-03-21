import json
import logging
from logging.config import dictConfig

from app.core.config import get_settings


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
        }
        correlation_id = getattr(record, 'correlation_id', None)
        if correlation_id:
            payload['correlation_id'] = correlation_id
        return json.dumps(payload)


def configure_logging() -> None:
    settings = get_settings()
    log_level = 'DEBUG' if settings.environment == 'development' else 'INFO'
    dictConfig(
        {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'json': {'()': JsonFormatter},
                'plain': {'format': '%(asctime)s %(levelname)s [%(name)s] %(message)s'},
            },
            'handlers': {
                'default': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'json' if settings.environment != 'development' else 'plain',
                }
            },
            'root': {'level': log_level, 'handlers': ['default']},
        }
    )
