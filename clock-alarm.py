import tkinter as tk
import datetime
import winsound

def set_alarm():
    alarm_time = entry.get()
    try:
        alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M")
        current_time = datetime.datetime.now().strftime("%H:%M")

        if alarm_time < datetime.datetime.strptime(current_time, "%H:%M"):
            alarm_time = alarm_time + datetime.timedelta(days=1)

        time_difference = alarm_time - datetime.datetime.strptime(current_time, "%H:%M")
        seconds = time_difference.seconds

        root.after(seconds * 1000, play_alarm)

        status_label.config(text="Alarm set for: " + alarm_time.strftime("%H:%M"))
    except ValueError:
        status_label.config(text="Invalid time format! Use HH:MM")

def play_alarm():
    # Play sound
    winsound.Beep(440, 1000)

def stop_alarm():
    root.after_cancel(play_alarm)

root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Enter alarm time (HH:MM):")
label.pack()

entry = tk.Entry(root)
entry.pack()

set_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

stop_button = tk.Button(root, text="Stop Alarm", command=stop_alarm)
stop_button.pack()

root.mainloop()
