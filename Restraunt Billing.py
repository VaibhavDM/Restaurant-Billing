x=1
while (x<=10):
    y=20
    while(y>=x):
        print(" ",end="")
        y=y-1
    
    z=1
    while (z<=x):
        print("*",end=" ")
        z=z+1
    print()
    x=x+1
print("           WELCOME TO WENDEY'S            ")




import mysql.connector as my
yu="n"
while yu=="n":
    print("---1-FOR LOGIN---")
    print("---2-FOR SIGNUP---")
    print("---0-EXIT---")
    a6=input("ENTER:-")
    if a6=="1":
        uname=input("    ENTER USERNAME:-")
        pswd=input("    ENTER PASSWORD:-")
        con=my.connect(host="localhost",user="root",passwd="vaibhav",database="hotel")
        cur=con.cursor()
        cur.execute("select passwd,user_n  from cred where user_n='"+uname+"'")
        row=cur.fetchall()
        for r in row:
            if r[0]==pswd:
                print("Sucessfully Login!")
                cur.close()
#                !!!hotel functions!!!

                f0="n"
                while f0=="n":
                    print("""
---1-Billing Menu---
---2-Food Menu---
---3-Update Or Delete LoginID And Password---
---0-LOGOUT---""")
                    a=input("ENTER:-")
                    if a=="1":
#                        !!!billing functions!!!

                        f1="n"
    
                        while f1=="n":
                            print("")
                            print("---1-See Menu---")
                            print("---2-Search Food Items---")
                            print("---3-Billing---")
                            print("---0-Exit Billing Functions---")
                            a1=input("ENTER:-")
#                            !!!all details!!!

                            if a1=="1":
                                con=my.connect(host="localhost",user="root",passwd="vaibhav",database="hotel")
                                cur=con.cursor()
                                cur.execute("select i_name from menu")
                                for i in cur:
                                    print(i)
                                con.close()


