# Реализуйте класс Order, который:
# Принимает order_id и статус (по умолчанию PENDING).
# Содержит метод update_status(new_status), который обновляет статус заказа.
# Содержит метод display_status(), который выводит текущий статус заказа.

from enum import Enum


class OrderStatus(Enum):
    PENDING = (1, ["IN_PROGRESS", "CANCELLED"])
    IN_PROGRESS = (2, ["READY", "CANCELLED"])
    READY = (3, ["COMPLETED", "CANCELLED"])
    COMPLETED = (4, [])
    CANCELLED = (5, [])

    def __init__(self, num, status):
        self.num = num
        self.status = status

    def is_changeable(self, new_status):
        return new_status.name in self.status


class Order:

    def __init__(self, order_id):
        self.order_id = order_id
        self.order_status = OrderStatus.PENDING

    def __str__(self):
        return f"Order Id: {self.order_id}, Status: {self.order_status.name}"

    def update_status(self, new_status):
        if self.order_status.is_changeable(new_status):
            self.order_status = new_status
            return f"Order status changed to {new_status.name}"
        else:
            return (f"Warning! Invalid status."
                    f"Order id: {self.order_id}."
                    f"Status from: {self.order_status.name}."
                    f"Status to: {new_status.name}")

    def display_status(self):
        return f"Order Id: {self.order_id}, Current Status: {self.order_status.name}"


order1 = Order("001")
print(order1)

print(order1.update_status(OrderStatus.IN_PROGRESS))
print(order1.display_status())
