from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Логирует начало и конец выполнения функции и ее результат или ошибки в файл или в консоль."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} called with args: {args}, kwargs:{kwargs}. Result: {result}"
                with open(filename, "a") as file:
                    file.write(log_message + "\n")
                print(log_message)
            except Exception as e:
                error_message = f"{func.__name__} error: {e}. Inputs:{args}, {kwargs}"
                with open(filename, "a") as file:
                    file.write(error_message + "\n")
                print(error_message)
            return result

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


print(my_function(1, 2))
