from dataclasses import dataclass

import requests

from models.responses.user_response import UserResponse


@dataclass
class CreatedUser:
    response: UserResponse
    user_data: dict