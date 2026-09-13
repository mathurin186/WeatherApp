# Weather App

An Application for finding the weather of any US city at a glance through any CLI interface.

The app uses python to allow the user to query the weather of any US City, for multiple cities of the same name the app will give a list of cities to choose from before displaying any information. 

To install and use, it is necessary to have Python or its latest version. 
* Download the weather.py file and place in a convenient location, such as: C:\Users\[Username]\Documents
* For the CLI, If you are on Linux or Mac, open terminal, Else for Windows use CMD (Command Prompt)
* In the CLI, type the following:
  ```py --version```  
  a) Something should return that looks like: Python 3.14.6, if not you will have to go through the installation process
* Make sure the default location for the CLI is whichever folder you placed your weather.py file  
  a) E.G. If you placed your file in the suggested location, ensure that default is set to: C:\Users\[Username]\Documents  
  b) If it is not, you may change the default location simply by using cd c:\[filepath], or in the above example: cd C:\Users\[Username]\Documents
* Run the program by typing:
  ```py weather.py```  
  a) The program will ask for a city, feel free to type the full name of any city.  
   - In my example I'll use: Sacramento  
  b) In the case of multiple cities of the same name, the app will create a list and allow you to choose which city you want to see. In my example I return:

Multiple matches found:
  1. Sacramento (California, United States)
  2. Sacramento (Kentucky, United States)
  3. Sacramento (New Mexico, United States)
  4. Sacramento (Pennsylvania, United States)
  5. Sacramento (Illinois, United States)
  6. Sacramento (Nebraska, United States)
  7. Sacramento Canyon (California, United States)
  8. Sacramento Landing (California, United States)
  9. Sacramento Zoo (California, United States)
  10. Sacramento Park (Illinois, United States)
Choose a location (1-10):

  c) Final choose a city from the list if necessary. In my above example I enter 1 for Sacramento (California, United States).
  
  Final Output shows the following:
  <img width="355" height="77" alt="image" src="https://github.com/user-attachments/assets/5a8453e2-5f24-4076-97cc-144dd947e36d" />
