from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is None:
        return Response(
            {'success': False, 'message': 'Credenciales inválidas', 'data': None},
            status=status.HTTP_401_UNAUTHORIZED
        )

    refresh = RefreshToken.for_user(user)

    return Response(
        {
            'success': True,
            'message': 'Login exitoso',
            'data': {
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user': {
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                }
            }
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def refresh_token(request):
    refresh = request.data.get('refresh')

    if not refresh:
        return Response(
            {'success': False, 'message': 'Token refresh requerido', 'data': None},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        token = RefreshToken(refresh)
        return Response(
            {
                'success': True,
                'message': 'Token refrescado',
                'data': {'access': str(token.access_token)}
            },
            status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {'success': False, 'message': 'Token inválido', 'data': None},
            status=status.HTTP_401_UNAUTHORIZED
        )
