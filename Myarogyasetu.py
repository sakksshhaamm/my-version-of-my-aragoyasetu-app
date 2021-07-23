print("***TESTING THE RIGHT PERSON***")
ll=[]
print('Based on the data....these are the main symptopms of 
the +ve corona infetced person..')
j,count=1,0
confirm,quar,ninety,cured,none,less,exc=0,0,0,0,0,0,0
feve,col,hea,coug,throa,breat,voic=0,0,0,0,0,0,0
def fever():
 print("As you have fever...please enter your fever in 
fahrenheit")
 f=float(input())
 if f>=95 and f<=98:
 print("It's just a weakness")
 elif f>98 and f<=99.7:
 print("It's less ...but take care!!")
 elif f>99.7 and f<=102.5:
 print("You have a high fever!!!")
 elif f>102.5:
 print("We recommend you to immediately visit the 
doctor!!")
def cough():
 print("\nAs you have cough!! please enter the level of 
cough")
 print('0 :: not much!','1 :: extreme!',sep="\t ")
 c=int(input())
 if c==0:
 print("You don't have much cough!! but still you have,use 
general precautions!")
 if c==1:
 print("We recommend you to please drink warm water 
only")
def breath():
 print("\nAs you have shortness of breath!!")
 b=age
 print("Please enter the detail while which shortness of breath 
occurs:: ")
 print("1:: while sitting only","2: while doing some 
work",sep="\t ")
 br=int(input())
 if br==1:
 print("Then you are advised to take proper medicines!!")
 elif br==2:
 print("Its normal, but we recommend yo to do less work at 
that time")
def cold():
 print("\nAs you have cold!! please enter the level of cold")
 print('0 :: just beginning','1 :: extreme!',sep="\t ")
 co=int(input())
 if co==0:
 print("You don't have much cold!! just take medicines 
only!")
 if co==1:
 print("We recommend you to take steam along with 
medicines")
def head():
 print("\n\nAs you have headache..","Take proper sleep as 
well as medicines!",sep="\n")
def throat():
 print("\n\nAs you have sore throat!!..You are advised to 
gargle daily with warm water.")
def voice():
 print("\n\nAs you have soarness of voice...take proper 
medicines")
 
l={1:"Fever",2:"Headache",3:"Cough",4:"Cold",5:"Sore 
throat",6:"Shortness of breath",7:"Coarness of voice"}
for i in l.values():
 print(j,i,sep=". ")
 j+=1
print('\nBased on this we are trying to check you out....',"Please 
be honest as it's your health only!!",sep="\n")
for i in range(0,70):
 print("_ ",end="")
print()
print("Please enter your name::",end=" ")
name=input()
print("Enter your age::",end=" ")
age=float(input())
print("Now lets start with the checkup!!\n")
for i in range(0,70):
 print("_ ",end="")
print()
for i in l:
 print("\nDo you have",l[i],"??")
 print("Enter","y :: yes","n::no",sep="\t")
 ch=input()
 if ch=='Y' or ch=='y':
 ll.append(i)
 count+=1
 if i==1:
 feve+=1
 elif i==2:
 hea+=1
 elif i==3:
 coug+=1
 elif i==4:
 col+=1
 elif i==5:
 throa+=1
 elif i==6:
 breat+=1
 elif i==7:
 voic+=1
 for ii in range(0,70):
 print("_ ",end="")
print("\nAs per your inputs, you have",count,"symptoms!!")
for i in ll:
 print(i,l[i],sep=". ")
print()
if count!=0:
 print("Now please tell us more some about these 
symptoms!!\n")
 if feve>0:
 fever()
 if hea>0:
 head()
 if coug>0:
 cough()
 if col>0:
 cold()
 if throa>0:
 throat()
 if breat>0:
 breath()
 if voic>0:
 voice()
# main code for detection of test:
for i in range(0,70):
 print("_ ",end="")
print()
if count==0:
 print("Plz tell have you visited another country (FOREIGN) 
before the happening of these symptoms?")
 print("Enter","y :: yes","n::no",sep="\t")
 coun=input()
 if coun=='Y' or coun=='y':
 print("Although you don't have any symptoms..But be 
inside your home only!!")
 elif coun=='N' or coun=='n':
 print("CONGRATS!! You don't have CORONA VIRUS!! BE 
SAFE and BE HEALTHY!")
 
elif count>0:
 print("Based on your inputs we have recoganized your 
case..")
 print("\nPlz tell have you visited another country (FOREIGN) 
before the happening of these symptoms?")
 print("Enter","y :: yes","n::no",sep="\t")
 country=input()
 if country=='Y' or country=='y': 
 if count==7 or count==6:
 print("Sorry! but according to your symptoms you have 
very risk of being infected!!")
 confirm+=1
 elif count>=4 and count<6:
 print("Immediately go for the test!!You have chances of 
CORONA VIRUS!!")
 ninety+=1
 elif count>=2 and count<=3:
 print("Although you have less symptoms,but still go for 
the CORONA test as life is precious!!!")
 quar+=1
 elif count==1:
 print("Very less chances of CORONA VIRUS!! But as you 
have visited other country..be safe!")
 less+=1
 print("And also you are recommended to be in the 
QUARANTINE STATE for atleast 14 days!!")
 elif country=='n' or country=='N':
 if count==7 or count==6:
 print("Sorry! but according to your symptoms you have 
very risk of being infected!!")
 exc+=1
 print("You are also advised to be in the QUARANTINE 
STATE for atleast 14 days!!")
 elif count==4 or count==5:
 print("Its normal....you have minor chances of corona 
virus!!, Just take common precautions only!")
 cured+=1
 else:
 print("You are safe!! no need to worry!! You dont have 
any CORONA VIRUS!!,But still take general precautions")
 none+=1
for i in range(0,70):
 print("_ ",end="")
print()
print("Printing the final details!!!!")
print("Name :: ",name)
print("Age :: ",int(age))
print("Result :: ",end=" ")
if confirm>0 or exc>0:
 print("You have more than 90% chance of CORONA VIRUS!!")
elif ninety>0:
 print("You have 80-90% chance of CORONA VIRUS!!")
elif quar>0:
 print("you have 40-50% chance of CORONA VIRUS!!")
elif less>0:
 print("you have 15-25% chance of CORONA VIRUS only!!")
elif cured>0:
 print("you have only 40-50% chance!! Dont worry it can be 
cured by general precautions as mentioned above earlier!")
elif none>0:
 print("You don't have CORONA VIRUS!!")
elif count==0 and (coun=='N' or coun=='n'):
 print("Free from CORONA!!")
elif count==0 and (coun=='Y' or coun=='y'):
 print("0 symptoms of CORONA, But have visited Foreign!!BE 
SAFE!!")
print("\nTHANKS FOR USING US!!")
for i in range(0,70):
 print("_ ",end="")
