# Simple Hotel Booking System using File Handling

import os

def initialize_files():
    if not os.path.exists("rooms.txt"):
        f = open("rooms.txt", "w")
        f.write("101,Single,1500,Available\n")
        f.write("102,Double,2500,Available\n")
        f.write("103,Suite,4000,Available\n")
        f.close()

    if not os.path.exists("customers.txt"):
        open("customers.txt", "w").close()

    if not os.path.exists("bookings.txt"):
        open("bookings.txt", "w").close()


# ----------------------------------
# Helper functions
# ----------------------------------
def read_rooms():
    rooms = []
    f = open("rooms.txt", "r")
    for line in f:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            rooms.append({
                "number": parts[0],
                "type": parts[1],
                "rate": float(parts[2]),
                "status": parts[3]
            })
    f.close()
    return rooms


def write_rooms(rooms):
    f = open("rooms.txt", "w")
    for r in rooms:
        line = r["number"] + "," + r["type"] + "," + str(r["rate"]) + "," + r["status"] + "\n"
        f.write(line)
    f.close()


def read_customers():
    customers = []
    f = open("customers.txt", "r")
    for line in f:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            customers.append({
                "id": int(parts[0]),
                "name": parts[1],
                "phone": parts[2]
            })
    f.close()
    return customers


def write_customers(customers):
    f = open("customers.txt", "w")
    for c in customers:
        line = str(c["id"]) + "," + c["name"] + "," + c["phone"] + "\n"
        f.write(line)
    f.close()


def read_bookings():
    bookings = []
    f = open("bookings.txt", "r")
    for line in f:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            bookings.append({
                "cust_id": int(parts[0]),
                "room_no": parts[1],
                "days": int(parts[2]),
                "total": float(parts[3])
            })
    f.close()
    return bookings


def write_bookings(bookings):
    f = open("bookings.txt", "w")
    for b in bookings:
        line = str(b["cust_id"]) + "," + b["room_no"] + "," + str(b["days"]) + "," + str(b["total"]) + "\n"
        f.write(line)
    f.close()


# ----------------------------------
# Core operations
# ----------------------------------
def add_customer():
    customers = read_customers()
    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    cust_id = len(customers) + 1
    customers.append({"id": cust_id, "name": name, "phone": phone})
    write_customers(customers)
    print("Customer added with ID: " + str(cust_id))


def show_customers():
    customers = read_customers()
    if len(customers) == 0:
        print("No customers found.")
        return
    print("\nCustomer List:")
    for c in customers:
        print("ID: " + str(c["id"]) + " | Name: " + c["name"] + " | Phone: " + c["phone"])


def show_rooms():
    rooms = read_rooms()
    print("\nRooms List:")
    for r in rooms:
        print("Room " + r["number"] + " - " + r["type"] + " - ₹" + str(r["rate"]) + " - " + r["status"])


def book_room():
    customers = read_customers()
    if len(customers) == 0:
        print("Add a customer first.")
        return

    show_customers()
    cust_id = int(input("Enter customer ID: "))

    rooms = read_rooms()
    show_rooms()
    room_no = input("Enter room number to book: ")

    for r in rooms:
        if r["number"] == room_no:
            if r["status"] != "Available":
                print("Room is already booked!")
                return
            days = int(input("Enter number of days: "))
            total = r["rate"] * days
            bookings = read_bookings()
            bookings.append({
                "cust_id": cust_id,
                "room_no": room_no,
                "days": days,
                "total": total
            })
            r["status"] = "Booked"
            write_rooms(rooms)
            write_bookings(bookings)
            print("Room " + room_no + " booked successfully for " + str(days) + " days. Total = ₹" + str(total))
            return
    print("Invalid room number!")


def view_bookings():
    bookings = read_bookings()
    customers = read_customers()
    if len(bookings) == 0:
        print("No bookings found.")
        return

    print("\nAll Bookings:")
    for b in bookings:
        cust_name = ""
        for c in customers:
            if c["id"] == b["cust_id"]:
                cust_name = c["name"]
        print("Customer: " + cust_name + " | Room: " + b["room_no"] + " | Days: " + str(b["days"]) + " | Total: ₹" + str(b["total"]))


def checkout():
    bookings = read_bookings()
    rooms = read_rooms()
    room_no = input("Enter room number to checkout: ")

    for b in bookings:
        if b["room_no"] == room_no:
            for r in rooms:
                if r["number"] == room_no:
                    r["status"] = "Available"
            print("Room " + room_no + " checked out successfully. Bill Amount: ₹" + str(b["total"]))
            bookings.remove(b)
            write_rooms(rooms)
            write_bookings(bookings)
            return
    print("No booking found for this room!")


# ----------------------------------
# Main menu
# ----------------------------------
def menu():
    initialize_files()

    while True:
        print("\n--- HOTEL BOOKING MENU ---")
        print("1. Add Customer")
        print("2. Show Customers")
        print("3. Show Rooms")
        print("4. Book Room")
        print("5. View Bookings")
        print("6. Checkout")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            show_customers()
        elif choice == "3":
            show_rooms()
        elif choice == "4":
            book_room()
        elif choice == "5":
            view_bookings()
        elif choice == "6":
            checkout()
        elif choice == "7":
            print("Thank you for using Hotel Booking System!")
            break
        else:
            print("Invalid choice. Try again.")


# Run program
menu()
