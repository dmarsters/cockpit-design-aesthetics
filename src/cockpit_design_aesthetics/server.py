"""
Cockpit Design Aesthetics MCP Server

Translates cockpit instrument panel design principles into vivid visual language
for image generation. Uses three-layer architecture:

Layer 1: Deterministic taxonomy (YAML olog) - zero LLM cost
Layer 2: Semantic mapping - deterministic composition  
Layer 3: Claude synthesis - single LLM call for vivid prompts

Cost savings: ~60-80% compared to pure LLM approaches.
"""

from fastmcp import FastMCP
import yaml
from pathlib import Path
from typing import Optional

# Load YAML taxonomies on startup BEFORE creating server
OLOG_PATH = Path(__file__).parent / "ologs" / "instruments.yaml"

def load_olog():
    """Load YAML taxonomy."""
    with open(OLOG_PATH, 'r') as f:
        return yaml.safe_load(f)

TAXONOMY = load_olog()

# Initialize FastMCP server
mcp = FastMCP("cockpit-design-aesthetics")


# ============================================================================
# Layer 1: Pure Taxonomy Lookup - Zero LLM Cost
# ============================================================================
# Internal implementation functions (testable)

def get_aircraft_type_profile_impl(aircraft_type: str) -> dict:
    """Internal: Get instrument configuration profile for aircraft type."""
    aircraft_types = TAXONOMY.get('aircraft_types', {})
    normalized_type = aircraft_type.lower().replace(' ', '_').replace('-', '_')
    
    if normalized_type not in aircraft_types:
        return {
            "error": f"Aircraft type '{aircraft_type}' not found",
            "available_types": list(aircraft_types.keys())
        }
    
    profile = aircraft_types[normalized_type]
    return {
        "aircraft_type": normalized_type,
        "examples": profile.get('examples', []),
        "configuration": profile.get('instrument_configuration'),
        "complexity": profile.get('panel_complexity'),
        "essential_instruments": profile.get('typical_instruments', {}).get('essential', []),
        "engine_instruments": profile.get('typical_instruments', {}).get('engine', []),
        "system_instruments": profile.get('typical_instruments', {}).get('systems', []),
        "features": profile.get('features', [])
    }


def get_instrument_details_impl(instrument_name: str) -> dict:
    """Internal: Get complete specifications for a single instrument."""
    instruments = {}
    for category, insts in TAXONOMY.get('instruments', {}).items():
        instruments.update(insts)
    
    normalized_name = instrument_name.lower().replace(' ', '_').replace('-', '_')
    
    if normalized_name not in instruments:
        return {
            "error": f"Instrument '{instrument_name}' not found",
            "available": list(instruments.keys())
        }
    
    inst = instruments[normalized_name]
    return {
        "name": inst.get('name'),
        "aliases": inst.get('aliases', []),
        "function": inst.get('function'),
        "visual_elements": inst.get('visual_elements', []),
        "color_scheme": inst.get('color_scheme', {}),
        "position": inst.get('typical_position'),
        "criticality": inst.get('criticality'),
        "warning_zones": inst.get('warning_zones', {}),
        "speed_arcs": inst.get('speed_arcs', {})
    }


def get_panel_layout_rules_impl() -> dict:
    """Internal: Get spatial positioning rules for instrument panels."""
    positioning = TAXONOMY.get('positioning', {})
    
    return {
        "primary_scan_area": positioning.get('primary_scan_area'),
        "engine_cluster": positioning.get('engine_cluster'),
        "navigation_cluster": positioning.get('navigation_cluster'),
        "systems_cluster": positioning.get('systems_cluster'),
        "design_principles": {
            "primary_scan": "T-shaped arrangement with attitude indicator as anchor",
            "eye_movement": "Minimize eye travel between critical instruments",
            "grouping": "Related functions cluster together",
            "scanning": "Layout supports natural pilot scan patterns"
        }
    }


def get_color_standards_impl() -> dict:
    """Internal: Get standard cockpit color conventions."""
    return TAXONOMY.get('color_standards', {})


def get_era_profile_impl(era: str) -> dict:
    """Internal: Get visual characteristics for a specific era of cockpit design."""
    eras = TAXONOMY.get('eras', {})
    normalized_era = era.lower().replace(' ', '_').replace('-', '_')
    
    if normalized_era not in eras:
        return {
            "error": f"Era '{era}' not found",
            "available_eras": list(eras.keys())
        }
    
    era_data = eras[normalized_era]
    return {
        "era": normalized_era,
        "period": era_data.get('period'),
        "description": era_data.get('description'),
        "visual_characteristics": era_data.get('visual_characteristics', []),
        "materials": era_data.get('materials', []),
        "advantages": era_data.get('advantages', [])
    }


def list_available_options_impl() -> dict:
    """Internal: Get all available options across all dimensions."""
    instruments = {}
    for category, insts in TAXONOMY.get('instruments', {}).items():
        instruments.update(insts)
    
    return {
        "aircraft_types": list(TAXONOMY.get('aircraft_types', {}).keys()),
        "instruments": list(instruments.keys()),
        "eras": list(TAXONOMY.get('eras', {}).keys()),
        "scan_patterns": list(TAXONOMY.get('scan_patterns', {}).keys()),
        "positioning_zones": list(TAXONOMY.get('positioning', {}).keys()),
        "instrument_categories": list(TAXONOMY.get('instruments', {}).keys())
    }


