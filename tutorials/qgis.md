---
layout: tutorial
title: "QGIS"
card_title: "QGIS"
permalink: /tutorials/qgis/
image: /assets/img/tutorials/card-qgis.png
order: 6
description: "Use the software to map some historical data and to georeference a historical map to display that data on."
audience: "HIST 502 · CSUSM"
steps: true
---

*Note: This tutorial is specifically for HIST 502 students at California State University San Marcos. It borrows heavily from the expertise of Dr. Jeffrey Charles and from* [*Dr. Fred Gibbs's tutorials*](http://fredgibbs.net/tutorials/)*.*
{: .note}

Now that you've watched the first half of [Klas Karlsson's tutorial](https://youtu.be/kCnNWyl9qSE) and gotten a bit familiar with QGIS, we are going to use the software to map some historical data and to georeference a historical map to display that data on.

## Create a Map

- Open QGIS and start a new project (select **New Project** from the top ribbon menu). Go ahead and save it (by clicking **Save Project**) in a dedicated folder for this tutorial. QGIS is not without glitches, so make it a habit to save things early and often as you work through the tutorial. I saved mine as the very creatively titled "QGIS Tutorial."

- Your new project will be blank because QGIS works with data, not maps, so we'll need to add some data to tell it to display something other than a blank slate. In this first exercise, we will make a map of the 1870 Census.

- The first thing we'll do is acquire the shapefile of U.S. and Native territories as they existed in 1870. Download the file titled "harvard-nhgis-pop1870-shapefile.zip" from [this Google Drive folder](https://drive.google.com/drive/folders/19p07NKywWybb1iv8lR8mm5VYZryD99ky?usp=drive_link) (your browser might say something like "Insecure download blocked," so you may need to tell it to download it anyway). Once you've downloaded the file, find it on your computer, unzip it, and move the extracted folder into whatever folder you dedicated for this tutorial.

- Now let's load it into QGIS. In the second-row ribbon layer, click **Open Data Source Manager** (the icon looks like three different folders with a green plus sign in the corner), under the left-hand Browser menu, select **Vector**, in the resulting window, under **Source Type** select **Directory**, then click the three dots (...) to the right of **Vector dataset(s)**, navigate to the unzipped folder you just downloaded, and select the file **NHGIS_POP1870.shp**. Click **Open** and then **Add**.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-1.jpg)

- Hit **Close** on the **Data Source Manager** window, and you should see a map with some county boundaries (the color may be different for you).

![]({{ site.baseurl }}/assets/img/tutorials/qgis-2.jpg)

- Click **Save Project** to save your progress (I will remind you to save your changes multiple times throughout the tutorial, as this is a profoundly useful habit to get into with any kind of DH work).

- Next, let's explore what we just imported. In the Layers panel (the one in the bottom left of your screen), right-click on the harvard-nhgis-pop1870-shapefile layer and select **Rename Layer**. Rename it to "1870 Census." It's always good to give the different layers logical names so as you add new layers, you know exactly what each one represents.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-3.jpg)

- Let's also actually look at the data we've imported to understand what kind of information we have beyond just the county/territory boundaries. To see the data, right-click on your 1870 Census layer again and select **Open Attribute Table**. In the table, you'll see a number of useful columns, such as the names of the territories in the NHGISNAM column (3rd column from the left) and, if you move all the way to the end of the columns, the POP_TOTAL column (3rd from the right/end), which gives us the number of residents in that county/territory. Another really important column is called GISJOIN—each county/territory in the dataset has a specific code that allows us to join other kinds of data to this file using this unique identifier column.

- For now, let's visualize that POP_TOTAL column on our map. To do so, let's get into the layer's Properties. There are two ways to do that: you can once again right-click on your 1870 Census layer and select **Properties** or you can simply double-click on the layer. Either way, you will see the **Symbology** properties pop up with **Single Symbol** selected at the top. Click on the menu arrow to the right of **Single Symbol** and select **Graduated**.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-4.jpg)

- You should now see the **Graduated** symbology properties. Right under Graduated, you will see the **Value** field, which is currently blank. This is where you tell QGIS what data you would like to see represented on your map and how to handle the different values in the particular data column that you select. We want to see the total population numbers categorized using different colors in our map, so we'll click on the arrow to the right of **Value** and select the POP_TOTAL column.

