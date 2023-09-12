FROM nvidia/cuda:11.6.2-runtime-ubuntu20.04

# # set non interactive mode
# ARG DEBIAN_FRONTEND=noninteractive

# # install dependencies to build python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    git \
    curl

# install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

# # copy the requirements.txt file first to avoid re-installing dependencies
# COPY requirements.txt .

# # install dependencies
# RUN pip install -r requirements.txt