# ============================================================================
# Layer 2: Semantic Mapping - Deterministic Composition
# ============================================================================

def suggest_instruments_impl(
    aircraft_type: str,
    mission_profile: Optional[str] = None,
    complexity_level: Optional[str] = None
) -> dict:
    """Internal: Suggest instruments for a given aircraft type and mission."""
    aircraft_profile = get_aircraft_type_profile_impl(aircraft_type)
    if "error" in aircraft_profile:
        return aircraft_profile
    
    additions = {}
    if mission_profile == 'ifr_cross_country':
        additions['nav_instruments'] = ['vor_indicator', 'adf_indicator', 'dme']
        additions['redundancy'] = True
    elif mission_profile == 'vfr_training':
        additions['nav_instruments'] = []
        additions['simplified'] = True
    
    return {
        "aircraft_type": aircraft_type,
        "mission": mission_profile or "general",
        "instruments": {
            "critical": aircraft_profile.get('essential_instruments', []),
            "engine": aircraft_profile.get('engine_instruments', []),
            "systems": aircraft_profile.get('system_instruments', []),
            "navigation": additions.get('nav_instruments', [])
        },
        "layout_style": aircraft_profile.get('configuration'),
        "panel_complexity": complexity_level or aircraft_profile.get('complexity'),
        "scan_pattern_recommendation": "instrument_flight" if mission_profile == 'ifr_cross_country' else "vfr_cruise"
    }


def build_panel_specification_impl(
    aircraft_type: str,
    panel_era: str,
    focus_area: Optional[str] = None,
    detail_level: str = "medium"
) -> dict:
    """Internal: Build complete semantic bridge for cockpit panel design."""
    aircraft = get_aircraft_type_profile_impl(aircraft_type)
    era = get_era_profile_impl(panel_era)
    positioning = get_panel_layout_rules_impl()
    colors = get_color_standards_impl()
    
    if "error" in aircraft or "error" in era:
        return {"error": "Invalid aircraft type or era"}
    
    spec = {
        "aircraft_type": aircraft_type,
        "era": panel_era,
        "focus_area": focus_area or "full_panel",
        "instruments": aircraft.get('essential_instruments', []),
        "layout": positioning.get('primary_scan_area', {}),
        "era_characteristics": era.get('visual_characteristics', []),
        "materials": era.get('materials', []),
        "color_palette": colors,
        "layout_logic": {
            "primary_scan_t_shape": True,
            "attitude_indicator_centered": True,
            "altitude_right_of_attitude": True,
            "airspeed_left_of_attitude": True
        }
    }
    
    if detail_level == 'comprehensive':
        spec['scan_patterns'] = TAXONOMY.get('scan_patterns', {}).get('instrument_flight', {})
    
    return spec


# ============================================================================
# Layer 3: Claude Synthesis - Image Generation
# ============================================================================

def generate_cockpit_prompt_impl(
    aircraft_type: str,
    panel_era: str,
    viewing_angle: str = "front_center",
    lighting_condition: str = "daytime",
    detail_intensity: str = "realistic",
    additional_context: Optional[str] = None
) -> dict:
    """Internal: Generate vivid image generation prompt for a cockpit."""
    spec = build_panel_specification_impl(aircraft_type, panel_era, "full_panel", "comprehensive")
    if "error" in spec:
        return spec
    
    instruments_detail = []
    for inst_name in spec.get('instruments', [])[:4]:
        inst = get_instrument_details_impl(inst_name)
        if "error" not in inst:
            instruments_detail.append(inst)
    
    angle_descriptions = {
        "front_center": "straight-on view centered on the instrument panel",
        "pilot_view": "from pilot seat perspective, slightly off-center",
        "oblique": "45-degree angle showing left side instruments",
        "overhead": "birds-eye view of full panel layout"
    }
    
    lighting_descriptions = {
        "daytime": "natural daylight streaming through windscreen",
        "instrument_lit": "instruments glowing with internal panel lighting",
        "twilight": "soft ambient light with instrument glow becoming prominent",
        "night": "complete darkness except for instrument backlighting and external lights"
    }
    
    context = {
        "subject": f"{aircraft_type.replace('_', ' ')} cockpit instrument panel",
        "era_characteristics": spec.get('era_characteristics', []),
        "materials": spec.get('materials', []),
        "viewing_angle": angle_descriptions.get(viewing_angle, viewing_angle),
        "lighting": lighting_descriptions.get(lighting_condition, lighting_condition),
        "key_instruments": instruments_detail,
        "color_conventions": {
            "warnings": "red lines and indicators for critical limits",
            "normal": "green arcs for normal operating ranges",
            "cautions": "yellow bands for caution zones",
            "neutral": "white backgrounds with black text and scales"
        },
        "design_principles": [
            "Attitude indicator prominently centered",
            "Altitude and airspeed flanking attitude indicator",
            "Organized layout minimizing pilot eye movement",
            "Color-coded zones for immediate comprehension",
            f"{panel_era.replace('_', ' ')} aesthetic with authentic details"
        ]
    }
    
    if additional_context:
        context['additional_context'] = additional_context
    
    return {
        "prompt_context": context,
        "synthesis_guidance": {
            "tone": "technical and precise yet visually striking",
            "detail_level": detail_intensity,
            "focus": "instrument panel authenticity and visual hierarchy",
            "avoid": "overly stylized or inaccurate instrument designs"
        },
        "ready_for_image_generation": True,
        "recommended_next_step": "Pass this context to Claude to synthesize final vivid prompt"
    }