- Now, nothing has happened yet because we haven't told QGIS what we want to do with the data in that column. Click on the **Classify** button at the bottom of the open menu.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-5.png)

- Once you click **Classify**, you will see 5 different categories populate in the Symbol/Values/Legend field above. QGIS looked at the range of the numbers in your POP_TOTAL column and divided them into 5 different groups ranging from smallest (white) to largest (red) values. You could decide to divide your data differently and change the **Mode** from Equal County to, say, Equal Interval, depending on what you want your data to communicate. If you wanted to include more groups, you could change the number of **Classes** to the right of the bottom menu from 5 to, say, 10. These settings really just depend on what you are trying to communicate with your categorization. For now, let's stick with the 5 classes. Click **OK** to apply your changes and close the Properties menu.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-6.jpg)

- The resulting map should now look like this—with the most populated areas appearing in the north and northeast, as well as parts of the south. This is not at all surprising but cool to visualize. The thing that I would change at this point is to add more Classes, since there are vast territories that appear in white, which I know looking at my legend under Layers means there could be anywhere from 0 to 3,343 people living there, and I'd probably want to know which places have closer to 0 people and which have more population. The same goes for my last group: the fact that it ranges from 21,661 people to 942,292 doesn't allow me to adequately distinguish between really densely populated areas and ones that only have 20+ thousand people. But let's not worry about any of that for now.

- Click **Save Project**.

- What we do want to do next is situate the lonely floating map in space. To do so, let's just use one of the automatically pre-loaded world maps available in QGIS's **Browser** (that's the menu to the left of the map and just above the **Layers** menu. You may need to scroll down a bit to get to **XYZ Tiles** and from there double-click on OpenStreetMap.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-7.jpg)

- Oh no! Our lovely census map seems to have disappeared! Good thing we've been saving our project frequently. We could just quit QGIS in a panic and re-open our project in a fresh session to see our map unharmed by the map of the world. But we don't need to do that. All that happened when you double-clicked on OpenStreetMap is that your project added a layer and placed that new layer on top of your 1870 Census layer. In the **Layers** menu simply drag the **OpenStreetMap** down and, voilà, you've rearranged the order in which the two layers are arranged—with your map being on top of the world map.

- Click **Save Project**.

- That new view is great, but what if we wanted to be able to see some of the base map under our 1870 Census layer? To do so, we'll adjust the layer's transparency settings. Let's go back into the 1870 Census layer **Properties** (double-click or right-click and select **Properties**), select **Symbology**, and at the very bottom, you should see **Layer Rendering** just above the Help/Style/Apply buttons. Click the arrow next to **Layer Rendering** to expand that sub-menu and set the **Opacity** slider to 50% (you can do so manually or by typing in 50 to the right of the slider). Click **OK**.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-8.jpg)

- Now when you zoom in on the map, you can actually make out state boundaries and town names. You can always change the transparency setting again later.

- Click **Save Project**.

## Add Map Features

- So far, you've learned how to add shapefiles with county/territory boundaries and other census information, how to visualize the kind of data you are interested in, and how to integrate your map with built-in QGIS features.

- Next, let's learn how to visualize other kinds of data. In this example, let's say we wanted to study the relationship between railroads and population in 1870 U.S. and western territories. We already have a great start with the county boundaries and population data. Now let's add some railroad data.

- We'll use the data available through the Railroads and the Making of Modern America Project. Go to their [Data](https://railroads.unl.edu/resources/) page, and under **Download Data**, click on "Historical GIS: The 1840-1845-1850-1861-1870 Railroad System in America, State and National Shapefiles." Unzip the downloaded file and place it into whatever folder has now become you QGIS tutorial directory.

- Examine the folder. Once you go in, you'll see 6 different subfolders. The one we are interested in is **RR1870**, and it contains a number of geospatial files. Let's get them loaded into QGIS.

- See if you remember how to upload data to your project. If not, no worries: from the second row of the ribbon menu at the top of QGIS, click **Open Data Source Manager**. In the left-hand menu that pops up, select Vector, under **Source Type**, make sure **Directory** is selected, and then click the three dots to the right of **Vector Dataset(s)** to navigate to your **RR1870** folder that you just downloaded. Click **Add** and then **Close**.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-9.jpg)

