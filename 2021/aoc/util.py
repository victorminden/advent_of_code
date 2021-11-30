import contextlib
import time


# Timer function taken (and cleaned a bit) from
# https://blog.usejournal.com/how-to-create-your-own-timing-context-manager-in-python-a0e944b48cf8
@contextlib.contextmanager
def timing(description: str) -> None:
    start = time.perf_counter()
    yield
    print(f"{description}: {time.perf_counter() - start} seconds")
