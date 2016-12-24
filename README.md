# holiday-lights-hack

> A holiday lights hack using the NeoPixel (WS2812 / WS2812b) from AdaFruit

Here we have a smart light ([Video on YouTube](https://www.youtube.com/watch?v=CjkovJdzmKw)) which will only run when it detects your presence in the room through a passive infrared PIR sensor. This means you can leave it plugged in all day and night and never have to worry about turning it off or shutting it down. The code in this respository is set to a 10-minute timeout.

**The build**

Parts:
* Raspberry Pi Zero
* USB WiFi adapter and shim
* 8-LED NeoPixel strip (from eBay)
* 1-2A 5v microUSB charger
* $1 holiday decoration
* A PIR sensor

For fixing everything in place I used hot glue, but be careful because it's easy to melt the plastic cover of the PIR sensor. The NeoPixel is plugged into 5v, GND and PIN 18 and can be driven straight from the Pi.

![Schematic](http://blog.alexellis.io/content/images/2016/11/schematic_b.png)

**Software**

The software is built into a Docker container with Python. To install Docker on your Raspberry Pi type in `curl -sSL get.docker.com | sh`.

**See also**

For my Alexa-controlled Christmas Tree check out this full write-up with schematics and diagrams.

* [Never too early for a Christmas IoT](http://blog.alexellis.io/christmas-iot-tree/)

