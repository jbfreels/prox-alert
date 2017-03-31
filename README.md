# proxfart
Python script which utilizes a Parallax PING ultrasonic distance sensor to randomly play an MP3 file when someone triggers the sensor.  

I used this to play a fart sound when someone walks by, but you could change the sounds to play whatever you wanted when triggered.  

There's a 1 minute delay between triggers, if removed, it will constantly loop sounds.  

The inspiration for this short sample came from a greeting card which emits fart sounds and started with a button which played a random sound.  

## sounds
I got a couple samples from here: https://www.freesound.org/search/?q=fart

They must go into './mp3/' folder.

## configuration
* PIN_TRIGGER GPIO pin connected to the trigger pin on the sensor, default is **16**
* PIN_ECHO GPIO pin connected to the echo pin on sensor, default is **18**
* MAX_TRIGGER_DISTANCE is the maximum distance to allow trigger, default is **1** (meter)

## wiring

GPIO Pin: 2 -> Sensor: VCC

GPIO Pin: 6 -> Sensor: GND

GPIO Pin: 16 -> Sensor: Trig

GPIO Pin: 18 -> Sensor: Echo 
