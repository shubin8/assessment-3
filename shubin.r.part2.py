#K.I.S.S(keep it simple,stupid) I use this method to keep my code simple
Booking_counter = 10000
# booking system
class BookingSystem:
    booking=[]
    def __init__(self):
        global Booking_counter
        #use global counter to make every booking diffrent.
        booking_counter +=1
        #input all the varibles.
        self.form_of_id="form_of_id"
        self.id_number="id_number"
        self.passenger_name="passenger_name"
        self.booking_id=Booking_counter
        self.total=0
        self.service=[]
        self.status="pending"
        self.approval_ref=None
        BookingSystem.Booking.append(self)

#custmer_info
    def customer_info(self):
        #collecting information from customers.
        self.form_of_id=input("Enter your form of id(passport,drive's license):")
        self.id.number=input("Enter your id number:")
        #Enter id.number instead of id_number.
        self.passenger_name=input("Enter the passenger name:")

#ferry_service_details
    def ferry_service_details(self):
        #collecting the services and prices of them.
        #use while to loop until customer type done.
        while True:
            service_name= input("passenger name (or type 'done' to finish): ")
            if service_name.lower() == "done":
                break
        while True:
            service_price = float(input(f"Enter price for {service_name}: $"))
            self.service.append((service_name, service_price))
            total += service_price
            break

#booking_approval
    def booking_approval(self):
        #making the decison to approve, not approved and pending the customers booking 
        if self.status == "Pending":
            decision = input(f"Booking {self.booking_id} is pending. Approve or Not approved? ")
            if decision.lower() == "approved":
                self.status = "Approved"
            if decision.lower() == "not approved":
                self.status = "Not approved"   

#display_booking_info
    def display_booking_info(self):
        #print all the varibles.
        print("\nBooking info")
        print(f"Form_of_id: {self.form_of_id}")
        print(f"Id_number: {self.id_number}")
        print(f"passenger_name: {self.passenger_name}")
        print(f"Booking_id: {Booking_counter}")
        print(f"Total: {self.total}")
        print(f"service: {self.service}")
        print(f"status: {self.status}")
        print(f"approval_ref {self.approval_ref}")

#booking_statistic
    def booking_statistic(self):
        #collect the statistic varibles.
        self.total=(self.total)
        approved = 0
        pending = 0
        not_approved = 0

        for self in self.booking: 
            if self.status == "Approved":
                approved += 1
            if self.status =="Pending":
                pending += 1
            if self.status =="not_approved":
                not_approved +=1

#print the output of statistic
        print("\nStatistics")
        print(f"Total booking: {self.total}")
        print(f"Approved: {approved}")
        print(f"Pending: {pending}") 
        print(f"Not approved: {not_approved}")

    if __name__ == "__main__":
        num=int(input("How many tickets do you want guys?"))
        #loop how many time the user'num'
        for book in range(num):
            book = BookingSystem()
            book.customer_info()
            book.ferry_service_details()
            book.booking_approval()
            book.display_booking_info()

#display all the things
        for book in booking.BookingSystem:
            book.display_booking()  