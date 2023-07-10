# NCLAB-Capstone-Project

## _Financing Calculators_

#####  _version 1.4 - see section 6 for changes_

## Table of Contents

- ### Section 1 - Overview
- ### Section 2 - Required Libraries
- ### Section 3 - Program steps
- ### Section 4 - Errors encountered
- ### Section 5 - Future Improvements
- ### Section 6 - Changes and updates
- ### Section 7 - Operating system used

### Section 1

##### The following program uses various modules to calculate the following information for the user

1. Initial payments for purchase of a house
2. Refinancing an existing mortgage
3. What if I make an additional payment to principal?
4. Sales proceeds when the house sells

### Section 2

##### Required libraries

1. Numpy  pip install numpy
2. Pandas pip install pandas
3. Tkinter pip install tk
4. Matplotlib pip install matplotlib


### Section 3    

##### The program will be utilizing Tkinter as the GUI.

1. The program starts with options for the user.

    ![Alt text](image.png)

2. Currently, the only option working is the mortgage calculation.
   The option to close the program has been added, when the user has completed the task.

   When the user presses submit for the mortgage calculator, this is the screen that appears

   ![Alt text](image-7.png)

  

3. Once the information is entered, a check is made to ensure 
   the information entered is accurate.
   If not, the user will receive an error message.

   ![Alt text](image-3.png)

4. Once the information is submitted, the user is given the option to verify the information submitted.
   The user can choose to keep the information and press submit or make changes in the fields.

   ![Alt text](image-4.png)

5. Checks are made to ensure the correct information is entered.  Once entered the results
   will be displayed along with a graph showing principal and interest payments over each month.  


   ![img_2.png](img_2.png)

6. The user will have the option to save the ammortization file as a .csv  or .xlsx file on the local computer
   utilizing filedialog.asksaveasfilename.

   ![Alt text](image-5.png)

7. Once saved, the file returns to the last screen with a pop up message stating the file has saved.  If the user
   presses cancel, the screen closes.

   ![Alt text](image-6.png)

8. When the users chooses to quit, the program will revert to the first window, giving the user the option to 
   complete a new task or end the program.

### Section 4

##### Errors encountered with fixes

- Unable to add the legend to the graph. - fixed version 1.1
- In order to save to Excel, openpyxl will need to be installed using pip install openpyxl.
   If using Anaconda, it will be necessary to add openpyxl in the environment.    

### Section 5

##### Future improvements

- add functionality for refinancing
- add functionality for additional payments
- add functionality for sales proceeds
- give user options to choose different charts(graphs) to view.
- add optional fields to consider mortgage insurance, homeowners insurance
   and property taxes

### Section 6

##### Changes

- Version 1 - Created program
- Version 1.1 - fixed legend in graph
- Version 1.2 - reformatted using Black.  Added additional information to locale code to 
        allow for currency to show in Mac OS.
- Version 1.3 - made changes to fields to show examples
- Version 1.4 - added additional formatting to frames.  Started work on refinance calculator

### Section 7

##### Operating System

- Windows







