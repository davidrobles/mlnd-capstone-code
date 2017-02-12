# Capstone Project Code - Udacity ML Nanodegree

This repo contains the code for the final project of the [Udacity Machine Learning Nanodegree](https://www.udacity.com/course/machine-learning-engineer-nanodegree--nd009). The aim of this project is to use [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning) with [deep learning](https://en.wikipedia.org/wiki/Deep_learning) to create an agent that learns to play the game of [Connect 4](https://en.wikipedia.org/wiki/Connect_Four) by playing games against itself.

## Run tests

```bash
make test
```

## Run an example

```bash
make file=examples/tictactoe_count_positions.py run
```

## List all environments
```bash
conda info --envs
```

## Create environment
```bash
conda env create -f environment.yml
```

## Activate environment
```bash
source activate capstone
```

## List environment packages
```bash
conda list
```

## Deactivate environment
```bash
source deactivate capstone
```

## Delete environment
```bash
conda remove -n capstone --all
```
