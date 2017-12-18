import tkinter as tk

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="gray")

        frame = tk.Frame(background="white", borderwidth=1, relief="sunken",
                         highlightthickness=1)
        frame.pack(side="top", fill="x", padx=4, pady=4)

        entry = tk.Entry(frame, borderwidth=0, highlightthickness=0, background="white")
        entry.image = tk.PhotoImage(data=cancelImageData)
        imageLabel = tk.Label(frame, image=entry.image)
        imageLabel.pack(side="right", fill="y")
        entry.pack(side="left", fill="both", expand=True)

        root.tk.call('wm', 'iconphoto', root._w, entry.image)

cancelImageData = '''
    R0lGODlhEAAQAPcAAAAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr
    /wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCq
    mQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMA
    MzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV
    /zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPV
    mTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYr
    M2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA
    /2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/
    mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlV
    M5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq
    /5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswA
    mcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyA
    M8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV
    /8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8r
    mf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+q
    M/+qZv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP//
    /wAAAAAAAAAAAAAAACH5BAEAAPwALAAAAAAQABAAAAiWAPcJHEiwYEFpCBMiNLhP
    WjZz4CB+A5dN2sGH2TJm+7ax4kCHEOlx3EgPHEeLDc1loydwokB6G1EJlEYRHMt6
    +1hW/IaSpreN+/ThzIYq5kyKGffV07ePpzSeMzl+UypU6aunMhtSdCcwI0t606A2
    3PjN3VVXK2NO+/iKIzZp0xB+Q4Xt4re7te4WZSgNVV+EfhkKLhgQADs=
'''

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()
