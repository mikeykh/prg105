# Write a GUI program that translates the numbers one through five in any foreign language to English. The window should have five buttons, one for each number. When the user clicks a button, the program displays the English translation in a label.

# Document your code with comments, upload to GitHub and hand in the link.

import tkinter


class MyGUI:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Create StringVar objects to display name,
        # street, and city-state-zip
        self.english_value = tkinter.StringVar()

        # Create two frames
        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create the label widgets associated with the StringVar objects
        self.english_label = tkinter.Label(self.info_frame,
                                           textvariable=self.english_value)

        # Pack the labels
        self.english_label.pack()

        # Create two buttons
        self.button1 = tkinter.Button(self.button_frame,
                                      text='1',
                                      command=self.one)
        self.button2 = tkinter.Button(self.button_frame,
                                      text='2',
                                      command=self.two)
        self.button3 = tkinter.Button(self.button_frame,
                                      text='3',
                                      command=self.three)
        self.button4 = tkinter.Button(self.button_frame,
                                      text='4',
                                      command=self.four)
        self.button5 = tkinter.Button(self.button_frame,
                                      text='5',
                                      command=self.five)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the buttons
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        self.quit_button.pack()

        # Pack the frames
        self.info_frame.pack()
        self.button_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Callback function for the Show Info button
    def one(self):
        self.english_value.set('One')

    def two(self):
        self.english_value.set('Two')

    def three(self):
        self.english_value.set('Three')

    def four(self):
        self.english_value.set('Four')

    def five(self):
        self.english_value.set('Five')

# Create an instance of the MyGUI class
my_gui = MyGUI()
