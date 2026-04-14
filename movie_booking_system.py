# Online Movie Ticket Booking System - Console-based Python Program

movies = {
    "1": "Harahara Veeramallu",
    "2": "Kingdom",
    "3": "bhairavam",
    "4": "Kgf"
}

cities = {
    "1": "Tirupati",
    "2": "Pileru",
    "3": "Banglore"
}

theaters = {
    "Tirupati": ["NVR Jayashyam Cinema Hall", "NVR Sandhya Cinema Hall", "S V Cineplex","S V Cineplex"],
    "pileru": ["SV Mahal", "GV Cinemas (Ajantha Theater)" ,"Grauman's Chinese Theatre"],
    "Banglore": ["PVR Orion Mall", "PVR Vega City","PVR Cinemas Phoenix Mall"]
}

show_timings = ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM"]

bookings = []

def display_options(options_dict):
    for key, value in options_dict.items():
        print(f"{key}. {value}")

def select_movie():
    print("\n🎬 Available Movies:")
    display_options(movies)
    choice = input("Enter movie number: ")
    movie = movies.get(choice)
    if not movie:
        print("❌ Invalid movie selection.")
    return movie

def select_city():
    print("\n🏙️ Available Cities:")
    display_options(cities)
    choice = input("Enter city number: ")
    city = cities.get(choice)
    if not city:
        print("❌ Invalid city selection.")
    return city

def select_theater(city):
    try:
        available_theaters = theaters[city]
    except KeyError:
        print("❌ No theaters available in the selected city.")
        return None

    print(f"\n🏢 Available Theaters in {city}:")
    for i, theater in enumerate(available_theaters, start=1):
        print(f"{i}. {theater}")
    try:
        choice = int(input("Enter theater number: "))
        if 1 <= choice <= len(available_theaters):
            return available_theaters[choice - 1]
        else:
            print("❌ Invalid theater number.")
    except ValueError:
        print("❌ Please enter a valid number.")
    return None

def select_timing():
    print("\n🕒 Available Show Timings:")
    for i, timing in enumerate(show_timings, start=1):
        print(f"{i}. {timing}")
    try:
        choice = int(input("Enter timing number: "))
        if 1 <= choice <= len(show_timings):
            return show_timings[choice - 1]
        else:
            print("❌ Invalid timing number.")
    except ValueError:
        print("❌ Please enter a valid number.")
    return None

def book_tickets():
    print("\n📖 Booking Tickets...")
    name = input("Enter your name (e.g., GJG, AF): ")

    movie = select_movie()
    if not movie:
        return

    city = select_city()
    if not city:
        return

    theater = select_theater(city)
    if not theater:
        return

    timing = select_timing()
    if not timing:
        return

    try:
        seats = int(input("🎟️ Enter number of seats to book: "))
        if seats <= 0:
            print("❌ Number of seats must be positive.")
            return
    except ValueError:
        print("❌ Invalid input for seats.")
        return

    booking = {
        "Name": name,
        "Movie": movie,
        "City": city,
        "Theater": theater,
        "Timing": timing,
        "Seats": seats
    }

    bookings.append(booking)
    print("\n✅ Booking Confirmed!")
    print(f"👤 Name: {name}")
    print(f"🎬 Movie: {movie}")
    print(f"🏙️ City: {city}")
    print(f"🏢 Theater: {theater}")
    print(f"🕒 Time: {timing}")
    print(f"🎟️ Seats: {seats}")

def view_bookings():
    print("\n📄 All Bookings:")
    if not bookings:
        print("No bookings yet.")
        return
    for i, booking in enumerate(bookings, start=1):
        print(f"\nBooking {i}:")
        for key, value in booking.items():
            print(f"{key}: {value}")

def main_menu():
    while True:
        print("\n==== 🎟️ Online Movie Ticket Booking System ====")
        print("1. Book Tickets")
        print("2. View Bookings")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_tickets()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            print("Thank you for using the Movie Ticket Booking System! 🎬")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
