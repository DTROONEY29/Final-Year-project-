Contextual understanding and object intent detection (CUAID)

@author: Daniel Rooney 2021

IMPORTANT: the only files in this folder are that of the system designed and the modified vizualisation_utils file, please
see instructions for other essential files needed to run this project. The models folder that is downloaded from the tensorflow object detection API repo is quite large and 
unweidly to drop into the submission filespace.

Instructions for use :

- Ensure you have downloaded all the files included in the object detection API repo - The object detection API is available at https://github.com/tensorflow/models/tree/master/research/object_detection for
  download. There are multiple utility files and modules needed to run the CUAID project. See https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html for API install.

- Please unpack all CUAID files from their respective folders individually into the object detection directory.

- Ensure test video is present in object detection directory and is not located in a separate folder.

- Run main.py to intialise startup, you will be prompted for the name of the file outlined above.

- The system will run the mobilenet model on your test video and output objects per frame to a text file.

- The system will run next step action classification using the convLSTM network and output to a text file.

- After output extraction and evaluation has finished you will be prompted as to whether you want to view the
  the results of the decision tree classifier or multinomial logistic regression model.


NOTE: visualization_utils.py has been modified for this project at lines 168, 169. All other util files (required to run this project as well)
      are unchanged.
Dependencies :

- Tensorflow (NOT GPU) 1.15 and python 3.7.
-  pycocotools 2.0
- UCF-101 Dataset can be downloaded from here https://www.crcv.ucf.edu/data/UCF101.php
- Anaconda distribution has been used for the virtual environment.
- IMPORTANT: 'models' must be set as root directory and 'research' as source folder

Package                  Version
------------------------ -------------------
absl-py                  0.11.0
attrs                    20.3.0
backcall                 0.2.0
certifi                  2020.6.20
chardet                  4.0.0
colorama                 0.4.4
decorator                4.4.2
dill                     0.3.3
future                   0.18.2
googleapis-common-protos 1.52.0
graphviz                 0.16
idna                     2.10
importlib-resources      5.1.0
ipykernel                5.3.4
ipython                  7.18.1
ipython-genutils         0.2.0
jedi                     0.18.0
jupyter-client           6.1.7
jupyter-core             4.6.3
np-utils                 0.5.12.1
numpy                    1.19.5
parso                    0.8.0
pickleshare              0.7.5
pip                      20.2.4
promise                  2.3
prompt-toolkit           3.0.8
protobuf                 3.14.0
pydotplus                2.0.2
Pygments                 2.7.1
pyparsing                2.4.7
python-dateutil          2.8.1
pywin32                  227
pyzmq                    19.0.2
requests                 2.25.1
setuptools               50.3.0.post20201006
six                      1.15.0
tensorflow-datasets      4.2.0
tensorflow-metadata      0.27.0
termcolor                1.1.0
tornado                  6.0.4
tqdm                     4.56.0
traitlets                5.0.5
urllib3                  1.26.3
wcwidth                  0.2.5
wheel                    0.35.1
wincertstore             0.2
