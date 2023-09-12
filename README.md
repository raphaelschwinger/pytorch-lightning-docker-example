# pytorch-lightning-docker-example
Example code how to run [pytorch lighting](https://www.pytorchlightning.ai/index.html) in a docker [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers) environment on a server with multiple Nvidia gpus.

## Setup

### Requirements
- Server with CUDA graphic cards
- Docker installed

### Installation

1. Clone repo

2. Open in VS Code

3. Reopen in Container

4. Install dependences
```
poetry install
```

5. Start shell
```
poetry shell
```

## Features

- [x] Multi-gpu support:
- [x] [Hyperparameter setup](https://lightning.ai/docs/pytorch/1.6.3/common/hyperparameters.html):
    - Easily save and load hyperparameters for different experiments
