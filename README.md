
# Project:
Acoustic Sentimental Analysis:
Our project uses an open library pyAudioAnalysis for feature Extraction.
The features extracted are:
1. Zero Crossing Rate
2. Energy
3. Entropy of Energy
4. Spectral Centroid
5. Spectral Spread
6. Spectral Entropy
7. Spectral Flux
8. Spectral rolloff
9-21. MFCC
22-33. Chroma Vector
34. Chroma Deviation

 
We explcitly convert the .mp3 files to .wav files using pydub.

The trained data set is loaded in a pickle file so as to avoid training everytime.

The Classifier used for prediction is Random Forest Classifier with
No of estimators: 30
No of Features: 6

## Requirements:

Operating system Ubuntu-14.04 and above
Python 2.7 and above

## Code Structure:
1. execute.py: python program for training and predicting the sentiment of files from input.txt
2. setup.py: python program that installs required packages and libraries to run the project.
3. run.sh: executes setup.py and execute.py
4. dataset.pickle , classifier.pickle: pickle file with trained dataset and classifier set.

## Steps to execute project:
1. Extract our zip file.
2. In order to be able to call the pyAudioAnalysis library from any path you need to add the folder that contains it in the ~/.bashrc file. In particular, add a line as the follow in ~/.bashrc:

export PYTHONPATH=$PYTHONPATH:"/home/bla/bla"

(use the exact path where the pyAudioAnalysis folder is contained - without the pyAudioAnalysis name, e.g. if the library is contained in /home/tyiannak/Research/libraries/pyAudioAnalysis, then use /home/tyiannak/Research/libraries in the bashrc file)

Then, you need to update the path details:

 source ~/.bashrc

3. Add the files to be predicted in given folder and their name in input.txt. 
4. Execute " bash run.sh " 

## Note: 

If you wish to change the training dataset just uncomment the line 'train_classifier()' in main in execute.py. This will create new classifier and save it in classifier.pickle.

