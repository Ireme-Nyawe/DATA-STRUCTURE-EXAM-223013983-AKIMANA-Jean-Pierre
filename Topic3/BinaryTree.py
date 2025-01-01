#here is implementation of Binary Tree for hotel management system with online booking processing.
class TreeNode:
    def __init__(self, booking_data):
        self.booking_data = booking_data
        self.left = None
        self.right = None
        self.key = booking_data['booking_id']

class HotelBookingTree:
    def __init__(self):
        self.root = None
        self.total_bookings = 0

    def add_booking(self, booking_data):
        self.total_bookings += 1
        if not self.root:
            self.root = TreeNode(booking_data)
            print("Booking added successfully!")
            return
        
        current = self.root
        while True:
            if booking_data['booking_id'] < current.key:
                if current.left is None:
                    current.left = TreeNode(booking_data)
                    print("Booking added successfully!")
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(booking_data)
                    print("Booking added successfully!")
                    break
                current = current.right

    def find_booking(self, booking_id):
        current = self.root
        while current:
            if booking_id == current.key:
                return current
            elif booking_id < current.key:
                current = current.left
            else:
                current = current.right
        return None

    def find_min_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def remove_booking(self, booking_id):
        self.root = self._remove_booking_recursive(self.root, booking_id)
        
    def _remove_booking_recursive(self, root, booking_id):
        if not root:
            print("Booking not found!")
            return None
            
        if booking_id < root.key:
            root.left = self._remove_booking_recursive(root.left, booking_id)
        elif booking_id > root.key:
            root.right = self._remove_booking_recursive(root.right, booking_id)
        else:
            self.total_bookings -= 1
            print("Booking removed successfully!")
            
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
                
            temp = self.find_min_node(root.right)
            root.booking_data = temp.booking_data
            root.key = temp.key
            root.right = self._remove_booking_recursive(root.right, temp.key)
            
        return root

    def display_bookings(self):
        if not self.root:
            print("No bookings available.")
            return
        
        print("\nCurrent Bookings (In-order traversal):")
        print("-------------------------------------")
        self._inorder_traversal(self.root)
        print(f"\nTotal number of bookings: {self.total_bookings}")
        print("-------------------------------------")

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            self._print_booking(node.booking_data)
            self._inorder_traversal(node.right)

    def _print_booking(self, booking_data):
        print(f"\nBooking ID: {booking_data['booking_id']}")
        print(f"Guest Name: {booking_data['guest_name']}")
        print(f"Room Number: {booking_data['room_number']}")
        print(f"Booking-Date: {booking_data['booking-date']}")
        print(f"Status: {booking_data['status']}")

def HotelManagementSystem():
    booking_system = HotelBookingTree()
    
    while True:
        print("\nHotel Management System with binary tree")
        print("1: Add New Booking")
        print("2: Find Booking")
        print("3: Remove Booking")
        print("4: Display All Bookings")
        print("0: Exit System")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            print("\nEnter booking details:")
            booking_data = {
                'booking_id': int(input("Booking ID: ")),
                'guest_name': input("Guest Name: "),
                'room_number': int(input("Room Number: ")),
                'booking-date': input("Booking Date-in Date (YYYY-MM-DD): "),
                'status': "Confirmed"
            }
            booking_system.add_booking(booking_data)

        elif choice == "2":
            booking_id = int(input("\nEnter Booking ID to find: "))
            booking = booking_system.find_booking(booking_id)
            if booking:
                print("\nBooking Found:")
                booking_system._print_booking(booking.booking_data)
            else:
                print("\nBooking not found!")

        elif choice == "3":
            booking_id = int(input("\nEnter Booking ID to remove: "))
            booking_system.remove_booking(booking_id)

        elif choice == "4":
            booking_system.display_bookings()

        elif choice == "0":
            print("\nThank you for using the Hotel Management System, if exited by mistake run again and enjoy usage of binary tree in Hotel MS")
            booking_system.display_bookings()
            break

        else:
            print("\nInvalid choice! Please try again.")


HotelManagementSystem()