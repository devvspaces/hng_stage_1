from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_user_details(request):
    data = {
        "slackUsername": "netrobe",
        "backend": True,
        "age": 20,
        "bio": "I am a student of UoL that loves coding."
    }
    return Response(data)


@api_view(['POST'])
def calculate(request):
    """
    Sample Input
    ```
    {
        "operation_type": Enum <addition | subtraction | multiplication> ,
        "x": Integer,
        "y": Integer
    }
    ```

    Sample Response Format
    ```
    {
        "slackUsername": String,
        "result": Integer,
        "operation_type": Enum.value
    }
    ```
    """

    data: dict = request.data
    operation_type = data.get('operation_type')
    x = float(data.get('x'))
    y = float(data.get('y'))

    operation_map = {
        'addition': lambda x, y: x + y,
        'subtraction': lambda x, y: x - y,
        'multiplication': lambda x, y: x * y
    }

    result = operation_map[operation_type](x, y)

    data = {
        "slackUsername": "netrobe",
        "result": result,
        "operation_type": operation_type
    }
    return Response(data)
