#!/bin/bash

echo
echo "Waiting for tor proxy to become ready ..."
while ! nc -z localhost 9050; do
  sleep 5
  echo .
done
echo "Tor proxy: ready"

tail -f /dev/null