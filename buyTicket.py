class BuyTicket:

    def __init__(self):
        pass

    def determine_seat_price(self, rows, columns, preferred_row):
        total_seats=rows*columns
        if total_seats <= 60:
            return 10
        else:
            if preferred_row <= (rows//2):
                return 10
            else:
                return 8


    def buy(self, preferred_row, preferred_clm, seat_price, database, seats):
        tmp={}
        print("\nFill Details -")
        tmp['name'] = input("Name: ")
        tmp['gender'] = input("Gender: ")
        tmp['age'] = input("Age: ")
        tmp['phone_no'] = input("Phone No: ")
        tmp['seat_row_num']=preferred_row
        tmp['seat_clm_num']=preferred_clm
        tmp['seat_price']=seat_price
        database.append(tmp)
        seats[preferred_row-1][preferred_clm-1]="B"
        print("Booked Successfully.")

# if __name__=="__main__":
#     b=BuyTicket()
#     b.buy(10,12,5,2)