### Goal

Install a strip of color changing LEDs in each bedroom in our house which will (1) act as a simple siri-controlled multicolor light; and (2) integrate into a smart home with functions such as
* slow fade on to wake the kids up on school days during the winter;
* communicate time and status in a simple way during critical business processes like "getting the fuck ready for school without constant reminders";
* disco mode for parties or special events;

The software side of all this was rather easy (don't get me wrong, it took forever) for me - I have a DIY home controller which knows things like "is today a school day" and "what time is sunrise". However I found the hardware side of this to be super interesting and a great learning experience.

The end result is lighting which performs all of the above functions and more. The kids like it and - I hope - it's made our wake up routine easier for everybody.

At some point I'd like to add a remote or some other self-service means of control. Siri on mom or dad's phone is a horrible UX for a kid who wants to turn on the lights.

### Parts List

* WS2812b 30 pixel LED strip
** Alitove $10 https://www.amazon.com/ALITOVE-Programmable-Individual-Addressable-Waterproof/dp/B01M5F571B/
* ESP8266
** D1 mini $9 https://www.amazon.com/Makerfocus-NodeMcu-Development-ESP8266-ESP-12F/dp/B01N3P763C/
* [5V 2A power supply](https://www.adafruit.com/products/276)
** $8 https://www.amazon.com/iMBAPrice-Adapter-Listed-Supply-5-Feet/dp/B00GUO5WUI/
* [female DC power adapter](https://www.adafruit.com/products/368)
** $6 for 5 but higher quality https://www.amazon.com/E-outstanding-Power-Female-5-5mm-Adapter/dp/B011YKCK5M/
* 470 ohm resister
** $3 in assortment of 300 https://www.amazon.com/gloednApple-300PCS-Resistors-Resistance-Assortment/dp/B01KFFH598/
* [4700uF 10v capacitor](https://www.adafruit.com/products/1589)
** $5.88 for 2 https://www.amazon.com/Electrolyt-Capacitor-4700mfd-HighTemperature-degrees/dp/B009SAKOW2/
** PCB
** case

### Schematic

TODO

### Softare 

Note that this assumes the Arduino IDE and that you have connected DIN to on the LED to pin TODO on the D1 mini.

It opens a server socket and listens for connections on port TODO. Usage is an exercise for the reader.

TODO

### Inspirations

* [Wifi controlled Christmahanukwanzaa tree](https://learn.adafruit.com/wifi-controlled-led-christmahanukwanzaa-tree/overview)

### References

* [Adafruit NeoPixel Überguide](https://learn.adafruit.com/adafruit-neopixel-uberguide)