from ttutils.TTConfigHandler import confighandler
SERVICE_NAME=confighandler.get_config('SERVICE_NAME', 'ASSIGNMENT')
from fastapi import APIRouter, Request, Depends
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from api.core.messages import messages
from api.viewmodels import vm_users
from api.dbutils import crud

from pydantic import BaseModel
from datetime import timedelta

router = APIRouter()

class Settings(BaseModel):
    authjwt_secret_key: str = confighandler.get_config("JWT_SECRET_KEY", "WpS+hfX3UO8oI9IHg7u//JVmfEQoI0kERSOC58gdbEY=")
    authjwt_algorithm: str = confighandler.get_config("JWT_ALGORITHM", "HS256")
    authjwt_access_token_expires: timedelta = timedelta(minutes=confighandler.get_config("ACCESS_TOKEN_VALID_MINUTES", 60))
    authjwt_refresh_token_expires: timedelta = timedelta(days=confighandler.get_config("REFRESH_TOKEN_VALID_DAYS", 365))


# callback to get your configuration
@AuthJWT.load_config
def get_config():
    return Settings()


@router.get(f'/{SERVICE_NAME}/api/v1/check-protected', tags=["CHECK"])
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    # current_user = Authorize.get_jwt_subject()
    # return {"user": current_user}
    return {"Hello": f"{SERVICE_NAME}"}
    
@router.post(f'/{SERVICE_NAME}/api/v1/users/login', response_model=vm_users.vm_response, tags=["USERS"])
def login(user: vm_users.vm_up, Authorize: AuthJWT = Depends()):
    is_valid = crud.is_user_valid(username=user.username, password=user.password)
    if not is_valid:
        return messages('fa').ERR_USERNAME_OR_PASSWORD_IS_WRONG()
    
    # subject identifier for who this token is for example id or username from database
    access_token = Authorize.create_access_token(subject=user.username)
    refresh_token = Authorize.create_refresh_token(subject=user.username)
    response = messages('fa').INF_SUCCESS()
    response['data'] = {"accessToken": access_token, "refreshToken": refresh_token}
    return response


@router.post(f'/{SERVICE_NAME}/api/v1/users/refresh', response_model=vm_users.vm_response, tags=["USERS"])
def refresh(Authorize: AuthJWT = Depends()):
    """
    The jwt_refresh_token_required() function insures a valid refresh
    token is present in the request before running any code below that function.
    we can use the get_jwt_subject() function to get the subject of the refresh
    token, and use the create_access_token() function again to make a new access token
    """
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    response = messages('fa').INF_SUCCESS()
    response['data'] = {"accessToken": new_access_token}
    return response
