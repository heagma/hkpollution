# HKPOLLUTION

Simple CLI tool to get the current details of the pollution on any district in Hong Kong. 
It will display the information in a human readable format. 
Air quality index are given in *abbr* like **pm2.5** which means atmospheric particulate matter so it make it easier to understand the indexes.


# How to use it

    hkpollution -d <district>




## Examples

Let's say we want to get the current air quality on Yuen Long. 

    hkpollution -d yuen-long

It'll be displaying:

    ******         Yuen Long, HongKong (香港元朗)         ******
    
    
    Total Air Quality      -> 45 --------> good
    Carbon Monoxide        :  4.8
    Nitrogen Dioxide       :  23.5
    Ground-Level Ozone     :  2
    Particular Matter 10   :  18
    Particulate Matter 2.5 :  45
    Sulfur Dioxide         :  1.8

## Basic Measurements

Measurements are given depending on the total air quality, as follow:

 - up to 50:     ***Good*** 
 - up to 100:  ***Moderate*** 
 - up to 150:   ***Sensitive*** 
 - up to 200:  ***Unhealthy*** 
 - up to 300:  ***Very Unhealthy***
 - More than 300:         ***Poisoning***


## Requirements

You would need a token from aqicn.org to get it working in a project of your own.
Then copy the token and paste it on the api_details file.
**NOTE**: Make sure you use `git-secret` to secure your token details otherwise it will be a security risk to store keys on plain text even on github/gitlab.