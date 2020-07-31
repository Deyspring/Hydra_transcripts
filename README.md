#########################################################
Hydra project -Alpha version 
########################################################

The Hydra project can accept one or multiple search terms. 
After providing the search terms, a spreadsheet with a list 
of the provided terms and their associate genes and transcripts is produced. 
This spreadsheet is placed in a folder. 


Start a virtual environment using Conda to test this environment, this project is not completed yet. 
Virtual environment creation command: 
conda create -n hyenv
conda activate hyenv
conda deactivate 


Check to see if Geckodriver is on the path: 
echo $PATH

Check to see what packages are installed: 
conda list

Notes: 
This program requires py2exe to be installed on your Windows machine. 
Type in your command line window the following to install it: 

pip install py2exe  

(Temp note, the package of files is not setup to be installed by py2exe just yet.
My upgraded virtual box is having some issues so it may take a bit before I can 
use py2exe to make a package for general use. 
For now run the following in your window: 

python hydra_trans_fetch.py


The spreadsheet is placed in the Hydra folder. 

