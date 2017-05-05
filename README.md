# Capstone Project Code - Udacity ML Nanodegree

This repo contains the code for the capstone project of the [Udacity Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009). The aim of this project is to learn
value functions to play board games using [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) with [deep learning](https://en.wikipedia.org/wiki/Deep_learning).

You can find the report for this project in [https://github.com/davidrobles/mlnd-capstone-report](https://github.com/davidrobles/mlnd-capstone-report).

And the proposal in [https://github.com/davidrobles/mlnd-capstone-proposal](https://github.com/davidrobles/mlnd-capstone-proposal).

This project requires the following dependencies:

- python=2.7
- keras=2.0.2
- numpy=1.11
- matplotlib=2.0.0
- pandas=0.18.1

which are specified in [environment.yml](../master/environment.yml).

Using [conda](https://conda.io/docs/) we can have this project running in three steps:

### 1. Create a conda environment
```bash
conda env create -f environment.yml
```

### 2. Activate environment
```bash
source activate capstone
```

### 3. Run an experiment

Experiments are located in [experiments/](experiments/).

```bash
make file=experiments/01_tic_ql_tab_simple.py run
```
