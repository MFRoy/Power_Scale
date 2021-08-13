#!/bin/bash

set -e

bash scripts/setup.sh

bash scripts/test.sh

bash scripts/build.sh

bash scripts/config.sh

bash scripts/deploy.sh