#                       !!!searcher!!!

                            if a1=="2":
                                y="y"
                                while y=="y":
                                    eid=input("Enter Item Name:-")
                                    con=my.connect(host="localhost",user="root",passwd="vaibhav",database="hotel")
                                    cur=con.cursor()
                                    cur.execute("select * from menu where i_name='"+eid+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                         print("Item Not Available!")
                                    else:
                                        cur.execute("select * from menu where i_name='"+eid+"'")
                                    for i in cur:
                                            print(i)
                                    con.close()
                                    y=input("Search Another Item(y/n):-")


#                          !!!Billing!!!
                            try:
                                total=0
                                if a1=="3":
                                    y="y"
                                    while y=="y":
                                        eid=input("Enter Item Name:-")
                                        con=my.connect(host="localhost",user="root",passwd="vaibhav",database="hotel")
                                        cur=con.cursor()
                                        cur.execute("select sum(i_price) from menu where i_name='"+eid+"'")
                                        x=cur.fetchone()
                                        if x==[]:
                                            print("Item not Available!!")
                                        else:
                                            cur.execute("select sum(i_price) from menu where i_name='"+eid+"'")
                                            z=cur.fetchall()
                                            a=z[0][0]
                                            total=total+int(a)
                                            print("total amount :",total)
                                        for i in cur:
                                                print(i)
                                        con.close()
                                        y=input("Do you want to order something else(y/n):-")
                                  
                                if a1=="0":
                                    f1="y"
                                    print("Billing Functions Closed!")
                            except:
                                print("Wrong Input")
#                        !!!Menu Functions!!!

                    if a=="2":
                        f1="n"
                        while f1=="n":
                            print("""
---1-All Food Items Details----
---2-Search Item---
---3-Add Item---
---4-Remove Item---
---5-Update Item---
---0-Exit Menu---""")
                            a2=input("ENTER:-")
#                            !!!see menu!!!

                            if a2=="1":
                                con=my.connect(host="localhost",user="root",passwd="vaibhav",database="hotel")
                                cur=con.cursor()
                                cur.execute("select * from menu")
                                for i in cur:
                                    print(i)
#                            !!!search item!!!
                            if a2=="2":
                                ad="y"
                                while ad=="y" or ad=="Y":
                                    con=my.connect(host="localhost",user="root",passwd="vaibhav",database="hotel")
                                    cur=con.cursor()
                                    a=input("Enter Item Code:-")
                                    cur.execute("select * from menu where i_code='"+a+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                        print("Invalid Id!")                                       
                                    else:
                                        cur.execute("select * from menu where i_code='"+a+"'")
                                        for i in cur:
                                            print(i) 
                                        ad=input("Search Other Item(y/n):-")
                                        
#                            !!!Add item!!!
                            try:
                                
                                if a2=="3":
                                    ad="y"
                                    while ad=="y" or ad=="Y":
                                        itemcode=input("Enter Item code:-")
                                        itemname=input("Enter Item Name:-")
                                        itemprice=int(input("Enter Item Price:-"))
                                        con=my.connect(host="localhost",user="root",passwd="vaibhav",database="hotel")
                                        cur=con.cursor()
                                        cur.execute("insert into menu values('"+itemcode+"','"+itemname+"','"+str(itemprice)+"')")
                                        print("Sucessfully Added!")
                                        con.commit()
                                        con.close()
                                        ad=input("Do You Want To Add Another Item?(y/n):-")
                            except:
                                print("No Item Addded")
#                            !!!remover!!!

                            if a2=="4":
                                
                                ad="y"
                                while ad=="y" or ad=="Y":
                                    con=my.connect(host="localhost",user="root",passwd="vaibhav",database="hotel")
                                    cur=con.cursor()
                                    a=input("Enter Item Code:-")
                                    cur.execute("select * from menu where i_code='"+a+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                        ad="f"
                                        print("No Item Removed!!!")                                                                                                                        
                                    else:
                                        cur.execute("delete from menu where i_code='"+a+"'")
                                        con.commit()
                                        con.close()
                                        print("Deleted Sucessfully!")
                                        ad=input("Remove Other Item(y/n):-")
                                        
                                        
#                            !!!updater!!!

                            if a2=="5":
                                ad="y"
                                while ad=="y" or ad=="Y":
                                    print("""
---1-Change Item Name---
---2-Change Item Price---""")
                                    i=input("ENTER:-")
                                    if i=="1":
                                        e="y"
                                        while e=="y" or e=="Y":
                                            a=input("Enter Item Code:-")
                                            na=input("Enter New Name:-")
                                            con=my.connect(host="localhost",user="root",passwd="vaibhav",database="hotel")
                                            cur=con.cursor()
                                            cur.execute("select * from menu where i_code='"+a+"'")
                                            x=cur.fetchone()
                                            if x==None:
                                                e="z"
                                                print("No Item Updated!!!")
                                                e=input("Change Any Other Name(y/n):-")
                                            else:
                                                cur.execute("update menu set i_name='"+na+"' where i_code='"+a+"'")
                                                con.commit()
                                                con.close()
                                                print("Record Updated!!!")
                                                e=input("Change Any Other Name(y/n):-")
                                    try:
                                        if i=="2":
                                            e="y"
                                            while e=="y" or e=="Y":
                                                a=input("Enter Item Code:-")
                                                na=int(input("Enter New price:-"))
                                                con=my.connect(host="localhost",user="root",passwd="vaibhav",database="hotel")
                                                cur=con.cursor()
                                                cur.execute("select * from menu where i_code='"+a+"'")
                                                x=cur.fetchone()
                                                cur.execute("update menu set i_price='"+str(na)+"' where i_code='"+a+"'")
                                                con.commit()
                                                con.close()
                                                print("Record Updated!")
                                                e=input("Change Any Other Price(y/n):-")
                                                    
                                        ad=input("Change Any Other Record(y/n):-")
                                    except:
                                        print("No Item Updated!!!")
                                        ad=input("Change Any Other Record(y/n):-")      
                                
                            if a2=="0":
                                f1="y"
                                print("Menu Closed!")
        
#                    !!!loginId or Password update or delete programme!!!

                    if a=="3":
                        lk="n"
                        while lk=="n" or lk=="N":
                            print("""
---1-For Updating LoginId Or Password---
---2-For Remove An ID---
---0-For Exit---""")
                            jkl=input("ENTER:-")
                            if jkl=="1":
                                ty="y"
                                while ty=="y":
                                    print("""
---1-Update LoginID---
---2-Update Password---""")
                                    rt=input("ENTER:-")
                                    if rt=="1":
                                        nm="y"
                                        while nm=="y" or nm=="Y":
                                            con=my.connect(host='localhost',user="root",passwd="vaibhav",database="hotel")
                                            cur=con.cursor()
                                            oid=input("Enter Old LoginID:-")
                                            nid=input("Enter New LoginID:-")
                                            cur.execute("select * from cred where user_n='"+oid+"'")
                                            x=cur.fetchone()
                                            if x==None:
                                                print("Id Does not Exists!")                                                    
                                            else:
                                                cur.execute("update cred set user_n='"+nid+"' where user_n='"+oid+"'")
                                                con.commit()
                                                con.close()
                                                print("LoginID Updated!")
                                                nm=input("Change Any Other LoginID(y/n):-")
            
                                    if rt=="2":
                                        nm="y"
                                        while nm=="y" or nm=="Y":
                                            con=my.connect(host='localhost',user="root",passwd="vaibhav",database="hotel")
                                            cur=con.cursor()
                                            oid=input("Enter LoginID:-")
                                            nid=input("Enter New Password:-")
                                            cur.execute("select * from cred where user_n='"+oid+"'")
                                            x=cur.fetchone()
                                            if x==None:
                                                print("Id Does not Exists!")                                                
                                            else:
                                                cur.execute("update cred set passwd='"+nid+"' where user_n='"+oid+"'")
                                                con.commit()
                                                con.close()
                                                print("Password Updated!")
                                                nm=input("Change Any Other Password(y/n):-")
                                            
                                    ty=input("Change Any Other Login Or Password(y/n):-")
                                    
                            if jkl=="2":
                                nm="y"
                                while nm=="y" or nm=="Y":
                                    con=my.connect(host='localhost',user="root",passwd="vaibhav",database="hotel")
                                    cur=con.cursor()
                                    oid=input("Enter LoginID:-")
                                    cur.execute("select * from cred where user_n='"+oid+"'")
                                    x=cur.fetchone()
                                    if x==None:
                                         print("Id Does not Exists!")                                       
                                    else:
                                        cur.execute("delete from cred where user_n='"+oid+"'")
                                        con.commit()
                                        con.close()
                                        print("LoginID Removed!")
                                        nm=input("Change Any Other Credential(y/n):-")
                                    
                            if jkl=="0":
                                lk="y"
                                print("Sucessfully Exit!")
              
                    if a=="0":
                        f0="y"
                        print("Sucessfully LOGOUT!")
                            
            else:
                print("Invalid Login Id or Password!")
                print("Try Again!!")
        
#    !!!Signup Function!!!            
    if a6=="2":
        y="y"
        while y=="y" or y=="Y":
            us=input("Enter New Username:-")
            ps=input("Enter New Password:-")
            con=my.connect(host="localhost",user="root",passwd="vaibhav",database="hotel")
            cur=con.cursor()
            cur.execute("select * from cred where user_n='"+us+"'")
            x=cur.fetchone()
            if x==None:
                cur.execute("insert into cred values('"+us+"','"+ps+"')")
                print("Sucessfully Saved!")
                con.commit()
                con.close()
            else:
                print("UserID Already Exists!")
                
            y=input("Create Other New id(y/n):-")
#   !!!Programme Closer!!!  
    if a6=="0":
        yu="y"
        print("Programme Closed!")
