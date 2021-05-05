class Statistics:
    def __init__(self):
        pass
    def stats(self, database, seats):
        print("Number of purchased tickets: ",len(database))
        print("Percentage: ",(len(database)/(len(seats)*len(seats[0])))*100)
        current_income=0
        for i in database:
            current_income += i['seat_price']
        print("Current Income: ",current_income)

        total_income = 0
        total_seats=len(seats)*len(seats[0])
        if total_seats<=60:
            total_income = total_seats*10
        else:
            total_income = ((len(seats)//2)*10*len(seats[0])) + ((len(seats)-(len(seats)//2))*8*len(seats[0]))
        print("Total Income: ",total_income)