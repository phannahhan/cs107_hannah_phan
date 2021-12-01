#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Markov import Markov

weather_today = Markov()
weather_today.load_data(file_path='./weather.csv')
print(weather_today.get_prob('sunny', 'cloudy')) # This line should print 0.3

