
# Event Ticketing System

A simple interactive ticket selling system written in Python. This script simulates a basic ticket booth where users can purchase tickets with constraints on the maximum number per buyer.

## Features

* Set a total number of tickets available for sale
* Limit the number of tickets each buyer can purchase in a single transaction
* Input validation for ticket purchase requests
* Tracks the number of buyers
* Graceful exit with `'q'` input
* Real-time feedback on ticket availability and successful transactions

## How It Works

* The program starts by displaying the total available tickets
* It prompts the user to enter the number of tickets they want to purchase (up to a set limit)
* It validates the input:

  * Must be an integer within the allowed range
  * Must not exceed the remaining tickets
* If the purchase is valid:

  * The ticket count is reduced
  * The number of buyers is incremented
  * A success message is printed
* The loop continues until:

  * All tickets are sold
  * The user chooses to quit by entering `'q'`

## Sample Interaction

Welcome! There are 20 tickets available.
Enter number of tickets to buy (1 to 4), or 'q' to quit: 3
Successfully purchased 3 ticket(s). Tickets remaining: 17


All tickets sold!
Total buyers: 7

## Code Overview

**TicketSeller class**

**def **init**(self, total\_tickets=20, ticket\_limit\_per\_buyer=4)**

* `total_tickets`: Total number of tickets available for sale
* `ticket_limit_per_buyer`: Maximum number of tickets one user can buy in a single purchase

**sell\_tickets() method**

* Handles the entire ticket-selling logic through a command-line interface

**main() function**

* Initializes a `TicketSeller` instance and starts the selling process

---
