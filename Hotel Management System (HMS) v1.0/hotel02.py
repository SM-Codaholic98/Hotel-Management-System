import pickle

htl={}
rest={}

def INSERT_GUEST_ROOM_CUM_REST_REC():
    f=open('HMS_GUEST_ROOM_REC.dat','rb')
    htl={}
    while True:
        try:
            htl=pickle.load(f)
        except EOFError:
            break
    f.close()
    
    print(htl)
    
    f=open('HMS_GUEST_ROOM_CUM_REST_REC.dat','wb')
    ans='i'
    while ans.lower()=='i':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& INSERT GUEST'S ROOM CUM RESTAURANT RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        g_id=int(input("Enter the ID number of the guest to insert the guest's room cum restaurant record: "))
        found=False      
        for j in htl:
            if j==g_id:
                found=True
                
                rest[g_id]=[0]
                pickle.dump(rest,f)
        
        if found==False:
            print("*** GUEST'S ROOM CUM RESTAURANT RECORD HAS NOT BEEN INSERTED !!! ***") 
            print("--> Please provide the correct ID number of the guest to store the guest's room cum restaurant record __/\__")
        else:
            print("*** GUEST'S ROOM CUM RESTAURANT RECORD HAS BEEN SUCCESSFULLY INSERTED !!! ***")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print()
        ans=input("Press 'i/I' to insert more guest's room cum restaurant record: ")
        print()
    f.close()
    
    
def COMPUTE_GUEST_REST_BILL():
    f=open('HMS_GUEST_ROOM_CUM_REST_REC.dat','rb+')
    rest={}
    while True:
        try:
            rest=pickle.load(f)
        except EOFError:
            break
    
    ans='c'
    while ans.lower()=='c':
        ID=int(input("Enter the ID number of the guest to compute the guest's restaurant record: "))
        found=False      
        for j in rest:
            if j==ID:
                found=True
                
                ans='y'
                while ans.lower()=='y':    
                    print("-------------------------------------------------------------------------")
                    print("						 HOTEL PYCODE INTERNATIONAL")
                    print("-------------------------------------------------------------------------")
                    print("						MENU CARD")
                    print("-------------------------------------------------------------------------")
                    print("\n BEVARAGES							 26 Dal Fry................ 140.00")
                    print("----------------------------------	 27 Dal Makhani............ 150.00")
                    print(" 1 Regular Tea............. 20.00	 28 Dal Tadka.............. 150.00")
                    print(" 2 Masala Tea.............. 25.00")
                    print(" 3 Coffee.................. 25.00	 ROTI")
                    print(" 4 Cold Drink.............. 25.00	 ----------------------------------")
                    print(" 5 Bread Butter............ 30.00	 29 Plain Roti.............. 15.00")
                    print(" 6 Bread Jam............... 30.00	 30 Butter Roti............. 15.00")
                    print(" 7 Veg. Sandwich........... 50.00	 31 Tandoori Roti........... 20.00")
                    print(" 8 Veg. Toast Sandwich..... 50.00	 32 Butter Naan............. 20.00")
                    print(" 9 Cheese Toast Sandwich... 70.00")
                    print(" 10 Grilled Sandwich........ 70.00	 RICE")
                    print("									 ----------------------------------")
                    print(" SOUPS								 33 Plain Rice.............. 90.00")
                    print("----------------------------------	 34 Jeera Rice.............. 90.00")
                    print(" 11 Tomato Soup............ 110.00	 35 Veg Pulao.............. 110.00")
                    print(" 12 Hot & Sour............. 110.00	 36 Peas Pulao............. 110.00")
                    print(" 13 Veg. Noodle Soup....... 110.00")
                    print(" 14 Sweet Corn............. 110.00	 SOUTH INDIAN")
                    print(" 15 Veg. Munchow........... 110.00	 ----------------------------------")
                    print("									 37 Plain Dosa............. 100.00")
                    print(" MAIN COURSE						 38 Onion Dosa............. 110.00")
                    print("----------------------------------	 39 Masala Dosa............ 130.00")
                    print(" 16 Shahi Paneer........... 110.00	 40 Paneer Dosa............ 130.00")
                    print(" 17 Kadai Paneer........... 110.00	 41 Rice Idli.............. 130.00")
                    print(" 18 Handi Paneer........... 120.00	 42 Sambhar Vada........... 140.00")
                    print(" 19 Palak Paneer........... 120.00")
                    print(" 20 Chilli Paneer.......... 140.00	 ICE CREAM")
                    print(" 21 Matar Mushroom......... 140.00	 ----------------------------------")
                    print(" 22 Mix Veg................ 140.00	 43 Vanilla................. 60.00")
                    print(" 23 Jeera Aloo............. 140.00	 44 Strawberry.............. 60.00")
                    print(" 24 Malai Kofta............ 140.00	 45 Pineapple............... 60.00")
                    print(" 25 Aloo Matar............. 140.00	 46 Butter Scotch........... 60.00")
                    print()
                    ch=int(input("Enter the menu number choosen by the guest: "))
                    qt=eval(input("Enter the quantity: "))
                    if ch==1 or ch==31 or ch==32:
                        rs=20*qt
                        rest[j][0]=rest[j][0]+rs
                    elif ch<=4 and ch>=2:
                        rs=25*qt
                        rest[j][0]=rest[j][0]+rs
                    elif ch<=6 and ch>=5:
                        rs=30*qt
                        rest[j][0]=rest[j][0]+rs
                    elif ch<=8 and ch>=7:
                        rs=50*qt
                        rest[j][0]=rest[j][0]+rs
                    elif ch<=10 and ch>=9:
                        rs=70*qt
                        rest[j][0]=rest[j][0]+rs
                    elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
                        rs=110*qt
                        rest[j][0]=rest[j][0]+rs
                    elif ch<=19 and ch>=18:
                        rs=120*qt
                        rest[j][0]=rest[j][0]+rs
                    elif (ch<=26 and ch>=20) or ch==42:
                        rs=140*qt
                        rest[j][0]=rest[j][0]+rs
                    elif ch<=28 and ch>=27:
                        rs=150*qt
                        rest[j][0]=rest[j][0]+rs
                    elif ch<=30 and ch>=29:
                        rs=15*qt
                        rest[j][0]=rest[j][0]+rs
                    elif ch==33 or ch==34:
                        rs=90*qt
                        rest[j][0]=rest[j][0]+rs
                    elif ch==37:
                        rs=100*qt
                        rest[j][0]=rest[j][0]+rs
                    elif ch<=41 and ch>=39:
                        rs=130*qt
                        rest[j][0]=rest[j][0]+rs
                    elif ch<=46 and ch>=43:
                        rs=60*qt
                        rest[j][0]=rest[j][0]+rs
                    else:
                        print()
                        print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
                        print("--> Please provide the appropriate menu number __/\__")
                    
                    pickle.dump(rest,f)
                    print()
                    ans=input("Press 'y/Y' to add more menu: ")
                    print()
                    
        if found==False:
            print("*** GUEST'S RESTAURANT RECORD HAS NOT BEEN FOUND !!! ***")
            print("--> Please provide the correct ID number of the guest to compute the guest's restaurant record __/\__")
        
        print()
        ans=input("Press 'c/C' to compute more guest's restaurant record: ")
        print()
    f.close()
    

