import functools
from typing import Any
from typing import Callable
from typing import Dict

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from pitter import exceptions


def request_query_parameters_serializer(
    # pylint: disable=bad-continuation
    serializer: type,
) -> Callable[[Callable[..., Response]], Callable[..., Response]]:
    # pylint: enable=bad-continuation
    """Валидация данных запроса"""

    def _decorator(handler: Callable[..., Response]) -> Callable[..., Response]:
        @functools.wraps(handler)
        def _wrapper(view: APIView, request: Request, *args: Any, **kwargs: Any) -> Response:
            ser = serializer(data=request.query_params)
            if not ser.is_valid():
                raise exceptions.BadRequestError(str(ser.errors))
            return handler(view, request, *args, **kwargs)

        return _wrapper

    return _decorator


def request_body_serializer(serializer: type) -> Callable[[Callable[..., Response]], Callable[..., Response]]:
    """Валидация данных запроса"""

    def _decorator(handler: Callable[..., Response]) -> Callable[..., Response]:
        @functools.wraps(handler)
        def _wrapper(view: APIView, request: Request, *args: Any, **kwargs: Any) -> Response:
            ser = serializer(data=request.data)
            if not ser.is_valid():
                raise exceptions.BadRequestError(str(ser.errors))
            return handler(view, request, *args, **kwargs)

        return _wrapper

    return _decorator


def response_dict_serializer(serializer: type) -> Callable[[Callable[..., Response]], Callable[..., Response]]:
    """Валидация данных ответа"""

    def _decorator(handler: Callable[..., Dict[str, Any]]) -> Callable[..., Response]:
        @functools.wraps(handler)
        def _wrapper(view: APIView, request: Request, *args: Any, **kwargs: Any) -> Response:
            response_data: Dict[str, Any] = handler(view, request, *args, **kwargs)
            ser = serializer(data=response_data)
            if not ser.is_valid():
                raise exceptions.InternalServerError(str(ser.errors))
            return Response(ser.validated_data)

        return _wrapper

    return _decorator
