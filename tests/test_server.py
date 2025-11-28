"""
Tests for Cockpit Design Aesthetics MCP Server

Tests Layer 1 (deterministic taxonomy), Layer 2 (mapping), and Layer 3 (synthesis).
"""

import pytest
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from cockpit_design_aesthetics.server import (
    get_aircraft_type_profile_impl,
    get_instrument_details_impl,
    get_panel_layout_rules_impl,
    get_color_standards_impl,
    get_era_profile_impl,
    list_available_options_impl,
    suggest_instruments_impl,
    build_panel_specification_impl,
    generate_cockpit_prompt_impl,
    explain_cockpit_design_impl,
    TAXONOMY
)

# Aliases for convenience in tests
get_aircraft_type_profile = get_aircraft_type_profile_impl
get_instrument_details = get_instrument_details_impl
get_panel_layout_rules = get_panel_layout_rules_impl
get_color_standards = get_color_standards_impl
get_era_profile = get_era_profile_impl
list_available_options = list_available_options_impl
suggest_instruments = suggest_instruments_impl
build_panel_specification = build_panel_specification_impl
generate_cockpit_prompt = generate_cockpit_prompt_impl
explain_cockpit_design = explain_cockpit_design_impl


# ============================================================================
# Layer 1: Taxonomy Lookup Tests
# ============================================================================

def test_taxonomy_loads():
    """Verify YAML taxonomy loads correctly."""
    assert TAXONOMY is not None
    assert 'instruments' in TAXONOMY
    assert 'aircraft_types' in TAXONOMY
    assert 'eras' in TAXONOMY
    assert 'positioning' in TAXONOMY
    assert 'color_standards' in TAXONOMY


def test_aircraft_type_profile_valid():
    """Test getting profile for valid aircraft type."""
    result = get_aircraft_type_profile('general_aviation_singles')
    assert result is not None
    assert 'aircraft_type' in result
    assert result['aircraft_type'] == 'general_aviation_singles'
    assert 'complexity' in result
    assert 'essential_instruments' in result


def test_aircraft_type_profile_invalid():
    """Test error handling for invalid aircraft type."""
    result = get_aircraft_type_profile('nonexistent_aircraft')
    assert 'error' in result
    assert 'available_types' in result


def test_instrument_details_attitude_indicator():
    """Test getting details for attitude indicator."""
    result = get_instrument_details('attitude_indicator')
    assert 'name' in result
    assert result['name'] == 'Attitude Indicator (Artificial Horizon)'
    assert 'function' in result
    assert 'visual_elements' in result
    assert 'color_scheme' in result


def test_instrument_details_invalid():
    """Test error handling for invalid instrument."""
    result = get_instrument_details('nonexistent_instrument')
    assert 'error' in result
    assert 'available' in result


def test_panel_layout_rules():
    """Test getting layout positioning rules."""
    result = get_panel_layout_rules()
    assert 'primary_scan_area' in result
    assert 'engine_cluster' in result
    assert 'navigation_cluster' in result
    assert 'systems_cluster' in result
    assert 'design_principles' in result


def test_color_standards():
    """Test getting color standards."""
    result = get_color_standards()
    assert 'warning' in result
    assert result['warning']['color'] == '#FF0000'
    assert 'caution' in result
    assert result['caution']['color'] == '#FFFF00'
    assert 'safe_normal' in result
    assert result['safe_normal']['color'] == '#00AA00'


def test_era_profile_analog():
    """Test getting era profile for analog mechanical."""
    result = get_era_profile('analog_mechanical')
    assert 'era' in result
    assert 'period' in result
    assert 'visual_characteristics' in result
    assert 'materials' in result


def test_era_profile_glass_cockpit():
    """Test getting era profile for glass cockpit."""
    result = get_era_profile('glass_cockpit')
    assert result['era'] == 'glass_cockpit'
    assert 'Liquid crystal displays' in result['visual_characteristics'][0]


def test_era_profile_invalid():
    """Test error handling for invalid era."""
    result = get_era_profile('nonexistent_era')
    assert 'error' in result
    assert 'available_eras' in result


def test_list_available_options():
    """Test listing all available options."""
    result = list_available_options()
    assert 'aircraft_types' in result
    assert 'instruments' in result
    assert 'eras' in result
    assert len(result['aircraft_types']) > 0
    assert len(result['instruments']) > 0
    assert len(result['eras']) > 0


# ============================================================================
# Layer 2: Semantic Mapping Tests
# ============================================================================

