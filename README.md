# Cockpit Design Aesthetics MCP

A deterministic visual vocabulary server that maps aircraft cockpit design principles to locked aesthetic parameters for image generation. Part of the Lushy.app Visual Vocabularies ecosystem.

## What This Does

Aircraft cockpit design is a highly specialized visual language shaped by human factors engineering, avionics technology, mission requirements, and historical eras. This MCP translates cockpit design principles and aircraft type specifications into locked parameters for reproducible, era-authentic, mission-appropriate cockpit visualization.

Specify an aircraft type, design era, and optional focus area. Get consistent instrumentation layouts, panel color schemes, lighting approaches, functional organization, visual hierarchy, and authentic technical aesthetics that stay locked across every generation.

Cockpit visualizations that respect human factors engineering while remaining visually coherent.

No drift. Functionally authentic aesthetics.

## Quick Start

### Installation

```bash
git clone https://github.com/dmarsters/cockpit-design-aesthetics-mcp.git
cd cockpit-design-aesthetics-mcp
pip install -r requirements.txt
```

### Usage with Claude

Add to your Claude client configuration:

```json
{
  "mcpServers": {
    "cockpit-design": {
      "command": "python",
      "args": ["cockpit_design_mcp.py"]
    }
  }
}
```

Then use Claude to enhance prompts:

```
Generate a cockpit visualization:
Aircraft type: Boeing 747
Design era: 1980s
Panel era: classic_analog
Detail level: medium
Viewing angle: front_center
Lighting condition: daylight
Additional context: Commercial airliner cruising altitude
```

Claude will layer cockpit design parameters onto your prompt, locking in the wide panel organization of a large commercial aircraft, 1980s analog instrumentation aesthetic, appropriate color standards (dark panels with bright displays), functional grouping of instruments, proper panel layout hierarchy, and authentic 1980s cockpit lighting.

## Aircraft Types

Cockpit design varies significantly by aircraft category and size:

### Commercial Aircraft

**Large Wide-Body** (Boeing 747, Airbus A380)
- Widest panel span
- Multiple flight engineer stations (vintage)
- Dual-redundant systems emphasized
- Extensive overhead panel for systems management
- Largest instrument cluster

**Medium Wide-Body** (Boeing 777, Airbus A350)
- Balanced panel width
- Integrated systems management
- Glass cockpit typical
- Sophisticated avionics integration
- Modern ergonomics

**Narrow-Body** (Boeing 737, Airbus A320)
- Compact, efficient panel design
- High-density instrumentation
- Space optimization emphasized
- Most common commercial cockpit size
- Standardized layouts across variants

**Regional Aircraft** (Bombardier CRJ, Embraer E-Jet)
- Smaller panel footprint
- Simplified systems compared to large aircraft
- Cost-effective instrumentation
- Efficient crew workload management
- Growing modernization with glass cockpits

### Military Aircraft

**Fighter/Combat** (F-16, F-18, Gripen)
- Compact, high-density layout
- Sidestick controllers (modern)
- Helmet-mounted displays integrated
- Combat-specific instrumentation
- High g-load considerations in design

**Transport/Cargo** (C-130 Hercules, C-17 Globemaster)
- Functional, utilitarian design
- Emphasis on visibility and control
- Redundant systems for reliability
- Robust instrumentation
- Crew comfort over luxury

**Bomber** (B-52, B-1, B-2)
- Specialized navigation and weapons systems
- Extensive target and threat displays
- Integrated electronic warfare displays
- Specialized crew stations
- Mission-specific instrumentation

**Helicopter**
- Centered collective and cyclic controls
- Different spatial organization than fixed-wing
- High-visibility requirements
- Compact vertical space utilization
- Unique panel arrangement

### General Aviation

**Single-Engine Piston** (Cessna 172, Piper Cherokee)
- Minimal panel, essential instruments only
- Simple, learn-able layout
- Basic avionics even in modern versions
- Student-friendly ergonomics
- Cost-optimized instrumentation

