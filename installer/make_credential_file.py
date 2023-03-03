#!/usr/bin/env python3
import argparse
import json
import os
import pathlib


def main(opts):
    secret_keys = opts.secret_keys.split(",")
    secret_dir = pathlib.Path("secrets")
    for secret_key in secret_keys:
        secret_file = secret_dir / f"{secret_key}"
        credential_file = pathlib.Path().cwd() / f".{secret_key}-cred.sh"

        with secret_file.open() as sfile:
            data = sfile.read()

        secret_data = json.loads(data)

        with credential_file.open("w") as cfile:
            for key, value in secret_data.items():
                variable = key.upper().replace("-", "_")
                export_line = f"export {variable}={value}" + os.linesep
                cfile.write(export_line)
            if secret_key == "lfa":
                cfile.write(
                    "export MYS3_ACCESS_KEY=$AWS_ACCESS_KEY_ID" + os.linesep
                )
                cfile.write(
                    "export MYS3_SECRET_KEY=$AWS_SECRET_ACCESS_KEY"
                    + os.linesep
                )


if __name__ == "__main__":
    description = []
    parser = argparse.ArgumentParser()

    parser.add_argument("secret_keys", help="List of keys for secrets")

    args = parser.parse_args()
    main(args)