def test_suggest_instruments_single_engine():
    """Test instrument suggestion for single-engine aircraft."""
    result = suggest_instruments('general_aviation_singles')
    assert 'aircraft_type' in result
    assert 'instruments' in result
    assert 'critical' in result['instruments']
    assert 'attitude_indicator' in result['instruments']['critical']


def test_suggest_instruments_ifr_mission():
    """Test instrument suggestion with IFR mission profile."""
    result = suggest_instruments('general_aviation_twins', mission_profile='ifr_cross_country')
    assert 'mission' in result
    assert result['mission'] == 'ifr_cross_country'
    assert 'navigation' in result['instruments']


def test_suggest_instruments_vfr_mission():
    """Test instrument suggestion with VFR mission profile."""
    result = suggest_instruments('general_aviation_singles', mission_profile='vfr_training')
    assert result['mission'] == 'vfr_training'


def test_suggest_instruments_twin_engine():
    """Test instrument suggestion for twin-engine aircraft."""
    result = suggest_instruments('general_aviation_twins')
    assert result['aircraft_type'] == 'general_aviation_twins'


def test_build_panel_specification_basic():
    """Test building a basic panel specification."""
    result = build_panel_specification('general_aviation_singles', 'analog_mechanical')
    assert 'aircraft_type' in result
    assert result['aircraft_type'] == 'general_aviation_singles'
    assert result['era'] == 'analog_mechanical'
    assert 'instruments' in result
    assert 'layout' in result
    assert 'era_characteristics' in result


def test_build_panel_specification_glass_cockpit():
    """Test building specification for glass cockpit."""
    result = build_panel_specification('commercial_airliners', 'glass_cockpit')
    assert result['era'] == 'glass_cockpit'
    assert 'era_characteristics' in result


def test_build_panel_specification_comprehensive():
    """Test building comprehensive specification."""
    result = build_panel_specification(
        'general_aviation_singles',
        'analog_mechanical',
        detail_level='comprehensive'
    )
    assert 'scan_patterns' in result


# ============================================================================
# Layer 3: Synthesis Tests
# ============================================================================

def test_generate_cockpit_prompt_basic():
    """Test basic cockpit prompt generation."""
    result = generate_cockpit_prompt(
        'general_aviation_singles',
        'analog_mechanical'
    )
    assert 'prompt_context' in result
    assert 'subject' in result['prompt_context']
    assert 'general aviation' in result['prompt_context']['subject'].lower()


def test_generate_cockpit_prompt_pilot_view():
    """Test prompt generation with pilot view angle."""
    result = generate_cockpit_prompt(
        'general_aviation_singles',
        'analog_mechanical',
        viewing_angle='pilot_view'
    )
    assert 'pilot' in result['prompt_context']['viewing_angle'].lower()


def test_generate_cockpit_prompt_night_lighting():
    """Test prompt generation with night lighting."""
    result = generate_cockpit_prompt(
        'general_aviation_singles',
        'analog_mechanical',
        lighting_condition='night'
    )
    assert 'darkness' in result['prompt_context']['lighting'].lower() or 'night' in result['prompt_context']['lighting'].lower()


def test_generate_cockpit_prompt_glass_cockpit():
    """Test prompt generation for glass cockpit era."""
    result = generate_cockpit_prompt(
        'commercial_airliners',
        'glass_cockpit'
    )
    assert 'key_instruments' in result['prompt_context']


def test_generate_cockpit_prompt_fighter():
    """Test prompt generation for fighter jet."""
    result = generate_cockpit_prompt(
        'fighter_jets',
        'hud_integration'
    )
    assert 'ready_for_image_generation' in result
    assert result['ready_for_image_generation'] is True


def test_generate_cockpit_prompt_with_context():
    """Test prompt generation with additional context."""
    result = generate_cockpit_prompt(
        'general_aviation_singles',
        'analog_mechanical',
        additional_context="during a thunderstorm approach"
    )
    assert 'additional_context' in result['prompt_context']


# ============================================================================
# Educational/Explanation Tests
# ============================================================================

def test_explain_scanning_logic():
    """Test explanation of scanning logic."""
    result = explain_cockpit_design('scanning_logic')
    assert 'aspect' in result
    assert result['aspect'] == 'scanning_logic'
    assert 'principle' in result['explanation']
    assert 'instruments' in result['explanation']


def test_explain_color_conventions():
    """Test explanation of color conventions."""
    result = explain_cockpit_design('color_conventions')
    assert 'color_conventions' in result['aspect']
    assert 'speed_arcs_example' in result['explanation']


