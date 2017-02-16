### Goal

Install a strip of color changing LEDs in each child's room which will (1) act as a simple siri-controlled multicolor light; and (2) integrate into a smart home with functions such as
* slow fade on to wake the kids up on school days, when helpful during the winter;
* communicate time and status in a simple way during critical business processes like "getting the fuck ready for school without constant reminders";
* disco mode for parties or special events;

The software side of all this was rather easy for me - I have a DIY home controller which knows things like "is today a school day" and "what time is sunrise today". However I found the hardware side of this to be super interesting and a great learning experience.

The end result is a lighting experience which performs all of the above functions and more. The kids like it and - I hope - it's made our wake up routine easier for everybody.

### Parts List

* WS2812b 30 pixel LED strip
* ESP8266
* [5V 2A power supply](https://www.adafruit.com/products/276)
* [female DC power adapter](https://www.adafruit.com/products/368)
* 470 ohm resister
* [4700uF 10v capacitor](https://www.adafruit.com/products/1589)

### Inspirations

* [Wifi controlled Christmahanukwanzaa tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree/overview)

### Guides

* [Adafruit NeoPixel Überguide](https://learn.adafruit.com/adafruit-neopixel-uberguide)