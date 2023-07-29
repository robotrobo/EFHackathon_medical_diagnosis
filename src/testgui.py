import tkinter as tk
from tkinter import ttk

# Define the conversation and annotation
conversation = [
    ("Doctor", "Hey, how is your day going"),
    ("Patient", "I have a headache."),
    ("Doctor", "How long have you had it?"),
    ("Patient", "For about 2 days now."),
]
annotations = {
    "Diagnosis": "Possible tension headache",
    "Treatment": "Over-the-counter pain relievers, rest, stress management techniques",
    "Next Question": "Have you noticed any triggers for your headaches, such as stress or lack of sleep?",
    "Notes": "Further information is needed to confirm the diagnosis and provide more specific recommendations."
}

# Create the main window
root = tk.Tk()
root.title("Medical Conversation Interface")

# Create the frames
conversation_frame = ttk.LabelFrame(root, text="Conversation")
conversation_frame.pack(fill="both", expand=True, padx=10, pady=10)

annotation_frame = ttk.LabelFrame(root, text="Annotations")
annotation_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Add the conversation to the conversation frame
for role, line in conversation:
    color = "blue" if role == "Doctor" else "green"
    label = tk.Label(conversation_frame, text=f"{role}: {line}", fg=color)
    label.pack(anchor="w")

# Add the annotations to the annotation frame
for key, value in annotations.items():
    label = tk.Label(annotation_frame, text=f"{key}: {value}")
    label.pack(anchor="w")

# Start the main loop
root.mainloop()
