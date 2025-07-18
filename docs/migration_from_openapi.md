## Migrating from OpenAPI → ATS

1. Keep only the **POST** endpoint you want agents to call.
2. Drop headers, auth, etc. into `authenticationMethod`.
3. Run `python scripts/openapi_to_ats.py openapi.yaml > ats.json`
4. Validate: `python scripts/validate.py ats.json`
