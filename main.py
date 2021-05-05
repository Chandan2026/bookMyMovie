from showTheSeats import ShowSeats
from buyTicket import BuyTicket
from statistics import Statistics
from userInfo import UserInfo

class Main:
    def __init__(self, rows, columns):
        self.rows=rows
        self.columns=columns
        self.seats=[["S" for j in range(self.columns)]for i in range(self.rows)]
        self.database=[]

    def showMainMenu(self):
        print("1.Show the seats")
        print("2.Buy a Ticket")
        print("3.Statistics")
        print("4.Show booked Ticket User info")
        print("0.Exit")

    def askPreferSeat(self):
        preferred_row=int(input("\nEnter row number: "))
        if preferred_row-1 >= self.rows:
            while preferred_row-1 >= self.rows:
                preferred_row=int(input("\nEnter valid row number: "))
        preferred_clm=int(input("Enter column number: "))
        if preferred_clm-1 >= self.columns:
            while preferred_clm-1 >= self.columns:
                preferred_clm=int(input("\nEnter valid column number: "))
        if self.seats[preferred_row-1][preferred_clm-1] == "B":
            print("Sorry the seat is already booked. Please choose another one...")
            self.askPreferSeat()
        return [preferred_row,preferred_clm]

    def main(self):
        ch=True
        while ch:
            print("\nChoose...")
            self.showMainMenu()
            opt=int(input("\n"))
            if opt not in range(5):
                while opt not in range(5):
                    opt=int(input("Please enter correct option: "))

            if opt == 0:
                ch=False
            elif opt == 1:
                s = ShowSeats()
                s.show(self.seats)
            elif opt == 2:
                preferred_row,preferred_clm=self.askPreferSeat()

                bt= BuyTicket()
                seat_price = bt.determine_seat_price(self.rows, self.columns, preferred_row)
                proceed_to_book = input("\nThe seat price is {}$. Want to proceed(Y/n): ".format(seat_price))

                if proceed_to_book.lower() in ['y','yes']:
                    bt.buy(preferred_row,preferred_clm,seat_price,self.database, self.seats)
                else:
                    continue
            elif opt == 3:
                s=Statistics()
                s.stats(self.database,self.seats)
            else:
                row=int(input("Enter row: "))
                clm=int(input("Enter column: "))
                user=UserInfo()
                user.info(row,clm,self.database)
                

if __name__=="__main__":
    rows=int(input("\nEnter the number of rows: "))
    columns=int(input("Enter the number of seats in each row: "))
    m=Main(rows,columns)
    m.main()