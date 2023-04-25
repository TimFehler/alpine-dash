# alpine-dash

*alpine-dash* is a python-based dashboard to facilitate a data-driven training approach for endurance sports and alpinism. Strava was chosen as the digital training data storage, as it is a popular platform in the industry, offering seamless syncing capabilities with other platforms and a wide range of digital fitness devices.

## Features

 - Access to athlete data via Strava API
 - Data analysis based on variance in event specific quantities (e.g. moving time, max speed, avg pace) over a distinct time frame
 - Documentation of weekly accomplished training metrics
 - Estimation of training intensities through the use of HR zones
 - Heatmap of past GPS tracks

## Dependencies

 - [`stravalib`](https://github.com/stravalib/stravalib) for interacting with the Strava API
 - [Dash](https://pypi.org/project/dash/) for the dashboard framework
 - `pandas`, `matplotlib` for data manipulation and visualization
 - [`folium`](https://pypi.org/project/folium/) for map-based visualizations

## Setup

For information how to run the dashbord on your own (debian-based) system refer to the [setup manual](docs/SETUP.md).

## Privacy notice

Since the publication of my own training data poses significant privacy concerns, outputs of the notebooks had to be omitted before uploading them. Anonymized exemplary plots are provided in [here](examples/)

## References

Large parts of the inital code commits, especially the interactions with the Strava API, where heavily inspired by this [blog article](https://medium.com/analytics-vidhya/accessing-user-data-via-the-strava-api-using-stravalib-d5bee7fdde17) and the corresponding [repository](https://github.com/mandieq/strava_related).
