# pytorch-lightning-docker-example
Example code how to run [pytorch lighting](https://www.pytorchlightning.ai/index.html) in a docker [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) environment on a server with multiple Nvidia gpus.

## Setup

- Server with CUDA graphic cards
- Docker installed

## Features

- [ ] Multi-gpu support:
    - Status: probably gpus can not communicate appropriately, need to check:
        - NV Link
        - driver / cuda version 
- [ ] [Hyperparameter setup](https://lightning.ai/docs/pytorch/1.6.3/common/hyperparameters.html):
    - Easily save and load hyperparameters for different experiments


## Add python packages

Install packages with `pip install <package>` and add them to the `requirements.txt` file with `pip freeze > .devcontainer/requirements.txt`.

## Add system packages

Install packages with `apt-get install <package>` and add them to the `Dockerfile` file.