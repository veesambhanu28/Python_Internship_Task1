
# Program to print your name, internship role, and today's date

from datetime import date  # Import date module

# Take input from user
my_name = input("Enter your name: ")          
internship_role = input("Enter your role: ")  

# Get today's date
today_date = date.today()  # Fetch today's date automatically

print("\n--- User Information ---")
print("Name:", my_name)
print("Role:", internship_role)
print("Date:", today_date)

