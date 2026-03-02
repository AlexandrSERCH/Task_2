from pydantic import BaseModel


class UserData(BaseModel):
    email: str
    name: str

class UserResponseBody(BaseModel):
    success: bool
    message: str | None = None
    user: UserData | None = None
    accessToken: str | None = None
    refreshToken: str | None = None

class UserResponse(BaseModel):
    status_code: int
    body: UserResponseBody