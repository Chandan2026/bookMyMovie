class ShowSeats:
    def __init__(self):
        pass

    def show(self, seats):
        print("\nCinema:\n\n********************************\n")
        for i in seats:
            for j in i:
                print(j,end=" ")
            print()
        print("\n********************************\n")

# if __name__=="__main__":
#     s=ShowSeats()
#     s.show(4,5)