def test_explain_positioning_rationale():
    """Test explanation of positioning rationale."""
    result = explain_cockpit_design('positioning_rationale')
    assert 'positioning_rationale' in result['aspect']


def test_explain_instrument_redundancy():
    """Test explanation of instrument redundancy."""
    result = explain_cockpit_design('instrument_redundancy')
    assert 'examples' in result['explanation']


def test_explain_invalid_aspect():
    """Test error handling for invalid aspect."""
    result = explain_cockpit_design('nonexistent_aspect')
    assert 'error' in result
    assert 'available_aspects' in result


# ============================================================================
# Integration Tests (Cross-layer)
# ============================================================================

def test_full_workflow_cessna_analog():
    """Test complete workflow: aircraft → specification → prompt."""
    # Layer 1: Get aircraft profile
    aircraft = get_aircraft_type_profile('general_aviation_singles')
    assert aircraft is not None
    assert 'error' not in aircraft
    
    # Layer 2: Build specification
    spec = build_panel_specification(
        'general_aviation_singles',
        'analog_mechanical'
    )
    assert spec is not None
    assert 'error' not in spec
    
    # Layer 3: Generate prompt
    prompt = generate_cockpit_prompt(
        'general_aviation_singles',
        'analog_mechanical'
    )
    assert prompt is not None
    assert 'ready_for_image_generation' in prompt


def test_full_workflow_airliner_glass():
    """Test complete workflow: airliner with glass cockpit."""
    aircraft = get_aircraft_type_profile('commercial_airliners')
    assert 'error' not in aircraft
    
    spec = build_panel_specification(
        'commercial_airliners',
        'glass_cockpit'
    )
    assert 'error' not in spec
    
    prompt = generate_cockpit_prompt(
        'commercial_airliners',
        'glass_cockpit',
        viewing_angle='overhead'
    )
    assert prompt['ready_for_image_generation'] is True


def test_full_workflow_fighter_hud():
    """Test complete workflow: fighter with HUD."""
    aircraft = get_aircraft_type_profile('fighter_jets')
    assert 'error' not in aircraft
    
    prompt = generate_cockpit_prompt(
        'fighter_jets',
        'hud_integration',
        lighting_condition='twilight'
    )
    assert 'ready_for_image_generation' in prompt


def test_mission_based_suggestion_ifr():
    """Test mission-based instrument selection for IFR."""
    result = suggest_instruments(
        'general_aviation_singles',
        mission_profile='ifr_cross_country'
    )
    assert 'navigation' in result['instruments']
    assert len(result['instruments']['navigation']) > 0


# ============================================================================
# Edge Cases and Robustness
# ============================================================================

def test_case_insensitivity():
    """Test that tool accepts case variations."""
    result1 = get_aircraft_type_profile('General_Aviation_Singles')
    result2 = get_aircraft_type_profile('general_aviation_singles')
    assert result1['aircraft_type'] == result2['aircraft_type']


def test_normalization_spaces_and_dashes():
    """Test that tools handle spaces and dashes."""
    result = get_instrument_details('Attitude Indicator')
    assert 'error' not in result
    assert 'Attitude Indicator' in result['name']


def test_all_aircraft_types_retrievable():
    """Verify all listed aircraft types are retrievable."""
    options = list_available_options()
    for aircraft_type in options['aircraft_types']:
        result = get_aircraft_type_profile(aircraft_type)
        assert 'error' not in result


def test_all_eras_retrievable():
    """Verify all listed eras are retrievable."""
    options = list_available_options()
    for era in options['eras']:
        result = get_era_profile(era)
        assert 'error' not in result


# ============================================================================
# Output Structure Tests
# ============================================================================

def test_prompt_context_has_required_fields():
    """Verify prompt context includes all required fields for Claude."""
    result = generate_cockpit_prompt(
        'general_aviation_singles',
        'analog_mechanical'
    )
    context = result['prompt_context']
    required = ['subject', 'viewing_angle', 'lighting', 'design_principles', 'color_conventions']
    for field in required:
        assert field in context, f"Missing required field: {field}"


def test_specification_completeness():
    """Verify panel specification is complete for synthesis."""
    result = build_panel_specification(
        'general_aviation_singles',
        'analog_mechanical'
    )
    required_keys = ['aircraft_type', 'era', 'instruments', 'layout', 'era_characteristics', 'color_palette']
    for key in required_keys:
        assert key in result, f"Missing required key in specification: {key}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
