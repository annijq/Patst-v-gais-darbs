"""
This module contains data related to consumption patterns, ecological footprints,
and other data points used throughout the application.
"""

# Average ecological footprint by country (global hectares per person)
ecological_footprint_by_country = {
    "United States": 8.04,
    "Australia": 6.75,
    "Russia": 5.69,
    "Germany": 4.88,
    "United Kingdom": 4.28,
    "France": 4.20,
    "China": 3.71,
    "Brazil": 3.11,
    "Mexico": 2.64,
    "India": 1.19,
    "Bangladesh": 0.85,
}

# Global average biocapacity: 1.63 global hectares per person
global_biocapacity = 1.63

# Earth Overshoot Day by year (day of year)
earth_overshoot_days = {
    1971: 359,
    1972: 362,
    1973: 337,
    1974: 334,
    1975: 331,
    1976: 326,
    1977: 321,
    1978: 316,
    1979: 305,
    1980: 321,
    1981: 324,
    1982: 335,
    1983: 338,
    1984: 322,
    1985: 311,
    1986: 309,
    1987: 303,
    1988: 290,
    1989: 286,
    1990: 291,
    1991: 293,
    1992: 304,
    1993: 300,
    1994: 289,
    1995: 282,
    1996: 278,
    1997: 279,
    1998: 280,
    1999: 269,
    2000: 261,
    2001: 256,
    2002: 262,
    2003: 255,
    2004: 246,
    2005: 239,
    2006: 236,
    2007: 227,
    2008: 229,
    2009: 235,
    2010: 222,
    2011: 218,
    2012: 217,
    2013: 215,
    2014: 217,
    2015: 219,
    2016: 222,
    2017: 217,
    2018: 213,
    2019: 215,
    2020: 223,  # Note: moved later due to COVID-19 pandemic
    2021: 215,
    2022: 213,
    2023: 217,
    2024: 214
}

# Resource consumption factors for calculator
transport_emission_factors = {
    "Car (gasoline)": 2.3,        # kg CO2 per liter
    "Car (diesel)": 2.7,          # kg CO2 per liter
    "Bus": 0.105,                 # kg CO2 per km
    "Train": 0.041,               # kg CO2 per km
    "Domestic flight": 0.255,     # kg CO2 per km
    "Long-haul flight": 0.150,    # kg CO2 per km
}

diet_emission_factors = {
    "Meat-heavy": 7.19,           # kg CO2e per day
    "Average omnivore": 4.67,     # kg CO2e per day
    "Pescatarian": 3.91,          # kg CO2e per day
    "Vegetarian": 3.18,           # kg CO2e per day
    "Vegan": 2.89,                # kg CO2e per day
}

water_usage_factors = {
    "Showering (5 min)": 95,      # liters
    "Bath": 113,                  # liters
    "Toilet flush": 6,            # liters
    "Washing machine": 50,        # liters per load
    "Dishwasher": 15,             # liters per load
    "Brushing teeth (tap running)": 8,  # liters
    "Washing hands": 2,           # liters
}

# Water footprint of common foods (liters per kg or liter of product)
food_water_footprint = {
    "Beef": 15400,
    "Lamb": 10400,
    "Pork": 5990,
    "Chicken": 4330,
    "Eggs": 3300,
    "Rice": 2500,
    "Soybeans": 2145,
    "Wheat": 1830,
    "Milk": 1020,
    "Potatoes": 290,
    "Vegetables (average)": 322,
    "Fruits (average)": 962,
}

# Solutions categories and impacts
solutions_data = {
    "Dietary Changes": {
        "Plant-rich diet": "Reducing meat consumption can cut your dietary carbon footprint by up to 60%",
        "Reduce food waste": "If food waste were a country, it would be the 3rd largest emitter of greenhouse gases",
        "Eat local & seasonal": "Local food can reduce transportation emissions by 4-5%"
    },
    "Transportation": {
        "Use public transport": "Public transport uses 45% less energy per person than private vehicles",
        "Bike or walk": "Short car trips are up to 3 times more polluting per kilometer",
        "Reduce flying": "One long-haul flight can emit as much CO2 as driving for a year"
    },
    "Consumer Habits": {
        "Buy less": "The average American throws away 37kg of clothes each year",
        "Repair and reuse": "Extending product life by 9 months reduces carbon footprint by 20-30%",
        "Choose quality": "Long-lasting products reduce waste and resource extraction"
    },
    "Home Energy": {
        "Use renewable energy": "Switching to renewable electricity can reduce your carbon footprint by 1.5 tons annually",
        "Improve insulation": "Proper insulation can reduce heating/cooling needs by 20-30%",
        "Energy-efficient appliances": "Can reduce electricity consumption by 10-50% compared to standard models"
    }
}