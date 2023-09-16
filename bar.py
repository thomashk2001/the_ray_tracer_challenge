import time
from tqdm import tqdm

# Define the total number of iterations
total_iterations = 1000

# Create a tqdm object to display the progress bar
progress_bar = tqdm(total=total_iterations, desc="Processing")

# Simulate a task that takes some time
for i in range(total_iterations):
    # Perform your task here
    time.sleep(0.1)  # Simulating work with a sleep

    # Update the progress bar
    progress_bar.update(1)

# Close the progress bar
progress_bar.close()

print("Task completed!")
