from datetime import datetime, timezone


def print_times():
    # Get the current local time
    local_time = datetime.now()

    # Format the local time as a string
    formatted_local_time = local_time.strftime("%Y-%m-%d %H:%M:%S")

    # Get the current time in GMT
    gmt_time = datetime.now(timezone.utc)

    # Format the GMT time as a string
    formatted_gmt_time = gmt_time.strftime("%Y-%m-%d %H:%M:%S")

    # Print the local time and GMT time
    print(f"Current local time: {formatted_local_time}")
    print(f"Current GMT time: {formatted_gmt_time}")


if __name__ == "__main__":
    print_times()

