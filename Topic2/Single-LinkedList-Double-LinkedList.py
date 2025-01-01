# Here Is Implementation of Linked List and Doubly Linked List to manage data in the hotel management system with online booking.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_booking(self, booking):
        new_node = Node(booking)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print("A new booking added")
        self.display_bookings()

    def display_bookings(self):
        current = self.head
        if not current:
            print("No bookings available.")
            return
        print("Here are available bookings:")
        while current:
            print(current.data)
            current = current.next
        print("\n---------------------------")

    def remove_booking(self, booking_id):
        current = self.head  
        prev = None  

        while current:
            if current.data['id'] == booking_id:
                break  
            prev = current  
            current = current.next  

        if not current:
            print(f"Booking with ID {booking_id} not found.")
            return

        if prev:
            prev.next = current.next  
        else:
            self.head = current.next  

        print(f"Booking with ID {booking_id} removed successfully.")
        self.display_bookings()

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_guest(self, guest):
        new_node = DoublyNode(guest)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        print("A new guest added")
        self.display_guests()

    def display_guests(self):
        current = self.head
        if not current:
            print("No guest details available.")
            return
        print("Here are available guests:")
        while current:
            print(current.data)
            current = current.next
        print("\n---------------------------")

    def remove_guest(self, guest_id):
        current = self.head
        while current and current.data['id'] != guest_id:
            current = current.next
        if not current:
            print(f"Guest with ID {guest_id} not found.")
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:
            self.head = current.next
        print(f"Guest with ID {guest_id} removed successfully.")
        self.display_guests()

# Run code
def HotelMS():
    bookings = LinkedList()
    guests = DoublyLinkedList()

    while True:
        print("\n Hotel Management system functions:")
        print("1: Add Booking")
        print("2: Remove Booking")
        print("3: Add Guest")
        print("4: Remove Guest")
        print("5: Hotels Details")
        print("0: Exit system")
        choice = input("Enter your choice of what you want to do: ")

        if choice == "1":
            print("\nEnter booking details:")
            booking_id = int(input("Booking ID: "))
            room_number = int(input("Room Number: "))
            guest_name = input("Guest Name: ")
            date = input("Date (YYYY-MM-DD): ")
            bookings.add_booking({
                "id": booking_id,
                "room_number": room_number,
                "guest_name": guest_name,
                "date": date
            })

        elif choice == "2":
            booking_id = int(input("\nEnter Booking ID to remove: "))
            bookings.remove_booking(booking_id)

        elif choice == "3":
            print("\nEnter guest details:")
            guest_id = int(input("Guest ID: "))
            name = input("Guest Name: ")
            contact = input("Contact Number: ")
            guests.add_guest({
                "id": guest_id,
                "name": name,
                "contact": contact
            })

        elif choice == "4":
            guest_id = int(input("\nEnter Guest ID to remove: "))
            guests.remove_guest(guest_id)
        elif choice == "5":
            bookings.display_bookings()
            guests.display_guests()

        elif choice == "0":
            print("\nSystem exited, if you done by mistake run again and enjoy it's functionalities.")
            print("\nFinalHotel Details:")
            bookings.display_bookings()
            guests.display_guests()
            break

        else:
            print("\nInvalid choice! Please try again.")

HotelMS()

