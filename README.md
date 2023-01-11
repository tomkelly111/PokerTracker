# [Poker Tracker](https://poker-tracker.herokuapp.com/)

<img width="389" alt="image" src="https://user-images.githubusercontent.com/111172617/211642971-d2cc6204-ecaf-4eed-b4ac-498deca9e619.png">

[Poker Tracker](https://poker-tracker.herokuapp.com/) is a Python terminal application which runs on the Code Institute mock terminal on Heroku. Poker Tracker is intended to be used by recreational poker players. The intended use is to store details of poker tournaments played i.e. entrance fees, winnings and hours played. Once details are stored it is possible to calculate your results to date i.e. profit, return on investment and hourly winrate. These are details which professional poker players will track themselves and the program makes this easy for recreational players.

## Data Storage
Poker Tracker is linked to a [Google Docs Excel sheet](https://docs.google.com/spreadsheets/d/11vh77G3YkgYBbyEdOOYomnT71VEXZQPJ3yv_YbMDx2s/edit?usp=sharing) which is made up of three separate worksheets to store the User's inputs. Totals are taken from all of the worksheets when the User's winrate is calculated.

## APPLICATION FEATURES

### Welcome Page
The welcome page displays the Poker Tracker logo, a welcome message and then offers the User choices.

<img width="392" alt="image" src="https://user-images.githubusercontent.com/111172617/211643598-1312cf03-c4dc-4967-8f65-734e9117950a.png">

### User Choices
Here the User is offered a choice of what they would like to do. They have the option to update the database with tournament details or view their current winrate which is based on previously entered data. Additionally there is the option to delete the last tournament entry or delete all data stored. There is also the option to exit the program. If the User enters an invalid option an error message displays and the options are displayed again. This feature is available at any stage throughout the programme.

<img width="384" alt="image" src="https://user-images.githubusercontent.com/111172617/211643419-bf12b183-590a-4920-95bc-fcebeed76241.png">


### Entry Fee
Should the User elect to enter tournament details they will first be asked to enter the tournament entry fee. a retrieve_user_data() function is used. The User is asked to enter a whole number without any commas and an example of a correct figure is displayed. The retrieve_user_data() function calls another function that will validate the User's entry and if an invalid entry is made an error message is displayed and the User is asked to enter fee again. 

<img width="388" alt="image" src="https://user-images.githubusercontent.com/111172617/211643727-c3a7b0a6-3d4e-4807-97dc-6f2848b5dbd0.png">


### Winnings
The User is then asked if they won anything in this tournament. If they respond no then a commiseration message is displayed and a zero value is returned. If they respond yes then a congratulations message displays and they are asked to enter the prize they won. This is requested using the retrieve_user_data() function that was used to request the tournament entry fee. 

<img width="400" alt="image" src="https://user-images.githubusercontent.com/111172617/211643917-fb12c8df-df49-491d-825e-3a5588bda151.png">


<img width="371" alt="image" src="https://user-images.githubusercontent.com/111172617/211644069-c5a4a34c-d074-4a25-9982-4a5061d76f6f.png">


### Hours Played
The User is then asked to input the number of hours they spent playing the tournament. Again the same retrieve_user_data() function is used to receive this input. 

<img width="401" alt="image" src="https://user-images.githubusercontent.com/111172617/211644318-445a15fc-d780-45c0-93a2-e302ebe2d050.png">


### Updating Database
Once the User has provided all 3 inputs, the inputs are added to the database and the User receives a message confirming when this is done. Initially the programme added the User's input to the database immediately after it was entered however, it was realised that if the User quit the program early there would be incomplete data stored in the database which would effect the winrate calculations. Instead all of the User's inputs are now added to the database at once to ensure this doesn't happen.

Once the database is updated the User is returned to the User Choices screen in case they have more tournament details to add.

### Calculate Winrate
If the user selects to calculate winrate then a function is ran that totals all of the data on all 3 worksheets and performs various calculations to provide the User's overall Profit, Return on Investment and Hourly Winrate. Once this information is provided the User is returned to the User Choices screen. Profit is determined by subtracting the total costs (i.e. all entries from the "entry_fee" worksheet) from the total winnings (i.e. all entries from the "winnings" worksheet). Return on Investment is calculated by dividing the profit by the total costs and multiplying by 100. Finally, the Hourly Winrate is calculated by taking profit and dividing it by the total hours played (i.e. all entries from the the "hours_played).

<img width="356" alt="image" src="https://user-images.githubusercontent.com/111172617/211644578-936d65e8-87c8-4c50-934c-1ec8d391adf4.png">


### Exit
The User is given the option to exit the programme at any time by inputting X. Should the User select this option then a Gooodbye and thank you message are displayed and the programme terminates.

<img width="353" alt="image" src="https://user-images.githubusercontent.com/111172617/211644685-22b29d41-c681-450a-9e5c-96e80dbf9924.png">


### Delete Last Entry
If the User chooses to delete last tournament entry then a function is ran which loops through the three worksheets and deletes the last entry from each.

### Delete All Entries Stored
If the User selects to delete all entries stored, a function is ran for this. The User will be asked to confirm that they want to delete all data and if they select yes then all three worksheets are looped through and all entries are cleared leaving a blank database.

## Flowchart
Before beginning the coding for this programme I designed the below flowchart in order to plan the functions I would need to create. This was done via [Lucid Chart](https://www.lucidchart.com/pages/). Although the programme remains largely the same as this layout, you can see that in this flowchart where it was initially intended that the database be updated after each input from the User. Additionally, the delete last entry and the delete all entries options were added after the program was created as an afterthought.

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
              <td>Delete last entry </td>
              <td>Last entry is deleted from all worksheets in Google Doc</td>
              <td>Pass </td>
            </tr>
	     <tr>
              <td>Delete all data </td>
              <td>All data is deleted from all worksheets in the Google Doc</td>
              <td>Pass </td>
            </tr>
	     <tr>
              <td>Calculate winrate after deleting all data </td>
              <td>Message prints to terminal saying no data available</td>
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
</table>

### User Testing
The application link was provided to four users all of whom were able to use the program easily and navigate the options without issue. A majority of the users said it might be useful to have an explaination of what return on investment and hourly winrate were. It was decided that although these terms may be unfamiliar to non-poker players, these terms are well known to the audience to which this programme is targeted (recreational poker players).

### Bugs
#### Solved Bugs
- Initially the programme added the User's input to the database immediately after it was entered however, it was realised that if the User quit the program early there would be incomplete data stored in the data base which would effect the winrate calculations. Instead all of the User's inputs are now added to the database at once to ensure this doesn't happen.
- Initially the User could only exit the programme from the User Choices Screen. This may be frustrating to some User's and so this option was added to all stages of the programme so it can be terminated at any time.
- It was realised late in the project that when all data is deleted and then the User decides to Calculate Winrate, a divide by zero error occurs. To overcome this, an if else statement was added to the Calculate Winrate function which checks if losses are equal to zero and if so a message is printed to the terminal rather than calculating winrate. If losses are not equal to zero then the winrate is calculated as normal.

#### Remaining Bugs
- none

## LIBRARIES
The following libraries were used:
- GSpread - to access the Google Docs sheet where data is stored
- Pyfiglet - to use ASCII font to provide styling throughout the programme
- Sys & Time - to create a function which types out text on the display rather than showing all at once
- Colorama - used to change to color of text throughout the programme

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
- Select github as deployment method, confirm connect to github;
- Search for github repository and once found click connect; and
- Enable automatic deployment to deploy.



## CREDITS
Thanks to:
- Code Institute for the deployment terminal.
- Code Institute for providing the Gitpod template.
- Youtuber - Tech With Tim - who provided a tutorial for using Colorama available [here.](https://www.youtube.com/watch?v=u51Zjlnui4Y)
- Instructions on how to use Pyfiglet to utilise ASCII fonts was take from [here.](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/)
- User Sebastian on Stack Overflow who provided the function to make sure all text printed to CLI is typed out slowly, available [here.](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing)
- Code for updating the Google Docs sheets was taken from the Code Institute's Love Sandwiches Walk Through Project.
		



