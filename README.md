# ML Detection Pipeline for LiDAR Data

## Introduction

This repository contains the machine learning detection pipeline designed to process and analyze LiDAR data collected during autonomous runs of a formula student race car. The goal of this project is to predict the positions of cones from noisy LiDAR data to improve the car's autonomous navigation capabilities.

## Experiment Overview

The experiment involved collecting LiDAR data during the race car's trial runs, pre-processing this data, and then applying a machine learning model to detect cones. The data is first filtered to remove noise, and then a neural network is used to segment the cone positions from the LiDAR point cloud.

## Repository Contents

- `preprocessing.ipynb`: Jupyter notebook containing all the pre-processing steps applied to the LiDAR data.
- `filtering.py`: Python script used for the initial filtration of LiDAR data to remove ground and other non-cone related noise.
- `pythonmakesmorens.py`: Python script used for collecting and aggregating LiDAR data from multiple trial runs.
- `trial_3.1/`: Directory containing the LiDAR data used in this experiment.

## Setup and Usage

To run the pre-processing notebook, you will need Jupyter Notebook or JupyterLab installed on your system. Make sure you have the required Python packages installed by running:

```bash
pip install -r requirements.txt
