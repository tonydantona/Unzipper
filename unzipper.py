import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from main import initiate_unzipper

root = tk.Tk()
root.title('Unzipper')
root.geometry('600x400')
root.iconbitmap('zipper.ico')


def select_source_folder():
    root.folder = filedialog.askdirectory(initialdir='/', title='Select Source')
    entry_src_path.insert(0, root.folder)


def select_dest_folder():
    root.folder = filedialog.askdirectory(initialdir='/', title='Select Destination')
    entry_dest_path.insert(0, root.folder)


def unzip():
    status_label['text'] = 'Status: unzipping...'
    initiate_unzipper(entry_src_path.get(), entry_dest_path.get())
    status_label['text'] = 'Status: done'
    print(entry_src_path.get())
    print(entry_dest_path.get())


# select source
button_select_src = tk.Button(root, text='Select Source Folder', command=select_source_folder)
button_select_src.pack(pady=(50, 10))

entry_src_path = ttk.Entry(root, width=35)
entry_src_path.pack(pady=(0, 30))

# select destination
button_select_dest = tk.Button(root, text='Select Destination Folder', command=select_dest_folder)
button_select_dest.pack(pady=(30, 10))

entry_dest_path = ttk.Entry(root, width=35)
entry_dest_path.pack(pady=(0, 30))


# unzip
button_unzip = tk.Button(root, text='Unzip', width=10, command=unzip)
button_unzip.pack(pady=(50, 50))

status_label = tk.Label(root, width=400, text='Status: ', relief='sunken', bd=1, anchor='w')
status_label.pack(side='bottom', padx=(0, 0))

root.mainloop()
