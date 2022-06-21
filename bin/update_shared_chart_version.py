import argparse
import pathlib

import yaml

APPS_DIR = "apps"


def main(opts):
    print(
        f"Updating {opts.app_type} apps Helm chart to version {opts.chart_version}"
    )

    apps = pathlib.PosixPath(APPS_DIR)
    dirlist = list(apps.iterdir())
    for appdir in dirlist:

        if opts.app_type == "collector":
            template_dir = appdir / "templates"
            if not (
                template_dir.is_symlink()
                and template_dir.resolve().name == "csc_collector"
            ):
                continue

        chart = appdir / "Chart.yaml"

        with chart.open() as ifile:
            values = yaml.safe_load(ifile)

        if opts.app_type == "csc":
            try:
                dependencies = values["dependencies"]
            except KeyError:
                continue
            for dependency in dependencies:
                if dependency["name"] == "csc":
                    dependency["version"] = opts.chart_version
        else:
            values["version"] = opts.chart_version

        # print(appdir, values)

        with chart.open("w") as ofile:
            yaml.dump(values, ofile, sort_keys=False)


if __name__ == "__main__":
    description = [
        "Update version for apps using the csc or shared Helm chart"
    ]
    parser = argparse.ArgumentParser(
        description=" ".join(description),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "app_type",
        choices=["csc", "collector"],
        help="Specify the application type to set the chart version for.",
    )
    parser.add_argument(
        "chart_version", help="The version of the Helm chart to set."
    )
    args = parser.parse_args()
    main(args)
