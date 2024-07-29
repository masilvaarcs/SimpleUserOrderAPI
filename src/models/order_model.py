class Order:
    def __init__(self, order_id: object, user_id: object, item: object) -> object:
        self.id = order_id
        self.user_id = user_id
        self.item = item

    def to_dict(self):
        return {"id": self.id, "user_id": self.user_id, "item": self.item}