**Multi-Engine Piston** (Piper Seneca, Beechcraft Baron)
- Expanded panel for dual-engine management
- More complex systems than single-engine
- Advanced avionics options available
- Higher performance instruments
- Pilot-owner market expectations

**Turboprop** (Beechcraft King Air, Pilatus PC-12)
- Professional-grade instrumentation
- Advanced avionics common
- Pressurization system instrumentation
- Higher-altitude capability displays
- Business aviation standards

**Business Jet** (Learjet, Citation, Gulfstream)
- Luxury cockpit design emphasis
- Sophisticated glass cockpit standard
- Advanced flight management systems
- Ergonomic comfort prioritized
- Cutting-edge avionics integration

## Design Eras

Cockpit design has distinct aesthetic periods shaped by technology and philosophy:

### Era 1: Mechanical Steam Gauges (1930s-1960s)
- Analog instruments dominate
- Round dial displays standard
- Mechanical autopilot systems
- Manual flight control emphasis
- Visible mechanical complexity
- Dense analog instrument panels

**Visual characteristics:**
- Dials, needles, indicators
- Beige and light colors typical
- Mechanical switch-heavy
- High instrument density
- Manual control dominant

### Era 2: Early Glass Cockpit Transition (1970s-1980s)
- Electronic instruments beginning
- Hybrid analog and CRT displays
- First flight management systems
- Navigation system integration
- Still substantial mechanical backups
- Increasing complexity

**Visual characteristics:**
- CRT green monochrome screens
- Analog dials still prominent
- Dark panels with bright displays
- Increasing switch density
- Transitional aesthetic

### Era 3: Mature Glass Cockpit (1990s-2000s)
- Full digital flight management systems
- Multi-function displays standard
- Integrated navigation systems
- Advanced autopilot capabilities
- Reduced mechanical backups
- Systems integration emphasized

**Visual characteristics:**
- Color LCD displays
- Streamlined panel organization
- Dark panels for display contrast
- Integrated system indication
- Modern ergonomic layouts

### Era 4: Modern Integrated Avionics (2010s-present)
- Advanced avionics integration
- Touchscreen interfaces emerging
- Fully redundant digital systems
- Synthetic vision systems
- Integrated weather and terrain
- Crew alerting systems sophisticated

**Visual characteristics:**
- High-resolution color displays
- Minimalist panel design
- Integrated information display
- Modern aesthetic
- User experience design evident

## Instrumentation Categories

Cockpit instruments organized by function:

### Flight Instruments (Primary Flight Display)
- Attitude indicator (artificial horizon)
- Airspeed indicator
- Altimeter
- Vertical speed indicator
- Heading indicator
- Turn coordinator

### Navigation Systems
- Navigation display (moving map)
- VOR/ILS indicators (classical) or integrated (modern)
- GPS/FMS integration
- Navigation guidance displays
- Precision approach displays

### Engine Instruments (Engine Indicating and Crew Alerting System)
- Engine temperature gauges
- Engine pressure gauges
- Fuel quantity indicators
- Electrical system indication
- Hydraulic system status
- Environmental control status

### Autopilot and Flight Control
- Mode annunciators
- Altitude pre-selector
- Heading selector
- Autopilot engagement switches
- Flight director indicators
- Flight control status displays

### Communication Systems
- VHF radio displays
- HF radio (military/long-haul)
- Intercom systems
- Audio selector panels
- Radio frequency indicators

### Systems Management
- Electrical system displays
- Hydraulic system indication
- Fuel system management
- Environmental control panels
- Anti-ice/de-ice systems
- Pressurization indicators

## Architecture

Three-layer design: aircraft specifications, design-era principles, and layout organization.

### Layer 1: Aircraft Type Olog

Categories defining cockpit design space:

**Aircraft Category**: commercial_widebody, commercial_narrowbody, commercial_regional, military_fighter, military_transport, military_bomber, helicopter, general_single, general_multi, general_turboprop, business_jet

