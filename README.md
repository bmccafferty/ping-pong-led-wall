# ping-pong-led-wall
My Ping Ping LED Wall, Created with Neopixels (WS2812(B))

## Overview
I love Christmas lights and Christmas decorations, I have been wanting to do an Programmable LED Project for a long time so this year I created an LED Wall.  Its mostly my own design with some inspiration from youtube videos e.g. the idea to use ping pong balls as diffusers came from [Bitlunis Lab](https://www.youtube.com/user/bitlunislab)

## See it in action!  Video
You can see a video of it in action with our christmas lights - [XMas Lights 2020](https://lightroom.adobe.com/gallery/49b7245c0c994274ad2b567c7e15d3b3/albums/5415eacbd05a417daf2fec101f77fa31/assets/1658f08c2bcf53be9f1d08cc86e28745)

## Progress Photos
Photo Progress of the Project from Start to End can be found Here - [LED Ping Pong Wall 2020](https://lightroom.adobe.com/gallery/49b7245c0c994274ad2b567c7e15d3b3/albums/5415eacbd05a417daf2fec101f77fa31/assets)

## My Shopping/Supplys List
* [Raspberry Pi Zero](https://shop.pimoroni.com/products/raspberry-pi-zero-wh-with-pre-soldered-header)
* [Pibow Case](https://shop.pimoroni.com/products/pibow-zero-w)
* 5v 2A USB Power Supply (I used an old Samsung fast charger)
* Old Poster Frame
* 255 Ping Pong Balls (Got Large Bags Cheap From ebay)
* Hot Glue Gun and LOTS of Hot Glue Sticks
* Soldering Iron
* Solder
* [Hook Up Wire](https://www.amazon.co.uk/gp/product/B07YFXG4KX/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)
* [2 x 5m 30 Pixels Per Meter WS2812(B) LEDs](https://www.aliexpress.com/item/32682015405.html?spm=a2g0s.9042311.0.0.36674c4dSAmHwG)
* Multimeter
* Wirecutters
* Wire strippers

## Design
My design was mainly driven by the size of the poster frame I had I Got 30 Pixel per Meter tape from Ali Express which cut nicly into 0.5m sections so that gave me 15 LEDs accross, Ping pong balls are 40mm so I mesured and placed me lines 40mm apart with the LED Strip in the middle of each 40mm section which gave me 17 lines down in total so my baord became 15 x 17.

To make hook up to power and the raspberry pi easy I put the connections at the bottom of the board for the data & power in.  As I am not running too many LEDs I was able to use the 5v out from the Pi Zero to drive the LEDs, I run them at 50% brightness which is plenty bright to see in the day & night in the window (See the photos for day & night shots)

## Wireing
In my design I started at the bottom of the board and wired up the way in a zig-zag fashion to make the soldering easier and shoter e.g. loops at the end of each row and not having to run wires all the way back to the start of each line as WS2812 Data lines required you to wire the data the correct way, power can be fed from either side of the strip but data must be fed from the side with the arrows pointing away so my wireing design looks like this (Albet 17 lines deep):

```
<---------------\
                |
/---------------/
|
\---------------< # Pi Connected Here
```
## The Build
Once the design and wireing plan was sorted it was time to get started on the build.  I mesured and drew my lines in pencil on the poster backboard, the WS2812s came with sticky tape on the back so I just removed the backing and attached that directly to the backboard, making sure that the arrows go one way then back the other on the line above to ensure easy to hook up the data line.

Once all attached I cut 3 x similar lengeths of wire and wired up the 5v, Data & Ground lines from the end of each line to the one above like this:

<img src="https://lightroom.adobe.com/v2c/spaces/49b7245c0c994274ad2b567c7e15d3b3/assets/1ca53e74ac3a4d9db2f5eb825446aded/revisions/989c49938917446398fcfee3baa518a5/renditions/0c011c7dbf78d242cf5fbc6cfe975c6b" width=50% height=50%>

As I was doing this after a few lines I wanted to test everything was going ok.  I was checking continuity between the 5v and ground lines between each strip to ensure my joints were correct, I also checked that I had not bridged any conenctions so checked that there was no continuity between the 5v and ground lines e.g. 5v on one line did not bridge to the ground on the next line.  I also ran some tests to ensure everything was lighting up correctly. See below in The Code section for the strand test code I was using to test everything was working.

Once this was completed I started to cut holes in the ping pong balls stabbing the scissors into bottom of them and cutting a small hole for the LED to shine into, there was no exact science to this, each was differant but the effect really worked.  As I was working with 30 pixels per meter this tape has about 30mm between each LED but ping pong balls are 40mm accross.  I was not about to start soldering each LED individually!  I am not that good at soldering (As my photos show!) and I thought well they are ping pong balls, I can just squash them together!  So thats what I did, Hot glue blob round each LED, Place the ping pong ball onto the LED over the hole and hold for about 5 seconds, then hold onto that one and slide the next one in pushing it against the one before to sort of fold it into its neighbour.  The effect worked really well.  I like how it started to look right away.  It also had the nice bonus of hideing my bad soldering job!

<img src="https://lightroom.adobe.com/v2c/spaces/49b7245c0c994274ad2b567c7e15d3b3/assets/fabeda65c4ce46b9a53ec4c541cb4b8a/revisions/9a56fc58a46044b1946f16ee79320f4f/renditions/e22d4036e19e2211bd329efa206d9fa6" width=25% height=25%>

I continued doing this for 255 LEDs/Ping ping balls.  There were a few crushed ping pong balls in the process but in the end I got there and the final result looked like this:

<img src="https://lightroom.adobe.com/v2c/spaces/49b7245c0c994274ad2b567c7e15d3b3/assets/372caf4801b64938b94ef7162957823d/revisions/f5148bcc2a344f9898f334c6d421cc83/renditions/4d6dc36526fad027b1af1ebc5f178cf0" width=50% height=50%>

## The Code
For the test code to ensure everything was working I used this [Adafruit Guide](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage) which lights each LED up red, green, blue then does a rainbow cycle.  I used this when I was building to ensure my connections were all correct and everything was wired/soldered correctly.

After that I designed a grid in excel to map each pixel to a grid postion, this was to make building images easier as my pixel numbers run in a zig zag patten it would of been hard to keep track of each LED, e.g. LED A1 was 256 and B1 was 226.  The sheet I used is in this repo.

Once this was all set it was designing some images, done on paper and in excel then codeing them.

It got a bit addictive and started adding some animation (using loops and turning pixels on to one colour then another colour) Just basic stuff this year (This was my first project after all!)

The end result I think turned out amazing. All the photos are in this gallary - [LED Ping Pong Wall 2020](https://lightroom.adobe.com/gallery/49b7245c0c994274ad2b567c7e15d3b3/albums/5415eacbd05a417daf2fec101f77fa31/assets) However some of my favorates ones are below:

<img src="https://lightroom.adobe.com/v2c/spaces/49b7245c0c994274ad2b567c7e15d3b3/assets/617fc871f7fb410fa57842473fb45c11/revisions/1a4ca63985594e5ca27e19f6f0a505e3/renditions/79a3440f2f2694acbef4e3a27e36b702" width=50% height=50%>

<img src="https://lightroom.adobe.com/v2c/spaces/49b7245c0c994274ad2b567c7e15d3b3/assets/3f27632f94874a3f9724dc4ba5375fce/revisions/2b757e7a4b8e40ddac213205058febc2/renditions/7eb4cb6673839d14cc7895dc615dcb37" width=50% height=50%>

<img src="https://lightroom.adobe.com/v2c/spaces/49b7245c0c994274ad2b567c7e15d3b3/assets/debd66ff455b46d09bdbf5209c3679cd/revisions/d6068ec45f1b49e0b344a102577d5b50/renditions/cfabb1eb50e18f0a31fe6d706f421002" width=50% height=50%>

## Next Steps
I am not sure this will ever be finished!  Nearly every night since its been up in the window I have added some new image/animation.  Already thinking about New Year.  I also wont be putting this in the loft with my Christmas Decorations in January so will have to think of other things to draw on it for an all year round project!  My friend suggested a Pixel Mario and I love that idea!

My code also needs some work, for example I do some scrolling text but I redraw the whole board for each position of the text so it took quite a bit of time to do.  I think I can do something with loops or perhaps the image libary to be able to scroll the letters easier and make it easier to just add text rather than turning on/off each pixel every step.

## Finally
I am really really pleased how this turned out and I think it looks amazing.  For a first attempt I have to say I am very please.  Very exicted to try some other LED Projects in the future.

