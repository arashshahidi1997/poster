import os
from pathlib import Path

# List of GIF file names (place them in a "gifs" folder on GitHub)
gif_folder = "gifs"  # Change this if you want to organize differently
gif_files_ = ["spectral_power_map_sws.gif"]

# Full path for saving the HTML file on your local machine
script_path = Path(__file__).resolve().parent
HTML_FILE_ = "swd_project_summary.html"
HTML_FILE = str(script_path / HTML_FILE_)

# Create the HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GIFs Display</title>
</head>
<body>
    <h1>My GIFs Collection</h1>
"""

# Loop through the list of GIFs and add them to the HTML content using relative paths
for gif in gif_files_:
    html_content += f'<div><img src="{gif_folder}/{gif}" alt="{gif}" width="400"></div>\n'

# Close the HTML tags
html_content += """
</body>
</html>
"""

# Write the HTML content to a file locally
with open(HTML_FILE, "w") as html_file:
    html_file.write(html_content)

print(f"HTML file '{HTML_FILE_}' created successfully!")