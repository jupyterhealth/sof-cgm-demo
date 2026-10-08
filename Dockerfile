FROM python:3.13-slim

RUN apt-get -y update \
 && apt-get -y install git \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /app

COPY pyproject.toml ./
COPY provider_app ./provider_app
COPY keep_cloned.py ./keep_cloned.py
RUN pip install --no-cache-dir .

COPY jupyter_server_config.py ./

ENV JUPYTER_CONFIG_DIR=/app
EXPOSE 8888

USER 1000

WORKDIR /tmp
CMD ["jupyter", "server", "--ip=0.0.0.0", "--port=8888", "--no-browser", \
      "--config=/app/jupyter_server_config.py"]
LABEL org.opencontainers.image.source=https://github.com/jupyterhealth/jupyterhealth-sof-provider-template
