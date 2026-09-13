import tkinter as tk
from tkinter import ttk
from datetime import datetime


root = tk.Tk()

root.title("Real-Time Transaction Risk System")
root.geometry("800x650")


# -----------------------------
# Title
# -----------------------------

title_label = ttk.Label(
    root,
    text="REAL-TIME TRANSACTION RISK SYSTEM",
    font=("Arial", 20, "bold")
)

title_label.pack(pady=20)


# -----------------------------
# Transaction Details
# -----------------------------

transaction_frame = ttk.LabelFrame(
    root,
    text="Transaction Details",
    padding=15
)

transaction_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


ttk.Label(
    transaction_frame,
    text="Transaction ID:"
).grid(row=0, column=0, padx=10, pady=8, sticky="w")

transaction_id_entry = ttk.Entry(
    transaction_frame,
    width=40
)

transaction_id_entry.grid(row=0, column=1, padx=10, pady=8)


ttk.Label(
    transaction_frame,
    text="User ID:"
).grid(row=1, column=0, padx=10, pady=8, sticky="w")

user_id_entry = ttk.Entry(
    transaction_frame,
    width=40
)

user_id_entry.grid(row=1, column=1, padx=10, pady=8)


ttk.Label(
    transaction_frame,
    text="Amount:"
).grid(row=2, column=0, padx=10, pady=8, sticky="w")

amount_entry = ttk.Entry(
    transaction_frame,
    width=40
)

amount_entry.grid(row=2, column=1, padx=10, pady=8)


# -----------------------------
# Location Details
# -----------------------------

location_frame = ttk.LabelFrame(
    root,
    text="Location Details",
    padding=15
)

location_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


ttk.Label(
    location_frame,
    text="Latitude:"
).grid(row=0, column=0, padx=10, pady=8, sticky="w")

latitude_entry = ttk.Entry(
    location_frame,
    width=40
)

latitude_entry.grid(row=0, column=1, padx=10, pady=8)


ttk.Label(
    location_frame,
    text="Longitude:"
).grid(row=1, column=0, padx=10, pady=8, sticky="w")

longitude_entry = ttk.Entry(
    location_frame,
    width=40
)

longitude_entry.grid(row=1, column=1, padx=10, pady=8)


# -----------------------------
# Transaction Context
# -----------------------------

context_frame = ttk.LabelFrame(
    root,
    text="Transaction Context",
    padding=15
)

context_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


ttk.Label(
    context_frame,
    text="Recipient ID:"
).grid(row=0, column=0, padx=10, pady=8, sticky="w")

recipient_entry = ttk.Entry(
    context_frame,
    width=40
)

recipient_entry.grid(row=0, column=1, padx=10, pady=8)


ttk.Label(
    context_frame,
    text="Device ID:"
).grid(row=1, column=0, padx=10, pady=8, sticky="w")

device_entry = ttk.Entry(
    context_frame,
    width=40
)

device_entry.grid(row=1, column=1, padx=10, pady=8)


ttk.Label(
    context_frame,
    text="IP Address:"
).grid(row=2, column=0, padx=10, pady=8, sticky="w")

ip_entry = ttk.Entry(
    context_frame,
    width=40
)

ip_entry.grid(row=2, column=1, padx=10, pady=8)


# -----------------------------
# Send Transaction
# -----------------------------

def send_transaction():

    transaction_id = transaction_id_entry.get()
    user_id = user_id_entry.get()
    amount = amount_entry.get()

    latitude = latitude_entry.get()
    longitude = longitude_entry.get()

    recipient_id = recipient_entry.get()
    device_id = device_entry.get()
    ip_address = ip_entry.get()

    timestamp = datetime.now().isoformat()

    print("\n--- TRANSACTION ---")
    print("Transaction ID:", transaction_id)
    print("User ID:", user_id)
    print("Amount:", amount)
    print("Timestamp:", timestamp)
    print("Latitude:", latitude)
    print("Longitude:", longitude)
    print("Recipient ID:", recipient_id)
    print("Device ID:", device_id)
    print("IP Address:", ip_address)


send_button = ttk.Button(
    root,
    text="SEND TRANSACTION",
    command=send_transaction
)

send_button.pack(pady=15)


root.mainloop()
