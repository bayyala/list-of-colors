#Enter a list of ten colours. Ask the user for a starting number between 0 and 4 and an end number between 5 and 9. Display the list for those colours between that start and end numbers the user input.  

print(" \n\n  LIST OF 10 COLOURS  ")
print(" ------------------- \n")
colorlist=[ "0=Red ", "1=Blue","2=Pink","3=Green ","4=Black","5=Brown", 
 "6=White","7=Voilet","8=Purple","9=Yellow" ] #LIST OF 10 COLOURS

for i in range(len(colorlist)):
 print(colorlist[i])
 length=(len(colorlist))

print("\n Enter the start and end numbers to display the list the  colours between")
  
start=int(input("\n Please enter the starting number btween 0 and 4:= ")) #Enter the start num between 0 & 4

end=int(input("\n Please enter the ending number between  5 and 9:= ")) #Enter the end num between 5 & 9
y=(colorlist[start : end])

print("\n COLOURS BETWEEN THE CHOSEN NUMBERS ARE: ")

print("\n", y,"\n") #list for those colours between that start and end numbers the user input.   
