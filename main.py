import tkinter as tk
from ttkthemes import ThemedTk
import matplotlib.pyplot as plt
from persiantools.jdatetime import JalaliDate

# Window
window = ThemedTk(theme="arc")
window.title("Nemigzare")
window.geometry("300x200")
window.resizable(False, False)

# Status Bar
status_var = tk.StringVar()
status_bar = tk.Label(window, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Defaults
default_tarikh = JalaliDate.today().strftime("%Y/%m/%d")
default_kasri = "0"
default_post = "3"
default_nezam = "24 mah"


# Form
def submit_form():
    tarikh = tarikh_entry.get()
    kasri = int(kasri_entry.get())
    post = int(post_entry.get())
    nezam = int(nezam_entry.get().split(" ")[0])  # Remove the "mah" part

    # Calculate remaining days, weeks, and months
    # current_date = datetime.date.today()
    current_date = JalaliDate.today()
    selected_date = JalaliDate(int(tarikh[:4]), int(tarikh[5:7]), int(tarikh[8:]))
    difference = current_date - selected_date
    remaining_days = ((nezam * 30) + (int(nezam / 12) * 5)) - difference.days - kasri
    remaining_weeks = remaining_days // 7
    remaining_months = remaining_days // 30
    remaining_posts = post * remaining_months

    # Show results
    status_var.set(
        f"Ruz: {remaining_days} | "
        f"Hafte: {remaining_weeks} | "
        f"Mah: {remaining_months} | "
        f"Post: {remaining_posts}"
    )

    # Graph
    labels = ["Days", "Weeks", "Months"]
    values = [remaining_days, remaining_weeks, remaining_months]
    plt.bar(labels, values)
    plt.xlabel("Time")
    plt.ylabel("Remaining")
    plt.title("Remaining Time")
    plt.show()


# Reset to defaults
def reset_form():
    tarikh_entry.delete(0, tk.END)
    tarikh_entry.insert(tk.END, default_tarikh)
    kasri_entry.delete(0, tk.END)
    kasri_entry.insert(tk.END, default_kasri)
    post_entry.delete(0, tk.END)
    post_entry.insert(tk.END, default_post)
    nezam_entry.delete(0, tk.END)
    nezam_entry.insert(tk.END, default_nezam)


# Tarikh
tarikh_frame = tk.Frame(window)
tarikh_frame.pack(side=tk.TOP, anchor=tk.W)
tarikh_label = tk.Label(tarikh_frame, text="Tarikh:")
tarikh_label.pack(side=tk.LEFT)
tarikh_entry = tk.Entry(tarikh_frame)
tarikh_entry.pack(side=tk.RIGHT, padx=23)
tarikh_entry.insert(tk.END, default_tarikh)

# Kasri
kasri_frame = tk.Frame(window)
kasri_frame.pack(side=tk.TOP, anchor=tk.W)
kasri_label = tk.Label(kasri_frame, text="Kasri:")
kasri_label.pack(side=tk.LEFT)
kasri_entry = tk.Entry(kasri_frame)
kasri_entry.pack(side=tk.RIGHT, padx=30)
kasri_entry.insert(tk.END, default_kasri)

# Post
post_frame = tk.Frame(window)
post_frame.pack(side=tk.TOP, anchor=tk.W)
post_label = tk.Label(post_frame, text="Post:")
post_label.pack(side=tk.LEFT)
post_entry = tk.Entry(post_frame)
post_entry.pack(side=tk.RIGHT, padx=32)
post_entry.insert(tk.END, default_post)

# Nezam
nezam_frame = tk.Frame(window)
nezam_frame.pack(side=tk.TOP, anchor=tk.W)
nezam_label = tk.Label(nezam_frame, text="Nezam:")
nezam_label.pack(side=tk.LEFT)
nezam_entry = tk.Entry(nezam_frame)
nezam_entry.pack(side=tk.RIGHT, padx=18)
nezam_entry.insert(tk.END, default_nezam)

# Button frame
button_frame = tk.Frame(window)
button_frame.pack(side=tk.RIGHT, anchor=tk.SE)

# Submit button
submit_button = tk.Button(button_frame, text="Submit", command=submit_form)
submit_button.pack(side=tk.RIGHT, padx=5, pady=7)

# Reset button
reset_button = tk.Button(button_frame, text="Reset", command=reset_form)
reset_button.pack(side=tk.RIGHT, padx=5, pady=7)

# Run
window.mainloop()
