class UserInfo:
    def __init__(self):
        pass
    def info(self,row,clm,database):
        for user in database:
            if user['seat_row_num'] == row and user['seat_clm_num']==clm:
                print("Name: ",user['name'])
                print("Gender: ",user['gender'])
                print("Age: ",user['age'])
                print("Ticket Price: ",user['seat_price'])
                print("Phone No: ",user['phone_no'])
                break