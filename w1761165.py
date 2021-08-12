#Created by Mudith Perera 
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.  
# Student ID: 2019845               # Date:  2019-11-07
#Last modified date : 2019-11-19

print("1: Student version")
print("2: Staff version with extended staff verson(part 3)")
print("3: Alternative Staff Version ")
print()
home=input("Enter the part you want (1,2 or 3): ")
print()


def display_range():
                                print("Range error")
                                print()
                                
########################################## PART 01(Student version) ##############################################################         

if home=="1":
                
                while True:
                                try:
                                                Pass=int(input("Enter Pass count: "))         #getting user input and assigning it into variable "Pass"
                                                if Pass not in range(0,121,20):                 #checking the range of Pass
                                                                display_range()
                                                                break

                                                if Pass==120:
                                                                print("Progress")
                                                                print()
                                                                break                                                
                                                defer=int(input("Enter defer count: "))         #getting user input for defer
                                                if defer not in range(0,121,20):                #checking range on defer
                                                                display_range()
                                                                break
                                                                
                                                fail=int(input("Enter fail count: "))              #getting user input for fail
                                                if fail not in range(0,121,20):                 #checking the range of fail
                                                                display_range()
                                                                break
                                                
                                except ValueError:                                              #except part will execute when user inputs a string.
                                                print("Integer required")
                                                break

                                total=Pass+defer+fail
                                if total!=120:
                                                print("Total incorrect")                 
                                                break
                                elif fail>=80:
                                                print("Exclude")
                                                print()
                                                break
                                elif Pass==100:
                                                print("Progress – module trailer")
                                                print()
                                                break
                                else:
                                                print("Do not progress – module retriever")
                                                print()
                                                break

########################################## PART 02 (Staff version) ##############################################################         

elif home=="2":
                progress_count=0
                trailing_count=0
                retriever_count=0
                excluded_count=0
                while True:
                                try:
                                                oPass=input("Enter Pass count: ")         #getting user input
                                                if oPass=="q":
                                                                break
                                                Pass=int(oPass)                                                 #coverting the input type to integer
                                                if Pass not in range(0,121,20):                 #checking the range of the input
                                                                display_range()
                                                                continue
                                                if Pass==120:
                                                                print("Progress ")
                                                                print()
                                                                progress_count+=1
                                                                continue
                                                
                                                odefer=int(input("Enter defer count: ")) #getting user input
                                                if odefer=="q":
                                                                break
                                                defer=int(odefer)
                                                if defer not in range(0,121,20):
                                                                display_range()
                                                                continue
                                                
                                                ofail=int(input("Enter fail count: "))          #getting user input
                                                if ofail=="q":
                                                                break
                                                fail=int(ofail)
                                                if fail not in range(0,121,20):
                                                                display_range()
                                                                continue
                                                
                                except ValueError:                                                              #except part will execute when user inputs a string except "q"
                                                print("Integer required")
                                                print()
                                                continue

                                total=Pass+defer+fail
                                if total!=120:
                                                print("Total incorrect")
                                                print()
                                                continue
                                elif fail>=80:
                                                print("Exclude")
                                                print()
                                                excluded_count+=1
                                                continue
                                elif Pass==100:
                                                print("Progress – module trailer")
                                                print()
                                                trailing_count+=1
                                                continue
                                else:
                                                print("Do not progress – module retriever")
                                                print()
                                                retriever_count+=1
                                                continue

                pstar="*"*progress_count
                tstar="*"*trailing_count
                rstar="*"*retriever_count
                estar="*"*excluded_count
                print()
                print("Progress",progress_count,":",pstar)
                print("Trailing",trailing_count,":",tstar)
                print("Retriever",retriever_count,":",rstar)
                print("Excluded",excluded_count,":",estar)
                print(progress_count+trailing_count+retriever_count+excluded_count,"outcomes in total")
                print()

########################################## PART 03 ##############################################################

                count=progress_count+trailing_count+retriever_count+excluded_count
                print("Progress  ","Trailing  ","Retriever  ","Excluded  ")
                while count>0 :
                                if progress_count>0:
                                                print("    *",end="                ")
                                                progress_count-=1
                                else:
                                                print("      ",end="                ")
                                if trailing_count>0:
                                                print("*",end="                ")
                                                trailing_count-=1
                                else:
                                                print("  ",end="                ")
                                                
                                if retriever_count>0:
                                                print("*",end="                ")
                                                retriever_count-=1
                                else:
                                                print("  ",end="                ")
                                if excluded_count>0:
                                                print("*")
                                                excluded_count-=1
                                else:
                                                print("  ")
                                count-=1
                               
########################################## PART 04 ##############################################################

elif home=="3":

                
                mylist=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]            #creating a list inside a list with the inputs given in the CW
                count=0
                list_count=0
                progress_count=0
                trailing_count=0
                retriever_count=0
                excluded_count=0
                while count<10:
                                Pass=mylist[count][list_count]
                                defer=mylist[count][list_count+1]
                                fail=mylist[count][list_count+2]
                                
                                if Pass==120:
                                                 print("Progress")
                                                 progress_count+=1      
                                elif fail>=80:
                                                print("Exclude")
                                                excluded_count+=1
                                elif Pass==100:
                                                print("Progress – module trailer")
                                                trailing_count+=1
                                else:
                                                print("Do not progress – module retriever")
                                                retriever_count+=1
                                count+=1
                                list_count=0

                pstar="*"*progress_count
                tstar="*"*trailing_count
                rstar="*"*retriever_count
                estar="*"*excluded_count
                print()
                print("Progress",progress_count,":",pstar)
                print("Trailing",trailing_count,":",tstar)
                print("Retriever",retriever_count,":",rstar)
                print("Excluded",excluded_count,":",estar)
                print(progress_count+trailing_count+retriever_count+excluded_count,"outcomes in total")
                print()

                count=progress_count+trailing_count+retriever_count+excluded_count
                print("Progress  ","Trailing  ","Retriever  ","Excluded  ")
                while count>0 :
                                if progress_count>0:
                                                print("    *",end="                ")
                                                progress_count-=1
                                else:
                                                print("      ",end="                ")
                                if trailing_count>0:
                                                print("*",end="                ")
                                                trailing_count-=1
                                else:
                                                print("  ",end="                ")
                                                
                                if retriever_count>0:
                                                print("*",end="                ")
                                                retriever_count-=1
                                else:
                                                print("  ",end="                ")
                                if excluded_count>0:
                                                print("*")
                                                excluded_count-=1
                                else:
                                                print("  ")
                                count-=1
