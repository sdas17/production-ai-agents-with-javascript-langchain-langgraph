# # object oritention programming
# # self is object reference of object
# class Point():
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
        
# p=Point(2,9)
# print(p.x,p.y)

# we have make it flight reserveration system one application we make it  
# we have make it application we have total seat 
#Method to create new flight with given capacity
# Method to add a passenger to the flight:
# check capacity
class Bookig_flight_reservation():
        def __init__(self, capacity):
            self.capacity=capacity
            self.pasenger_list =[]

        def added_passenger(self,name):
            if not self.open_seats():
                return False
            else:
                 self.pasenger_list.append(name)
                 return True
        def open_seats(self):
                return self.capacity-len(self.pasenger_list)

flight_reservation=Bookig_flight_reservation(3)

customer_list =['Rahul','Ram','santosh','sohil']
for person in customer_list:
    if flight_reservation.added_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")
    