**Cockpit Size**: extra_large, large, medium, compact, minimal

**Crew Size**: single_pilot, two_pilot, four_plus_crew

**Primary Systems**: mechanical, hybrid_analog_digital, glass_cockpit, modern_integrated

**Control Type**: yoke, sidestick, control_stick, collective_cyclic

**Panel Organization**: traditional_horizontal, modern_streamlined, specialized_military, helicopter_vertical

### Layer 2: Design Era Morphisms

Deterministic mapping from era to visual parameters:

- `era_to_instrumentation_style()` — Era → analog/digital/hybrid approach
- `era_to_display_technology()` — Era → CRT/LCD/mechanical displays
- `era_to_color_scheme()` — Era → panel and text colors
- `era_to_control_philosophy()` — Era → automation level reflected in design
- `aircraft_to_panel_layout()` — Aircraft type → panel organization
- `build_cockpit_specification()` — Master morphism orchestrating all factors

### Layer 3: MCP Interface

Claude-facing tools for cockpit visualization:

- `list_available_options()` — All aircraft, eras, styles available
- `get_aircraft_type_profile()` — Complete specifications for aircraft
- `get_era_profile()` — Visual characteristics of design era
- `get_instrument_details()` — Technical specs for specific instruments
- `get_panel_layout_rules()` — How instruments should be organized
- `get_color_standards()` — Official cockpit color standards
- `suggest_instruments()` — Recommended instruments for aircraft type
- `build_panel_specification()` — Complete cockpit specification
- `generate_cockpit_prompt()` — Full image generation prompt

## How Cockpit Design Aesthetics Works

### The Problem It Solves

Cockpit design is highly specialized with specific human factors requirements, technical standards, and historical evolution. Asking for "a realistic cockpit" produces inconsistent results:

- Generation 1: Looks like a 1960s cockpit with modern electronics
- Generation 2: Instruments are organized illogically
- Generation 3: Panel colors and lighting don't match era
- Generation 4: Lost sense of coherent design

Without locked parameters, cockpit visualizations fail to respect the real constraints that shape cockpit design.

### The Solution: Locked Aircraft-Era-Layout Parameters

Cockpit design vocabulary locks specific parameter combinations:

```
Boeing 747, 1980s, Classic Analog Era:
  aircraft_category: large_widebody
  cockpit_size: extra_large
  era: early_glass_cockpit_transition
  instrumentation_style: hybrid_analog_crt
  display_technology: crt_green_monochrome + analog_dials
  color_scheme: light_beige_panels + dark_CRT_screens
  panel_layout: traditional_horizontal_with_overhead
  control_philosophy: manual_with_early_automation
  lighting: overhead_fluorescent + instrument_backlighting
  primary_focus: flight_instruments_center + engine_instruments_left
  visual_hierarchy: instrument_density_high + functional_organization_clear
```

Every generation with this specification produces a cockpit that feels authentically 1980s Boeing 747: CRT displays with green text, hybrid analog and digital systems, proper panel organization, historically accurate instrumentation, appropriate crew workload indication.

### Functional Authenticity

These aren't arbitrary aesthetic choices. They reflect real human factors engineering:

- Panel layout follows crew scanning patterns
- Instrument color standards improve readability
- System organization matches workflow and emergency procedures
- Era-appropriate technology reflects actual historical cockpits
- Crew station relationships reflect real coordination needs

The vocabulary makes functional requirements visible in aesthetic form.

### Cost Efficiency

Traditional approach: Describe aircraft, era, and desired features to LLM for synthesis (expensive)

This approach:
1. Aircraft specification lookup (zero tokens) — deterministic mapping
2. Era principle lookup (zero tokens) — design history reference
3. Layout organization (zero tokens) — human factors rules
4. Single LLM call — creative synthesis of base prompt + locked parameters

Result: ~60% token savings vs. pure LLM enhancement.

## Usage Patterns

