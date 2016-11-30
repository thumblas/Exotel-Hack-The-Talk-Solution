import os ,pickle ,wave
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
from pydub import AudioSegment
import numpy ,thread ,time ,math
from thread import start_new_thread
from threading import Thread
from pyAudioAnalysis import audioTrainTest as aT
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

data_set= []


def read_input():
    # input.txt contains the mp3 file name in each line which are present int
    # In the current directory the program is being executed.
    f = open('input.txt')
    files = f.read().split('\n')
    # Sanity cleaning to remove empty strings
    files = [f for f in files if f]
    return files




data_set = []
for file in os.listdir("training_dataset/unhappy"):
    temp = []
    mean_value = []
    if file.endswith(".mp3"):
        #print "training_dataset/unhappy/"+file
        sound=AudioSegment.from_mp3("training_dataset/unhappy/"+file)
        sound.export("test.wav",format="wav")
        [Fs, x] = audioBasicIO.readAudioFile("test.wav");
        F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.05*Fs, 0.025*Fs);
        for i in range(len(F)):
            temp.append(numpy.mean(F[i]))
        mean_value.append(temp)
        mean_value.append(1)
        data_set.append(mean_value)
for file in os.listdir("training_dataset/happy"):
    temp = []
    mean_value = []
    if file.endswith(".mp3"):
        #print "training_dataset/happy/"+file
        sound=AudioSegment.from_mp3("training_dataset/happy/"+file)
        sound.export("test.wav",format="wav")
        [Fs, x] = audioBasicIO.readAudioFile("test.wav");
        F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.05*Fs, 0.025*Fs);
        for i in range(len(F)):
            temp.append(numpy.mean(F[i]))
        mean_value.append(temp)
        mean_value.append(2)
        data_set.append(mean_value)
for file in os.listdir("training_dataset/angry"):
    temp = []
    mean_value = []
    if file.endswith(".mp3"):
        #print "training_dataset/angry/"+file
        sound=AudioSegment.from_mp3("training_dataset/angry/"+file)
        sound.export("test.wav",format="wav")
        [Fs, x] = audioBasicIO.readAudioFile("test.wav");
        F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.05*Fs, 0.025*Fs);
        for i in range(len(F)):
            temp.append(numpy.mean(F[i]))
        mean_value.append(temp)
        mean_value.append(3)
        data_set.append(mean_value)
for file in os.listdir("training_dataset/neutral"):
    temp = []
    mean_value = []
    if file.endswith(".mp3"):
        #print "training_dataset/neutral/"+file
        sound=AudioSegment.from_mp3("training_dataset/neutral/"+file)
        sound.export("test.wav",format="wav")
        [Fs, x] = audioBasicIO.readAudioFile("test.wav");
        F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.05*Fs, 0.025*Fs);
        for i in range(len(F)):
            temp.append(numpy.mean(F[i]))
        mean_value.append(temp)
        mean_value.append(4)
        data_set.append(mean_value)

x = []
y = []
for i in range(len(data_set)):
    x.append(data_set[i][0])
    y.append(data_set[i][1])

clf = RandomForestClassifier(n_estimators=30,max_features=6,max_depth=None,min_samples_split=1,bootstrap=True)
clf = clf.fit(x, y)
#f2 = open('classifier.pickle', 'wb')
#pickle.dump(clf, f2)
#f2.close()
#print "Written to pickle"
files = read_input()
os.system("touch test.wav")
for mp3_file in files:
	mean_value = []
	sound=AudioSegment.from_mp3(mp3_file)
	sound.export("test.wav",format="wav")
	#print mp3_file
	[Fs, x] = audioBasicIO.readAudioFile("test.wav");
	F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs);
	for i in range(len(F)):
		mean_value.append(numpy.mean(F[i]))

x=clf.predict(mean_value)

if x==1:
        print("unhappy")
if x==2:
    print("happy")
if x==3:
    print("angry")
if x==4:
    print("neutral")
