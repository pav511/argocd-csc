#!/usr/bin/env python3
import argparse
import json
import os
import pathlib

from onepassword import OnePassword


class VaultKeyRetriever:
    def __init__(self):
        self.op = OnePassword()
        vault_keys_doc = self.op.get_item(uuid=os.environ["VAULT_DOC_UUID"])
        vault_keys_json = vault_keys_doc["details"]["notesPlain"]
        self.vault_keys = json.loads(vault_keys_json)

    def retrieve_key(self, environment, key_type):
        env_key = f"k8s_operator/{environment}"
        for e in self.vault_keys:
            if env_key in e:
                return e[env_key][key_type]["id"]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="fetch the vault key for an environment"
    )
    parser.add_argument(
        "environment", help="Environment name to retrieve key for"
    )
    parser.add_argument(
        "key_type", choices=["read", "write"], help="Which key to retrieve"
    )
    parser.add_argument(
        "--use-file",
        type=pathlib.Path,
        help="Use a temporary file to write the token to.",
    )
    args = parser.parse_args()

    vkr = VaultKeyRetriever()
    if args.use_file is None:
        print(vkr.retrieve_key(args.environment, args.key_type))
    else:
        with args.use_file.open("w") as ofile:
            ofile.write(vkr.retrieve_key(args.environment, args.key_type))
