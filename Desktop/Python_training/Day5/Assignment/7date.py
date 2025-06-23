from datetime import datetime, timedelta

def calculate_date(input_date):
    
    try:
        # Convert to datetime object
        date_obj = datetime.strptime(input_date, "%Y-%m-%d %H:%M:%S")

        #  Define time to add (7 days + 12 hours)
        added_time = timedelta(days=7, hours=12)

        # add the time
        new_date = date_obj + added_time

        #  Print the result
        print("New Date:", new_date.strftime("%Y-%m-%d %H:%M:%S"))

    except Exception as e:
        print(f"Error: {e}")


input_date = "2020-03-21 10:00:00"
calculate_date(input_date)