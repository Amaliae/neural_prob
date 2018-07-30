
# coding: utf-8

# In[9]:

# This model was created to answer to question whether prestimulus activity of prefrontal cortex is more predictive for auditory cortex activity in cocktail-party than cue tasks.
#The original research is described in Rodgers CC, DeWeese MR. (2014); Spiking responses of neurons in rodent prefrontal cortex and auditory cortex during a novel stimulus selection task. CRCNS.org.
#http://dx.doi.org/10.6080/K0W66HPJ


# In[10]:

import keras
from keras.preprocessing import sequence as seq
from keras.utils import to_categorical


# In[ ]:

#prestimulus=fantasy.loc[(fantasy['Stim_time']!=1) & (fantasy['Choice_time']!=1) & (fantasy['Stop']!=1)] #EXTRACT PRESTIMULUS ACTIVITY 


# In[8]:

#The Keras model was created by following the tutorials and instructions that can be found in https://machinelearningmastery.com/ and
#https://keras.io/getting-started/functional-api-guide/ 


# In[2]:

#The collected and one-hot enoded data has 21000 data  points and 4 feature column, the spiking actvity of neurons of one group
#is presented one column


# In[7]:

from keras.utils import plot_model
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from keras.layers.recurrent import LSTM
from keras.layers.wrappers import TimeDistributed
# input layer
visible = Input(shape=(100,4))

layer1 = LSTM(100, return_sequences=True)(visible)




output = TimeDistributed(Dense(4, activation='sigmoid'))(layer1)
# output
model4= Model(inputs=visible, outputs=output)
print(model4.summary())


# In[ ]:

model4.compile(optimizer='nadam',
              loss='poisson', metrics=['accuracy'])


# In[ ]:

long=model4.fit(X, y, validation_split=0.2, epochs=100, batch_size=100, verbose=2)


# In[ ]:

long1=model4.evaluate(X, y)


# In[ ]:

model4.save('my_model4.h5')  


# In[ ]:

from keras.models import load_model
mod1 = load_model('mod_file')

