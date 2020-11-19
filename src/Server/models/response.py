from rest_framework.response import Response


def JsonResponse(code=None, msg=None, data=None) -> Response:
    if code is None:
        code = 0
    if msg is None:
        msg = ''
    if data is None:
        data = ''

    json = {
        "code": code,
        "msg": msg,
        "data": data
    }
    return Response(json)