def DISP_GUEST_ROOM_CUM_REST_BILL():
    f=open('HMS_GUEST_ROOM_REC.dat','rb')
    htl={}
    while True:
        try:
            htl=pickle.load(f)
        except EOFError:
            break
    f.close()
    
    f=open('HMS_GUEST_ROOM_CUM_REST_REC.dat','rb')
    rest={}
    while True:
        try:
            rest=pickle.load(f)
        except EOFError:
            break
        
    ans='d'
    while ans.lower()=='d':
        ID=int(input("Enter the ID number of the guest to display the Guest's ROOM CUM RESTAURANT BILL: "))
        found=False
        for id in rest:
            if id==ID:
                found=True
                print()
                print("-------------------------------------------------------------------")
                print("%%%%%%%%%%%%%%%%%%%%%% GUEST'S ROOM CUM RESTAURANT BILL %%%%%%%%%%%%%%%%%%%%%%")
                print("-------------------------------------------------------------------")
                print("Guest's Unique ID Number: ",id)
                print("Guest's Full Name: ",htl[id][0],htl[id][1])
                print("Guest's age: ",htl[id][2])
                print("Guest's Sex: ",htl[id][12])
                print("Guest's Phone Number: +91",htl[id][3])
                print("Guest's Aadhaar Number: ",htl[id][14])
                print("Guest's Email Address: ",htl[id][4])
                print("Guest's House Address: ",htl[id][5])
                print("Guest's Check-in Date: ",htl[id][6])
                print("Guest's Check-out Date: ",htl[id][7])
                print("Total Number Of Days: ",htl[id][11])
                print("Total Number Of Persons: ",htl[id][9])
                print("Guest's Room Type: ",htl[id][8])
                print("Total Number Of Rooms: ",htl[id][15])
                print("Guest's Room Number: ",htl[id][13])
                print("Guest's Room Charges: Rs.",htl[id][10])
                print("Room SGST 9% : Rs.",htl[id][10]*0.09)
                print("Room CGST 9% : Rs.",htl[id][10]*0.09)
                print("Total Room Charges (Inclusive all taxes): Rs.",htl[id][10]*0.18)
                print("Guest's Restaurant Charges: Rs.",rest[id][0])
                print("Restaurant SGST 9% : Rs.",rest[id][0]*0.09)
                print("Restaurant CGST 9% : Rs.",rest[id][0]*0.09)
                print("Total Restaurant Charges (Inclusive all taxes): Rs.",rest[id][0]*0.18)
                print("Total amount to be paid by the guest: Rs.",htl[id][10]+(htl[id][10]*0.18)+rest[id][0]+(rest[id][0]*0.18))
                print("----------------------------------------------------------------")
                print()
                
        if found==False:
            print("*** GUEST'S ROOM CUM RESTAURANT RECORD HAS NOT BEEN FOUND !!! ***")
            print("--> Please provide the correct ID number of the guest to display the Guest's ROOM CUM RESTAURANT BILL __/\__")
        
        print()
        ans=input("Press 'd/D' to display more Guest's ROOM CUM RESTAURANT BILL: ")
        print()
    f.close()
    

