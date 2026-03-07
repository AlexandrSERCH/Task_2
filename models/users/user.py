from dataclasses import dataclass

from models.responses.user_response import UserResponse


@dataclass
class CreatedUser:
    response: UserResponse
    user_data: dict
