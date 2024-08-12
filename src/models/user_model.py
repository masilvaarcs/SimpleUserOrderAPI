from dataclasses import dataclass, asdict


@dataclass
class User:
    user_id: int
    name: str
    phone: str
    street: str
    city: str
    neighborhood: str
    zip_code: str
    state: str
    email: str
    password_hash: str  # Use um hash seguro para a senha

    def to_dict(self):
        # Convert dataclass to dictionary excluding the password hash for security reasons
        user_dict = asdict(self)
        user_dict.pop(
            "password_hash", None
        )  # Remove password hash from the dictionary if necessary
        return user_dict
