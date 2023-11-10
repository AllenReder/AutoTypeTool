import tkinter as tk

def getArgsFromWindow():
    """
    Get the arguments from the window.
    """
    text = interval = delay = None
    def saveInput():
        """
        The callback function of the button.
        """
        nonlocal text, interval, delay
        text = tk_text_text.get("1.0", "end") 
        interval = tk_entry_interval.get()
        delay = tk_entry_delay.get()
        root.destroy()

    # create a window
    root = tk.Tk()

    # create some widgets
    tk_label_text = tk.Label(root, text="Text:")
    tk_text_text = tk.Text(root, height=5, width=30)
    tk_label_interval = tk.Label(root, text="interval(s):")
    tk_entry_interval = tk.Entry(root)
    tk_entry_interval.insert(0, "0.1")
    tk_label_delay = tk.Label(root, text="delay(s):")
    tk_entry_delay = tk.Entry(root)
    tk_entry_delay.insert(0, "3")
    tk_button = tk.Button(root, text="确定", command=saveInput)

    # pack the widgets
    tk_label_text.grid(row=0, column=0)
    tk_text_text.grid(row=0, column=1)
    tk_label_interval.grid(row=1, column=0)
    tk_entry_interval.grid(row=1, column=1)
    tk_label_delay.grid(row=2, column=0)
    tk_entry_delay.grid(row=2, column=1)
    tk_button.grid(row=3, column=1)

    root.mainloop()
    if text == None:
        exit(0)
    return str(text), float(interval), float(delay)