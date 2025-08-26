class TicketSeller:
    def __init__(self, total_tickets=20, ticket_limit_per_buyer=4):
        self.total_tickets = total_tickets
        self.ticket_limit = ticket_limit_per_buyer
        self.total_buyers = 0

    def sell_tickets(self):
        print(f"Welcome! There are {self.total_tickets} tickets available.")
        while self.total_tickets > 0:
            try:
                user_input = input(f"Enter number of tickets to buy (1 to {self.ticket_limit}), or 'q' to quit: ").strip()
                if user_input.lower() == 'q':
                    print("Exiting ticket sales. Have a nice day!")
                    break
                tickets_requested = int(user_input)
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")
                continue

            if tickets_requested < 1 or tickets_requested > self.ticket_limit:
                print(f"Invalid number of tickets. You can buy between 1 and {self.ticket_limit} tickets at a time.")
                continue

            if tickets_requested > self.total_tickets:
                print(f"Sorry, only {self.total_tickets} tickets are left.")
                continue

            # Process purchase
            self.total_tickets -= tickets_requested
            self.total_buyers += 1
            print(f"Successfully purchased {tickets_requested} ticket(s).")
            print(f"Tickets remaining: {self.total_tickets}")

        if self.total_tickets == 0:
            print(f"All tickets sold! Total buyers: {self.total_buyers}")

def main():
    seller = TicketSeller(total_tickets=20, ticket_limit_per_buyer=4)
    seller.sell_tickets()

if __name__ == "__main__":
    main()
