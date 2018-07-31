# neural_prob

In DataEngin file the functions and examples to handle and process the data are presented. 


The data that was used for analysis was taken from crcns.org,  http://crcns.org/data-sets/pfc/pfc-1/about-pfc-1 here

And in https://github.com/cxrodgers/Rodgers2014 repository you can find moduls for data analysis created by authors and additional information about data and experiment. 

Models 
LSTM  network with Input, LSTM and TimeDistributed layers was trained on collected data and the model evaluation on test data does not show enough performance to be able to do assumptions about prestimulus activity of prefrontal and auditory cortices. 


To reveal whether the represantation of auditory stimulus varies in different tasks , the Bayesian network with two fully connected layers was created. The goal of analysis was to classify the evoked activity of auditory cortex into localisation and pitch dicrimination tasks. 
For that reason neurons responding to pitch stimulus were indentified in cue trials of pitch discrimination blocks then the evoked  activity of that neurons was extracted for 'le_lo_pw' and 'le_low_lc' trials. After Bayesian inference and  approximation of posteriors the evaluation of Bayesian Network model on train data was performed and the model demonstrated 82% accuracy with 'Binary accuracy' metric. 












