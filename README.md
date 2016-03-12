# Kegomatic 
This is a project copied from Adafruit, thanks guys

## Purpose
After the second time, my iron filter broke I decided I needed to moniter the amount of water it was ejecting.
A little googling lead me to this handy flow meter.
It was easy to setup and adapt to my purposes.

## Parts

1. Raspberry Pi
1. [Flow Meter](https://www.adafruit.com/products/828)


# Setting up the Pi

1. Disable Power management, create a file called: /etc/modprobe.d/8192cu.conf, add the following line:
    
        options 8192cu rtw_power_mgnt=0 rtw_enusbss=0


1. If you are using wireless, I found that I had to disable rtl8192 as well:
Create a file called: /etc/modprobe.d/rtl8192cu-blacklist.conf
    
        blacklist rtl8192cu

1. To complete the setup I followed these [install instructions](https://learn.adafruit.com/adafruit-keg-bot/raspberry-pi-code)

        git clone https://github.com/adafruit/Kegomatic.git
        sudo -i wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python
        sudo easy_install twitter
        sudo easy_install simplejson
        sudo easy_install httplib2
        #sudo easy_install python-oauth2
        sudo easy_install requests




