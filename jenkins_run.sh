#!/bin/bash

# Run Every features
for folder in features*; do
	behave $folder -f json.pretty -o json_reports/$folder.json || true;
done
