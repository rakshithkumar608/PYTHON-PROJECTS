import datetime
import random
import string

class KSRTCTicketSystem:
    def __init__(self):
        self.routes = {
            "Bangalore": ["Mysore", "Mangalore", "Hubli", "Hassan", "Tumkur", "Kolar", "Devanahalli"],
            "Mysore": ["Bangalore", "Mangalore", "Ooty", "Hassan", "Coorg"],
            "Mangalore": ["Bangalore", "Mysore", "Udupi", "Karwar", "Gokarna"],
            "Hubli": ["Bangalore", "Belgaum", "Bijapur", "Gadag", "Haveri"],
            "Hassan": ["Bangalore", "Mysore", "Chikmagalur", "Belur", "Halebid"]
        }

        self.bus_types = { 
            "Ordinary": {"fare_per_km": 1.2, "amenities": "Basic seating"},
            "Express": {"fare_per_km": 1.5, "amenities": "Comfortable seating, faster travel"},
            "Volvo": {"fare_per_km": 2.0, "amenities": "AC, comfortable seating, entertainment"},
            "Sleeper": {"fare_per_km": 2.5, "amenities": "Sleeping berths, AC, blankets"},
            "Luxury": {"fare_per_km": 3.0, "amenities": "Premium seating, AC, entertainment, meals"}
        }

        self.distances = {
            ("Bangalore", "Mysore"): 150,
            ("Bangalore", "Mangalore"): 352,
            ("Bangalore", "Hubli"): 410,
            ("Bangalore", "Hassan"): 183,
            ("Bangalore", "Tumkur"): 70,
            ("Bangalore", "Kolar"): 68,
            ("Mysore", "Mangalore"): 250,
            ("Mysore", "Hassan"): 118,
            ("Mysore", "Coorg"): 120,
            ("Mangalore", "Udupi"): 58,
            ("Mangalore", "Karwar"): 260,
            ("Hubli", "Belgaum"): 102,
            ("Hubli", "Bijapur"): 165
        }
 

    def generate_ticket_number(self):
        """Generate a unique ticket number"""
        return "KSRTC" + ''.join(random.choices(string.digits, k=8))

    def generate_bus_number(self):
        """Generate a bus number"""
        return "KA" + ''.join(random.choices(string.digits, k=2)) + "F" + ''.join(random.choices(string.digits, k=4))

    def display_routes(self):
        """Display available routes"""
        print("\n" + "="*50)
        print("           AVAILABLE ROUTES")
        print("="*50)
        for origin, destinations in self.routes.items():
            print(f"{origin} -> {', '.join(destinations)}")
        print("="*50)

    def display_bus_types(self):
        """Display available bus types"""
        print("\n" + "="*60)
        print("                BUS TYPES & AMENITIES")
        print("="*60)
        for bus_type, details in self.bus_types.items():
            print(f"{bus_type:10} | ₹{details['fare_per_km']}/km | {details['amenities']}")
        print("="*60)

    def get_distance(self, origin, destination):
        """Get distance between two cities"""
        route = (origin, destination)
        reverse_route = (destination, origin)
        
        if route in self.distances:
            return self.distances[route]
        elif reverse_route in self.distances:
            return self.distances[reverse_route]
        else:
            # If route not found, return a default distance
            return 200

    def calculate_fare(self, distance, bus_type, passenger_count):
        """Calculate total fare"""
        base_fare = distance * self.bus_types[bus_type]["fare_per_km"]
        total_fare = base_fare * passenger_count
        
        # Add service tax (5%)
        service_tax = total_fare * 0.05
        total_amount = total_fare + service_tax
        
        return base_fare, service_tax, total_amount

    def get_user_input(self):
        """Get all user inputs for ticket booking"""
        print("\n" + "="*60)
        print("     WELCOME TO KSRTC BUS TICKET BOOKING SYSTEM")
        print("="*60)
        
        # Display available routes
        self.display_routes()
        
        # Get origin and destination
        while True:
            origin = input("\nEnter Origin City: ").strip().title()
            if origin in self.routes:
                break
            print("Invalid origin city. Please choose from available routes.")
        
        while True:
            destination = input("Enter Destination City: ").strip().title()
            if destination in self.routes[origin]:
                break
            print(f"Invalid destination. Available destinations from {origin}: {', '.join(self.routes[origin])}")
        
        # Display bus types
        self.display_bus_types()
        
        # Get bus type
        while True:
            bus_type = input("\nEnter Bus Type: ").strip().title()
            if bus_type in self.bus_types:
                break
            print("Invalid bus type. Please choose from: " + ", ".join(self.bus_types.keys()))
        
        # Get travel date
        while True:
            try:
                travel_date = input("Enter Travel Date (DD-MM-YYYY): ").strip()
                travel_date_obj = datetime.datetime.strptime(travel_date, "%d-%m-%Y")
                if travel_date_obj.date() < datetime.date.today():
                    print("Travel date cannot be in the past. Please enter a valid date.")
                    continue
                break
            except ValueError:
                print("Invalid date format. Please use DD-MM-YYYY format.")
        
        # Get travel time
        while True:
            try:
                travel_time = input("Enter Travel Time (HH:MM in 24-hour format): ").strip()
                datetime.datetime.strptime(travel_time, "%H:%M")
                break
            except ValueError:
                print("Invalid time format. Please use HH:MM format (e.g., 14:30)")
        
        # Get number of passengers
        while True:
            try:
                passenger_count = int(input("Enter Number of Passengers: "))
                if passenger_count <= 0:
                    print("Number of passengers must be greater than 0.")
                    continue
                if passenger_count > 10:
                    print("Maximum 10 passengers allowed per booking.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        
        # Get passenger details
        passengers = []
        for i in range(passenger_count):
            print(f"\n--- Passenger {i+1} Details ---")
            name = input("Enter Name: ").strip().title()
            
            while True:
                try:
                    age = int(input("Enter Age: "))
                    if age <= 0 or age > 120:
                        print("Please enter a valid age (1-120).")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid age.")
            
            while True:
                gender = input("Enter Gender (MALE/FEMSLE/OTHERS): ").strip().upper()
                if gender in ['MALE', 'FEMALE', 'OTHERS']:
                    break
                print("Please enter MALE for Male, FEMALE for Female, or OTHER for Other.")
            
            passengers.append({
                "name": name,
                "age": age,
                "gender": gender,
                "seat_number": f"S{i+1:02d}"
            })
        
        # Get contact details
        print("\n--- Contact Details ---")
        while True:
            mobile = input("Enter Mobile Number: ").strip()
            if len(mobile) == 10 and mobile.isdigit():
                break
            print("Please enter a valid 10-digit mobile number.")
        
        email = input("Enter Email ID : ").strip()
        
        return {
            "origin": origin,
            "destination": destination,
            "bus_type": bus_type,
            "travel_date": travel_date,
            "travel_time": travel_time,
            "passenger_count": passenger_count,
            "passengers": passengers,
            "mobile": mobile,
            "email": email
        }

    def generate_ticket(self, booking_details):
        """Generate and display the ticket"""
        distance = self.get_distance(booking_details["origin"], booking_details["destination"])
        base_fare, service_tax, total_amount = self.calculate_fare(
            distance, booking_details["bus_type"], booking_details["passenger_count"]
        )
        
        ticket_number = self.generate_ticket_number()
        bus_number = self.generate_bus_number()
        
        # Display ticket
        print("\n" + "="*80)
        print("                    KARNATAKA STATE ROAD TRANSPORT CORPORATION")
        print("                                  BUS TICKET")
        print("="*80)
        print(f"Ticket Number: {ticket_number:>20}    Date: {datetime.date.today().strftime('%d-%m-%Y')}")
        print(f"Bus Number: {bus_number:>23}    Time: {datetime.datetime.now().strftime('%H:%M')}")
        print("-"*80)
        
        print(f"From: {booking_details['origin']:<20} To: {booking_details['destination']:<20}")
        print(f"Travel Date: {booking_details['travel_date']:<15} Travel Time: {booking_details['travel_time']}")
        print(f"Bus Type: {booking_details['bus_type']:<18} Distance: {distance} km")
        print(f"Amenities: {self.bus_types[booking_details['bus_type']]['amenities']}")
        
        print("-"*80)
        print("PASSENGER DETAILS:")
        print("-"*80)
        print(f"{'Name':<20} {'Age':<5} {'Gender':<8} {'Seat':<6}")
        print("-"*40)
        
        for passenger in booking_details["passengers"]:
            print(f"{passenger['name']:<20} {passenger['age']:<5} {passenger['gender']:<8} {passenger['seat_number']:<6}")
        
        print("-"*80)
        print("FARE BREAKDOWN:")
        print("-"*80)
        print(f"Base Fare ({booking_details['passenger_count']} passengers): ₹{base_fare:.2f}")
        print(f"Service Tax (5%): ₹{service_tax:.2f}")
        print(f"Total Amount: ₹{total_amount:.2f}")
        
        print("-"*80)
        print(f"Contact: {booking_details['mobile']}")
        if booking_details['email']:
            print(f"Email: {booking_details['email']}")
        
        print("-"*80)
        print("TERMS & CONDITIONS:")
        print("1. Please arrive at the bus station 30 minutes before departure")
        print("2. Ticket is non-refundable")
        print("3. Valid ID proof required during travel")
        print("4. Smoking and drinking alcohol is prohibited")
        print("="*80)
        print("              Thank you for choosing KSRTC!")
        print("                Have a safe journey!")
        print("="*80)

    def run(self):
        """Main function to run the ticket booking system"""
        try:
            booking_details = self.get_user_input()
            print("\n" + "="*50)
            print("           PROCESSING YOUR BOOKING...")
            print("="*50)
            
            # Simulate processing time
            import time
            time.sleep(2)
            
            print("✓ Booking confirmed!")
            self.generate_ticket(booking_details)
            
        except KeyboardInterrupt:
            print("\n\nBooking cancelled by user.")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again.")

# Run the KSRTC ticket booking system
if __name__ == "__main__":
    ksrtc = KSRTCTicketSystem()
    ksrtc.run()
