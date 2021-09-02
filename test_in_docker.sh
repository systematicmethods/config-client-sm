#!/usr/bin/env bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

. ${SCRIPT_DIR}/env.sh

echo docker run -it --rm  -v $(pwd):/code -w /code ${IMAGE}:${VERSION} "/code/test.sh"
docker run -it --rm  -v $(pwd):/code -w /code ${IMAGE}:${VERSION} "/code/test.sh"

