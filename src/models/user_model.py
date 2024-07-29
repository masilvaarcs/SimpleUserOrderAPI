class User:
    def __init__(
        self,
        user_id: object,
        name: object,
        phone: object,
        street: object,
        city: object,
        neighborhood: object,
        zip_code: object,
        state: object,
        email: object,
        password: object,
    ) -> object:
        self.user_id = user_id
        self.name = name
        self.phone = phone
        self.street = street
        self.city = city
        self.neighborhood = neighborhood
        self.zip_code = zip_code
        self.state = state
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "phone": self.phone,
            "street": self.street,
            "city": self.city,
            "neighborhood": self.neighborhood,
            "zip_code": self.zip_code,
            "state": self.state,
            "email": self.email,
            "password": self.password,
        }