- It may not look like much, but you have successfully added your railroads data. You can tell by the new yellow lines on my map (your colors might be different) and by the fact that there is a new layer added in my **Layers** menu. Let's rename the new layer (currently RR1870-RR1870WGS84) to "Railroads."

- Click **Save Project**.

- Let's also play around with how the railroads are displayed. To help make things easier, let's temporarily remove the Census and OpenStreetMap layers from view. To do so, simply un-click the checkmarks next to both of those layers in your **Layers** menu.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-10.png)

- We are back to the railroads lonesomely floating in space, which is fine because we are trying to change how they are displayed on the map.

- Let's get into our Railroads' **Properties** and once again deal with the **Symbology** tab in the left-hand menu. You'll see right away under **Single Symbol** that the railroads are displayed as a **Line/Simple Line**. If you look down, you'll see their color, opacity, and width, along with various other options available to you underneath.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-11.png)

- I like the **topo railway** option in the right-hand corner of my menu, so I'll select that. Once I do, the menu will automatically update the color and width. Click **OK**.

- Great! Now our railroads actually kind of look like railroads.

- Click **Save Project**.

- Make the 1870 Census and OpenStreetMap layers visible again by clicking the check boxes next to them, and we have something resembling a map of 1870s U.S./North American territories, which allows us to confirm that yes, most railroad hubs were indeed placed in densely populated areas, but we also see the railroads expansion into the west, which of course would, in turn, bring more people into these territories. Neat!

![]({{ site.baseurl }}/assets/img/tutorials/qgis-12.jpg)

## Georeference a Historical Map

- What we have here is great, but what if we wanted to make the map even more historically accurate by overlaying our data on a map that not only has the correct county/territory boundaries (which our map does, thanks to the 1870 Census shapefile), but also actual contemporary historical markers? We can do that by adding a scanned image of an actual 1870s map and aligning it to our map in a process called georeferencing. 

