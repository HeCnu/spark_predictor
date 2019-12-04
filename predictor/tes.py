import random
from tkinter import *
from tkinter.scrolledtext import ScrolledText

kolvoznachenii = 100
dopchislo = 123456
clicks = 0

def func_connect_to_BD():
    return 0


def func_generate_List(List):
    for number in range(9999):
        variable = random.randint(100000, 999999)
        List.append(variable)
    return List


def func_show_num_of_info(List, numofinfo):
    showList = []
    for number in range(0, numofinfo):
        showList.append(List[number])
    return showList


def func_analize_List(List, numofpredict):
    ListOfPredicted = []
    newnumofpred1 = list(map(int, str(numofpredict)))

    for number in range(len(List) - 1):
        VarOfPredicted = []
        z_Place = 0
        z_Number = 0
        newnumofpred2 = list(map(int, str(List[number])))
        newnumofpred2_1 = []

        for i in range(6):
            if newnumofpred1[i] == newnumofpred2[i]:
                z_Place += 1
            else:
                newnumofpred2_1.append(newnumofpred2[i])

        for key2 in newnumofpred2_1:
            for key1 in newnumofpred1:
                if key1 == key2:
                    z_Number += 1

        VarOfPredicted.append(List[number])
        VarOfPredicted.append(z_Place)
        VarOfPredicted.append(z_Number)
        ListOfPredicted.append(VarOfPredicted)

    return ListOfPredicted

def create_window(List):

    def click_button():
        global clicks
        clicks += 1
        root.title("Clicks {}".format(clicks))

    def invert_text(arr):
        text = ""

        for i in arr:
            text += str(i)
            text += "\n"

        return text

    root = Tk()
    root.title("Графическая программа на Python")
    root.geometry("600x600")

    btn_output = Button(text="Click",
                 background="#555",
                 foreground="#ccc",
                 padx="20",
                 pady="10",
                 font="16",
                 command = click_button
                 )

    btn_output.pack()
    frame1 = Frame()
    frame1.pack(fill="both", expand="yes")
    editArea = ScrolledText(
        master=frame1,
        wrap=WORD
    )
    editArea.pack(padx=10,pady=10, fill=BOTH, expand=True)
    editArea.insert(INSERT, invert_text(List))
    """label1 = Label(text=List, fg="#333", bg="#aaa", wraplength=300)
    label1.pack(side=LEFT, padx=5)"""

    root.mainloop()

generatedList = []
generatedList = func_generate_List(generatedList)
generatedList = func_show_num_of_info(generatedList, kolvoznachenii)

newgen = func_analize_List(generatedList, dopchislo)

create_window(newgen)