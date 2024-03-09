import pickle, random
from datetime import datetime

htl={}
g_rt=0


def INSERT_GUEST_ROOM_REC():
    global g_rt
    f=open('HMS_GUEST_ROOM_REC.dat','wb')
    ans='i'
    while ans.lower()=='i':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& INSERT GUEST'S ROOM RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        g_id=random.randint(10000,99999)
        g_t=input("Enter the guest's Title as either Mr, Ms, Mrs or Mx: ").capitalize()
        g_n=input("Enter the guest's Full Name: ")
        print("ID Number of",g_t,g_n,"is: ",g_id)
        g_sex=input("Enter the guest's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
        g_age=input("Enter the guest's Age: ")
        
        print()
        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) \\")
        g_phno=int(input("Enter the guest's Mobile/Phone Number: +91 "))
        print()
        
        print()
        print("// Note:- Aadhaar number must be of 12 digits \\")
        g_adhr=int(input("Enter the guest's Aadhaar Number: "))
        print()
        
        g_email=input("Enter the guest's Email Address: ")
        g_add=input("Enter the guest's House Address: ")
        g_ci=input("Enter the guest's Check-in Date (DD/MM/YYYY): ")
        g_co=input("Enter the guest's Check-out Date (DD/MM/YYYY): ")
        date_format = "%d/%m/%Y"
        a = datetime.strptime(g_ci, date_format)
        b = datetime.strptime(g_co, date_format)
        delta = b - a
        g_days=delta.days
        
        ROOM_INFO()
        g_nop=int(input("Enter the number of persons: "))
        g_rt=int(input("Enter the type of room choosen by the guest (Press 1, 2, 3, 4, 5, 6, 7, 8 or 9): "))
        g_nor=int(input("Enter the number of rooms: "))
        g_rno=input("Enter the guest's Room Number: ")
        
        found_title=False
        found_sex=False
        found_email=False
        found_phno=False
        found_adhr=False
        
        if len(str(g_adhr))==12:
            htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
            found_adhr=True
        else:
            print()
            print("~~~ Invalid aadhaar number of the guest has been entered !!! ~~~")
            print("--> Please provide the valid aadhaar number of the guest to store the guest's details __/\__")
            print()
            print("// Note:- Aadhaar number must be of 12 digits \\")
            g_adhr=int(input("Enter the guest's Aadhaar Number: "))
            if len(str(g_adhr))==12:
                htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
                found_adhr=True
            else:
                print()
                found_adhr=False
                print("~~~ Invalid aadhaar number of the guest has been entered !!! ~~~")
        
        if len(str(g_phno))==10:
            htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
            found_phno=True
        else:
            print()
            print("~~~ Invalid mobile/phone number of the guest has been entered !!! ~~~")
            print("--> Please provide the valid mobile/phone number of the guest to store the guest's details __/\__")
            print()
            print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) \\")
            g_phno=int(input("Enter the guest's Mobile/Phone Number: +91 "))
            if len(str(g_phno))==10:
                htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
                found_phno=True
            else:
                print()
                found_phno=False
                print("~~~ Invalid mobile/phone number of the guest has been entered !!! ~~~")
        
        if g_t=='Mr' or g_t=='Ms' or g_t=='Mrs' or g_t=='Mx':
            htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
            found_title=True
        else:
            print()
            print("~~~ Invalid title of the guest has been entered !!! ~~~")
            print("--> Please provide the valid title of the guest to store the guest's details __/\__")
            print()
            g_t=input("Enter the guest's Title as either Mr, Ms or Mrs: ").capitalize()
            if g_t=='Mr' or g_t=='Ms' or g_t=='Mrs' or g_t=='Mx':
                htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
                found_title=True
            else:
                print()
                found_title=False
                print("~~~ Invalid title of the guest has been entered !!! ~~~") 
                
        if g_sex=='MALE' or g_sex=='FEMALE' or g_sex=='THIRD GENDER' or g_sex=='M' or g_sex=='F' or g_sex=='TG' :
            htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr]
            found_sex=True
        else:
            print()
            print("~~~ Invalid sex of the guest has been entered !!! ~~~")
            print("--> Please provide the valid sex of the guest to store the guest's details __/\__")
            print()
            g_sex=input("Enter the guest's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
            if g_sex=='MALE' or g_sex=='FEMALE' or g_sex=='THIRD GENDER' or g_sex=='M' or g_sex=='F' or g_sex=='TG' :
                htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
                found_sex=True
            else:
                print()
                found_sex=False
                print("~~~ Invalid sex of the guest has been entered !!! ~~~")        
                
        if '@' and '.com' in g_email:
            htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
            found_email=True
        else:
            print()
            print("~~~ Guest's email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the guest to store the guest's details __/\__")
            print()
            g_email=input("Enter the guest's Email Address: ")
            if '@' and '.com' in g_email:
                htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
                found_email=True
            else:
               print()
               found_email=False
               print("~~~ Guest's email address doesn't contain '@' or '.com' !!! ~~~")
        
        
        if found_title==True and found_sex==True and found_email==True and found_phno==True and found_adhr==True:
            pickle.dump(htl,f)
            g_rt=0
            print()
            print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY INSERTED !!! ***")
        else:
            print()
            print("*** GUEST'S ROOM RECORD HAS NOT BEEN INSERTED !!! ***")
            print("--> something went wrong in provided data, please provide the proper data of the guest to store the guest's room record __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print()
        ans=input("Press 'i/I' to insert more guest's room record: ")
        print()
    f.close()
    
    
def ROOM_INFO():
    print()
    print(''' ************* TYPES OF ROOM AVAILABLE IN HOTEL PYCODE INTERNATIONAL *************
          
          1) STANDARD NON-AC (Rs. 1200/- per day)
            ----------------------------------------------------------------------------
            Room amenities include: 1 Double Bed, Television, Free Wifi, Telephone,
            Double-Door Cupboard, 1 Coffee Table with 2 Sofa, Wall Hanger, Balcony 
            and an attached Washroom with hot/cold water.
            
          2) STANDARD AC (Rs. 1600/- per day)
            ----------------------------------------------------------------------------
            Room amenities include: 1 Double Bed, Television, Free Wifi, Telephone,
            Double-Door Cupboard, 1 Coffee Table with 2 Sofa, Wall Hanger, Balcony 
            and an attached Washroom with hot/cold water + Window/Split AC.
           
          3) TRIPLE-BED NON-AC (Rs. 2000/- per day)
            ----------------------------------------------------------------------------
            Room amenities include: 1 Triple Bed, Free Wifi, Television, Telephone,
            a Triple-Door Cupboard, 1 Coffee Table with 3 Sofa, Wall Hanger, 2 Side
            Table, Balcony with an Accent Table with 3 Chair and an attached
            Washroom with hot/cold water.
            
          4) TRIPLE-BED AC (Rs. 2400/- per day)
            ----------------------------------------------------------------------------
            Room amenities include: 1 Triple Bed, Free Wifi, Television, Telephone,
            a Triple-Door Cupboard, 1 Coffee Table with 3 Sofa, Wall Hanger, 2 Side
            table, Balcony with an Accent Table with 3 Chair and an attached 
            Washroom with hot/cold water + Window/Split AC.
          
          5) FOUR-BEDDED NON-AC (Rs. 2800/- per day)
            ----------------------------------------------------------------------------
            Room amenities include: 2 Double Bed, Free Wifi, Television, Telephone,
            2 Double-Door Cupboard, 2 Coffee Table with 4 Sofa, Wall Hanger, 3 Side
            Table, Balcony with an Accent Table with 4 Chair and 2 attached
            Washroom with hot/cold water.
          
          6) FOUR-BEDDED AC (Rs. 3200/- per day)
            ----------------------------------------------------------------------------
            Room amenities include: 2 Double Bed, Free Wifi, Television, Telephone, 
            2 Double-Door Cupboard, 2 Coffee Table with 4 Sofa, Wall Hanger, 3 Side
            Table, Balcony with an Accent Table with 4 Chair and 2 attached 
            Washroom with hot/cold water + Window/Split AC.
          
          7) DELUXE (Rs. 4500/- per day with Complimentary Breakfast)
            ----------------------------------------------------------------------------
            Room amenities include: 1 Triple Bed + 1 Single Bed, Free Wifi, Television,
            Telephone, 1 Triple-Door Cupboard, 1 Coffee Table with 3 Sofa, Almirah, 2 
            Side table, Washing Machine, Induction Oven, Microwave Oven, Refrigerator, 
            Music System, a Standard size Balcony with an Accent Table with 3 Chair and 2
            attached Washroom with hot/cold water + Window/Split AC.
          
          8) COTTAGE (Rs. 5500/- per day with Complimentary Breakfast)
            ----------------------------------------------------------------------------
            Room amenities include: 1 Triple Bed + 1 Single Bed, Free Wifi, Television,
            Telephone, 1 Triple-Door Cupboard, 1 Coffee Table with 3 Sofa, Almirah, 2
            Side table, Washing Machine, Induction Oven, Microwave Oven, Refrigerator,
            Music System, 1 Small and 1 Medium size Balcony with an Accent Table with 
            3 Chair and 2 attached Washroom with hot/cold water + Window/Split AC.
          
          9) SUITE (Rs. 7000/- per day with Complimentary Breakfast)
            ----------------------------------------------------------------------------
            Room amenities include: 1 Triple Bed + 1 Double Bed, Free Wifi, Television,
            Telephone, 2 Double-Door Cupboard, 2 Coffee Table with 4 Sofa, 2 Almirah, 3 
            Side table, Washing Machine, Induction Oven, Microwave Oven, Refrigerator, 
            Music System, 2 Large size Balcony with 2 Accent Table with 5 Chair and 2
            attached Washroom with hot/cold water + Window/Split AC.''')
    print()
    
def APPEND_GUEST_ROOM_REC():
    global g_rt
    f=open('HMS_GUEST_ROOM_REC.dat','rb')
    htl={}
    while True:
        try:
            htl=pickle.load(f)
        except EOFError:
            break
    f.close()
    
    f=open('HMS_GUEST_ROOM_REC.dat','ab')
    ans='a'
    while ans.lower()=='a':
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& APPEND GUEST'S ROOM RECORD &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        g_id=random.randint(10000,99999)
        g_t=input("Enter the guest's Title as either Mr, Ms, Mrs or Mx: ").capitalize()
        g_n=input("Enter the guest's Full Name: ")
        print("ID Number of",g_t,g_n,"is: ",g_id)
        g_sex=input("Enter the guest's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
        g_age=input("Enter the guest's Age: ")
        
        print()
        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) \\")
        g_phno=int(input("Enter the guest's Mobile/Phone Number: +91 "))
        print()
        
        print()
        print("// Note:- Aadhaar number must be of 12 digits \\")
        g_adhr=int(input("Enter the guest's Aadhaar Number: "))
        print()
        
        g_email=input("Enter the guest's Email Address: ")
        g_add=input("Enter the guest's House Address: ")
        g_ci=input("Enter the guest's Check-in Date (DD/MM/YYYY): ")
        g_co=input("Enter the guest's Check-out Date (DD/MM/YYYY): ")
        date_format = "%d/%m/%Y"
        a = datetime.strptime(g_ci, date_format)
        b = datetime.strptime(g_co, date_format)
        delta = b - a
        g_days=delta.days
        
        ROOM_INFO()
        g_nop=int(input("Enter the number of persons: "))
        g_rt=int(input("Enter the type of room choosen by the guest (Press 1, 2, 3, 4, 5, 6, 7, 8 or 9): "))
        g_nor=int(input("Enter the number of rooms: "))
        g_rno=input("Enter the guest's Room Number: ")
        
        found_title=False
        found_sex=False
        found_email=False
        found_phno=False
        found_adhr=False
        
        if len(str(g_adhr))==12:
            htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
            found_adhr=True
        else:
            print()
            print("~~~ Invalid aadhaar number of the guest has been entered !!! ~~~")
            print("--> Please provide the valid aadhaar number of the guest to store the guest's details __/\__")
            print()
            print("// Note:- Aadhaar number must be of 12 digits \\")
            g_adhr=int(input("Enter the guest's Aadhaar Number: "))
            if len(str(g_adhr))==12:
                htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
                found_adhr=True
            else:
                print()
                found_adhr=False
                print("~~~ Invalid aadhaar number of the guest has been entered !!! ~~~")
        
        if len(str(g_phno))==10:
            htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
            found_phno=True
        else:
            print()
            print("~~~ Invalid mobile/phone number of the guest has been entered !!! ~~~")
            print("--> Please provide the valid mobile/phone number of the guest to store the guest's details __/\__")
            print()
            print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) \\")
            g_phno=int(input("Enter the guest's Mobile/Phone Number: +91 "))
            if len(str(g_phno))==10:
                htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
                found_phno=True
            else:
                print()
                found_phno=False
                print("~~~ Invalid mobile/phone number of the guest has been entered !!! ~~~")
        
        if g_t=='Mr' or g_t=='Ms' or g_t=='Mrs' or g_t=='Mx':
            htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
            found_title=True
        else:
            print()
            print("~~~ Invalid title of the guest has been entered !!! ~~~")
            print("--> Please provide the valid title of the guest to store the guest's details __/\__")
            print()
            g_t=input("Enter the guest's Title as either Mr, Ms or Mrs: ").capitalize()
            if g_t=='Mr' or g_t=='Ms' or g_t=='Mrs' or g_t=='Mx':
                htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
                found_title=True
            else:
                print()
                found_title=False
                print("~~~ Invalid title of the guest has been entered !!! ~~~") 
                
        if g_sex=='MALE' or g_sex=='FEMALE' or g_sex=='THIRD GENDER' or g_sex=='M' or g_sex=='F' or g_sex=='TG' :
            htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
            found_sex=True
        else:
            print()
            print("~~~ Invalid sex of the guest has been entered !!! ~~~")
            print("--> Please provide the valid sex of the guest to store the guest's details __/\__")
            print()
            g_sex=input("Enter the guest's Gender as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
            if g_sex=='MALE' or g_sex=='FEMALE' or g_sex=='THIRD GENDER' or g_sex=='M' or g_sex=='F' or g_sex=='TG' :
                htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
                found_sex=True
            else:
                print()
                found_sex=False
                print("~~~ Invalid sex of the guest has been entered !!! ~~~")        
                
        if '@' and '.com' in g_email:
            htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
            found_email=True
        else:
            print()
            print("~~~ Guest's email address doesn't contain '@' or '.com' !!! ~~~")
            print("--> Please provide the proper email address of the guest to store the guest's details __/\__")
            print()
            g_email=input("Enter the guest's Email Address: ")
            if '@' and '.com' in g_email:
                htl[g_id]=[g_t,g_n,g_age,g_phno,g_email,g_add,g_ci,g_co,g_rt,g_nop,0,g_days,g_sex,g_rno,g_adhr,g_nor]
                found_email=True
            else:
               print()
               found_email=False
               print("~~~ Guest's email address doesn't contain '@' or '.com' !!! ~~~")
        
        
        if found_title==True and found_sex==True and found_email==True and found_phno==True and found_adhr==True:
            pickle.dump(htl,f)
            g_rt=0
            print()
            print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY APPENDED !!! ***")
        else:
            print()
            print("*** GUEST'S ROOM RECORD HAS NOT BEEN APPENDED !!! ***")
            print("--> something went wrong in provided data, please provide the proper data of the guest to store the guest's room record __/\__")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        print()
        ans=input("Press 'a/A' to append more guest's room record: ")
        print()
    f.close()
    

def SEARCH_GUEST_ROOM_REC():
    f=open('HMS_GUEST_ROOM_REC.dat','rb')
    htl={}
    while True:
        try:
            htl=pickle.load(f)
        except EOFError:
            break
        
    ans='s'
    while ans.lower()=='s':
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("########################################################### SEARCH GUEST'S ROOM RECORD ###########################################################")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     ID=int(input("Enter the ID number of the guest to search the guest's room record: "))
     found=False      
     for j in htl:
        if j==ID:
            print("--x--x-- Provided ID number of the guest is present in the database ...@ Press 7 to display the Guest's ROOM BILL --x--x--")
            found=True
            break
        
     if found==False:
        print("*** GUEST'S ROOM RECORD HAS NOT BEEN FOUND !!! ***") 
        print("--> Please provide the correct ID number of the guest to search the guest's room record __/\__")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
     print()
     ans=input("Press 's/S' to search more guest's room record: ")
     print()
    f.close()
    
    
def UPDATE_GUEST_ROOM_REC():
    f=open('HMS_GUEST_ROOM_REC.dat','rb+')
    htl={}
    while True:
        try:
            htl=pickle.load(f)
        except EOFError:
            break
        
    ans='u'
    while ans.lower()=='u':
     ID=int(input("Enter the ID number of the guest to update the guest's room record: "))
     found=False
     for j in htl:
        if j==ID:
            
            ans='o'
            while ans.lower()=='o':
                print()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ UPDATE GUEST'S ROOM RECORD $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("--x--x-- GUEST UPDATE MENU --x--x--")
                print("Press 't/T' to update the guest's Title")
                print("Press 'f/F' to update the guest's Full Name")
                print("Press 'g/G' to update the guest's Gender")
                print("Press 'n/N' to update the guest's Aadhaar Number")
                print("Press 'p/P' to update the guest's Mobile/Phone Number")
                print("Press 'e/E' to update the guest's Email Address")
                print("Press 'h/H' to update the guest's House Address")
                print("Press 'a/A' to update the guest's Age")
                print("Press 'd/D' to update the number of Days")
                print("Press 'nop/NOP' to update the Number Of Persons")
                print("Press 'rt/RT' to update the type of room choosen by the guest")
                print("Press 'nor/NOR' to update the Number Of Rooms")
                print("Press 'rn/RN' to update the guest's Room Number")
                ch=input("Enter your choice: ").upper()
                
                if ch=='T':
                    print()
                    t=input("Enter the updated Title of the guest as either Mr, Ms, Mrs or Mx: ")
                    if t=='Mr' or t=='Ms' or t=='Mrs' or t=='Mx':
                        htl[j][0]=t
                        print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** GUEST'S ROOM RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid title of the guest has been entered !!! ~~~")
                        print("--> Please provide the valid title of the guest to update the field of the guest's title __/\__")
                        print()
                        t=input("Enter the updated Title of the guest as either Mr, Ms, Mrs or Mx: ").capitalize()
                        if t=='Mr' or t=='Ms' or t=='Mrs' or t=='Mx':
                            htl[j][0]=t
                            print("*** NOW GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** GUEST'S ROOM RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid title of the guest has been entered !!! ~~~") 
                    
                elif ch=='F':
                    print()
                    f=input("Enter the updated Full Name of the guest: ")
                    htl[j][1]=f
                    print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='G':
                    print()
                    g=input("Enter the updated Gender of the guest as either MALE or M, FEMALE or F, THIRD GENDER or TG: ")
                    if g=='MALE' or g=='FEMALE' or g=='THIRD GENDER' or g=='M' or g=='F' or g=='TG' :
                        htl[j][12]=g
                        print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** GUEST'S ROOM RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid sex of the guest has been entered !!! ~~~")
                        print("--> Please provide the valid sex of the guest to update the field of the guest's sex __/\__")
                        print()
                        g=input("Enter the updated Gender of the guest as either MALE or M, FEMALE or F, THIRD GENDER or TG: ").upper()
                        if g=='MALE' or g=='FEMALE' or g=='THIRD GENDER' or g=='M' or g=='F' or g=='TG' :
                            htl[j][12]=g
                            print("*** NOW GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** GUEST'S ROOM RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid sex of the guest has been entered !!! ~~~")
                            
                elif ch=='N':
                    print()
                    n=int(input("Enter the updated Aadhaar Number of the guest: "))
                    if len(str(n))==12:
                        htl[j][14]=n
                        print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** GUEST'S ROOM RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid aadhaar number of the guest has been entered !!! ~~~")
                        print("--> Please provide the valid aadhaar number of the guest to update the field of the guest's aadhaar number __/\__")
                        print()
                        print("// Note:- Aadhaar number must be of 12 digits \\")
                        n=int(input("Enter the updated Aadhaar Number of the guest: "))
                        if len(str(n))==12:
                            htl[j][14]=n
                            print("*** NOW GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** GUEST'S ROOM RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ Invalid aadhaar number of the guest has been entered !!! ~~~")
                    
                elif ch=='P':
                    print()
                    print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) \\")
                    p=int(input("Enter the updated Mobile/Phone Number of the guest: +91 "))
                    if len(str(p))==10:
                        htl[j][3]=p
                        print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** GUEST'S ROOM RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Invalid mobile/phone number of the guest has been entered !!! ~~~")
                        print("--> Please provide the valid mobile/phone number of the guest to update the field of the guest's mobile/phone number __/\__")
                        print()
                        print("// Note:- Mobile/Phone number must be of 10 digits (without ISD code) \\")
                        p=int(input("Enter the updated Mobile/Phone Number of the guest: +91 "))
                        if len(str(p))==10:
                            htl[j][3]=p
                            print("*** NOW GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** GUEST'S ROOM RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ As invalid mobile/phone number of the guest has been entered !!! ~~~")
                    
                elif ch=='E':
                    print()
                    e=input("Enter the updated Email Address of the guest: ")
                    if '@' and '.com' in g_email:
                        htl[j][4]=e
                        print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    else:
                        print()
                        print("*** GUEST'S ROOM RECORD HAS NOT BEEN UPDATED !!! ***")
                        print("~~~ Guest's email address doesn't contain '@' or '.com' !!! ~~~")
                        print("--> Please provide the proper email address of the guest to update the field of the guest's email address __/\__")
                        print()
                        g_email=input("Enter the updated Email Address of the guest: ")
                        if '@' and '.com' in g_email:
                            htl[j][4]=e
                            print("*** NOW GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                        else:
                            print()
                            print("*** GUEST'S ROOM RECORD HAS NOT BEEN UPDATED !!! ***")
                            print("~~~ As guest's email address doesn't contain '@' or '.com' !!! ~~~")
        
                elif ch=='H':
                    print()
                    h=input("Enter the updated House Address of the guest: ")
                    htl[j][5]=h
                    print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")

                elif ch=='A':
                    print()
                    a=input("Enter the updated Age of the guest: ")
                    htl[j][2]=a
                    print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")

                elif ch=='D':
                    print()
                    ci=input("Enter the updated Check-in Date (DD/MM/YYYY) of the guest: ")
                    co=input("Enter the updated Check-out Date (DD/MM/YYYY) of the guest: ")
                    date_format = "%d/%m/%Y"
                    a = datetime.strptime(ci, date_format)
                    b = datetime.strptime(co, date_format)
                    delta = b - a
                    d=delta.days
                    htl[j][6]=ci
                    htl[j][7]=co
                    htl[j][11]=d
                    print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")

                elif ch=='NOP':
                    print()
                    nop=input("Enter the updated Number Of Persons: ")
                    htl[j][9]=nop
                    print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")

                elif ch=='RT':
                    print()
                    ROOM_INFO()
                    rt=input("Enter the updated Room Type of the guest: ")
                    htl[j][8]=rt
                    print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")
                    
                elif ch=='NOR':
                    print()
                    nor=input("Enter the updated Number Of rooms: ")
                    htl[j][15]=nor
                    print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")

                elif ch=='RN':
                    print()
                    rn=input("Enter the updated Room Number of the guest: ")
                    htl[j][13]=rn
                    print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY UPDATED !!! ***")

                else:
                    print()
                    print("*** ID NUMBER OF THE GUEST HAS BEEN MATCHED BUT YOU HAVE ENTERED WRONG CHOICE FROM THE GUEST UPDATE MENU !!! ***")
                    print("--> Please provide the appropriate choice to update the guest's detail __/\__")
                
                found=True
                pickle.dump(htl,f)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                ans=input("Press 'o/O' to update any other detail of the guest: ")
     
     if found==False:
        print("*** GUEST'S ROOM RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the guest to update the guest's details __/\__")
        
     print()
     ans=input("Press 'u/U' to update more guest's room record: ")
     print()
    f.close()
    
    
def DEL_GUEST_ROOM_REC():
    HTL={}
    f=open('HMS_GUEST_ROOM_REC.dat','rb+')
    while True:
        try:
            htl=pickle.load(f)
        except EOFError:
            break
        
    ans='r'
    while ans.lower()=='r':
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     print("################################################ DELETE GUEST'S ROOM RECORD ################################################")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     ID=int(input("Enter the ID number of the guest, to be search and to delete or remove the guest's room record: "))
     found=False
     for k in htl:
        if k!=ID:
            found=True
            HTL[k]=htl[k]
            pickle.dump(HTL,f)
            
     if found==False:
        print("*** GUEST'S ROOM RECORD HAS NOT BEEN FOUND !!! ***")
        print("--> Please provide the correct ID number of the guest to delete or remove the guest's room record __/\__")
     else:
        print("*** GUEST'S ROOM RECORD HAS BEEN SUCCESSFULLY DELETED !!! ***")
     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
     print()
     ans=input("Press 'r/R' to delete or remove more guest's room record: ")
     print()
    f.close()


def DISP_GUEST_ROOM_BILL():
    f=open('HMS_GUEST_ROOM_REC.dat','rb+')
    htl={}
    while True:
        try:
            htl=pickle.load(f)
        except EOFError:
            break
        
    ans='d'
    while ans.lower()=='d':
        ID=int(input("Enter the ID number of the guest to display the Guest's ROOM BILL: "))
        found=False
        for id in htl:
            if id==ID:
                found=True
                if htl[id][8]==1:
                    htl[id][10]=htl[id][15]*1200*htl[id][11]
                elif htl[id][8]==2:
                    htl[id][10]=htl[id][15]*1600*htl[id][11]
                elif htl[id][8]==3:
                    htl[id][10]=htl[id][15]*2000*htl[id][11]
                elif htl[id][8]==4:
                    htl[id][10]=htl[id][15]*2400*htl[id][11]
                elif htl[id][8]==5:
                    htl[id][10]=htl[id][15]*2800*htl[id][11]
                elif htl[id][8]==6:
                    htl[id][10]=htl[id][15]*3200*htl[id][11]
                elif htl[id][8]==7:
                    htl[id][10]=htl[id][15]*4500*htl[id][11]
                elif htl[id][8]==8:
                    htl[id][10]=htl[id][15]*5500*htl[id][11]
                elif htl[id][8]==9:
                    htl[id][10]=htl[id][15]*7000*htl[id][11]
                else:
                    print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
                    print("--> Please provide the proper room type __/\__")
                    ROOM_INFO()
                    g_nor=int(input("Enter the number of rooms: "))
                    g_rt=int(input("Enter type of room choosen by the guest (Press 1, 2, 3, 4, 5, 6, 7, 8 or 9): "))
                    htl[id][8]=g_rt
                    htl[id][15]=g_nor
                    
                    if htl[id][8]==1:
                        htl[id][10]=htl[id][15]*1200*htl[id][11]
                    elif htl[id][8]==2:
                        htl[id][10]=htl[id][15]*1600*htl[id][11]
                    elif htl[id][8]==3:
                        htl[id][10]=htl[id][15]*2000*htl[id][11]
                    elif htl[id][8]==4:
                        htl[id][10]=htl[id][15]*2400*htl[id][11]
                    elif htl[id][8]==5:
                        htl[id][10]=htl[id][15]*2800*htl[id][11]
                    elif htl[id][8]==6:
                        htl[id][10]=htl[id][15]*3200*htl[id][11]
                    elif htl[id][8]==7:
                        htl[id][10]=htl[id][15]*4500*htl[id][11]
                    elif htl[id][8]==8:
                        htl[id][10]=htl[id][15]*5500*htl[id][11]
                    elif htl[id][8]==9:
                        htl[id][10]=htl[id][15]*7000*htl[id][11]
                    else:
                        print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
                        print("--> Please provide the proper room type __/\__")
                print()
                print("-------------------------------------------------------------------")
                print("%%%%%%%%%%%%%%%%%%%%%% GUEST'S ROOM BILL %%%%%%%%%%%%%%%%%%%%%%")
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
                print("Total amount to be paid by the guest: Rs.",htl[id][10]+(htl[id][10]*0.18))
                print("----------------------------------------------------------------")
                print()
                pickle.dump(htl,f)
                
        if found==False:
            print("*** GUEST'S ROOM RECORD HAS NOT BEEN FOUND !!! ***")
            print("--> Please provide the correct ID number of the guest to display the Guest's ROOM BILL __/\__")
        
        print()
        ans=input("Press 'd/D' to display more Guest's ROOM BILL: ")
        print()
    f.close()
    

def DISP_ALL_GUEST_ROOM_REC():
    f=open('HMS_GUEST_ROOM_REC.dat','rb')
    htl={}
    while True:
        try:
            htl=pickle.load(f)
        except EOFError:
            break
    print(htl)
    f.close()
    