### Pattern 1: Aircraft + Era Specification

Simple approach: specify aircraft and era, get complete cockpit design:

```python
build_panel_specification(
    aircraft_type="Boeing 747",
    panel_era="classic_analog_1980s",
    detail_level="medium"
)
```

Returns: Complete cockpit specification with all parameters locked.

### Pattern 2: Detailed Customization

Specify aircraft, era, and focus area:

```python
build_panel_specification(
    aircraft_type="Airbus A320",
    panel_era="modern_integrated_2010s",
    detail_level="high",
    focus_area="flight_deck_overview"
)
```

Returns: High-detail specification focused on flight deck perspective.

### Pattern 3: Instrument Inspection

Understand what specific instruments appear in a cockpit:

```python
suggest_instruments(
    aircraft_type="Cessna 172",
    complexity_level="basic"
)
```

Returns: List of instruments appropriate for this aircraft, with technical details.

### Pattern 4: Visual Generation

Generate complete image prompt from specification:

```python
generate_cockpit_prompt(
    aircraft_type="F-16 Falcon",
    panel_era="modern_fighter",
    viewing_angle="front_center",
    lighting_condition="night",
    detail_intensity="realistic"
)
```

Returns: Detailed, authentic image generation prompt ready for visualization.

## Color Standards

Cockpit color standards define how different elements appear:

### Panel Colors
- **Light Beige/Cream** (mechanical era) — Traditional, instrument background
- **Dark Gray** (early digital) — Reduces glare from CRT displays
- **Black** (modern digital) — Maximizes contrast with LCD displays
- **Light Gray** (some specialist areas) — For specific system panels

### Text and Display Colors
- **Green** (CRT monochrome) — Historical, reduces eye strain on green screens
- **White** (digital era) — Standard for LCD displays
- **Amber/Yellow** (warning/caution) — Safety indication
- **Red** (emergency) — Critical alerts
- **Blue** (information) — Informational displays in modern glass cockpits

### Lighting
- **Overhead Fluorescent** (bright operations) — White light
- **Instrument Backlighting** (general operations) — White or green
- **Red Backlighting** (night operations) — Preserves night vision
- **Accent Lighting** (modern) — Task-specific illumination

## Cockpit Layout Principles

How instruments are organized reflects human factors engineering:

### Primary Flight Display Position
- Typically center and directly in line of sight
- Pilot and copilot mirrors (dual cockpits)
- Glance-distance optimized

### Engine Instruments Grouping
- Pilot's side (primary responsibility)
- Vertical organization from left to right: N1, EGT, N2
- Emergency procedures organized by scanning pattern

### Navigation Display Positioning
- Right side of primary flight display typically
- Strategic for navigation tasks
- Integrated with flight management systems

### System Management Organization
- Overhead panels for systems not requiring constant monitoring
- Logical grouping by system type
- Emergency procedures organized for quick access

### Control Placement
- Primary controls (yoke/sidestick) in natural reach
- Throttles in standard position
- Landing gear and flap controls in logical sequence
- Emergency controls accessible and distinct

## Lighting Scenarios

Cockpit lighting changes based on operational phase:

**Daylight Operations**
- Overhead fluorescent lights on
- Instrument panel display brightness balanced
- Glare reduction important
- Full visibility of panel details

**Dusk/Twilight**
- Transitional lighting
- Gradual instrument backlighting increase
- Display brightness adjustment
- Mixed natural and artificial light

**Night Operations**
- Red backlighting standard (night vision preservation)
- Display brightness carefully set
- External lights navigation aids
- High contrast maintained for readability

**Approach/Landing**
- Specific lighting profile for precision tasks
- Reduced ambient light to focus attention
- Landing light and approach light integration
- Critical information highlighted

## Customization and Extension

Cockpit design specifications are based on real aircraft and design principles. You can modify or extend them:

### Add a New Aircraft

Specify aircraft profile:

