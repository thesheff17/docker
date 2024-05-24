#!/bin/bash

echo "build.sh started..."
start_time=$(date +%s)

export BUILDKIT_PROGRESS=plain
docker build . -t thesheff17/dev:latest

end_time=$(date +%s)
elapsed_time=$((end_time - start_time))
minutes=$((elapsed_time / 60))
seconds=$((elapsed_time % 60))

echo "Elapsed time: $minutes minutes and $seconds seconds."
echo "build.sh completed."