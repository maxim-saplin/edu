import subprocess
import csv
import json

# Define the command to invoke yt-dlp
command = [
    'yt-dlp',
    '-j',  # Output the info as JSON lines
    '--skip-download',  # Don't download video files
    f'https://www.youtube.com/c/AutoTopnl'
]

# Run the command and capture the output
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
output, error = process.communicate()

# Check if there was an error
if process.returncode != 0:
    print(f'Error fetching video data: {error}')
else:
    # Split the output by lines as each line is a JSON object
    lines = output.strip().split('\n')

    # Parse JSON lines and extract the desired information
    videos_info = []
    for line in lines:
        video_data = json.loads(line)
        title = video_data.get('title')
        upload_date = video_data.get('upload_date')
        view_count = video_data.get('view_count')
        videos_info.append([title, upload_date, view_count])

    # Write the video information to a CSV file
    csv_filename = 'channel_videos.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Upload Date', 'Views'])  # Write the header
        writer.writerows(videos_info)  # Write video data

    print(f'Data for all videos from the channel has been saved to {csv_filename}')