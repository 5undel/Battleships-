# Love Sandwiches

Love Sandwiches is a command-line based Python program to handle data automation for a sandwich company. Love Sandwiches runs a local market stall, selling a small range of sandwiches. For each market day, the staff pre-make stock to sell. If they sell out of a particular sandwich, the staff make extra for their customers, unsold sandwiches are thrown away at the end of the day.

Love Sandwiches will collect the company's market day sales data,  calculate the surplus for the day, and produce recommendations for the number of each sandwich to make for the next market. The goal is to save the company staff time by automating a repetitive task and help reduce the surplus by better predicting sales for future markets. To achieve this, we will wire up our Python program to interact with a Google Sheet, so that we can push and pull data to and from the spreadsheet.

<insert screenshot of application from amiresponsive website> http://ami.responsivedesign.is/

## Features 

### Existing Features

__ The Run Program Button  __

Featured at the top of the page, 

(screenshot of button)

__ The Terminal Area  __

In this section, the program will request the market day sales data from our user,  and then check if the data provided is valid.  If it isn't, the data will be requested again. Once the data is confirmed as valid, the rest of the program will run to add the sales data to the sales worksheet, calculate and update the surplus data, calculate the sales averages and make stock recommendations. 

(screenshot of terminal)

__ The Program Structure __

(screenshot of a workflow logic for the game)

...and the other features on your project like the game-play functionality (with screenshots)...

### Features Left to Implement

- Another feature idea that I can add 

## Testing 

### Validator Testing 

Python (PEP8online.com)
After checking the Python code for PEP8 requirements, no errors were found

![image](doc/pep8online-vali.png)

### Browser Compatibility
    - Edge browser

![image](doc/edge.png)

    - Firefox browser

![image](doc/firefox.png)

    - Chrome browser

![image](doc/chrome.png)


### Responsivenes

(screenshot of the game on desktop, tablet, and mobile, include from your phone if possible)

### Unfixed Bugs

Mention of unfixed bugs and why they were not fixed 

## Deployment

This project has been deployed to Heroku.
Steps taken to deploy are as follows:

- Create a **requirements.txt** file using the terminal command `pip3 freeze --local > requirements.txt`
- Create a **Procfile** with the terminal command `echo web: python3 run.py > Procfile`
- `git add` and `git commit` the new **requirements** and **Procfile**, then `git push` the project to GitHub.

- Navigate over to Heroku.com
- Click the "new" button, and give the project a name & set the region to Europe.
- From the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
- Confirm the linking of the Heroku app to the correct GitHub repository.
- Select "Enable Manual Deployment", and then click the "Deploy" button.

The live link can be found here - https://max-battleship.herokuapp.com/

### Local Deployment

For local deployment, if you would like to make a clone of this repository, you can type the following command in your terminal:
- `git clone https://github.com/5undel/Battleships-.git`

Alternatively, if you are using Gitpod, you can simply click on the green Gitpod button at the top of the repository, and this will create a new workspace in your Gitpod account.
This [link](https://gitpod.io/#https://github.com/5undel/Battleships-) will do the same thing for you if you do not see the green Gitpod button.

## Credits 

Inspiration for the site was taken from … 

### Content 

List all of the relevant sources you've used, including the Emojipedia for the icons for example.
- [Emojipedia](https://emojipedia.org/) for the icons on the game
- etc.