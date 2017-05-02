# A county collects property taxes on the assessment value of property, which is 60% of the property's actual value. If an acre of land is valued at $10,000, its assessment value is $6,000. The property tax is then $.75 for each $100 of the assessment value. The tax for the acre assessed at $6,000 will be $45.00. Write a GUI program that displays the assessment value and property tax when a user enters in the actual value of a property.
# Upload to GitHub and hand in link.
# Document appropriately with comments.

import tkinter


class Tax:
    def __init__(self):

        # Create the main window
        self.main_window = tkinter.Tk()

        # Create four frames to group widgets
        self.top_frame = tkinter.Frame()
        self.next_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Enter the actual value of a property:')
        self.value_entry = tkinter.Entry(self.top_frame,
                                         width=8)

        # Pack the top_frame widgets
        self.prompt_label.pack(side='left')
        self.value_entry.pack(side='left')

        # Create widgets for the next frame
        self.assessment_label = tkinter.Label(self.next_frame,
                                              text='Assessment Value: ')

        # Store a string of blank characters with the objects set method
        self.value1 = tkinter.StringVar()

        # Create a label and associate it StringVar
        # Any value stored in StringVar will be displayed in label
        self.assessment_number = tkinter.Label(self.next_frame,
                                               textvariable=self.value1)

        # Pack the next frame's widgets
        self.assessment_label.pack(side='left')
        self.assessment_number.pack(side='left')

        # Create widgets for the middle frame
        self.tax_label = tkinter.Label(self.mid_frame,
                                       text='Property Tax Value: ')

        # Store a string of blank characters with the objects set method
        self.value2 = tkinter.StringVar()

        # Create a label and associate it StringVar
        # Any value stored in StringVar will be displayed in label
        self.tax_number = tkinter.Label(self.mid_frame,
                                        textvariable=self.value2)

        # Pack the middle frame's widget
        self.tax_label.pack(side='left')
        self.tax_number.pack(side='left')

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
        actual_value = float(self.value_entry.get())

        # Calculate the assessment value
        assessment_value = actual_value * .6
        format_ass_val = '${:0,.2f}'.format(assessment_value).replace('$-', '-$')

        # Calculate the property tax of the assessment value
        prop_tax = (assessment_value/100) * .75
        tax_format = '${:0,.2f}'.format(prop_tax).replace('$-', '-$')

        # store the calculated values to their correct set function
        self.value1.set(format_ass_val)
        self.value2.set(tax_format)

# Create an instance of the Tax class
run = Tax()
