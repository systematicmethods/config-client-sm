#!/usr/bin/env bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

. ${SCRIPT_DIR}/env.sh

docker build \
  --build-arg image_full_name=${IMAGE}:${VERSION} \
  --build-arg cache_date="$(date)" \
  -t "${SMIMAGE}:${SMVERSION}" .
