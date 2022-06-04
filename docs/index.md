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
<sub>The program I created uses pickling and exception handling when asking the user for their favorite basketball player and details about the player. I start the script by importing the pickle module to serialize the input data from the user. Pickling is defined as a method to store data to a file that can be accessed randomly.</sub>
