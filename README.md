# Cockpit Design Aesthetics MCP Server

Translates cockpit instrument panel design principles into vivid visual language for image generation.

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Test
./tests/run_tests.sh

# Run locally
python -m cockpit_design_aesthetics
```

## Architecture

Three-layer system for cost-optimized image generation:

1. **Layer 1 (Deterministic)**: Instrument taxonomies, positioning rules, color conventions
2. **Layer 2 (Mapping)**: Compose requirements → visual parameters  
3. **Layer 3 (Synthesis)**: Claude generates vivid image prompts

## Tools

- `get_aircraft_type_profile()` - Aircraft configurations
- `get_panel_layout_rules()` - Positioning and grouping logic
- `suggest_instruments()` - Instrument selection for mission
- `build_panel_specification()` - Semantic bridge
- `generate_cockpit_prompt()` - Final image generation prompt

## Documentation

See `docs/DOCUMENTATION.md` for full API reference.
