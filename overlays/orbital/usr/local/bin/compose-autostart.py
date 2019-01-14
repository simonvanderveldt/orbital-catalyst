#!/usr/bin/env python3

import logging
import os
import subprocess
import sys

logging.basicConfig()
LOGGER = logging.getLogger("compose-autostart")
LOGGER.setLevel(logging.INFO)

if len(sys.argv) != 2:
    sys.exit("Please pass the parent directory for the compose projects "
             "as the one and only argument")

COMPOSE_LOCATION = sys.argv[1]
COMPOSE_FILES = []

LOGGER.info("Starting compose projects in %s", COMPOSE_LOCATION)

for root, _, files in os.walk(COMPOSE_LOCATION):
    for file in files:
        if file == "docker-compose.yml":
            COMPOSE_FILES.append(os.path.join(root, file))

if COMPOSE_FILES:
    for compose_file in COMPOSE_FILES:
        composefile_path = os.path.dirname(compose_file)
        project_name = os.path.basename(composefile_path)
        LOGGER.info("Starting project %s from %s", project_name, composefile_path)
        subprocess.run(["docker-compose", "-p", project_name, "up", "-d"],
                       check=True, cwd=composefile_path)
        LOGGER.info("Done. %s is running", project_name)
else:
    LOGGER.info("No docker-compose.yml files found")

LOGGER.info("Done")
