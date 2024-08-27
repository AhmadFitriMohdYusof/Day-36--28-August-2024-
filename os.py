import os

# Check if the "data" directory does not exist
if not os.path.exists("data"):
    # Create the "data" directory
    os.mkdir("data")

# Loop from 0 to 99 (100 iterations)
#for i in range(0, 100):
    # Create a directory named "DayX" inside the "data" directory, where X is the current loop index + 1
    #os.mkdir(f"data/Day{i+1}")

import os

for i in range(0, 100):
    os.rename(f"data/Day{i+1}", f"data/tutorial{i+1}")
