#!/usr/bin/env python3
import json, sys, jsonschema

schema = json.load(open("schema/ats-v1.schema.json"))
data   = json.load(open(sys.argv[1]))
jsonschema.validate(data, schema)
print("✅ Valid ATS")