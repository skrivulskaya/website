---
layout: tutorial
title: "Census Data"
card_title: "Census Data"
permalink: /tutorials/census-data/
image: /assets/img/tutorials/card-census-data.jpg
order: 1
---

## Locating and Exporting Historical Census Data

Commercial record collection websites like [FamilySearch](https://www.familysearch.org/en/) and [Ancestry](https://www.ancestry.com/) will let users explore individual census records (up until the year 1940 as of 2021), but what if you wanted to look at large-scale state, county, or city-level data to track change over time? Many historians have created such datasets for their own projects, and you could borrow from (and cite) their work. Here are just two examples: [Urban Transition Historical GIS Project](https://s4.ad.brown.edu/Projects/UTP2/DataS.htm) and [Placing Segregation](http://dsps.lib.uiowa.edu/placingsegregation/downloads/). But what if you wanted to do research on a topic that doesn't have a pre-made dataset? This is possible with [IPUMS National Historical Geographic Information System (NHGIS)](https://www.nhgis.org/), which provides free access to census statistics and GIS shape files from 1790 to the present.

1.  Create an [account](https://uma.pop.umn.edu/nhgis/user/new) with IPUMS NHGIS (it's free but required to request, extract, and download data from the site).

2.  Once [logged in](https://www.nhgis.org/), click **Get Data** on the home page and read through the ["How to Use the Data Finder"](https://www.nhgis.org/sites/www.nhgis.org/files/using_the_nhgis_data_finder.pdf) PDF on the next page.

3.  Once you understand how to apply filters and select the data you are searching for, proceed to add datasets to your **Data Cart**.

Let's try an example export. Suppose that I was interested in studying the racial composition of the city of San Diego during the Gilded Age and Progressive Era (let's say 1880 through 1920). Here is how I would proceed... and what challenges I would encounter.

- Under, Apply Filters, I click on **Geographic Levels** and the menu that pops up presents a number of (overwhelming) choices.

![]({{ site.baseurl }}/assets/img/tutorials/census-data-1.png)

- Do not fret. Clicking on each geographic level category will provide information about its availability for each census year as well as whether or not a corresponding boundary map exists in the system. Read through what is available—you will see that many of the really detailed reports (such as **Urban Area**, for example) are only available beginning in the 1970s.

- Ideally, I would want to find tract-level data. Think of tracts as small census subdivisions that account for areas within cities. And if I were doing research about the late 20th century, I would be in luck. Unfortunately, in the 1880s, census tracts did not yet exist. In fact, there are [a lot of differences]({{ site.baseurl }}/assets/files/supplement-ca.pdf) between the different census iterations, including shifting territorial boundaries and classifications of [race](https://www.pewresearch.org/social-trends/2015/06/11/chapter-1-race-and-multiracial-americans-in-the-u-s-census/) and [ethnicity](https://journeys.dartmouth.edu/censushistory/2016/01/24/asian-classification-1880-1990/).

- So now in addition to the already challenging task of trying to find the data, I have to make some methodological decisions about how I'll deal with those inconsistencies in my research. How will I explain that the data is available for different territorial levels across the years of my research? How will I explain that the notion of "race" is a category that's fraught with cultural assumptions that are products of their own time? To start, I will read and cite other historians who have already wrestled with these issues, but I will also still need to explain in my project what research choices I made and why.

- What I'll find is that the closest I can come to locating race-related data in 1880 San Diego will be to select **County** in the above filter. (Click the **+** button to add the filter and then **Submit**.)

- In the **Years** filter, I'll select 1880.

- As I select new filters, the **Select Data** table underneath the filters will change—listing all available data for the filters currently selected. With my current filters (County + 1880), I am able to get access to 74 Source tables, 2 Time Series tables, and 2 GIS files.

![]({{ site.baseurl }}/assets/img/tutorials/census-data-2.png)

- There are 4 pages of datasets. To find anything relevant to the issue of race/ethnicity, I might sort the table by the **Universe** category and then skim through the 4 pages. On the 4th page, I see the thing I came here in the first place: **Race**. But I also see 2 other potentially relevant categories: **Place of Birth** and **Nativity**. I'll go ahead and click the + sign to add all 3 to my **Data Cart**, which will now show that I've added **3 Source Tables**.

![]({{ site.baseurl }}/assets/img/tutorials/census-data-3.png)

- I'm also going to need that corresponding GIS file if I want to map the data using ArcGIS or QGIS, so I'll head over to that last tab under **Select Data** and click the + opposite the **2008 TIGER/Line +** dataset.

- With 4 things in my **Data Cart**, I will click **Continue** (twice) to get to the **Review & Submit** page. Under **Table File Structure**, tick **"Include additional descriptive header row (best for spreadsheets)"**—this will help you later when working with the different column labels. Then, in the text field, I'll write a brief description, something like "1880 race/place of birth/nativity county-level" to remember what filters I selected. When I hit **Submit**, the system will take some time to process the request. I will get an email when it's complete and follow the link to download my data.

- When I download and unzip the **Tables** file, I will get to 2 files: the county-level data .csv file and the codebook .txt file. The latter is needed to decipher the column names in the former.

- Let's take a look at the codebook file. In the **Race** category in Table 1, as the codebook will explain, column APP001 stands for "White," APP002 for (the offensive and outdated) "Colored," APP003 for "Chinese" (though what it might really stand for is all people of Asian origin), and APP004 for "Indian" (presumably for Indigenous people). Table 2 has some other interesting categories, such as country of origin, beginning with AP3052, "Foreign-born Africa." This might be of interest for my research, so I'll pay attention to those data as well. Table 3 just has 2 columns: AP4001 for "Native-born" and AP4002 for "Foreign-born." Not terribly specific, but it gives me some data if I wanted to look at changes in immigration to California over time.

- I can now open the .csv file and get rid of all fields that are not related to San Diego or, at the very least, California. It's always a good idea to save multiple versions of different files as you make changes, so I'll save the new copy of my file under a different name to indicate that this version only contains California data.

- The other thing to note (and keep) is the very first column in all these exports: **GISJOIN**. This is the column that will let me join the file that has data in it with the GIS county boundary file that I also requested to download (the **2008 TIGER/Line +** dataset). Opening that file in QGIS and joining it with my CA data file will allow me to map the different racial/ethnicities categories that I was able to find for 1880.

- Repeat the above steps for 1890, 1900, 1910, and 1920—remembering that some data will likely be missing and that territorial boundaries and definitions of "race" will shift over time. Remember to always cite [IPUMS NHGIS](https://www.nhgis.org/citation-and-use-nhgis-data) in any project that uses their data.

Page updated Google SitesReport abuseGoogle SitesReport abusePage details
