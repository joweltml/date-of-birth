# date-of-birth
#TAMALE JOEL JOSEPH
#16/U/11830/PS
#BSc COMPUTER ENGINEERING
import datetime,calendar

current_year = int(datetime.date.today().strftime('%Y'))

date = input("Enter day of birth  (1-31)\n")#This prompts the user to input his birth date ranging from 1-31

endings = ["st", "nd", "rd"]+ 17*["th"] + ["st", "nd", "rd"] + 7*["th"] + ["st"]

days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday']

month = int(input("Enter month you were born in(1-12)\n"))#This prompts the user to input his birth month ranging from 1-12

month_names = ['January','February','March','April','May','June','July','August','September','October','November','December']

age = int(input("How old are you now? \n"))#This prompts the user to input his age 

tj1 = month_names[month-1]
tj2 = int(date)
tj3 = (current_year-age)
tj4 = date+endings[tj2-1]
tj5 = calendar.weekday(tj3,month,tj2)
tj6 = days[tj5]

print("You were born on",tj6 ,tj4, tj1,"of the year \n" ,tj3)#returns the day of the month one was born and the year of birth.
print("Goodbye\n')
quit()
