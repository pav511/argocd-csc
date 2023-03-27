#!/bin/bash -x

ENVIRONMENT=${1:?"Usage: write_secrets.sh ENVIRONMENT"}
TS_KEY=ts/software

VAULT_PATH_PREFIX=$(yq -r .vaultPathPrefix ../apps/cluster-config/values-$ENVIRONMENT.yaml)

# This is a bit tricky.  This makes the path different for
# $SECRET, which ends up getting passed into vault and making
# the keys.
cd secrets

for SECRET in *
do
  vault kv put $VAULT_PATH_PREFIX/$TS_KEY/$SECRET @$SECRET
done
