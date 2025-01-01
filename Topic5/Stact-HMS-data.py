# Program tha Use Stack to track data dynamically in hotel management system with online booking.
class BookingStack:
    def __init__(self):
        self.bookings = []

    def push_booking(self, booking):
        self.bookings.append(booking)
        print("New booking added successfully!")
        self.display_current_bookings()

    def pop_booking(self):
        if not self.bookings:
            print("No bookings to remove.")
            return None
        booking = self.bookings.pop()
        print("Latest booking removed successfully!")
        return booking

    def peek_booking(self):
        if not self.bookings:
            print("No bookings available.")
            return None
        return self.bookings[-1]

    def display_current_bookings(self):
        if not self.bookings:
            print("\nNo current bookings.")
            return
        
        print("\nCurrent Bookings (Latest to Oldest):")
        print("------------------------------------")
        for i in range(len(self.bookings) - 1, -1, -1):
            booking = self.bookings[i]
            print(f"\nBooking ID: {booking['id']}")
            print(f"Guest Name: {booking['guest_name']}")
            print(f"Room Number: {booking['room_number']}")
            print(f"Date: {booking['date']}")
            print(f"Status: {booking['status']}")
            print("------------------------------------")


def HotelManagementSystem():
    booking_stack = BookingStack()
    
    while True:
        print("\nHotel Management System (Stack Implementation)")
        print("1: Add New Booking")
        print("2: Remove Latest Booking")
        print("3: View Latest Booking")
        print("4: Display All Current Bookings")
        print("0: Exit System")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\nEnter booking details:")
            booking_id = int(input("Booking ID: "))
            guest_name = input("Guest Name: ")
            room_number = int(input("Room Number: "))
            date = input("Date (YYYY-MM-DD): ")
            
            booking = {
                "id": booking_id,
                "guest_name": guest_name,
                "room_number": room_number,
                "date": date,
                "status": "Confirmed"
            }
            
            booking_stack.push_booking(booking)

        elif choice == "2":
            removed_booking = booking_stack.pop_booking()
            if removed_booking:
                booking_stack.display_current_bookings()

        elif choice == "3":
            latest = booking_stack.peek_booking()
            if latest:
                print("\nLatest Booking Details:")
                print("------------------------------------")
                print(f"Booking ID: {latest['id']}")
                print(f"Guest Name: {latest['guest_name']}")
                print(f"Room Number: {latest['room_number']}")
                print(f"Date: {latest['date']}")
                print(f"Status: {latest['status']}")
                print("------------------------------------")

        elif choice == "4":
            booking_stack.display_current_bookings()


        elif choice == "0":
            print("\nFinal System Status:")
            booking_stack.display_current_bookings()
            print("\nThank you for using the Hotel Management System!")
            break

        else:
            print("\nInvalid choice! Please try again.")

HotelManagementSystem()