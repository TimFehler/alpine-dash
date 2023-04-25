# How to run the dashbord on your own (debian-based) system 

## Setting up the virtual environment

Clone/copy the repository to workplace and navigate into directory

`cd strava-heatmap`

Install necessary software packages

`sudo apt install python3 python3-pip python3-venv`

Create virtual environment with `venv`

`python3 -m venv env`

Working with the virtual environment in CLI:

 - Activate with `source env/bin/activate`
 - Deactivate with `deactivate`

Installing dependencies from text file in repository

`python3 -m pip install -r requirements.txt`

⚠️ **Disclaimer**: Although the correct functionality has only been tested with the package versions specified in the text file, it can be, nevertheless, assumed that various other versions can be used without any issues.

## Running the code

### Client ID and secret

On the developer webpage of Strava a new Strava Application has to be registered. The provided client ID and secret then have to be saved in `access/client.secret` comma-separated, without any spaces.

### One time authentication with athlete

Using `get_access.ipynb`, generate an URL, where the targeted athlete can approve the access to their data. Note that this application has the same level of access as the athlete themself. Private zones configured in the Strava profile will not have any restrictive effect on the data visualization.
Once the athlete approves the access, a response URL will be entered. This URL will not be valid, but the part after `code=` has to be pasted into `access/response_code.json` from where an inital access token will be generated and saved to `access/access_token.pickle`.  

This step does only have to be performed once per athlete!

### Read in and refresh of access token

Each time before any data will be downloaded from Strava the access token will be read in from `access/access_token.pickle` and refreshed if necessary.

### Analysis

Commence with the data analysis.