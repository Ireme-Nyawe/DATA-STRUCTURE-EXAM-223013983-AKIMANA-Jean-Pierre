#Implementation of a tree to represent hierarchical data in the hotel management system with online booking.
class HotelNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

class HotelTree:
    def __init__(self):
        self.root = None

    def create_hotel_structure(self):
        hotel_data = {
            "name": "Grand Hotel",
            "type": "hotel"
        }
        self.root = HotelNode(hotel_data)
        print("Hotel structure created successfully!")

    def add_floor(self, floor_number):
        if not self.root:
            print("Please create hotel structure first!")
            return
        
        floor_data = {
            "number": floor_number,
            "type": "floor"
        }
        floor_node = HotelNode(floor_data)
        floor_node.parent = self.root
        self.root.children.append(floor_node)
        print(f"Floor {floor_number} added successfully!")
        return floor_node

    def add_room(self, floor_number, room_data):
        if not self.root:
            print("Please create hotel structure first!")
            return

        # Find the floor
        floor_node = None
        for child in self.root.children:
            if child.data["number"] == floor_number:
                floor_node = child
                break

        if not floor_node:
            print(f"Floor {floor_number} not found!")
            return

        room_node = HotelNode(room_data)
        room_node.parent = floor_node
        floor_node.children.append(room_node)
        print(f"Room {room_data['number']} added to floor {floor_number}!")

    def display_structure(self):
        if not self.root:
            print("No hotel structure exists.")
            return

        print("\nHotel Structure:")
        print("================")
        print(f"Hotel: {self.root.data['name']}")
        
        for floor in self.root.children:
            print(f"\nFloor {floor.data['number']}:")
            print("--------------")
            if not floor.children:
                print("No rooms added yet")
                continue
            
            for room in floor.children:
                print(f"Room {room.data['number']}:")
                print(f"  Type: {room.data['type']}")
                print(f"  Status: {room.data['status']}")
                if 'booking' in room.data:
                    print(f"  Booked by: {room.data['booking']['guest_name']}")
                    print(f"  Date: {room.data['booking']['date']}")
                print("--------------")

    def find_room(self, room_number):
        if not self.root:
            return None

        for floor in self.root.children:
            for room in floor.children:
                if room.data['number'] == room_number:
                    return room
        return None

def HotelManagementSystem():
    hotel = HotelTree()
    hotel.create_hotel_structure()

    while True:
        print("\nHotel Management System (Hierarchical Tree)")
        print("1: Add New Floor")
        print("2: Add New Room")
        print("3: Book a Room")
        print("4: Display Hotel Structure")
        print("0: Exit System")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            floor_number = int(input("Enter floor number: "))
            hotel.add_floor(floor_number)

        elif choice == "2":
            floor_number = int(input("Enter floor number: "))
            room_number = int(input("Enter room number: "))
            room_type = input("Enter room type (Single/Double/Suite): ")
            
            room_data = {
                "number": room_number,
                "type": room_type,
                "status": "Available"
            }
            hotel.add_room(floor_number, room_data)

        elif choice == "3":
            room_number = int(input("Enter room number to book: "))
            room_node = hotel.find_room(room_number)
            
            if room_node:
                if room_node.data['status'] == 'Booked':
                    print("Room is already booked!")
                    continue
                    
                guest_name = input("Enter guest name: ")
                date = input("Enter date (YYYY-MM-DD): ")
                
                room_node.data['status'] = 'Booked'
                room_node.data['booking'] = {
                    'guest_name': guest_name,
                    'date': date
                }
                print(f"Room {room_number} booked successfully!")
            else:
                print("Room not found!")

        elif choice == "4":
            hotel.display_structure()

        elif choice == "0":
            print("\nFinal Hotel Status:")
            hotel.display_structure()
            print("\nThank you for using the Hotel Management System!")
            break

        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    HotelManagementSystem()