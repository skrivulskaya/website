---
layout: tutorial
title: "Geocoding"
card_title: "Geocoding"
permalink: /tutorials/geocoding/
image: /assets/img/tutorials/card-geocoding.png
order: 3
---

![]({{ site.baseurl }}/assets/img/tutorials/geocoding-1.png)

If you have a list of places, and you need to find their latitude/longitude coordinates, you have a couple of options.

OPTION 1. The first and more convoluted (but ultimately worthwhile) option is to [get a Google API key](https://developers.google.com/maps/documentation/javascript/get-api-key) from the free tier of the [Google Cloud Platform](https://cloud.google.com/free/), install [R](https://www.r-project.org/) and [RStudio](https://rstudio.com/products/rstudio/download/), and then use [this tutorial](https://www.storybench.org/geocode-csv-addresses-r/) to work with the "[ggmap](https://github.com/dkahle/ggmap)" R package. I would also recommend watching [this YouTube tutorial](https://www.youtube.com/watch?v=A7LzEJiKQvc) to fill in some gaps in the first tutorial. 

OPTION 2. Assuming you don't want to learn a new programming language and deal with Google's developer code, here is an alternative:

1.  Go to <https://www.gpsvisualizer.com/geocoder/> and read about the service (including its limitations and having to potentially double-check/clean up the results).

2.  Get an API key from **MapQuest**. 

    - Go to <https://developer.mapquest.com/>.

    - Click on **Get Started** and complete registration for a free account.

    - Once registered, go to <https://developer.mapquest.com/user/me/profile> and find your API key (note that it may take up to an hour for the system to process your request and generate your key).

3.  Copy your API key from MapQuest and paste it into the **Your MapQuest AppKey** field on the [GPS Visualizer](https://www.gpsvisualizer.com/geocoder/) website. 

4.  Next, open the .csv file that contains your data. For this tutorial, I am using the "city" and "state" columns from [Lincoln Mullen](https://lincolnmullen.com/)'s "[early-colleges.csv](https://github.com/ropensci/historydata/blob/master/data-raw/early-colleges.csv)" file.

    - You can download this (or any other file) from GitHub by using [DownGit](https://downgit.github.io/#/home?url=https:%2F%2Fgithub.com%2Fropensci%2Fhistorydata%2Fblob%2Fmaster%2Fdata-raw%2Fearly-colleges.csv) (this link will specifically take you to Mullen's file).

5.  Whatever dataset you use, select only the columns that specify the location (can be a single "address" column or a combination of several columns, such as "city," "state," and "country"). Copy those columns and paste them into the Input field in GPS Visualizer.

6.  Click **Start geocoding** and wait for the process to go through all of the fields (more fields = more time). 

7.  Once finished, click to select all & copy the results from the **Results as text** field in GPS Visualizer.

8.  In your .csv file, select the first empty cell of a new/empty column and paste the results—you should now have several new columns added to your spreadsheet. Some will be duplicates, so remove those. Most importantly, you should have brand-new "latitude" and "longitude" columns. If that is the case, well done.

9.  Go through the list and note any potential discrepancies. Misspellings or places that the tool cannot locate will be assigned wrong coordinates that should be obvious to spot. 

10. Note: in the event that the data you've copied gets pasted into a single column as a string of text, do the following: select the column, in the menu go to **Data**, select **Text to Columns**, select **Delimited**, click **Next**, select **Comma** from the **Delimited** category (and unselect everything else), click **Next**, and click **Finish**.

Page updated Google SitesReport abuseGoogle SitesReport abusePage details