```python
AIRCRAFT_PROFILES = {
    "airbus_a400m": {
        "name": "Airbus A400M",
        "category": "military_transport",
        "crew_size": 2,
        "cockpit_size": "large",
        "primary_systems": "modern_integrated",
        "control_type": "yoke",
        "panel_organization": "modern_streamlined",
        "typical_era": "2010s"
    }
}
```

### Modify Era Characteristics

Change how a design era appears:

```python
ERA_PROFILES = {
    "classic_analog_1960s": {
        "instrumentation": "mechanical_pneumatic",
        "display_tech": "round_dials_only",
        "color_scheme": "light_beige",
        "automation_level": "minimal",
        "lighting": "incandescent_backlit"
    }
}
```

### Create Custom Specification

Build bespoke cockpit specification:

```python
def custom_cockpit_spec(aircraft, era, custom_params):
    # Your custom mapping logic
    return complete_specification
```

## Example Use Cases

### Use Case 1: Historical Cockpit Recreation

```
Aircraft: Douglas DC-3
Era: mechanical_1930s_40s
Viewing angle: front_center
Detail level: medium

↓ Creates:
1930s-40s mechanical cockpit:
- Round dial instruments dominating
- Manual flight controls prominent
- Mechanical autopilot (if equipped)
- Simple electrical systems
- Beige panel with black dials
- Dual crew stations clearly defined
- No electronic navigation displays
- Visual flying emphasis

Result: Authentic 1930s-40s transport aircraft cockpit
```

### Use Case 2: Commercial Modern Glass Cockpit

```
Aircraft: Boeing 787 Dreamliner
Era: modern_integrated_2010s_20s
Viewing angle: front_center
Lighting: daylight
Detail level: high

↓ Creates:
Modern glass cockpit:
- Large color LCD displays
- Fully integrated flight management system
- Advanced autopilot with mode annunciators
- Integrated navigation and weather
- Dark panels for display contrast
- Streamlined control layout
- Minimal mechanical backups visible
- Crew alerting system integrated
- Head-up display visible

Result: Authentic modern commercial cockpit
```

### Use Case 3: Fighter Cockpit

```
Aircraft: F-16 Falcon
Era: modern_fighter_current
Viewing angle: overhead_view
Detail level: high
Focus area: ejection_seat_perspective

↓ Creates:
Modern fighter cockpit:
- Sidestick control prominent
- Head-up display integration
- Multi-function display buttons surrounding field
- Helmet-mounted display consideration visible
- Compact, high-density instrument layout
- Military-specific avionics
- Ejection seat prominent in perspective
- Combat-focused instrumentation

Result: Authentic modern fighter cockpit perspective
```

### Use Case 4: Vintage Civil Aviation

```
Aircraft: Cessna 172 (1970s variant)
Era: early_glass_transition_1970s
Viewing angle: front_center
Detail level: medium

↓ Creates:
1970s general aviation cockpit:
- Basic VOR/ILS instruments
- Mechanical turn coordinator
- Simple autopilot indication
- Essential engine instruments
- Yoke controls prominent
- White instruments on light background
- Functional minimalism
- Student pilot focus evident

Result: Authentic 1970s general aviation cockpit
```

## Composition with Other Vocabularies

Cockpit design can layer with other visual vocabulary MCP servers, though carefully:

```
Base: "A pilot at the controls during an emergency"
+ Cockpit Design (Boeing 747, 1980s): authentic instrument layout, period aesthetics
+ Slapstick Enhancer (strong): exaggerated crew reaction, physical comedy
= Comedic interpretation of crisis cockpit situation
```

Cockpit aesthetics work well with:
- Technical and educational contexts
- Historical documentation
- Engineering visualization
- Technical writing and manuals

Cockpit aesthetics may conflict with:
- Highly stylized or surreal aesthetics (cockpits are functional)
- Extreme abstraction (instruments must remain recognizable)
- Minimal or reductive approaches (cockpits are complex)

Composition with cockpit design should respect functional requirements. These aren't arbitrary aesthetics; they're shaped by safety and human factors engineering.

