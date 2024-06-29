
#####################
#  BUILDER          #
#####################
# Argumentos definidos no início para flexibilidade
ARG USERNAME="userapp"

# Primeira etapa: Construção do ambiente de desenvolvimento
FROM python:3.10-alpine3.20 as builder

# Define o diretório de trabalho
ARG USERNAME
WORKDIR /home/${USERNAME}/app

# Instala dependências necessárias para compilação de pacotes Python
RUN apk --update add musl-dev gcc libffi-dev 

ARG APP ENVIRONMENT
ENV PIPENV_VENV_IN_PROJECT=true

RUN pip install pipenv 

# Copia os arquivos de definição de dependências
COPY ./Pipfile ./Pipfile.lock ./install.sh ./init.sql ./

RUN sed -i 's/\r$//' ./install.sh && \
    /bin/sh ./install.sh
    
#####################
#  RUNNER           #
#####################
FROM python:3.10-alpine3.20 as runner

# Adiciona uma etiqueta de identificação
LABEL vendor1="LeandrinSoftwares"

# Segunda etapa: Configuração do ambiente de execução
ARG USERNAME
RUN adduser -D -s /bin/ash ${USERNAME}
WORKDIR /home/${USERNAME}/app

# Instala certificados SSL e atualiza a lista de certificados confiáveis
RUN apk --update --no-cache add ca-certificates && \
    update-ca-certificates

    # Configura variáveis de ambiente para localização e PYTHONPATH
ENV LANG=pt_BR.UTF-8 \
    LANGUAGE=pt_BR:pt_br \
    LC_ALL=pt_BR.UTF-8 \
    PYTHONPATH=/home/${USERNAME}/app/app/src
    
# Copia o ambiente virtual Python criado na etapa anterior
COPY --from=builder /home/${USERNAME}/app/.venv /home/${USERNAME}/app/.venv

ENV PATH="/home/${USERNAME}/app/.venv/bin:$PATH"

# Copia o código do projeto para o diretório de trabalho
COPY --chown=${USERNAME}:${USERNAME} . .

# Remove caracteres de retorno de carro dos scripts shell e define permissões de execução
RUN sed -i 's/\r$//' /home/${USERNAME}/app/*.sh && chmod +x /home/${USERNAME}/app/*.sh

# Define o usuário não privilegiado como o usuário padrão para execução
USER ${USERNAME}

RUN mkdir -p /home/${USERNAME}/.vscode-server/extensions

# Define o comando padrão para iniciar o contêiner
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]