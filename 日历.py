import calendar

# Set the first weekday to Sunday
calendar.setfirstweekday(calendar.SUNDAY)

# Define the years and the months we are interested in
years = [2024, 2025, 2026]
months = [6, 7, 8]

# Function to print the calendar for a specific month and year
def print_month_calendar(year, month):
    month_cal = calendar.monthcalendar(year, month)
    print(calendar.month_name[month], year)
    print("Su Mo Tu We Th Fr Sa")
    for week in month_cal:
        print(" ".join(f"{day:2}" if day != 0 else "  " for day in week))
    print()

# Print the calendars for June, July, and August of 2024, 2025, and 2026
for year in years:
    for month in months:
        print_month_calendar(year, month)