## Technical Details and Standards

Cockpit design references real human factors and aviation standards:

### Human Factors Principles

- **Scanning pattern optimization** — Instruments positioned for crew visual scan patterns
- **Workload distribution** — Systems organized by pilot responsibility
- **Emergency access** — Critical controls accessible under stress
- **Fatigue consideration** — Lighting and ergonomics support long flights
- **Automation integration** — Crew maintains situational awareness with advanced systems

### Aviation Standards

- **FAA Certification Requirements** (commercial US aircraft)
- **EASA Certification Requirements** (European aircraft)
- **Military Specifications** (military aircraft)
- **Human Factors Standards** (ergonomic requirements)
- **Color and Symbol Standards** (readable, consistent)

These standards make cockpit design functionally coherent, not arbitrary.

## Limitations and Intentionality

Cockpit design vocabularies are based on real, functional requirements:

### What They Do Well

- Create authentic cockpit designs respecting real constraints
- Communicate technical complexity visually
- Support educational and technical contexts
- Preserve historical design evolution
- Connect aesthetic choices to human factors principles

### What They Don't Do

- Substitute for actual engineering documentation
- Provide complete functional specifications
- Detail all system redundancies and backups
- Explain operational procedures
- Provide training-grade accuracy

### Important Considerations

- Cockpit design reflects safety-critical decisions
- Functionality is not optional; it shapes aesthetics
- Historical accuracy matters for education and authenticity
- Aircraft design is regulated and standardized for good reasons
- Respect these constraints; don't treat them as arbitrary

## Implementation Details

### Dependencies

- Python 3.8+
- fastmcp (for MCP server)
- No external API calls
- All operations deterministic and local

### File Structure

```
cockpit-design-aesthetics-mcp/
├── cockpit_design_mcp.py           # MCP interface and tools
├── aircraft_profiles.py             # Aircraft type definitions
├── era_specifications.py            # Design era characteristics
├── layout_principles.py             # Panel organization rules
├── instrumentation_catalog.py       # Instrument specifications
├── color_standards.py               # Cockpit color conventions
├── requirements.txt                 # Dependencies
└── README.md                         # This file
```

### Performance

- Cold start: ~100ms (profile loading)
- Aircraft lookup: <5ms (specification retrieval)
- Era selection: <3ms (design era reference)
- Layout organization: <10ms (panel arrangement)
- Per-query: <20ms (complete specification assembly)
- Token cost: Single LLM call for prompt synthesis

## Educational Value

This vocabulary is useful for:

- **Aviation Education** — Understanding cockpit design principles
- **Engineering Education** — Human factors and design constraints
- **History of Technology** — Evolution of cockpit design across eras
- **Technical Illustration** — Accurate cockpit visualization
- **Aviation Art and Media** — Authentic-looking cockpit scenes

## Contributing

Cockpit design specifications are based on real aircraft and principles. If you extend:

1. Document your aircraft specifications (real aircraft data preferred)
2. Reference human factors principles underlying your choices
3. Test coherence across different viewing angles and lighting conditions
4. Consider historical accuracy for vintage aircraft
5. Share your work with technical context

## References and Further Learning

Cockpit design derives from:

- Aviation human factors engineering
- Aircraft design and certification standards
- Cockpit illustration and technical documentation
- Aviation history
- Ergonomics and human-machine interaction

**Technical References:**
- FAA Type Certificate Data Sheets (specifications)
- EASA Certification Specifications
- Cockpit design case studies in aviation publications
- Human factors research in aviation

## License

MIT

## Related

Part of the Lushy.app Visual Vocabularies ecosystem:


See the visual vocabularies intro post for context on how these systems work together.

## Questions?

Open an issue or reach out. This is an active project exploring how technical design constraints become aesthetic choices, and how to authentically represent specialized visual domains shaped by human factors engineering and functional requirements.

## Author
Dal Marsters - Lushy.app
