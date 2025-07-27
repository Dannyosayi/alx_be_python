from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    
    # Format: YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    try:
        # Prompt user for number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        # Calculate future date
        future_date = datetime.now() + timedelta(days=days_to_add)
        
        # Print future date in YYYY-MM-DD format
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Please enter a valid number.")

# Run the functions
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
