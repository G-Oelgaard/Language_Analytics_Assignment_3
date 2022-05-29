## Import packages ##
import re, os, sys
sys.path.append(os.path.join(".."))

import spacy 
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import argparse
    
# create illustration and .csv
def network(file):
    file_name = os.path.basename(file)
    file_name = file_name.split(".")[0]
    
    if os.path.isdir(file):
        outpath_fig = os.path.join("..","out", "plots", file_name+"_network.png") # Set outpath for illustration. Filename will be filename+"_network.png"
        outpath_csv = os.path.join("..","out", "tables", file_name+"_network_output.csv") # Set outpath for .csv. Filename will be filename+"_network.csv"
    else:
        outpath_fig = os.path.join("..","out", "plots", file_name+"_network.png") # Set outpath for illustration. Filename will be filename+"_network.png"
        outpath_csv = os.path.join("..","out", "tables", file_name+"_network_output.csv") # Set outpath for .csv. Filename will be filename+"_network.csv"
    
    data = pd.read_csv(file, delim_whitespace=True) # read file
    G = nx.from_pandas_edgelist(data, "Source", "Target", ["Weight"]) # create network
    
    plt.figure(figsize=(12,12)) # plot and save
    nx.draw_networkx(G, with_labels=True, node_size=20, width=0.5)
    plt.savefig(outpath_fig, dpi=300, bbox_inches="tight") # save .png
    
    ev = nx.eigenvector_centrality(G) # Get eigenvector, betweeness and degree
    bc = nx.betweenness_centrality(G)
    de = dict(G.degree)
    
    output_data = pd.DataFrame(dict(Eigenvector = ev, # Create dataframe with the three values above
                                    Betweenness = bc,
                                    Degree = de))
    output_data.index.name = "Name" # set name of index to "name" as it correlates with the word name

    output_data.to_csv(outpath_csv) # save .csv

# Do network analysis for single file or whole directory
def full_edgelist_output(file):
    filepath = os.path.join("..","in", file)
    if filepath.endswith(".csv"):
        network(filepath)
    else:
        for filename in os.listdir(filepath):
            filename_filepath = os.path.join(filepath, filename)
            network(filename_filepath)
            print(f"{filename}: Done!")

# args_parse
def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required = True, help="Name of file or directory to be used by the script?")
    args = vars(ap.parse_args())
    return args

## Main ##
# Defining main
def main():
    args = parse_args()
    full_edgelist_output(args["file"])

# Running main
if __name__ == "__main__":
    main()