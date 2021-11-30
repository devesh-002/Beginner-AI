# README

## Introduction:- 

This is  a implementation for Connect4 and the readme aims on explaining the file structure and dependicies only, regarding more intrinsic details on why stuff works check out the report of the Project. The dependencies here are tried to be kept as close to the original alpha-zero as the original one also used Tensorflow and keras.

### Dependencies:-

<ol>
    <li>Pygame version 2.0.1 </li>
    <li> Tensorflow  2.6.0 </li>
    <li> Keras 2.1.6</li>
    <li> Numpy  </li>
    <li> Python 3</li>
</ol>

### Run the Programme:-

To run it simply cd into the Alpha_zero directory or the classical_eval directory and run

```
python3 visualise.py
```

### File Structure:-

code folder contains some of my implementations and src is the main game playing folder. This has 2 parts one being the Classical Evaluation which uses minimax and other being the Neural-Network part which has the projects, both having a seperate visualise.py file.  To run this on your local machine run the **visualise.py** file in your computer. Make sure you are in the **same** directory as your file is in else there can be a few path errors. There is no need for any datasets as the model produces datasets from its own by playing with itself.

<ol>
    <li>To train you own model run the train.py file and to custom change anything along to your needs, change the variables in initialiser.py.</li>
    <li>C4.py contains the entire class of Connect i.e. the implementation of the entire game, it uses lists to make an empty board and then works further from there.</li>
    <li>Neural_Network.py contains a custom made model according to the description of Google Deepbrain, to learn more about it see the Report.</li>
    <li>self_train.py generates games so that the neural network can learn from itself.</li>
<li>mct.py and node_class.py are files for the MCT structure which is different from a generic MCT file and is made according to the needs of alpha zero and its evaluations.</li>
<li>minimax.py contains the implementation of the minimax algorithm and evaluation.py provides for the evaluation function of it. </li>
<li>Note that Depth>4 can be implemented but is not supported right now because it was taking a lot of time.
models/ folder contains few trained model in .h5 format and can be downloaded directly. </li>
</ol>

**Models folder**:- The levels are clearly specified in the model and they all vary over the amount of training provided with Level 4 trained over 5000 epochs, Level 3 over 3000 epochs, Level 2 over 500 epochs and Level 1 over just 3 to demonstrate it's learning. Similarly in minimax the depth signifies the level of the game.

A sample game played with the AI is :-

![Alt Text](https://github.com/devesh-002/Beginner-AI/blob/main/Readme_files/Connect4.gif)

