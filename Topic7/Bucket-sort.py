class HotelBucketSort:
    def __init__(self):
        self.buckets = {
            1: [], 
            2: [], 
            3: [], 
            4: [],
            5: []   
        }
        self.all_bookings = []

    def add_booking(self, booking):
        priority = booking['priority']
        if priority in self.buckets:
            self.buckets[priority].append(booking)
            self.all_bookings.append(booking)
            print("Booking added successfully!")
            self._sort_bucket(priority)
            self.display_bookings()
        else:
            print("Invalid priority level! Use 1-5")

    def _sort_bucket(self, priority):
        self.buckets[priority].sort(key=lambda x: x['date'])

    def display_bookings(self):
        print("\nCurrent Bookings (Sorted by Priority):")
        print("-------------------------------------")
        
        for priority in self.buckets:
            if self.buckets[priority]:
                print(f"\nPriority Level {priority}:")
                print("------------------------")
                for booking in self.buckets[priority]:
                    print(f"Booking ID: {booking['id']}")
                    print(f"Guest Name: {booking['guest_name']}")
                    print(f"Room Number: {booking['room_number']}")
                    print(f"Date: {booking['date']}")
                    print(f"Priority: {booking['priority']} - {self._get_priority_name(booking['priority'])}")
                    print("------------------------")

    def _get_priority_name(self, priority):
        priority_names = {
            1: "Emergency",
            2: "Premium Member",
            3: "Regular Booking",
            4: "Flexible Booking",
            5: "Waitlist"
        }
        return priority_names.get(priority, "Unknown")

    def get_next_priority_booking(self):
        for priority in range(1, 6):
            if self.buckets[priority]:
                booking = self.buckets[priority][0]
                self.buckets[priority].pop(0)
                self.all_bookings.remove(booking)
                print(f"Processing booking with priority: {self._get_priority_name(priority)}")
                return booking
        return None

def HotelManagementSystem():
    booking_system = HotelBucketSort()

    while True:
        print("\nHotel Management System (Bucket Sort by Priority)")
        print("1: Add New Booking")
        print("2: Process Next Priority Booking")
        print("3: Display All Bookings")
        print("0: Exit System")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\nEnter booking details:")
            booking_id = int(input("Booking ID: "))
            guest_name = input("Guest Name: ")
            room_number = int(input("Room Number: "))
            date = input("Date (YYYY-MM-DD): ")
            
            print("\nPriority Levels:")
            print("1: Emergency")
            print("2: Premium Member")
            print("3: Regular Booking")
            print("4: Flexible Booking")
            print("5: Waitlist")
            priority = int(input("Enter priority level (1-5): "))

            booking = {
                "id": booking_id,
                "guest_name": guest_name,
                "room_number": room_number,
                "date": date,
                "priority": priority
            }
            
            booking_system.add_booking(booking)

        elif choice == "2":
            processed_booking = booking_system.get_next_priority_booking()
            if processed_booking:
                print("\nProcessed Booking Details:")
                print("-------------------------")
                print(f"Booking ID: {processed_booking['id']}")
                print(f"Guest Name: {processed_booking['guest_name']}")
                print(f"Room Number: {processed_booking['room_number']}")
                print(f"Date: {processed_booking['date']}")
                print("-------------------------")
                booking_system.display_bookings()
            else:
                print("No bookings available to process!")

        elif choice == "3":
            booking_system.display_bookings()

        elif choice == "0":
            print("\nFinal Booking Status:")
            booking_system.display_bookings()
            print("\nThank you for using the Hotel Management System!")
            break

        else:
            print("\nInvalid choice! Please try again.")

HotelManagementSystem()