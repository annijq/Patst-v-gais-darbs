"""
Utility functions for the overconsumption educational application
"""

def calculate_carbon_footprint(transport_emissions, food_emissions, home_emissions):
    """Calculate carbon footprint based on transportation, food, and home energy use"""
    return transport_emissions + food_emissions + home_emissions

def calculate_water_footprint(food_water, home_water, goods_water):
    """Calculate water footprint based on food, home use, and goods purchased"""
    return food_water + home_water + goods_water