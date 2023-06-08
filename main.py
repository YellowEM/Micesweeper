import tkinter as tk

ROW = 5
COLUMNS = 7
window = tk.Tk()
buttons = []
for i in range(ROW):
    temp = []
    for j in range(COLUMNS):
        btn = tk.Button(window, width=3,font='Calibri 15 bold')
        temp.append(btn)
    buttons.append(temp)

for i in range(ROW):
    for j in range(COLUMNS):
        btn = buttons[i][j]
        btn.grid(row=i, column=j)

window.mainloop()
