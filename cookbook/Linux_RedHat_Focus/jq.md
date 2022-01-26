# Parse a json with  forced color and without line formatting:

```
jq -rc
```

# Parse deeper into a JSON
```
jq '.hits .hits[0] ._source .quote' 
```

# Parse a JSON raw (so it wont have quotes around it)
```
jq --raw-output {.states, .last_updated, etc}
```

