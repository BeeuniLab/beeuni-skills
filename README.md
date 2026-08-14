# Valkor Skills

Public Marketplace skills, agents, and use-case templates for Valkor.

## Registry

The generated `registry.json` is the entry point consumed by Valkor's
Marketplace resolver. The source layout is intentionally kept readable:

- `runtime/skills/` contains installable skills.
- `runtime/agents/` contains optional agent personas.
- `.valkor/opencode/skills/` contains standalone skills such as `threejs-dev`.
- `.valkor/opencode/tools/` contains optional OpenCode tools.

Installers should resolve this repository at a pinned commit or release tag.
Marketplace items become project-owned files after installation.

Some entries depend on external services or connectors. Review their
capability metadata and upstream attribution before enabling them in a
production project.