- First, let's find a high quality historical map. I used David Rumsey's Map Collection to do a quick search for 1870. On the first results page, I found [this map](https://www.davidrumsey.com/luna/servlet/detail/RUMSEY~8~1~219371~5504599:United-States-?sort=Pub_List_No_InitialSort%2CPub_Date%2CPub_List_No%2CSeries_No&qvq=w4s:/where%2FUnited%2BStates;q:1870;sort:Pub_List_No_InitialSort%2CPub_Date%2CPub_List_No%2CSeries_No;lc:RUMSEY~8~1&mi=10&trs=189) by A. J. Johnson. To download the map, you could right-click on the map and save the image to your hard drive, but remember: you want a high resolution copy, in order to get which click on the **EXPORT** button in the top right-hand corner of the page. A small menu with available size options should pop up. Click on the **Extra Large** option, wait for the export to complete, unzip the downloaded file, and move it to your QGIS tutorial folder. Open the image and inspect it: when you zoom in, you can clearly see the various map features, which is great for our purposes.

- Now let's get the image into QGIS. We will add the image—you guessed it—as a new layer, but this time, we will be adding a raster layer. From the second row of the ribbon menu at the top of QGIS, click **Open Data Source Manager**. In the left-hand menu that pops up, select **Raster**, under **Source**, click the three dots and then navigate to the .jpg file you just downloaded (notice that this time you are not navigating to a folder containing a file, but to the file itself). Click **Add** and **Close**.

- Click **Save Project**.

- Depending on your zoom level, you may not see the newly added layer at all, but you will see that a new layer has been added in the **Layers** menu. Let's rename that layer "1870 Map." When you go to rename it, you'll see a question mark next to it, and if you click on it, QGIS will tell you that it doesn't know what to do with this layer because it has no georeferencing information.

- This is what we'll be working on next. (By the way, to see where your new layer actually ended up, zoom out until you see the image floating in some corner of your QGIS canvas. This is fine for now. It will likely look something like this.)

![]({{ site.baseurl }}/assets/img/tutorials/qgis-13.jpg)

- To fix whatever is happening here, let's georeference our map. Essentially, you will be adding points to both the world map and your image to tell QGIS how to properly align the image on your canvas.

- There is a built-in tool called **Georeferencer** that will help us do that. In the main QGIS menu (at the top of the window), select **Layer** and click on **Georeferencer**. (If you can't find it there for whatever reason, you can always type the word Georeferencer into the Help menu at the top as well.)

- A new, depressingly blank Georeferencer window should pop up. If your mouse hovers over the blank canvas, you will notice it will change its cursor and clicking anywhere will leave a dot. These dots will tell QGIS which feature in your .jpg map corresponds to the existing georeferenced map.

- You technically only need three points to georeference an image, but the more points you add, the better your accuracy will be. My strategy: click on easily identifiable features, such as distinct borders, lakes, and curves for perfect alignment.

- Let's try this. At the top of the **Georeferencer** menu window, click on the **Open Raster** button (blue square in the left-hand corner) and once again navigate to the .jpg of the map you just downloaded; it should now show up in your canvas.

- In the middle of the **Georeferencer** menu window, click on the **Add Point** button (looks like a plane with a yellow star next to it) and begin adding points. Again, here precision matters. So start by zooming into Florida and clicking the southernmost point. Once you've hit that, a new dialogue window will pop up asking you how you want to go about georeferencing that point. Click From **Map Canvas** in the left-hand corner of the pop-up. Repeat what you did with the image on the actual map: zoom all the way into Florida and find the exact same point that you had clicked on in Georeferencer. 

- Now that same pop up will appear with filled-in coordinates. Click **OK**.

- Under your image in Georeferencer, you should now see a new row, which corresponds to your first point's coordinates. 

- If you make a mistake, you can right-click on the appropriate row and remove that point.

- Rinse and repeat at least 5 more times in various parts of the image/map to finish georeferencing your image. In the Georeferencer menu, switch between the **Pan** option and the **Add Point** option to move around your map between points. As you work, it might be helpful to have the two maps side-by-side in order to avoid making mistakes. If you are anything like me, you'll need to actually decide on where the two points will be before starting adding the next point—otherwise, trying to zoom and pan in your main QGIS window is a real pain. If you are smarter than me, you will first un-click the visibility layer of your 1870 Census to be able to better see your base map.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-14.jpg)

- In the end, I've added 13 points, trying my best to use obvious spots, such as boundaries, islands, and unusual geographical features.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-15.jpg)

- Once you've entered 5–10 points, in the **Georeferencer** menu, click on **Transformation Settings** (yellow gear icon). For **Transformation type**, choose **Thin Plate Spline** and for **Resampling methods**, choose **Cubic Spline**. Click the three dots to the right of **Output file** and select a folder in which your warped image will be saved (I recommend your QGIS tutorial folder). Finally, check the box that says **Use 0 for transparency when needed**. Click **OK**.

- Go back to the top of the Georeferencer menu and click the green **Play** button. This is what **initiates** the merging of your image with the map. Wait...

- Once the process is done, go back to your main QGIS window, and you'll see that QGIS added your image to your map. It's not the prettiest map I've ever seen, but it did the job!

- Click **Save Project**.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-16.jpg)

- QGIS named the new georeferenced image "0358021_modified," and I'll want to adjust that layer's transparency. Go to the layer's **Properties** and select **Transparency** in the right-hand menu column. Change **Global opacity** to about 60%, which should let you see all of your layers together, assuming you have turned the 1870 Census layer's visibility back on.

- Let's do just a couple more things to make the map prettier. Let's turn off the visibility of the **OpenStreetMap** layer, since we (sort of) have a good map background now to see our census/railroad data on. And let's change the colors of the total population graduated symbology in the 1870 Census layer to blue, since the red scale interferes with the pinks and reds in our historical map. go to 1870 Census layer's **Properties**, select **Symbology**, and under **Color ramp** navigate to **Blues**. Under Layer rendering, bring **Opacity** up to about 80%. Click **OK**.

- Ah... much better.

![]({{ site.baseurl }}/assets/img/tutorials/qgis-17.jpg)

- Click **Save Project**.

- You can continue customizing your visibility settings and playing around with different views. You can also export any view of your map and share it with others. Congratulations on successfully learning how to make maps, add data and features, and georeference historical maps!
