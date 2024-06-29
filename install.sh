#!/bin/sh

# Install project dependencies
if [ "$APP_ENVIRONMENT" = "dev" ]; then
    echo "Instalando dependências de DESENVOLVIMENTO..."
    pipenv install --dev -v
else
    echo "Instalando dependências de PRODUÇÃO..."
    pipenv install --deploy -v
fi

# Check for errors
if [ "$?" -ne "0" ]; then
    echo "Houve uma falha no processo de instalação de dependências!"
    exit 1
fi