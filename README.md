# Backend for a Simple Event Booking System 
The system will have two types of users: Event Organisers and Customers.

Event Organisers should be able to create, read, and update events, while Customers should be able to book tickets for these events.

The API access should be restricted based on the user role.

#Core Functionalities

System Setup (Python, Django, Django Rest Framework) 
Initialise a new Django project. 
Set up Django Rest Framework for RESTful APIs.

Database Design Tables:
*EventOrganizers: Information about the event organisers. 
*Customers: Information about customers. 
*Events: Information about each event, including date, venue, and organiser. 
*Tickets: Types of tickets available for each event, including pricing and availability. 
*Bookings: Information about ticket bookings by customers.

Relationships: 
*An Event Organiser can create multiple Events.
*An Event can have multiple Ticket types (General Admission, VIP, etc.). 
*A Customer can make multiple Bookings. 
*A Booking will relate to a single Event and specific Ticket types.

User Authentication and Role-based API Access 
*Create a user login and signup feature using OAuth 2.0 
*Implement authentication for two roles: Event Organisers and Customers. 
*Restrict API access based on the role. Only Event Organizers should be able to create, read and update events, and only Customers should be able to make bookings. 

Efficient and Scalable APIs
*Event Management: 
APIs to create, read, update, and delete events. 
*Booking API: 
Allow customers to book tickets.

Asynchronous Tasks (Celery, Redis) 
*Implement a simple Celery task to send email confirmations when a ticket is booked. In the scope of this assignment, an actual email need not be sent; a print statement stating that an email will be sent inside the celery task will suffice. 
*Implement another simple Celery task to send email notifications to those Customers who have booked tickets for an event that gets updated. Again, a print statement is sufficient for the scope of this assignment.

Documentation and Unit Tests 
*Documentation: Document the codebase for maintainability. 
*Unit Tests: Write a unit test for the ticket booking process covering all of the business logic.
