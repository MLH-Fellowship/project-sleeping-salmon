#!/bin/bash

echo "Creating post with name TEST, email TEST, and content TEST"
curl -X POST http://localhost:5000/api/timeline_post -d 'name=TEST&email=TEST&content=TEST'

echo "Deleting test post"
ID=$(curl http://localhost:5000/api/timeline_post | jq '.[]' | head -n 6 | tail -n 1 | awk '{print $2}' | tr -d ',')
curl -X DELETE http://localhost:5000/api/timeline_post/$ID

echo "Current posts"
curl http://localhost:5000/api/timeline_post