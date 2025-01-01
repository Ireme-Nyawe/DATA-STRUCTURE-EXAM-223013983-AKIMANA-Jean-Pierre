class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self, max_orders):
        self.head = None
        self.max_orders = max_orders
        self.current_orders = 0

    def add_order(self, order):
        new_node = Node(order)
        
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            self.current_orders += 1
            print("First order added successfully!")
        elif self.current_orders < self.max_orders:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.current_orders += 1
            print("New order added successfully!")
        else:
            print(f"Order limit reached! Maximum {self.max_orders} orders allowed.")
            return
        
        self.display_orders()

    def remove_order(self, order_id):
        if not self.head:
            print("No orders to remove.")
            return

        if self.head.data['id'] == order_id:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            self.current_orders -= 1
            print(f"Order with ID {order_id} removed successfully!")
            self.display_orders()
            return

        current = self.head
        prev = None
        while current.next != self.head:
            if current.data['id'] == order_id:
                prev.next = current.next
                self.current_orders -= 1
                print(f"Order with ID {order_id} removed successfully!")
                self.display_orders()
                return
            prev = current
            current = current.next

        if current.data['id'] == order_id:
            prev.next = self.head
            self.current_orders -= 1
            print(f"Order with ID {order_id} removed successfully!")
            self.display_orders()
            return

        print(f"Order with ID {order_id} not found!")

    def display_orders(self):
        if not self.head:
            print("\nNo orders available.")
            return

        print("\nCurrent Orders:")
        print("---------------")
        current = self.head
        while True:
            print(f"Order ID: {current.data['id']}")
            print(f"Room Number: {current.data['room_number']}")
            print(f"Items: {current.data['items']}")
            print(f"Status: {current.data['status']}")
            print("---------------")
            current = current.next
            if current == self.head:
                break
        print(f"Total Orders: {self.current_orders}/{self.max_orders}")

def HotelOrderSystem():
    MAX_ORDERS = 5
    orders = CircularLinkedList(MAX_ORDERS)

    while True:
        print("\nHotel Order Management System")
        print(f"(Maximum {MAX_ORDERS} orders allowed)")
        print("1: Place New Order")
        print("2: Complete/Remove Order")
        print("3: Display All Orders")
        print("0: Exit System")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\nEnter order details:")
            order_id = int(input("Order ID: "))
            room_number = int(input("Room Number: "))
            items = input("Order Items (comma-separated): ").split(',')
            
            orders.add_order({
                "id": order_id,
                "room_number": room_number,
                "items": [item.strip() for item in items],
                "status": "Processing"
            })

        elif choice == "2":
            order_id = int(input("\nEnter Order ID to remove: "))
            orders.remove_order(order_id)

        elif choice == "3":
            orders.display_orders()

        elif choice == "0":
            print("\nFinal Order Status:")
            orders.display_orders()
            print("\nThank you for using the Hotel Order Management System!")
            break

        else:
            print("\nInvalid choice! Please try again.")


HotelOrderSystem()