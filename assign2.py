#Day 19(29-09-2026)
# Assignment 2 – Movie Ticket Booking

# Build a complete movie ticket booking program using functions for every operation: listing available shows, booking seats, calculating the total price (including any applicable discounts), and cancelling a booking.
# Requirements:
# •	Write a function list_shows() that displays available movies, show timings, and ticket prices using a list/dictionary of show data. 
# •	Write a function book_tickets(show_name, number_of_tickets, *seat_numbers) that uses variable-length arguments (*args) to accept any number of seat numbers. 
# •	Write a function calculate_total(price, quantity, discount=0) using a default argument for optional discounts. Apply the following payment-based pricing: 
# 	               - GPay : Add ₹30 convenience fee. 
# 	               - Credit Card : Apply 30% discount. 
# 	               - Cash : Use the normal ticket price of ₹230 per ticket. 
# •	Write a recursive function to calculate the total bill when a loyalty combo offer applies cumulative discounts for every 2 tickets booked. 
# •	Write a cancel_booking() function that reverses a booking and issues a refund amount using the same pricing function. 
# •	Tie all functions together in a menu-driven program that lets the user book, view, and cancel tickets.



shows = [
    ["Leo", "10:00 AM", 230],
    ["Vikram", "2:00 PM", 230],
    ["KGF", "6:00 PM", 230]
]

booking = []


def list_shows():
    print("\nAvailable Shows")

    for show in shows:
        print(show[0], "-", show[1], "- Rs", show[2])


def book_tickets(show_name, number_of_tickets, *seat_numbers):

    price = 230

    print("\nPayment Method")
    print("1. GPay")
    print("2. Credit Card")
    print("3. Cash")

    choice = int(input("enter choice: "))

    if choice == 1:
        total = calculate_total(price, number_of_tickets)
        total = total + 30

    elif choice == 2:
        total = calculate_total(price, number_of_tickets, 30)

    elif choice == 3:
        total = calculate_total(price, number_of_tickets)

    else:
        print("invalid choice")
        return

    discount = loyalty_discount(number_of_tickets)
    total = total - (total * discount / 100)

    booking.append([show_name, number_of_tickets, seat_numbers, total])

    print("\nBooking Successful")
    print("Movie:", show_name)
    print("Seats:", seat_numbers)
    print("Total Amount: Rs", total)


def calculate_total(price, quantity, discount=0):

    total = price * quantity
    total = total - (total * discount / 100)

    return total


def loyalty_discount(tickets):

    if tickets < 2:
        return 0

    return 5 + loyalty_discount(tickets - 2)


def cancel_booking():

    movie = input("enter movie name: ")

    for book in booking:

        if book[0] == movie:

            refund = calculate_total(230, book[1])

            print("\nBooking Cancelled")
            print("Refund Amount: Rs", refund)

            booking.remove(book)
            return

    print("Booking not found")


def view_booking():

    if len(booking) == 0:
        print("\nNo booking found")

    else:
        print("\nYour Booking")

        for book in booking:
            print("Movie:", book[0])
            print("Tickets:", book[1])
            print("Seats:", book[2])
            print("Total: Rs", book[3])


def main():

    while True:

        print("\n----- MOVIE TICKET BOOKING -----")
        print("1. List Shows")
        print("2. Book Tickets")
        print("3. View Booking")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            list_shows()

        elif choice == 2:

            list_shows()

            movie = input("Enter movie name: ")
            tickets = int(input("Enter number of tickets: "))

            seats = []

            for i in range(tickets):
                seat = int(input("Enter seat number: "))
                seats.append(seat)

            book_tickets(movie, tickets, *seats)

        elif choice == 3:
            view_booking()

        elif choice == 4:
            cancel_booking()

        elif choice == 5:
            print("Thank you!")
            break

        else:
            print("Invalid choice")


main()