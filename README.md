# Agent Tool Specification (ATS)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![OpenAPI 3.1](https://img.shields.io/badge/OpenAPI-3.1-green.svg)](https://spec.openapis.org/oas/v3.1.0)

A minimal, declarative JSON schema that turns any REST endpoint into an **agent-ready** capability.  
Built for compatibility with the **Model Context Protocol (MCP)** and the **AgentConnect** gateway.

---

## 📦 Contents

| Path        | Purpose                                           |
| ----------- | ------------------------------------------------- |
| `/schema`   | Latest ATS JSON Schema (`ats-v1.schema.json`)     |
| `/examples` | Real-world tool examples (Stripe, Weather, Slack) |
| `/docs`     | Markdown specifications and migration guides      |
| `/scripts`  | OpenAPI → ATS converter (Python)                  |

---

## 🚀 Quick Start

1. Copy `examples/weather.json` and rename it.
2. Replace values with your endpoint details.
3. Validate with:

```bash
python scripts/validate.py my_tool.json
```

## 📊 Versioning

- v1.x – current stable
- v2.x – draft (semantic discovery, streaming)

## 🤝 Contributing

Issues, PRs and new examples welcome!
See CONTRIBUTING.md.

## 📄 Licence

MIT © 2024 agenttoolconnect
