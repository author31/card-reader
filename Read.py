import tkinter as tk
import gspread
import pandas as pd
import PySimpleGUI as sg
from oauth2client.service_account import ServiceAccountCredentials
from gspread.models import Cell

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('sample.json', scope) 
gc = gspread.authorize(credentials)

def nAvailable(worksheet):
    avail = len(worksheet.col_values(1))+1
    return avail



class Reader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x200")
        self.ent_name = tk.Entry(width=45)
        self.ent_id = tk.Entry(width=45)
        button = tk.Button(self, text="Enter")
        lbl_name = tk.Label(text="Name")
        lbl_id = tk.Label(text="ID")

        self.ent_name.place(x=40,y=0,width=150,height=20)
        self.ent_id.place(x=40,y=25,width=150,height=20)
        lbl_name.place(x=0,y=0)
        lbl_id.place(x=0,y=25)
        button.place(x=40,y=50,width=50)
        self.bind("<Return>",self.writing)
        button.bind("<Button-1>",self.writing)
        
        
    def writing(self,event):
        temp =[]
        table = gc.open("Name").sheet1
        rs = nAvailable(table)
        temp.append(Cell(rs,1,self.ent_name.get()))
        temp.append(Cell(rs,2,self.ent_id.get()))
        self.ent_name.delete(0,tk.END)
        self.ent_id.delete(0,tk.END)
        return table.update_cells(temp)


if __name__ == "__main__":
    read = Reader()
    read.mainloop()