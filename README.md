# Manage an IMU with Python and Tkinter
Do you want work with an IMU? This would be a good point.


## Preparing the environment
In this tutorial we see the software that we need to start run the IMU and Raspbery Pi B+.

### What we need?
For this example we need the next hardware:
- Raspberry Pi B+
- IMU's Pololu MinIMU-9 v2

And the software:
-	python-smbus_3.1.0-2_armhf.deb
-	i2c-tools_3.1.0-2_armhf.deb
- minimu9-ahrs software

We should install this software in order to begin run the feartures of this Pololu IMU.

### Configure I2C port
The Raspberry PI B+ has two I2C ports, 0 and 1. By default, we work on port 1 and now we can see how configure it.

1. Kernel configuration: Installing Kernel Support (with Raspi-Config)
First we acces the Raspberry configuration menu with the command *sudo raspi-config*

2. The main configuration menu appears and we go to Advanced Options

<img src="/img/Screenshot_1.png" width="70%" height="auto">
 
3. We will move with the arrow keys to option A7 I2C

<img src="/img/Screenshot_2.png" width="70%" height="auto">

4. We will be asked if we want to activate the ARM I2C interface option

<img src="/img/Screenshot_3.png" width="70%" height="auto">

4. We will select yes anda screen will notify us taht ARM I2C interface has been activated

 <img src="/img/Screenshot_4.png" width="70%" height="auto">

5. After we will do this process, we will modify the Raspberry's modules fils in order to acces I2C port. For this, we type in the terminal *sudo nano /etc/modules*

In it, we will include these two lines at the end of the file

 <img src="/img/Screenshot_5.png" width="70%" height="auto">

Finally, we have to restart the Raspberry Pi and test if the I2C port works.

### Install minimu9-ahrs software
For the installation of the minimu9-ahrs software, we looking for the repository of links to be able to download al the necesary files on the URL

http://www.davidegrayson.com/minimu9-ahrs/debian/

Once this is done, we can already read the Pololu sensor, the MinIMU-9 v2 and calibrate ir correctly.

### Concluding
Now, if you want to learn more about IMU Pololu and know how we can manage it, I invite you to download the PDF of my project in which yo can see all of this with more and details. You can find in it, how you can use the GUI developed with pyton in order to run and extract all information that you want.


