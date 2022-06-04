<sub>Key Murray   
     06/03/2022    
     IT FDN 110 A Sp 22: Foundations of Scripting: Python    
     Assignment 07</sub>

# **Creating a Script using Exception Handling and Pickling**

## **Introduction**
<sub>In this document, I will explain the steps I took to create a script using exception handling and pickling. I will also share the resources I found that helped me understand both topics in depth. These concepts were both challenging to understand and having to create a script demonstrating how they could be used together had me puzzled for a while. Simplifying the script helped me better demonstrate how both could be used in the script. I choose to create a script asking the user for their favorite basketball player, their jersey number, and the team they play for.</sub>

## **Exception Handling in Python**

### **[Python Exceptions: An Introduction](https://realpython.com/python-exceptions/) (External site)**
<sub>While doing my research on exception handling, I came across this article on realpython (realpython, [https://realpython.com](https://realpython.com), created by Said van de Klundert) (External Site) that explained python exceptions pretty well. What I liked about it is that it started off with explaining the difference between exceptions and syntax errors. The code being syntactically correct is important when demonstrating exception handling as you need the code to be able to run and it cannot if there are syntax errors. Exception handling is only important if the code can run because if not the user will not see the exceptions you have created with the custom message. Another reason I found his article helpful was because of the examples used to demonstrate each condition and statement. They were very concise and were not jumbled with too much code so you could see exactly what was happening in each example. That made it easy to break down and figure out how to demonstrate the same in my script. It was also helpful to see exception handling used with different types of data. There were examples of how to use exception handling with numbers, files, and operating systems. Overall, I found this article to be the easiest resource to help expand my understanding of exception handling.</sub>

## **Pickling in Python**

### **[Pickle in Python Tutorial: Object Serialization](https://www.datacamp.com/tutorial/pickle-python-tutorial) (External site)**
<sub>The data camp tutorial I found about pickling was very informative and easy to follow. I really liked how it explained why pickling is useful and the advantages and disadvantages of using pickling. The examples used in this article were also concise and defined well so it was easy to see how to use it in my script. I also found that it was helpful the article explained that pickling is not the same as compressing a file. It can seem, especially if looking at the .dat file that it does not consume a lot of space but in fact it can as pickling is only converting the data to another depiction and not less bits as that would be the process of compression. The examples in chapter 7 of our textbook along with this article really helped me understand pickling and why it is useful.</sub>

## **Favorite Basketball Player Script**
### **Pickle Module**
<sub>The program I created uses pickling and exception handling when asking the user for their favorite basketball player and details about the player. I start the script by importing the pickle module to serialize the input data from the user. Pickling is defined as a method to store data to a file that can be accessed randomly. (Figure 1)</sub>

![Figure 1:Screen shot of the script to import the pickle module.](https://kam9010.github.io/IntroToProg-Python-Mod07/Figure07-1.png)

<sub> ***Figure 1:Screen shot of the script to import the pickle module.*** </sub>

<sub>I created the variable “strFileName“ to represent the file PlayerData.dat and the variable “lstFavorite” to capture the list data provided from the user to save to the file. Before this assignment we had been writing data to text files because we were working with data that we wanted to be human readable but now, we are writing to binary files. When writing the data to the binary file the data will be converted from plain text to binary. When I open the file and use the mode “rb” it reads from the binary file. When I open the file and use “wb” it will write to and create the binary file if it doesn’t exist. Unlike before when we were using the modes “r” and “w” when working with a text file we have now added the b to indicate that the data should be binary. Another difference with using pickling is that we no longer use functions like “write” or “append. Instead we use the “pickle.dump” function which will write data to the file and “pickle.load” function which will read and retrieve data from the binary file. (Figure 2)</sub>

![Figure 2:Screen shot of pickling being used in the script.](https://kam9010.github.io/IntroToProg-Python-Mod07/Figure07-2.png)

<sub> ***Figure 2:Screen shot of pickling being used in the script.*** </sub>

### **Exception Handling**

<sub>The next part of the script is where I use exception handling. Exception handling is used when the script runs into an error while running the program and displays an error message. There are built in exceptions that can be used but sometimes the language is not user friendly and can be difficult for an end user to understand. In my script I used the built-in exception “ValueError” when asking the user for their favorite player’s jersey number. If the user provides input that is not a number, then a message will be displayed indicting there was an error and why. Instead of using the built-in message I created my own detailed response so the user can better understand why there was an error. I use the while true loop and then “try” to declare that it should try to execute the following code and to raise an exception if the user provides anything other than a number with the ValueError message that I created indicting the error. Then to continue to ask the question until an integer is provided and then break from the while true loop and finish executing the rest of the script. (Figure 3)</sub>

![Figure 3:Screen shot of Exception Handling being used in the script.](https://kam9010.github.io/IntroToProg-Python-Mod07/Figure07-3.png)

<sub> ***Figure 3:Screen shot of Exception Handling being used in the script.*** </sub>

## **Summary**

<sub>At first this assignment was very challenging as I tried to start from scratch and then decided to use code that I had already used in previous assignments to accomplish the task. Learning about exception handling was fun because I had tried to figure it out in previous assignments when I only wanted specific input from the user. I also now understand how to store data in another format and recognize the risks of unpickling unknown data. Now I have another tool under my belt and can write better scripts and get the information I want from the user.</sub>


## **Script running in PyCharm**


### **PyCharm**
![Figure 4](https://kam9010.github.io/IntroToProg-Python-Mod07/Figure07-4.png)

### **PlayerData.dat**
![Figure 5](https://kam9010.github.io/IntroToProg-Python-Mod07/Figure07-5.png)


## **Script running in Terminal**


### **Terminal**
![Figure 6](https://kam9010.github.io/IntroToProg-Python-Mod07/Figure07-6.png)

### **PlayerData.dat**
![Figure 7](https://kam9010.github.io/IntroToProg-Python-Mod07/Figure07-7.png)