def explain_cockpit_design_impl(aspect: str) -> dict:
    """Internal: Educational tool explaining cockpit design principles."""
    explanations = {
        "scanning_logic": {
            "principle": "The 'Basic T' scan pattern",
            "description": "Pilots scan instruments in a T-shaped pattern: attitude indicator at center, with altitude/airspeed on sides, heading/VSI below",
            "why": "Minimizes eye movement and keeps critical flight information in primary scan area",
            "instruments": ["attitude_indicator", "airspeed_indicator", "altimeter", "heading_indicator", "vertical_speed_indicator"]
        },
        "color_conventions": {
            "principle": "Immediate visual comprehension",
            "description": "Red = critical/warning, Yellow = caution, Green = normal, White = neutral data",
            "why": "Pilots can interpret instrument status at a glance without reading exact numbers during high-workload situations",
            "speed_arcs_example": "Airspeed indicator has white, green, yellow, and red arcs showing flap limits, normal range, caution, and never-exceed"
        },
        "positioning_rationale": {
            "principle": "Functional grouping with proximity priority",
            "description": "Primary flight instruments cluster in center; engine instruments below/right; systems and nav instruments in periphery",
            "why": "Frequent-use instruments are central, reducing scan distance. Related functions grouped reduces context-switching",
            "scan_pattern_supported": "T-shaped scan minimizes eye fatigue and mental load"
        },
        "instrument_redundancy": {
            "principle": "Safety through multiple independent sources",
            "description": "Attitude, altitude, and airspeed each displayed through multiple instruments",
            "examples": [
                "Attitude from both attitude indicator and turn coordinator",
                "Altitude from altimeter and VSI trend",
                "Heading from compass and heading indicator"
            ],
            "why": "If one instrument fails, pilot can cross-check with others and maintain situational awareness"
        }
    }
    
    if aspect in explanations:
        return {
            "aspect": aspect,
            "explanation": explanations[aspect]
        }
    else:
        return {
            "error": f"Unknown aspect '{aspect}'",
            "available_aspects": list(explanations.keys())
        }


# ============================================================================
# FastMCP Tool Decorators
# ============================================================================

@mcp.tool()
def get_aircraft_type_profile(aircraft_type: str) -> dict:
    """Get instrument configuration profile for aircraft type."""
    return get_aircraft_type_profile_impl(aircraft_type)


@mcp.tool()
def get_instrument_details(instrument_name: str) -> dict:
    """Get complete specifications for a single instrument."""
    return get_instrument_details_impl(instrument_name)


@mcp.tool()
def get_panel_layout_rules() -> dict:
    """Get spatial positioning rules for instrument panels."""
    return get_panel_layout_rules_impl()


@mcp.tool()
def get_color_standards() -> dict:
    """Get standard cockpit color conventions."""
    return get_color_standards_impl()


@mcp.tool()
def get_era_profile(era: str) -> dict:
    """Get visual characteristics for a specific era of cockpit design."""
    return get_era_profile_impl(era)


@mcp.tool()
def list_available_options() -> dict:
    """Get all available options across all dimensions."""
    return list_available_options_impl()


@mcp.tool()
def suggest_instruments(
    aircraft_type: str,
    mission_profile: Optional[str] = None,
    complexity_level: Optional[str] = None
) -> dict:
    """Suggest instruments for a given aircraft type and mission."""
    return suggest_instruments_impl(aircraft_type, mission_profile, complexity_level)


@mcp.tool()
def build_panel_specification(
    aircraft_type: str,
    panel_era: str,
    focus_area: Optional[str] = None,
    detail_level: str = "medium"
) -> dict:
    """Build complete semantic bridge for cockpit panel design."""
    return build_panel_specification_impl(aircraft_type, panel_era, focus_area, detail_level)


@mcp.tool()
def generate_cockpit_prompt(
    aircraft_type: str,
    panel_era: str,
    viewing_angle: str = "front_center",
    lighting_condition: str = "daytime",
    detail_intensity: str = "realistic",
    additional_context: Optional[str] = None
) -> dict:
    """Generate vivid image generation prompt for a cockpit."""
    return generate_cockpit_prompt_impl(
        aircraft_type, panel_era, viewing_angle, 
        lighting_condition, detail_intensity, additional_context
    )


@mcp.tool()
def explain_cockpit_design(aspect: str) -> dict:
    """Educational tool: Explain cockpit design principles."""
    return explain_cockpit_design_impl(aspect)


if __name__ == "__main__":
    mcp.run()
