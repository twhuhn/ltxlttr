FROM python:3.13-bookworm
LABEL maintainer="twhuhn" \
      description="A docker image based on Debian that provides a service for creating beautiful letters" \
      repo="https://github.com/huhntw/ltxlttr"

# Latex packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends texlive-latex-recommended texlive-fonts-recommended && \
    apt-get install -y --no-install-recommends texlive-latex-extra texlive-fonts-extra texlive-lang-all && \
    rm -rf /var/lib/apt/lists/*

RUN pip install pipenv
#COPY src /ltxlttr
#WORKDIR /ltxlttr