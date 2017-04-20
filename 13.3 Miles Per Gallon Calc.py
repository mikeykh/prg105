# Write a GUI program that calculates a car’s gas mileage. The program’s window should have Entry widgets that let the user enter the number of gallons of gas the car holds, and the number of miles it can be driven on a full tank. When a Calculate MPG button is clicked, the program should display the number of miles that the car may be driven per gallon of gas. Use the following formula to calculate miles per gallon:
# MPG = miles / gallons
# Document appropriately with comments, upload to GitHub and hand in a link to the code.

import tkinter


class MpG:
    def __init__(self):

        # Create the main window
        self.main_window = tkinter.Tk()

        # Create four frames to group widgets
        self.top_frame = tkinter.Frame()
        self.next_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widget for the top frame
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Enter the number of gallons of gas your car holds:')
        self.gallons_entry = tkinter.Entry(self.top_frame,
                                           width=5)

        # Pack the top_frame widgets
        self.prompt_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        # Create the widget for the second frame
        self.prompt_label2 = tkinter.Label(self.next_frame,
                                           text='Enter the number of miles your car can be driven on a full tank:')
        self.miles_entry = tkinter.Entry(self.next_frame,
                                         width=5)

        # Pack the next_frame widgets
        self.prompt_label2.pack(side='left')
        self.miles_entry.pack(side='left')

        # Create widgets for the middle frame
        self.descr_label = tkinter.Label(self.mid_frame,
                                         text='MPG:')

        # Store a string of blank characters with the objects set method
        self.value = tkinter.StringVar()

        # Create a label and associate it StringVar
        # Any value stored in StringVar will be displayed in label
        self.MPG_label = tkinter.Label(self.mid_frame,
                                       textvariable=self.value)

        # Pack the middle frame's widget
        self.descr_label.pack(side='left')
        self.MPG_label.pack(side='left')

        # Create a Quit Button and Calc Button for bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text='Calculate',
                                          command=self.convert)

        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        # Pack the Buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the Frames
        self.top_frame.pack()
        self.next_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # The convert method is a callback function for the Calc button
    def convert(self):
        # Get the value entered by the user into the
        gallons = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())

        # Convert kilometers to miles
        miles_per_gallon = miles / gallons

        # Convert miles to a string and store it in StringVar
        self.value.set(miles_per_gallon)

# Create an instance of the MpG class
kilo_conv = MpG()
