#!/usr/bin/env python
# coding: utf-8

# In[60]:


import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import datetime
from time import sleep, time, localtime
from matplotlib import animation, rc


# In[63]:


fig = plt.figure(figsize = (6,6), dpi = 100)
# maintain consistent aspect ratio

# plot will appear in separate window
x = 0
get_ipython().run_line_magic('matplotlib', '')
while x < 40:
    plt.cla()
    current_time = datetime.datetime.now()
    # output current hour; since it is in military time, subtract 12 from the hour if greater than 12
    current_hour = current_time.hour
    if current_hour > 12:
        current_hour = current_hour - 12
    # output current minute
    current_minute = current_time.minute
    # output current second
    current_second = current_time.second

    theta_h = (np.pi/180) * (90 - 30 * current_hour - current_minute/2)
    theta_m = (np.pi/180) * (90 - 6 * current_minute)
    theta_s = (np.pi/180) * (90 - 6 * current_second)

    # outer function takes length of clock hand passed to it
    def outer(r):
        # inner function takes angle of clock hand, which is calculated above
        def inner(theta):
            # converting angle and length into x, y coordinates
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            coords = (x,y)
            return coords
        return inner

    # call outer function, pass 5 for r
    hour_hand = outer(5)
    # calculate x,y coordinates of hour hand, passing angle hand to hour_hand func
    x_hour, y_hour = hour_hand(theta_h)

    minute_hand = outer(7)
    x_minute, y_minute = minute_hand(theta_m)

    second_hand = outer(9)
    x_second, y_second = second_hand(theta_s)
    
    # remove axes
    ax = plt.gca()
    ax.axis('off')
    # center clock
    ax.axis('equal')
    

    # plotting x, y coordinates of each hand
    plt.plot([0, x_hour], [0, y_hour], linewidth = 10, label = "hour")
    plt.plot([0, x_minute], [0, y_minute], linewidth = 5, label = "minute")
    plt.plot([0, x_second], [0, y_second], linewidth = 2.5, label = "second")
    plt.axis([-20, 20, -20, 20])
    
    fig.canvas.draw()
    plt.pause(0.1)

    x = x + 1

    

