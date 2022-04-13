from rest_framework import status
import datetime
import pytz
import json
from config.helpers.errors import error_response
from .models import User

utc = pytz.UTC

# Add to login-required classes.
class LoginRequired():

    def dispatch(self, request, *args, **kwargs):
        if 'Authorization' not in request.headers:
            return error_response('Please set Auth-Token.', status.HTTP_401_UNAUTHORIZED)

        authJson = json.loads(request.headers['Authorization'])
        token = authJson['token']
        # now = utc.localize(datetime.datetime.now())
        login_user = User.objects.filter(token = token)
        # if len(login_user) == 0 or login_user[0].getExp() < now:
        #     return error_response('This token is invalid or expired.', status.HTTP_401_UNAUTHORIZED)
        if len(login_user) == 0:
            return error_response('This token is invalid or expired.', status.HTTP_401_UNAUTHORIZED)

        # request.login_user - login_user[0]
        return super().dispatch(request, *args, **kwargs)