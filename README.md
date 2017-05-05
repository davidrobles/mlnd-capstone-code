# Capstone Project Code - Udacity ML Nanodegree

This repo contains the code for the capstone project of the [Udacity Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009). The aim of this project is to learn
value functions to play board games using [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) with [deep learning](https://en.wikipedia.org/wiki/Deep_learning).

You can find the proposal for this project in [https://github.com/davidrobles/mlnd-capstone-report](https://github.com/davidrobles/mlnd-capstone-report).

This project requires the following dependencies:

- python=2.7
- keras=2.0.2
- numpy=1.11
- matplotlib=2.0.0
- pandas=0.18.1

which are specified in [environment.yml](../master/environment.yml).

## Create environment
```bash
conda env create -f environment.yml
```

## Activate environment
```bash
source activate capstone
```

## Run an experiment

```bash
make file=experiments/01_tic_ql_tab_simple.py run
```
