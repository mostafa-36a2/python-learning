# https://www.youtube.com/watch?v=XIdQ6gO3Anc
from pydantic import BaseModel, EmailStr, ValidationError, field_validator


class User(BaseModel):
    name: str
    email: str
    account_id: int

    # @field_validator("name")
    # @classmethod
    # def validate_name(cls, value):
    #     if value == "mostafa":
    #         raise ValueError("mostafa should not be applied")
    #     return value

    @field_validator("account_id")
    @classmethod
    def validate_account_id(cls, value):
        if value <= 0:
            raise ValueError("Must be positive")
        return value


user = User(name="mostafa", email="test@email.com", account_id=1)

try:
    user = User(name=123, email="test@email.com", account_id=1)
except ValidationError as e:
    print(f"Oops, validation error.")

# user = User(name="mostafa", email="test@email.com", account_id=-1)

json_dump = user.model_dump_json()
print(json_dump, type(json_dump))

dict_dump = user.model_dump()
print(dict_dump, type(dict_dump))

user = User.model_validate_json(
    """
                                {"name":"aziz","email":"aziz@gitlab.com"}
                                """
)
print(user)
