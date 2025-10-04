import logging
import traceback

class TracebackFormatter(logging.Formatter):
    def format(self, record):
        # Format the base log message
        log_msg = super().format(record)

        # Only append traceback if exception info exists
        if record.exc_info:
            log_msg += "\n" + "".join(traceback.format_exception(*record.exc_info))

        return log_msg