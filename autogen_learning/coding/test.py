import subprocess


def list_volumes():
    try:
        # Use the 'df' command to list mounted volumes
        result = subprocess.run(["df", "-h"], capture_output=True, text=True)

        # Parse and print the output
        lines = result.stdout.splitlines()
        for line in lines[1:]:  # Skip the header
            columns = line.split()
            if len(columns) > 0:
                print(
                    f"Volume: {columns[-1]}, Size: {columns[1]}, Used: {columns[2]}, Available: {columns[3]}, Use%: {columns[4]}"
                )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    list_volumes()
