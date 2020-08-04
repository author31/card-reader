import tkinter as tk
import gspread
import pandas as pd
import PySimpleGUI as sg
from datetime import datetime
from gspread.models import Cell
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('sample.json', scope) 
gc = gspread.authorize(credentials)

def nAvailable(worksheet):
    rs = len(worksheet.col_values(1))+1
    return rs


class Tap(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.ent_input = tk.Entry(width=45)
        button = tk.Button(self, text="Enter")
        self.lbl_res = tk.Label(text="")
        self.lbl_id = tk.Label(text="ID")

        self.ent_input.place(x=45,width=50)
        self.lbl_id.place(x=0,y=0)
        self.lbl_res.pack()
        button.place(x=0,y=30)
        self.bind("<Return>",self.checking)
        
    def checking(self,event):
        temp=[]
        data = gc.open("Name").sheet1
        record = gc.open("Record").sheet1
        vals = data.get_all_values()
        df = pd.DataFrame(vals)
        rs = nAvailable(record)
        result = list(df[df[1].astype(str)==self.ent_input.get()][0])[0]
        self.lbl_res["text"] = result
        now = datetime.now()
        curT = now.strftime("%Y-%m-%d, %H:%M:%S")
        temp.append(Cell(rs,1,result))
        temp.append(Cell(rs,2,curT))
        self.ent_input.delete(0,tk.END)
        return record.update_cells(temp)


if __name__ == "__main__":
    tap = Tap()
    tap.mainloop()