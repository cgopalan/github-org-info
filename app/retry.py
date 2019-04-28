
def retry(logger, count=3):
    """ Decorator for retries """
    def retry_decorator(f):
        # This wrapper preserves the original method metadata
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            # Retry logic
            retries = count + 1
            while retries > 0:
                try:
                    return f(*args, **kwargs)
                except RetryError as e:
                    retries -= 1
                    if retries > 0:
                        logger.info(f'Failed with error code {e.code}. Retrying...')
            else:
                logger.info("Retries exhausted. Stopping")
        return wrapper
    return retry_decorator


class RetryError(Exception):
    pass