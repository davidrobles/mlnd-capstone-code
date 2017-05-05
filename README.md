# Capstone Project Code - Udacity ML Nanodegree

This repo contains the code for the final project of the [Udacity Machine Learning
Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009). The aim of
this project is to use [reinforcement
learning](https://en.wikipedia.org/wiki/Reinforcement_learning) with [deep
learning](https://en.wikipedia.org/wiki/Deep_learning) to learn value functions that can be used by
an agent to play the games of [Tic-Tac-Toe](https://en.wikipedia.org/wiki/Tic-tac-toe) and [Connect
4](https://en.wikipedia.org/wiki/Connect_Four) by playing games against itself.

This project requires the following dependencies:

- python=2.7
- ipython
- scikit-learn=0.18
- keras=2.0.2
- numpy
- matplotlib=2.0.0
- pandas

## Create environment
```bash
conda env create -f environment.yml
```

## Activate environment
```bash
source activate capstone
```

## Run an example

```bash
make file=experiments/tictactoe_count_positions.py run
```
