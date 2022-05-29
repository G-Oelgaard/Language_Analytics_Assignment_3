# Language_Analytics_Assignment_3
## ------ SCRIPT DESCRIPTION ------
This repository contains a script that takes either a directory full of edgelists or a single edgelist, and produces a table showing relevant information for each node plus a simple visualisation.  

The script will:
- Take either a single edgelist in a .csv file, or a whole directory of them.
- Saves a .csv table containing each nodes: name, degree, betweenness centrality and eigenvector_centrality 
- Saves a plot containing a simple visualisation of the edgelist network. 

If a whole directory is given, it will create a table and plot for each file.

## ------ METHODS ------


## ------ DATA ------
The data should be a .csv file containing each nodes "source", "type", "target" and "weight" 

## ------ REPO STRUCTURE ------
"src" FOLDER:
- This folder contains the .py script.

"in" FOLDER:
- This is where the data used in the scripts should be placed. Ie. where the either the directory of edgelists or a single edgelist should be placed.

"out" FOLDER:
- This is where the new .csv and plots files will be placed. The plots will be placed in the "tables" subfolder and the plots in the "plots" subfolder.

"utils" FOLDER:
- This folder should include all utility scripts used by the main script.

## ------ SCRIPT USAGE ------
### Arguments

**Required**
Argument         | What it specifies / does
---------------- | -------------------------
"-f" / "--file" | Name of file or directory in the "out" folder to be used by the script.

## ------ RESULTS ------
The model achieves what it sets out to do. Although the user is not able to set custom names for the output tables and plots.
