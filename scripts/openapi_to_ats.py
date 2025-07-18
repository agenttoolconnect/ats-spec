#!/usr/bin/env python3
"""
Very small helper: reads a trimmed OpenAPI spec and
spits out a basic ATS skeleton.
"""
import json, sys, yaml

spec = yaml.safe_load(open(sys.argv[1]))
# simplistic extraction – extend as needed
print(json.dumps({
    "name": spec["info"]["title"],
    "description": spec["info"]["description"],
    "parameters": spec["paths"]["/"]["post"]["requestBody"]["content"]["application/json"]["schema"]
}, indent=2))