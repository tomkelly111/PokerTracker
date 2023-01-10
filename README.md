# [Poker Tracker](https://poker-tracker.herokuapp.com/)

<img >


[Poker Tracker](https://poker-tracker.herokuapp.com/) is a Python terminal application which runs on the Code Institute mock terminal on Heroku. Poker Tracker is intended to be used by recreational poker players. The intended use is to store details of poker tournaments played i.e. entrance fees, winnings and hours palyed. Once details are stored it is possible to calculate your results to date i.e. profit, return on investment and hourly winrate. These are details which professional poker players will track themselves and the program makes this easy for recreational players.

## Data Storage
Poker Tracker is linked to a [Google Docs Excel sheet](https://docs.google.com/spreadsheets/d/11vh77G3YkgYBbyEdOOYomnT71VEXZQPJ3yv_YbMDx2s/edit?usp=sharing) which is made up of three separate worksheets to store the User's inputs. Totals are taken from all of the worksheets when the User's winrate is calculated.

## APPLICATION FEATURES

### Welcome Page
The welcome page displays the Poker Tracker logo, a welcome message and then offers the User choices.

<img >


### User Choices
Here the User is offered a choice of what they would like to do. They have the option to update the database with tournament details or view their current winrate which is based on previously entered data. There is also the option to exit the program. If the User enters an invalid option an error message displays and the options are displayed again.

<img >

### Entry Fee
Should the User elect to enter tournament details they will first be asked to enter the tournament entry fee. a retrieve_user_data() function is used. The User is asked to enter a whole number without any commas and an example of a correct figure is displayed. The retrieve_user_data() function calls another function that will validate the User's entry and if an invalid entry is made an error message is dispalyed and the User is asked to enter fee again. 

<img >


### Winnings
The User is then asked if they won anything in this tournament. If they respond no then a commiseration message is displayed and a zero value is returned. If they respond yes then a congratulations message displays and they are asked to enter the prize they won. This is requested using the retrieve_user_data() function that was used to request the tournament entry fee. 

<img >

### Hours Played
The User is then asked to input the number of hours they spent playing the tournament. Again the same retrieve_user_data() function is used to receive this input. 

### Updating Database
Once the User has provided all 3 inputs, the inputs are added to the database and the User recieves a message confirming when this is done. Initially the programme added the User's input to the database immediately after it was entered however, it was realised that if the User quit the program early there would be incomplete data stored in the data base which would effect the winrate calculations. Instead all of the User's inputs are now added to the database at once to ensure this doesn't happen.

Once the database is updated the User is returned to the User Choices screen in case they have more tournament details to add.

### Calculate Winrate
If the user selects to calculate winrate then a function is ran that totals all of the data on all 3 worksheets and performs various calculations to provide the User's overall Profit, Return on Investment and Hourly Winrate. Once this information is provided the User is returned to the User Choices screen in case they have more tournament details to add.

### Exit
The User is given the option to exit the programme at any time by inputting X. Should the User select this option then a Gooodbye and thank you message are displayed and the programme terminates.

<img >

## Flowchart
Before beginning the coding for this programme I designed the below flowchart in order to plan the functions I would need to create. This was done via [Lucid Chart](https://www.lucidchart.com/pages/). Although the programme remains largley the same as this layout, you can see that in this flowchart where it was initially intended that the database be updated after each input from the User.

<img width="371" alt="Screenshot 2023-01-09 205737" src="https://user-images.githubusercontent.com/111172617/211407010-718abaca-7418-43eb-a0d1-8745ed48509b.png">

## TESTING

### Manual Testing
<table>  
            <tr>
              <th>Action</th>
              <th>Expected Behaviour</th>
              <th>Pass / Fail </th>
            </tr>
            <tr>
              <td>Passed the code through the Code Institute Python Linter </td>
              <td>No Errors </td>
              <td>Pass </td>
            </tr>
            <tr>
              <td>Add tournament details </td>
              <td>Google Docs worksheets are updated with User's input </td>
              <td>Pass </td>
            </tr>
            <tr>
              <td>Check winrate </td>
              <td>Totals are drawn from Google Docs worksheets and calculations 
		    are carried out to return profit, return on investment and hourly winrate</td>
              <td>Pass </td>
            </tr>
            <tr>
              <td>Input "x" at anytime </td>
              <td>Goodbye message displays, programme terminates and no data is added to Google Docs </td>
              <td>Pass </td>
            </tr>
            <tr>
              <td>Input invalid data at all stages of programme </td>
              <td>Error message displays showing User's invalid input and options are asked again </td>
              <td>Pass </td>
            </tr>
              <tr>
              <td> </td>
              <td> </td>
              <td> </td>
            </tr>
</table>

### User Testing
The application link was provided to four users all of whom were able to use the program easily and navigate the options without issue. A majority of the users said it might be useful to have an axplaination of what return on investment and hourly winrate were. It was decided that although these terms may be unfamiliar to non-poker players, these terms are well know to the audience to which this programme is targeted (recreational poker players).

### Bugs
#### Solved Bugs
- Initially the programme added the User's input to the database immediately after it was entered however, it was realised that if the User quit the program early there would be incomplete data stored in the data base which would effect the winrate calculations. Instead all of the User's inputs are now added to the database at once to ensure this doesn't happen.
- Initially the User could only exit the programme from the User Choices Screen. This may be frustrating to some User's and so this option was added to all stages of the programme so it can be trminated at any time.

#### Remaining Bugs
- none

## LIBRARIES
The following libraries were used:
- GSpread - to access the Google Docs sheet where data is stored
- Pyfiglet - to use ASCII font to provide styling throughout the programme
- Sys & Time - to create a function which types out text on the display rather than showing all at once
- Colorama - used to change to color of text throughout the programme
- 
## DEPLOYMENT

The project was deployed using Code Institute's mock terminal for Heroku. To do this the following steps were followed:
- From the Heroku dashboard, create a new app;
- Navigate to settings tab;
- Create confg var with key "CREDS" and for  value copy and paste the contents of creds.json file - click add;
- Create config var with key "PORT" and value "8000" - click add;
- Next add buildpacks to install dependencies;
- Click add buildpack and select python then save changes. Then select node.js and click save again;
- Buildpacks must be in this order with python first and node.js second;
- Next navigate to deploy tab;
- Select github as deplyment method, confirm connect to github;
- Search for github repository and once found click connect; and
- Enable automatic deployment to deploy.



## CREDITS
Thanks to:
- Code Institute for the deployment terminal.
- Code Institute for providing the Gitpod template.
- Youtuber - Tech With Tim - who provided a tutorial for using Colorama available [here.](https://www.youtube.com/watch?v=u51Zjlnui4Y)
- https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
- Instructions on how to use Pyfiglet to utilise ASCII fonts was take from [here.](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)
- User Sebastian on Stack Overflow who provided the function to make sure all text printed to CLI is typed out slowly, available [here.](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing)
- Code for updating the Google Docs sheets was taken from the Code Institute's Love Sandwhiches Walk Through Project.
		



