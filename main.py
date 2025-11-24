from datetime import datetime, timedelta

def calculate_time_difference(date_start_str, date_end_str, date_format="%Y-%m-%d %H:%M:%S":
    try:
        # Convert the date strings into datetime objects
        date_start = datetime.strptime(date_start_str, date_format)
        date_end = datetime.strptime(date_end_str, date_format)

        # Calculate the time difference (timedelta object)
        time_difference = date_end - date_start

        # Calculate the total difference in seconds
        total_seconds = int(time_difference.total_seconds())

        # Breakdown using modulo arithmetic for the *remaining* time
        remaining_seconds = total_seconds
        
        # Calculate remaining days and update remaining_seconds
        remaining_days = remaining_seconds // 86400  # 86400 seconds in a day
        remaining_seconds %= 86400

        # Calculate remaining hours and update remaining_seconds
        remaining_hours = remaining_seconds // 3600  # 3600 seconds in an hour
        remaining_seconds %= 3600

        # Calculate remaining minutes and remaining seconds
        remaining_minutes = remaining_seconds // 60
        remaining_seconds %= 60

        return {
            "timedelta": time_difference,
            "total_days": time_difference.days,
            "total_hours": total_seconds // 3600,
            "total_minutes": total_seconds // 60,
            "total_seconds": total_seconds,
            "difference_breakdown": {
                "days": remaining_days,
                "hours": remaining_hours,
                "minutes": remaining_minutes,
                "seconds": remaining_seconds
            }
        }

    except ValueError as e:
        print(f"Error parsing date strings: {e}")
        return None

# --- Example Usage ---

# 1. Define the date strings and their format (CHANGE THESE VALUES)
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
date1 = "2025-11-20 10:00:00"
date2 = "2025-11-24 15:30:45"

print(f"Start Date: {date1}")
print(f"End Date:   {date2}")
print("-" * 30)

# 2. Call the function
result = calculate_time_difference(date1, date2, DATE_FORMAT)

# 3. Print the results
if result:
    print(f"Time Difference: {result['timedelta']}")
    print("\n--- Total Difference ---")
    print(f"Total Days:    {result['total_days']}")
    print(f"Total Hours:   {result['total_hours']}")
    print(f"Total Minutes: {result['total_minutes']}")

    print("\n--- Difference Breakdown (Days, HH:MM:SS) ---")
    breakdown = result['difference_breakdown']
    print(f"Days:    {breakdown['days']}")
    print(f"Hours:   {breakdown['hours']}")
    print(f"Minutes: {breakdown['minutes']}")
    print(f"Seconds: {breakdown['seconds']}")
