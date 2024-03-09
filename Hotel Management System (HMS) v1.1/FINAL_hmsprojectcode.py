import hotel01,hotel02,hotel03,stdiomask,pyttsx3,ascii_magic

ans='c'
while ans.lower()=='c':
 print()
 un=input("Enter Username: ").upper()
 pw=stdiomask.getpass("Enter Password: ")
 if un=='HOTEL_PC_INT' and pw=='htlpcinthms2023':
  print()
  print('''                    *************************        
                  *         WELCOME TO        *     
                *   HOTEL PYCODE INTERNATIONAL  *
              *                                   *
            *---------------        ----------------*
            [\ ############{\      /}#############/]
            [+\:::::/\:::::{%\    /%}:::::/\:::::/+] 
            [++\___/OO\____{%%\==/%%}____/OO\___/++]
            [++/((((((((((({%%/==\%%})))))))))))\++]
            [+/::::::::::::{%/    \%}::::::::::::\+]
            [/#############{/      \}#############\]
            ----------------        ----------------''')
  print()
  text_speech=pyttsx3.init()
  a="welcome to hotel management system of hotel piecode international"
  text_speech.setProperty("rate",110)
  text_speech.say(a)
  text_speech.runAndWait()
  print()
  output=ascii_magic.from_image_file("ba1b92fd2141aef3075da367ea805eb4.jpg",columns=130,char='@')
  ascii_magic.to_terminal(output)
  print()
  
  ANS='H'
  while ANS.upper()=='H':
    print()
    output=ascii_magic.from_image_file("home tab.png",columns=200,char='@')
    ascii_magic.to_terminal(output)
    print()
    print("~~~ HOME PAGE --> MENU ~~~")
    print("# Press 1 to go to the GUEST ROOM PAGE")
    print("# Press 2 to go to the GUEST ROOM CUM RESTAURANT PAGE")
    print("# Press 3 to go to the CUSTOMERS RESTAURANT PAGE")
    ch=int(input("Enter your choice from the MENU of HOME PAGE: "))
    
    if ch==1:
        print()
        ANS='Y'
        while ANS.upper()=='Y':
         output=ascii_magic.from_image_file("guest room tab.png",columns=200,char='@')
         ascii_magic.to_terminal(output)
         print()
         print("~~~ GUEST ROOM PAGE --> MENU ~~~")
         print("# Press 1 to insert the details of the guests")
         print("# Press 2 to display the record of all guests")
         print("# Press 3 to append the details of the guests")
         print("# Press 4 to search the record of the guests")
         print("# Press 5 to update the details of the guests")
         print("# Press 6 to delete the record of the guests")
         print("# Press 7 to display the ROOM BILL of the particular guest")
         ch=int(input("Enter your choice from the MENU of GUEST ROOM PAGE: "))
         if ch==1:
            print()
            hotel01.INSERT_GUEST_ROOM_REC()
            print()
         elif ch==2:
            print()
            hotel01.DISP_ALL_GUEST_ROOM_REC()
            print()
         elif ch==3:
            print()
            hotel01.APPEND_GUEST_ROOM_REC()
            print()
         elif ch==4:
            print()
            hotel01.SEARCH_GUEST_ROOM_REC()
            print()
         elif ch==5:
            print()
            hotel01.UPDATE_GUEST_ROOM_REC()
            print()
         elif ch==6:
            print()
            hotel01.DEL_GUEST_ROOM_REC()
            print()
         elif ch==7:
            print()
            hotel01.DISP_GUEST_ROOM_BILL()  
            print()
         else:
            print()
            print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
            print("--> Please the provide the appropriate choice to access the MENU of GUEST ROOM PAGE __/\__")
            print()
         ANS=input("Press 'y/Y' to go to the GUEST ROOM PAGE or Press 'q/Q' to quit: ")
         print()
         
    elif ch==2:
        print()
        ANS='Y'
        while ANS.upper()=='Y':
         output=ascii_magic.from_image_file("two-men-friends-sitting-at-a-table-eating-vector-359624322.jpg",columns=140,char='@')
         ascii_magic.to_terminal(output)
         print()
         output=ascii_magic.from_image_file("guest room cum restaurant tab.png",columns=200,char='@')
         ascii_magic.to_terminal(output)
         print()
         print("~~~ GUEST ROOM CUM RESTAURANT PAGE --> MENU ~~~")
         print("# Press 1 to insert the details of the guests")
         print("# Press 2 to compute the restaurant bill of the guests")
         print("# Press 3 to display the record of all guests")
         print("# Press 4 to append the details of the guests")
         print("# Press 5 to search the record of the guests")
         print("# Press 6 to delete the record of the guests")
         print("# Press 7 to display the ROOM CUM RESTAURANT BILL of the particular guest")
         ch=int(input("Enter your choice from the MENU of GUEST ROOM CUM RESTAURANT PAGE: "))
         if ch==1:
           print()
           hotel02.INSERT_GUEST_ROOM_CUM_REST_REC()
           print()
         elif ch==2:
           print()
           hotel02.COMPUTE_GUEST_REST_BILL()
           print()
         elif ch==3:
           print()
           hotel02.DISP_ALL_GUEST_ROOM_CUM_REST_REC()
           print()
         elif ch==4:
           print()
           hotel02.APPEND_GUEST_ROOM_CUM_REST_REC()
           print()
         elif ch==5:
           print()
           hotel02.SEARCH_GUEST_ROOM_CUM_REST_REC()
           print()
         elif ch==6:
           print()
           hotel02.DEL_GUEST_REST_REC()
           print()
         elif ch==7:
           print()
           hotel02.DISP_GUEST_ROOM_CUM_REST_BILL()
           print()
         else:
           print()
           print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
           print("--> Please provide the appropriate choice to access the MENU of GUEST ROOM CUM RESTAURANT PAGE __/\__")
           print()
         ANS=input("Press 'y/Y' to go to the GUEST ROOM CUM RESTAURANT PAGE or Press 'q/Q' to quit: ")
         print()
         
    elif ch==3:
        print()
        ANS='Y'
        while ANS.upper()=='Y':
         output=ascii_magic.from_image_file("couples-date-cafe-flat-color-vector-illustration-boyfriend-girlfriend-talking-table-partner-with-phones-two-group-people-2d-cartoon-characters-with-cafeteria-interior-background_151150-5710.webp",columns=200,char='@')
         ascii_magic.to_terminal(output)
         print()
         output=ascii_magic.from_image_file("customers restaurant tab.png",columns=200,char='@')
         ascii_magic.to_terminal(output)
         print()
         print("~~~ CUSTOMERS RESTAURANT PAGE --> MENU ~~~")
         print("# Press 1 to insert the details of the customers")
         print("# Press 2 to compute the restaurant bill of the customers")
         print("# Press 3 to display the record of all customers")
         print("# Press 4 to append the details of the customers")
         print("# Press 5 to search the record of the customers")
         print("# Press 6 to update the details of the customers")
         print("# Press 7 to delete the record of the customers")
         print("# Press 8 to display the RESTAURANT BILL of the particular customer")
         ch=int(input("Enter your choice from the MENU of CUSTOMERS RESTAURANT PAGE: "))
         if ch==1:
           print()
           hotel03.INSERT_CUST_REST_REC()
           print()
         elif ch==2:
           print()
           hotel03.COMPUTE_CUST_REST_BILL()
           print()
         elif ch==3:
           print()
           hotel03.DISP_ALL_CUST_REST_REC()
           print()
         elif ch==4:
           print()
           hotel03.APPEND_CUST_REST_REC()
           print()
         elif ch==5:
           print()
           hotel03.SEARCH_CUST_REST_REC()
           print()
         elif ch==6:
           print()
           hotel03.UPDATE_GUEST_ROOM_REC()
           print()
         elif ch==7:
           print()
           hotel03.DEL_CUST_REST_REC()
           print()
         elif ch==8:
           print()
           hotel03.DISP_CUST_REST_BILL()
           print()
         else:
           print()
           print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
           print("--> Please provide the appropriate choice to access the MENU of CUSTOMERS RESTAURANT PAGE __/\__")
           print()
         ANS=input("Press 'y/Y' to go to the CUSTOMERS RESTAURANT PAGE or Press 'q/Q' to quit: ")
         print()
    
    else:
        print()
        print("*** YOU HAVE ENTERED WRONG CHOICE !!! ***")
        print("--> Please provide the appropriate choice to access the MENU of HOME PAGE __/\__")
        print()
    
    print()
    output=ascii_magic.from_image_file("hotel-main.gif",columns=105,char='@')
    ascii_magic.to_terminal(output)
    print()
    ANS=input("Press 'h/H' to go to the HOME PAGE or Press 'q/Q' to quit: ")
    print()
    if ANS.lower()=='q':
      print()
      print('****************************************************************************************************************')
      print('''                                    THANK YOU FOR USING HOTEL MANAGEMENT SYSTEM OF HOTEL PYCODE INTERNATIONAL _/\_,
                                                                    PLEASE VISIT AGAIN....''')
      print('****************************************************************************************************************')
      text_speech=pyttsx3.init()
      a="Thank you for using hotel management system of hotel piecode international, please visit again"
      text_speech.setProperty("rate",110)
      text_speech.say(a)
      text_speech.runAndWait()
      print()
      output=ascii_magic.from_image_file("how-to-respond-to-thank-you.webp",columns=150,char='@')
      ascii_magic.to_terminal(output)
      print()
 
 elif un=='HOTEL_PC_INT' and pw!='htlpcinthms2023':
    print("~~ Access denied !!! ,invalid password has been entered ~~")
    text_speech=pyttsx3.init()
    a="Access denied, invalid password has been entered, please provide valid and correct authorised credentials to access the account"
    text_speech.setProperty("rate",110)
    text_speech.say(a)
    text_speech.runAndWait()
    print()
 
 elif un!='HOTEL_PC_INT' and pw=='htlpcinthms2023':
    print("~~ Access denied !!! ,invalid username has been entered ~~")
    text_speech=pyttsx3.init()
    a="Access denied, invalid username has been entered, please provide valid and correct authorised credentials to access the account"
    text_speech.setProperty("rate",110)
    text_speech.say(a)
    text_speech.runAndWait()
    print()
 
 else:
    print("~~ Access denied !!! ,invalid username and password has been entered ~~")
    text_speech=pyttsx3.init()
    a="Access denied, invalid username and password has been entered, please provide valid and correct authorised credentials to access the account"
    text_speech.setProperty("rate",110)
    text_speech.say(a)
    text_speech.runAndWait()
    print()
    
 ans=input("Press 'c/C' to continue to run the hms or Press 'e/E' to exit: ")
 print()
