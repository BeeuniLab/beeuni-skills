# Beeuni Skills

Public standalone Marketplace skills for Beeuni.

## Registry

The generated `registry.json` is the entry point consumed by Beeuni's
Marketplace resolver. This repository intentionally contains the ten public
standalone skills under `.beeuni/opencode/skills/`, plus the `people_search`
tool used by `people-search`.

Installers should resolve this repository at a pinned commit or release tag.
Marketplace items become project-owned files after installation.

Some entries depend on external services or connectors. Review their
capability metadata and upstream attribution before enabling them in a
production project.
