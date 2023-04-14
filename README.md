# strava-heatmap
Python based notebooks for a data driven training approach. 

## Purpose

The mission of this coding project lay in restructuring my personal day-to-day training for endurance sports and alpinism, especially, to a more data driven approach. Strava was chosen as the storage for digital training data, as it is one of the industry leaders, providing various syncing capabilities to other platform and numerous digital fitness devices.

## Features

 - Access to athlete data via Strava API
 - Data analysis based on variance in event specific quantities (e.g. moving time, max speed, avg pace) over a distinct time frame
 - Documentation of weekly accomplished training metrics
 - Estimation of training intensities through the use of HR zones
 - Heatmap of past GPS tracks

## Dependencies

 - [`stravalib`](https://github.com/stravalib/stravalib) for interacting with the Strava API
 - `pandas`, `matplotlib` for data manipulation and visualization
 - [`folium`](https://pypi.org/project/folium/) for map-based visualizations

## How to run the notebooks on your own (debian-based) system 

### Setting up the virtual environment

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

⚠️ **Disclaimer**: Although the correct functionality has been only tested with the package versions specified in the text file, it can be, nevertheless, assumed that various other versions can be used without any issues.

### Running the code

#### Client ID and secret

On the developer webpage of Strava a new Strava Application has to be registered. The provided client ID and secret then have to be saved in `access/client.secret` comma-separated, without any spaces.

#### One time authentication with athlete

Using `get_access.ipynb`, generate an URL, where the targeted athlete can approve the access to his/her data. Note that this application has the same level of access as the athlete him-/herself. Private zones configured in the Strava profle will not have any effect on the data visualization.
Once the athlete approves the access, a response URL will entered. This URL will not be valid, but the part after `code=` has to be pasted into `access/response_code.json` from where an inital access token will be generated and saved to `access/access_token.pickle`.  

This step does only have to be performed once per athlete!

#### Read in and refresh of access token

Each time before any data will be downloaded from Strava the access token will be read in from `access/access_token.pickle` and refreshed if necessary.

#### Analysis

Commence with the data analysis.

## Privacy notice

Since the publication of my own training data poses significant privacy concerns, outputs of the notebooks had to be omitted before uploading them. Anonymized exemplary plots are provided in `examples/`.

## References

Large parts of the inital code commits, especially the interactions with the Strava API, where heavily inspired by this [blog article](https://medium.com/analytics-vidhya/accessing-user-data-via-the-strava-api-using-stravalib-d5bee7fdde17) and the corresponding [repository](https://github.com/mandieq/strava_related).
