import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Create a pandas DataFrame from the given data
data = {
    "Artefact": [
        "128K",
        "A tweet",
        "Book page (Robinson Crusoe)",
        "Google Results Page (copy/paste, txt)",
        "apple.com (copy/paste, txt)",
        "StackOverflow Question",
        "Blog post (Markdown)",
        "Linux Kernel average source file",
        "SCRUM Guide (2020)",
        "Wikipedia page (Albania, copy/paste, txt)",
        "Wikipedia page (Albania, source, wikitext)",
        "apple.com (source, HTML)",
        "The Lean Startup book",
        "PM BoK (4th edition, 2008)",
        "Google Results Page (source, HTML)",
        #"Linux Kernel largest source file",
    ],
    "Tokens": [
        128000, 76, 282, 975, 997, 1037, 4572, 5205, 5440, 42492, 76462, 92091, 113264, 228880, 246781, #69039016
    ],
}
df = pd.DataFrame(data)

# Normalize the data
df["Normalized"] = df["Tokens"] / df["Tokens"].sum()

colors = plt.get_cmap('viridis')(np.linspace(0, 1, len(df))).tolist()

# Function to create rectangle
def rectangle(area, aspect_ratio=1):
    width = np.sqrt(area * aspect_ratio)
    height = area / width
    return width, height

# Function to update and animate the rectangles
def update(num, df, rectangles, labels):
    rects, labs = [], []
    xlim, ylim = 0, 0
    for n in range(num+1):
        width, height = rectangle(df["Normalized"].iloc[n])
        rect = patches.Rectangle((xlim, ylim), width, height, linewidth=1, edgecolor='black', facecolor=colors[n], alpha=0.8)
        ax.add_patch(rect)
        rects.append(rect)
        # xlim += width
        # ylim += height

        label = ax.text(xlim - width / 2, ylim - height / 2, df["Artefact"].iloc[n],
                        fontsize=8, ha='center', va='center', rotation=0)
        labs.append(label)

    for r in rectangles:
        if r not in rects:
            r.set_alpha(0)
    for lbl in labels:
        if lbl not in labs:
            lbl.set_visible(False)

    return rects, labs


# Initialize the plot
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel("Artefact token size (normalized)")
ax.set_ylabel("Artefact token size (normalized)")
ax.set_title("Comparing Artefacts within the 128K tokens context")
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')

rectangles = []
labels = []

# Create and save the animation
ani = FuncAnimation(fig, update, len(df), fargs=(df, rectangles, labels), interval=1000, blit=False)
ani.save("animated_diagonal_barchart.mp4", writer="ffmpeg", dpi=150)

plt.show()