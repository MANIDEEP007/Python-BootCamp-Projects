#Setting up Things
import numpy as np
import pandas as pd
import plotly as pl
import plotly.offline as po
import plotly.graph_objects as pg
import cufflinks as cf
get_ipython().run_line_magic('matplotlib', 'inline')
po.init_notebook_mode(connected=True)
cf.go_offline()

#Based on choice create data
def create_data(choice):
    #Random Data
    if choice == 1:
        #Create Random Array using NumPy
        rand_array = np.random.rand(100,5)
        #Convert Numpy array as Pandas DataFrame
        df = pd.DataFrame(rand_array,columns=["A","B","C","D","E"])
        return df
    #Customized User defined data(4 x 5 Size)
    elif choice == 2:
        cols = [0] * 5
        rows = [[0]*5 for _ in range(4)] 
        #Get The Columns Name
        print("Enter the Column Names")
        for ind in range(5):
            cols[ind] = input("Enter the "+ str(ind+1) + " th Column Name:")
        #Get the values for Rows
        for ind in range(0,len(rows)):
            for row_ind in range(5):
                temp = input("Enter the "+ str(ind+1) +" Row Values" )
                try:
                    rows[ind][row_ind] = int(temp)
                except:
                    rows[ind][row_ind] = temp
        #Convert List to DataFrame
        df = pd.DataFrame(rows,columns=cols)
        return df
    elif choice == 3:
        file = input("Enter the Name of the file:")
        #Read Data
        data = pd.read_csv(file)
        #Convert Data to DataFrame
        df = pd.DataFrame(data)
        return df
    else:
        return "DataFrame Creation Failed. Please enter between 1-3 and try again"

#Function to Plot for all Columns
def plotter(plot_choice):
    #Line Plot
    if plot_choice == 1:
        final_plot = df1.iplot(kind="scatter")
    #Scatter Plot
    elif plot_choice == 2:
        final_plot = df1.iplot(kind="scatter",mode="markers",symbol="x",colorscale="paired")
    #Bar Plot
    elif plot_choice == 3:
        final_plot = df1.iplot(kind="bar")
    #Histogram
    elif plot_choice == 4:
        final_plot = df1.iplot(kind="hist")
    #Box Plot
    elif plot_choice == 5:
        final_plot = df1.iplot(kind="box")
    #Surface Plot
    elif plot_choice == 6:
        final_plot = df1.iplot(kind="surface")
    else:
        print("Invalid Choice. Please enter 1-6 and try again")
        final_plot = "Invalid Choice. Please enter 1-6 and try again"
    return final_plot

#Function to plot based on choice of number of columns 1/2/3
def plotter2(plot_choice):
    num_col = int(input("Select Number of Column 1/2/3:"))
    #Plot for 1 Column
    if num_col == 1:
        cols = input("Enter the Column Name present in DataFrame:")
        if plot_choice == 1:
            final_plot = df1[cols].iplot(kind="scatter")
        elif plot_choice == 2:
            final_plot = df1[cols].iplot(kind="scatter",mode="markers",symbol="x",colorscale="paired")
        elif plot_choice == 3:
            final_plot = df1[cols].iplot(kind="bar")
        elif plot_choice == 4:
            final_plot = df1[cols].iplot(kind="hist")
        elif plot_choice == 5:
            final_plot = df1[cols].iplot(kind="box")
        elif plot_choice == 6 or plot_choice == 7:
            print("Surface Plot & Bubble Plot works for two or more columns")
        else:
            print("Please Enter 1-7 & Try Again")
    #Plot for 2 Columns
    elif num_col == 2:
        print("Enter the 2 Column names present in dataFrame")
        x = input("Enter first Column Name:")
        y = input("Enter second Column Name:")
        if plot_choice == 1:
            final_plot = df1[[x,y]].iplot(kind="scatter")
        elif plot_choice == 2:
            final_plot = df1[[x,y]].iplot(kind="scatter",mode="markers",symbol="x",colorscale="paired")
        elif plot_choice == 3:
            final_plot = df1[[x,y]].iplot(kind="bar")
        elif plot_choice == 4:
            final_plot = df1[[x,y]].iplot(kind="hist")
        elif plot_choice == 5:
            final_plot = df1[[x,y]].iplot(kind="box")
        elif plot_choice == 6:
            final_plot = df1[[x,y]].iplot(kind="surface")
        elif plot_choice == 7:
            size = input("Please enter size column")
            final_plot = df1[[x,y]].iplot(kind="bubble",x=x,y=y,size=size)
        else:
            print("Please Enter 1-7 & Try Again")
            final_plot = "Please Enter 1-7 & Try Again"
    #Plot for 3 Columns
    elif num_col == 3:
        print("Enter the 3 Column names present in dataFrame")
        x = input("Enter first Column Name:")
        y = input("Enter second Column Name:")
        z = input("Enter third Column Name:")
        if plot_choice == 1:
            final_plot = df1[[x,y,z]].iplot(kind="scatter")
        elif plot_choice == 2:
            final_plot = df1[[x,y,z]].iplot(kind="scatter",mode="markers",symbol="x",colorscale="paired")
        elif plot_choice == 3:
            final_plot = df1[[x,y,z]].iplot(kind="bar")
        elif plot_choice == 4:
            final_plot = df1[[x,y,z]].iplot(kind="hist")
        elif plot_choice == 5:
            final_plot = df1[[x,y,z]].iplot(kind="box")
        elif plot_choice == 6:
            final_plot = df1[[x,y,z]].iplot(kind="surface")
        elif plot_choice == 7:
            size = input("Please enter size column")
            final_plot = df1[[x,y,z]].iplot(kind="bubble",x=x,y=y,size=size)
        else:
            print("Please Enter 1-7 & Try Again")
            final_plot = "Please Enter 1-7 & Try Again"
    else:
        print("Please enter only 1-3 & Try Again")
        final_plot = "Please Enter 1-3 & Try Again"
    return final_plot
        
#Function calling Plotters
def main(choice):
    #Plot All the Data
    if choice == 1:
        print('''Select Type of Plot you desire to plot by writing 1-6
        1.Line Plot
        2.Scatter Plot
        3.Bar Plot
        4.Histogram
        5.Box Plot
        6.Surface Plot
        ''')
        plot_choice = int(input())
        plot = plotter(plot_choice)
    #Plot Specific Columns
    elif choice == 2:
        print('''Select Type of Plot you desire to plot by writing 1-7
        1.Line Plot
        2.Scatter Plot
        3.Bar Plot
        4.Histogram
        5.Box Plot
        6.Surface Plot
        7.Bubble Plot
        ''')
        plot_choice = int(input())
        plot = plotter2(plot_choice)
    else:
        print("Please enter 1-2 and try again")

#Start Execution
print("Select type of Data you need to Plot?(By Choosing 1-3)")
print('''1. Random Data(100 Rows, 5 Columns)
2. Customize Data Frame(5 Columns, 4 Rows)
3. Upload CSV/Textfile/Json
''')
choice = int(input()) #Get the User choice

#Create Data
df1 = create_data(choice) #Have function to create data

#Print first 5 rows of DataFrame
print("Your Data Frame is given below")
print(df1.head())

#Get the User Choice for columns
col_choice = int(input("Press 1 for Plotting for all columns, 2 for Specific columns:"))

#Plot the Data
main(col_choice)
