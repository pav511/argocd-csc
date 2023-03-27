#!/bin/bash -e

ENVIRONMENT=${1:?"Usage: read_secrets.sh ENVIRONMENT"}
TS_KEY=ts/software

VAULT_PATH_PREFIX=$(yq -r .vaultPathPrefix ../apps/cluster-config/values-$ENVIRONMENT.yaml)

mkdir -p secrets

COMPONENTS=$(vault kv list --format=yaml $VAULT_PATH_PREFIX/$TS_KEY | yq -r '.[]')
for SECRET in $COMPONENTS
do
  if [ "$SECRET" == "nexus3-docker" ]; then
    continue
  fi
  vault kv get --field=data --format=json $VAULT_PATH_PREFIX/$TS_KEY/$SECRET > secrets/$SECRET
done
