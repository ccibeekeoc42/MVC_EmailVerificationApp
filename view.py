from tkinter import END, ttk
import tkinter as tk


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # label
        self.label = ttk.Label(self, text='Email:')
        self.label.grid(row=1, column=0)

        # email entry
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(
            self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(
            self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # retrieve button
        self.retrieve_button = ttk.Button(
            self, text='Retrieve', command=self.retrieve_button_clicked)
        self.retrieve_button.grid(row=1, column=4, padx=0)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        '''Sets the controller'''
        self.controller = controller

    def save_button_clicked(self):
        '''Handles the save button click event'''
        if self.controller:
            self.controller.save(self.email_var.get())

    def retrieve_button_clicked(self):
        '''Handles the retrieve button click event'''
        if self.controller:
            text = self.controller.retrieve()
            print(text)
            self.email_entry.delete(0, END)
            self.email_entry.insert(0, text)

    def show_error(self, message):
        '''Show an error message'''
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        '''Show a success message'''
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        '''Hide the message'''
        self.message_label['text'] = ''
