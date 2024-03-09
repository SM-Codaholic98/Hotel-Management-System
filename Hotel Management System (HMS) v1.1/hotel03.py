import pickle, random
from datetime import datetime

cust={}

def INSERT_CUST_REST_REC():
    f=open('HMS_CUST_REST_REC.dat','wb')
    ans='i'
    while ans.lower()=='i':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& INSERT CUSTOMER'S RESTAURANT RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        c_id=random.randint(10000,99999)
        c_t=input("Enter the customer's Title as either Mr, Ms, Mrs or Mx: ").capitalize()
        c_n=input("Enter the customer's Full Name: ")
        print("ID Number of",c_t,c_n,"is: ",c_id)
        c_sex=input("Enter the customer's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
        c_email=input("Enter the customer's Email Address: ")
        
        print()
        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) \\")
        c_phno=int(input("Enter the customer's Mobile/Phone Number: +91 "))
        print()
        
        found_title=False
        found_sex=False
        found_email=False
        found_phno=False
        
        if len(str(c_phno))==10:
            cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
            found_phno=True
        else:
            print()
            print("~~~ Invalid mobile/phone number of the customer has been entered !!! ~~~")
            print("--> Please provide the valid mobile/phone number of the customer to store the customer's details __/\__")
            print()
            print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) \\")
            c_phno=int(input("Enter the customer's Mobile/Phone Number: +91 "))
            if len(str(c_phno))==10:
                cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
                found_phno=True
            else:
                print()
                found_phno=False
                print("~~~ Invalid mobile/phone number of the customer has been entered !!! ~~~")
        
        if c_t=='Mr' or c_t=='Ms' or c_t=='Mrs' or c_t=='Mx':
            cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
            found_title=True
        else:
            print()
            print("~~~ Invalid title of the customer has been entered !!! ~~~")
            print("--> Please provide the valid title of the customer to store the customer's details __/\__")
            print()
            c_t=input("Enter the customer's Title as either Mr, Ms or Mrs: ").capitalize()
            if c_t=='Mr' or c_t=='Ms' or c_t=='Mrs' or c_t=='Mx':
                cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
                found_title=True
            else:
                print()
                found_title=False
                print("~~~ Invalid title of the customer has been entered !!! ~~~") 
                
        if c_sex=='MALE' or c_sex=='FEMALE' or c_sex=='THIRD GENDER' or c_sex=='M' or c_sex=='F' or c_sex=='TG' :
            cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
            found_sex=True
        else:
            print()
            print("~~~ Invalid sex of the customer has been entered !!! ~~~")
            print("--> Please provide the valid sex of the customer to store the customer's details __/\__")
            print()
            c_sex=input("Enter the customer's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
            if c_sex=='MALE' or c_sex=='FEMALE' or c_sex=='THIRD GENDER' or c_sex=='M' or c_sex=='F' or c_sex=='TG' :
                cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
                found_sex=True
            else:
                print()
                found_sex=False
                print("~~~ Invalid sex of the customer has been entered !!! ~~~")        
                
        if '@' and '.com' in c_email:
            cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
            found_email=True
        else:
            print()
            print("~~~ Customer's email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the customer to store the customer's details __/\__")
            print()
            c_email=input("Enter the customer's Email Address: ")
            if '@' and '.com' in c_email:
                cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
                found_email=True
            else:
               print()
               found_email=False
               print("~~~ Customer's email address doesn't contain '@' or '.com' !!! ~~~")
        
        
        if found_title==True and found_sex==True and found_email==True and found_phno==True:
            pickle.dump(cust,f)
            print()
            print("*** CUSTOMER'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY INSERTED !!! ***")
        else:
            print()
            print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN INSERTED !!! ***")
            print("--> something went wrong in provided data, please provide the proper data of the customer to store the customer's restaurant record __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print()
        ans=input("Press 'i/I' to insert more customer's restaurant record: ")
        print()
    f.close()
    
    
def APPEND_CUST_REST_REC():
    f=open('HMS_CUST_REST_REC.dat','rb')
    cust={}
    while True:
        try:
            cust=pickle.load(f)
        except EOFError:
            break
    f.close()
    
    f=open('HMS_CUST_REST_REC.dat','ab')
    ans='a'
    while ans.lower()=='a':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& APPEND CUSTOMER'S RESTAURANT RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        c_id=random.randint(10000,99999)
        c_t=input("Enter the customer's Title as either Mr, Ms, Mrs or Mx: ").capitalize()
        c_n=input("Enter the customer's Full Name: ")
        print("ID Number of",c_t,c_n,"is: ",c_id)
        c_sex=input("Enter the customer's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
        c_email=input("Enter the customer's Email Address: ")
        
        print()
        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) \\")
        c_phno=int(input("Enter the customer's Mobile/Phone Number: +91 "))
        print()
        
        found_title=False
        found_sex=False
        found_email=False
        found_phno=False
        
        if len(str(c_phno))==10:
            cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
            found_phno=True
        else:
            print()
            print("~~~ Invalid mobile/phone number of the customer has been entered !!! ~~~")
            print("--> Please provide the valid mobile/phone number of the customer to store the customer's details __/\__")
            print()
            print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) \\")
            c_phno=int(input("Enter the customer's Mobile/Phone Number: +91 "))
            if len(str(c_phno))==10:
                cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
                found_phno=True
            else:
                print()
                found_phno=False
                print("~~~ Invalid mobile/phone number of the customer has been entered !!! ~~~")
        
        if c_t=='Mr' or c_t=='Ms' or c_t=='Mrs' or c_t=='Mx':
            cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
            found_title=True
        else:
            print()
            print("~~~ Invalid title of the customer has been entered !!! ~~~")
            print("--> Please provide the valid title of the customer to store the customer's details __/\__")
            print()
            c_t=input("Enter the customer's Title as either Mr, Ms or Mrs: ").capitalize()
            if c_t=='Mr' or c_t=='Ms' or c_t=='Mrs' or c_t=='Mx':
                cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
                found_title=True
            else:
                print()
                found_title=False
                print("~~~ Invalid title of the customer has been entered !!! ~~~") 
                
        if c_sex=='MALE' or c_sex=='FEMALE' or c_sex=='THIRD GENDER' or c_sex=='M' or c_sex=='F' or c_sex=='TG' :
            cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
            found_sex=True
        else:
            print()
            print("~~~ Invalid sex of the customer has been entered !!! ~~~")
            print("--> Please provide the valid sex of the customer to store the customer's details __/\__")
            print()
            c_sex=input("Enter the customer's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
            if c_sex=='MALE' or c_sex=='FEMALE' or c_sex=='THIRD GENDER' or c_sex=='M' or c_sex=='F' or c_sex=='TG' :
                cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
                found_sex=True
            else:
                print()
                found_sex=False
                print("~~~ Invalid sex of the customer has been entered !!! ~~~")        
                
        if '@' and '.com' in c_email:
            cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
            found_email=True
        else:
            print()
            print("~~~ Customer's email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the customer to store the customer's details __/\__")
            print()
            c_email=input("Enter the customer's Email Address: ")
            if '@' and '.com' in c_email:
                cust[c_id]=[c_t,c_n,c_phno,c_email,c_sex,0]
                found_email=True
            else:
               print()
               found_email=False
               print("~~~ Customer's email address doesn't contain '@' or '.com' !!! ~~~")
        
        
        if found_title==True and found_sex==True and found_email==True and found_phno==True:
            pickle.dump(cust,f)
            print()
            print("*** CUSTOMER'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY APPENDED !!! ***")
        else:
            print()
            print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN APPENDED !!! ***")
            print("--> something went wrong in provided data, please provide the proper data of the customer to store the customer's restaurant record __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print()
        ans=input("Press 'a/A' to append more customer's restaurant record: ")
        print()
    f.close()
    
    
def COMPUTE_CUST_REST_BILL():
    f=open('HMS_CUST_REST_REC.dat','rb+')
    cust={}
    while True:
        try:
            cust=pickle.load(f)
        except EOFError:
            break
    
    ans='c'
    while ans.lower()=='c':
        ID=int(input("Enter the ID number of the customer to compute the customer's restaurant record: "))
        found=False      
        for j in cust:
            if j==ID:
                found=True
                
                ans='y'
                while ans.lower()=='y':    
                    print("-------------------------------------------------------------------------")
                    print("						 HOTEL PYCODE INTERNATIONAL")
                    print("-------------------------------------------------------------------------")
                    print("						 MENU CARD")
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
                    ch=int(input("Enter the menu number choosen by the customer: "))
                    qt=eval(input("Enter the quantity: "))
                    if ch==1 or ch==31 or ch==32:
                        rs=20*qt
                        cust[j][5]=cust[j][5]+rs
                    elif ch<=4 and ch>=2:
                        rs=25*qt
                        cust[j][5]=cust[j][5]+rs
                    elif ch<=6 and ch>=5:
                        rs=30*qt
                        cust[j][5]=cust[j][5]+rs
                    elif ch<=8 and ch>=7:
                        rs=50*qt
                        cust[j][5]=cust[j][5]+rs
                    elif ch<=10 and ch>=9:
                        rs=70*qt
                        cust[j][5]=cust[j][5]+rs
                    elif (ch<=17 and ch>=11) or ch==35 or ch==36 or ch==38:
                        rs=110*qt
                        cust[j][5]=cust[j][5]+rs
                    elif ch<=19 and ch>=18:
                        rs=120*qt
                        cust[j][5]=cust[j][5]+rs
                    elif (ch<=26 and ch>=20) or ch==42:
                        rs=140*qt
                        cust[j][5]=cust[j][5]+rs
                    elif ch<=28 and ch>=27:
                        rs=150*qt
                        cust[j][5]=cust[j][5]+rs
                    elif ch<=30 and ch>=29:
                        rs=15*qt
                        cust[j][5]=cust[j][5]+rs
                    elif ch==33 or ch==34:
                        rs=90*qt
                        cust[j][5]=cust[j][5]+rs
                    elif ch==37:
                        rs=100*qt
                        cust[j][5]=cust[j][5]+rs
                    elif ch<=41 and ch>=39:
                        rs=130*qt
                        cust[j][5]=cust[j][5]+rs
                    elif ch<=46 and ch>=43:
                        rs=60*qt
                        cust[j][5]=cust[j][5]+rs
                    else:
                        print()
                        print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
                        print("--> Please provide the appropriate menu number __/\__")
                    
                    pickle.dump(cust,f)
                    print()
                    ans=input("Press 'y/Y' to add more menu: ")
                    print()
                    
        if found==False:
            print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN FOUND !!! ***")
            print("--> Please provide the correct ID number of the customer to compute the customer's restaurant record __/\__")
        
        print()
        ans=input("Press 'c/C' to compute more customer's restaurant record: ")
        print()
    f.close()
    
    
def UPDATE_GUEST_ROOM_REC():
    f=open('HMS_CUST_REST_REC.dat','rb+')
    cust={}
    while True:
        try:
            cust=pickle.load(f)
        except EOFError:
            break
        
    ans='u'
    while ans.lower()=='u':
     ID=int(input("Enter the ID number of the customer to update the customer's restaurant record: "))
     found=False
     for j in cust:
        if j==ID:
            
            ans='o'
            while ans.lower()=='o':
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ UPDATE CUSTOMER'S RESTAURANT RECORD $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("--x--x-- CUSTOMER UPDATE MENU --x--x--")
                print("Press 't/T' to update the customer's Title")
                print("Press 'f/F' to update the customer's Full Name")
                print("Press 'g/G' to update the customer's Gender")
                print("Press 'p/P' to update the customer's Mobile/Phone Number")
                print("Press 'e/E' to update the customer's Email Address")
                ch=input("Enter your choice: ").upper()
                
                if ch=='T':
                    print()
                    t=input("Enter the updated Title of the customer as either Mr, Ms or Mrs: ")
                    if t=='Mr' or t=='Ms' or t=='Mrs' or t=='Mx':
                        cust[j][0]=t
                        print("*** CUSTOMER'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid title of the customer has been entered !!! ~~~")
                        print("--> Please provide the valid title of the customer to update the field of the customer's title __/\__")
                        print()
                        t=input("Enter the updated Title of the customer as either Mr, Ms or Mrs: ").capitalize()
                        if t=='Mr' or t=='Ms' or t=='Mrs' or t=='Mx':
                            cust[j][0]=t
                            print("*** NOW CUSTOMER'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid title of the customer has been entered !!! ~~~") 
                    
                elif ch=='F':
                    print()
                    f=input("Enter the updated Full Name of the customer: ")
                    cust[j][1]=f
                    print("*** CUSTOMER'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='G':
                    print()
                    g=input("Enter the updated Gender of the customer as either MALE or M, FEMALE or F, THIRD GENDER or TG: ")
                    if g=='MALE' or g=='FEMALE' or g=='THIRD GENDER' or g=='M' or g=='F' or g=='TG' :
                        cust[j][4]=g
                        print("*** CUSTOMER'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid sex of the customer has been entered !!! ~~~")
                        print("--> Please provide the valid sex of the customer to update the field of the customer's sex __/\__")
                        print()
                        g=input("Enter the updated Gender of the customer as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
                        if g=='MALE' or g=='FEMALE' or g=='THIRD GENDER' or g=='M' or g=='F' or g=='TG' :
                            cust[j][4]=g
                            print("*** NOW CUSTOMER'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid sex of the customer has been entered !!! ~~~")
                    
                elif ch=='P':
                    print()
                    print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) \\")
                    p=int(input("Enter the updated Mobile/Phone Number of the customer: +91 "))
                    if len(str(p))==10:
                        cust[j][3]=p
                        print("*** CUSTOMER'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid mobile/phone number of the customer has been entered !!! ~~~")
                        print("--> Please provide the valid mobile/phone number of the customer to update the field of the customer's mobile/phone number __/\__")
                        print()
                        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) \\")
                        p=int(input("Enter the updated Mobile/Phone Number of the customer: +91 "))
                        if len(str(p))==10:
                            cust[j][2]=p
                            print("*** NOW CUSTOMER'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ As invalid mobile/phone number of the customer has been entered !!! ~~~")
                    
                elif ch=='E':
                    print()
                    e=input("Enter the updated Email Address of the customer: ")
                    if '@' and '.com' in g_email:
                        cust[j][3]=e
                        print("*** CUSTOMER'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ customer's email address doesn't contain '@' or '.com' !!! ~~~")
                        print("--> Please provide the proper email address of the customer to update the field of the customer's email address __/\__")
                        print()
                        g_email=input("Enter the updated Email Address of the customer: ")
                        if '@' and '.com' in g_email:
                            cust[j][3]=e
                            print("*** NOW CUSTOMER'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ As customer's email address doesn't contain '@' or '.com' !!! ~~~")
        
                else:
                    print()
                    print("*** ID NUMBER OF THE CUSTOMER HAS BEEN MATCHED BUT YOU HAVE ENTERED WRONG CHOICE FROM THE CUSTOMER UPDATE MENU !!! ***")
                    print("--> Please provide the appropriate choice to update the customer's detail __/\__")
                
                found=True
                pickle.dump(cust,f)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                ans=input("Press 'o/O' to update any other detail of the customer: ")
     
     if found==False:
        print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the customer to update the customer's details __/\__")
        
     print()
     ans=input("Press 'u/U' to update more customer's restaurant record: ")
     print()
    f.close()
    
    
def DISP_CUST_REST_BILL():
    f=open('HMS_CUST_REST_REC.dat','rb')
    rest={}
    while True:
        try:
            rest=pickle.load(f)
        except EOFError:
            break
        
    ans='d'
    while ans.lower()=='d':
        ID=int(input("Enter the ID number of the customer to display the Customer's RESTAURANT BILL: "))
        found=False
        for id in rest:
            if id==ID:
                found=True
                print()
                print("-------------------------------------------------------------------")
                print("%%%%%%%%%%%%%%%%%%%%%% CUSTOMER'S RESTAURANT BILL %%%%%%%%%%%%%%%%%%%%%%")
                print("-------------------------------------------------------------------")
                print("Customer's Unique ID Number: ",id)
                print("Customer's Full Name: ",rest[id][0],rest[id][1])
                print("Customer's Sex: ",rest[id][12])
                print("Customer's Phone Number: +91",rest[id][3])
                print("Customer's Email Address: ",rest[id][4])
                print("Customer's Restaurant Charges: Rs.",rest[id][5])
                print("Restaurant SGST 9% : Rs.",rest[id][5]*0.09)
                print("Restaurant CGST 9% : Rs.",rest[id][5]*0.09)
                print("Total Restaurant Charges (Inclusive all taxes): Rs.",rest[id][5]*0.18)
                print("Total amount to be paid by the guest: Rs.",rest[id][5]+(rest[id][5]*0.18))
                print("----------------------------------------------------------------")
                print()
                
        if found==False:
            print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN FOUND !!! ***")
            print("--> Please provide the correct ID number of the guest to display the Customer's RESTAURANT BILL __/\__")
        
        print()
        ans=input("Press 'd/D' to display more Customer's RESTAURANT BILL: ")
        print()
    f.close()
    
    
def SEARCH_CUST_REST_REC():
    f=open('HMS_CUST_REST_REC.dat','rb')
    cust={}
    while True:
        try:
            cust=pickle.load(f)
        except EOFError:
            break
        
    ans='s'
    while ans.lower()=='s':
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("########################################################### SEARCH CUSTOMER'S RESTAURANT RECORD ###########################################################")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     ID=int(input("Enter the ID number of the customer to search the customer's restaurant record: "))
     found=False      
     for j in cust:
        if j==ID:
            print("--x--x-- Provided ID number of the customer is present in the database ...@ Press 8 to display the customer's RESTAURANT BILL --x--x--")
            found=True
            break
        
     if found==False:
        print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN FOUND !!! ***") 
        print("--> Please provide the correct ID number of the customer to search the customer's restaurant record __/\__")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
     print()
     ans=input("Press 's/S' to search more customer's restaurant record: ")
     print()
    f.close()
    
    
def DEL_CUST_REST_REC():
    CUST={}
    f=open('HMS_CUST_REST_REC.dat','rb+')
    while True:
        try:
            cust=pickle.load(f)
        except EOFError:
            break
        
    ans='r'
    while ans.lower()=='r':
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("################################################ DELETE CUSTOMER'S RESTAURANT RECORD ################################################")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     ID=int(input("Enter the ID number of the customer, to be search and to delete or remove the customer's restaurant record: "))
     found=False
     for k in cust:
        if k!=ID:
            found=True
            CUST[k]=cust[k]
            pickle.dump(CUST,f)
            
     if found==False:
        print("*** CUSTOMER'S RESTAURANT RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the customer to delete or remove the customer's restaurant record __/\__")
     else:
        print("*** CUSTOMER'S RESTAURANT RECORD HAS BEEN SUCCESSFULLY DELETED !!! ***")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
     print()
     ans=input("Press 'r/R' to delete or remove more customer's restaurant record: ")
     print()
    f.close()


def DISP_ALL_CUST_REST_REC():
    f=open('HMS_CUST_REST_REC.dat','rb')
    cust={}
    while True:
        try:
            cust=pickle.load(f)
        except EOFError:
            break
    print(cust)
    f.close()