def APPEND_GUEST_ROOM_CUM_REST_REC():
    f=open('HMS_GUEST_ROOM_REC.dat','rb')
    htl={}
    while True:
        try:
            htl=pickle.load(f)
        except EOFError:
            break
    f.close()
    
    print(htl)
    
    f=open('HMS_GUEST_ROOM_CUM_REST_REC.dat','ab')
    ans='a'
    while ans.lower()=='a':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& APPEND GUEST'S ROOM CUM RESTAURANT RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        g_id=int(input("Enter the ID number of the guest to append the guest's room cum restaurant record: "))
        found=False      
        for j in htl:
            if j==g_id:
                found=True
                
                rest[g_id]=[0]
                pickle.dump(rest,f)
        
        if found==False:
            print("*** GUEST'S ROOM CUM RESTAURANT RECORD HAS NOT BEEN APPENDED !!! ***") 
            print("--> Please provide the correct ID number of the guest to store the guest's room cum restaurant record __/\__")
        else:
            print("*** GUEST'S ROOM CUM RESTAURANT RECORD HAS BEEN SUCCESSFULLY APPENDED !!! ***")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print()
        ans=input("Press 'a/A' to append more guest's room cum restaurant record: ")
        print()
    f.close()
    
    
def SEARCH_GUEST_ROOM_CUM_REST_REC():
    f=open('HMS_GUEST_ROOM_CUM_REST_REC.dat','rb')
    rest={}
    while True:
        try:
            rest=pickle.load(f)
        except EOFError:
            break
        
    ans='s'
    while ans.lower()=='s':
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("########################################################### SEARCH GUEST'S ROOM CUM RESTAURANT RECORD ###########################################################")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     ID=int(input("Enter the ID number of the guest to search the guest's room cum restaurant record: "))
     found=False      
     for j in rest:
        if j==ID:
            print("--x--x-- Provided ID number of the guest is present in the database ...@ Press 7 to display the Guest's ROOM CUM RESTAURANT BILL --x--x--")
            found=True
            break
        
     if found==False:
        print("*** GUEST'S ROOM CUM RESTAURANT RECORD HAS NOT BEEN FOUND !!! ***") 
        print("--> Please provide the correct ID number of the guest to search the guest's room cum restaurant record __/\__")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
     print()
     ans=input("Press 's/S' to search more guest's room cum restaurant record: ")
     print()
    f.close()
    
    
def DEL_GUEST_REST_REC():
    REST={}
    f=open('HMS_GUEST_ROOM_CUM_REST_REC.dat','rb+')
    while True:
        try:
            rest=pickle.load(f)
        except EOFError:
            break
        
    ans='r'
    while ans.lower()=='r':
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("################################################ DELETE GUEST'S RESTAURANT RECORD ################################################")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     ID=int(input("Enter the ID number of the guest, to be search and to delete or remove the guest's restaurant record: "))
     found=False
     for k in rest:
        if k!=ID:
            found=True
            REST[k]=rest[k]
            pickle.dump(REST,f)
            
     if found==False:
        print("*** GUEST'S RESTAURANT RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the guest to delete or remove the guest's restaurant record __/\__")
     else:
        print("*** GUEST'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY DELETED !!! ***")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
     print()
     ans=input("Press 'r/R' to delete or remove more guest's restaurant record: ")
     print()
    f.close()


def DISP_ALL_GUEST_ROOM_CUM_REST_REC():
    f=open('HMS_GUEST_ROOM_CUM_REST_REC.dat','rb')
    rest={}
    while True:
        try:
            rest=pickle.load(f)
        except EOFError:
            break
    print(rest)
    f.close()