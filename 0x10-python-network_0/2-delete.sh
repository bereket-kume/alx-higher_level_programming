#!/bin/bash
# sends a DELETE request to the URL passed as the first argument a
curl -sX DELETE $1 -L
