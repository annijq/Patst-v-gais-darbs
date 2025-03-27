from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import io
import base64
from data.consumption_data import ecological_footprint_by_country, global_biocapacity, earth_overshoot_days
from utils import calculate_carbon_footprint, calculate_water_footprint

app = Flask(__name__)

@app.route('/')
def home():
    """Home page about overconsumption"""
    # Ecological footprint chart
    ecological_footprint = pd.DataFrame({
        'Region': ['North America', 'Europe', 'Asia', 'Africa', 'South America', 'Australia/Oceania'],
        'Ecological Footprint (gha per capita)': [8.4, 4.7, 2.2, 1.4, 2.8, 6.6],
        'Biocapacity (gha per capita)': [4.2, 3.1, 0.9, 1.3, 5.5, 7.3]
    })
    
    fig, ax = plt.subplots(figsize=(10, 6))
    bar_width = 0.35
    x = np.arange(len(ecological_footprint['Region']))
    
    ax.bar(x - bar_width/2, ecological_footprint['Ecological Footprint (gha per capita)'], 
           bar_width, label='Ecological Footprint')
    ax.bar(x + bar_width/2, ecological_footprint['Biocapacity (gha per capita)'], 
           bar_width, label='Biocapacity')
    
    ax.set_xlabel('Region')
    ax.set_ylabel('Global Hectares per Capita')
    ax.set_title('Ecological Footprint vs. Biocapacity by Region')
    ax.set_xticks(x)
    ax.set_xticklabels(ecological_footprint['Region'], rotation=45, ha='right')
    ax.legend()
    plt.tight_layout()
    
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    eco_plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close(fig)
    
    return render_template('home.html', eco_plot_url=eco_plot_url)

@app.route('/solutions')
def solutions():
    """Solutions to overconsumption page"""
    from data.consumption_data import solutions_data
    
    # Visual comparison of high vs low consumption lifestyles
    lifestyle_data = pd.DataFrame({
        'Category': ['Carbon Footprint (tons CO2/year)', 'Water Usage (gallons/day)', 'Waste Generated (lbs/week)'],
        'High-Consumption Lifestyle': [16, 100, 35],
        'Average Lifestyle': [10, 80, 21],
        'Sustainable Lifestyle': [4, 40, 7]
    })
    
    categories = lifestyle_data['Category']
    high_consumption = lifestyle_data['High-Consumption Lifestyle']
    average = lifestyle_data['Average Lifestyle']
    sustainable = lifestyle_data['Sustainable Lifestyle']
    
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(categories))
    width = 0.25
    
    ax.bar(x - width, high_consumption, width, label='High-Consumption Lifestyle', color='#D9534F')
    ax.bar(x, average, width, label='Average Lifestyle', color='#F0AD4E')
    ax.bar(x + width, sustainable, width, label='Sustainable Lifestyle', color='#5CB85C')
    
    ax.set_ylabel('Amount')
    ax.set_title('Environmental Impact by Lifestyle Type')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    plt.tight_layout()
    
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    lifestyle_plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close(fig)
    
    return render_template('solutions.html', 
                          solutions_data=solutions_data,
                          lifestyle_plot_url=lifestyle_plot_url)

@app.route('/earth-overshoot')
def earth_overshoot():
    """Earth Overshoot Day page"""
    import datetime
    
    # Format overshoot days data for visualization
    years = list(earth_overshoot_days.keys())
    days_data = list(earth_overshoot_days.values())
    
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Main line plot with smoother line and markers at every 5 years
    ax.plot(years, days_data, linestyle='-', color='#E74C3C', linewidth=2, alpha=0.9)
    
    # Add markers at every 5 years for better readability
    marked_years = [year for year in years if year % 5 == 0]
    marked_days = [earth_overshoot_days[year] for year in marked_years]
    ax.plot(marked_years, marked_days, 'o', color='#E74C3C', markersize=6)
    
    # Customize the plot
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Day of Year', fontsize=12)
    ax.set_title('Earth Overshoot Day (1971-2024)', fontsize=14, fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Set the x-axis ticks to be every 5 years
    ax.set_xticks([year for year in years if year % 5 == 0])
    ax.set_xticklabels([str(year) for year in years if year % 5 == 0], rotation=45)
    
    # Invert y-axis so earlier days (lower numbers) appear at the top
    ax.invert_yaxis()
    
    # Define month positions and names for secondary y-axis
    month_positions = [15, 46, 74, 105, 135, 166, 196, 227, 258, 288, 319, 349]  # Mid-month days
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Add a secondary y-axis for months
    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    ax2.set_yticks(month_positions)
    ax2.set_yticklabels(month_names, fontsize=10)
    ax2.invert_yaxis()  # Also invert the secondary axis
    
    # Add horizontal lines at month boundaries for better readability
    month_boundaries = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
    for boundary in month_boundaries:
        ax.axhline(y=boundary, color='gray', linestyle='-', alpha=0.2)
    
    # Add trend annotation
    ax.annotate('Earlier date = Earlier resource depletion', 
                xy=(1990, 270), 
                xytext=(1990, 240),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8),
                fontsize=10,
                ha='center')
    
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    overshoot_plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close(fig)
    
    # Country comparison chart
    countries = list(ecological_footprint_by_country.keys())
    footprints = list(ecological_footprint_by_country.values())
    earths_needed = [fp / global_biocapacity for fp in footprints]
    
    # Sort by footprint for better visualization
    countries_sorted = [x for _, x in sorted(zip(earths_needed, countries), reverse=True)]
    earths_needed_sorted = sorted(earths_needed, reverse=True)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.barh(countries_sorted, earths_needed_sorted, color=plt.cm.Reds(np.array(earths_needed_sorted)/max(earths_needed_sorted)))
    ax.set_xlabel('Number of Earths Needed')
    ax.set_title('How Many Earths Would We Need if Everyone Lived Like...')
    ax.grid(True)
    
    img2 = io.BytesIO()
    plt.savefig(img2, format='png', bbox_inches='tight')
    img2.seek(0)
    country_plot_url = base64.b64encode(img2.getvalue()).decode('utf8')
    plt.close(fig)
    
    # Footprint breakdown pie chart
    components = ['Carbon', 'Cropland', 'Grazing', 'Forest', 'Fishing', 'Built-up Land']
    
    # World average ecological footprint components (simplified)
    world_average = [60, 18, 8, 8, 3, 3]
    
    # Create pie chart for world average
    pie_charts = {}
    
    fig, ax = plt.subplots(figsize=(8, 8))
    # Use a custom color palette for better visualization
    colors = ['#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
    ax.pie(world_average, labels=components, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.set_title(f'Global Ecological Footprint Components')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
    
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    region_plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close(fig)
    
    pie_charts['World Average'] = region_plot_url
    
    return render_template('earth_overshoot.html',
                          overshoot_plot_url=overshoot_plot_url,
                          country_plot_url=country_plot_url,
                          pie_charts=pie_charts,
                          overshoot_days=earth_overshoot_days)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    """Environmental Impact Calculator page"""
    from data.consumption_data import transport_emission_factors, diet_emission_factors
    
    results = None
    
    if request.method == 'POST':
        # Calculate carbon footprint based on form data
        # Transport emissions
        car_type = request.form.get('car_type')
        car_distance = float(request.form.get('car_distance', 0))
        transport_emissions = 0
        
        if car_type != "None/Don't drive":
            # Initialize car_factor with a default value
            car_factor = 0.0
            
            if "Small car" in car_type:
                car_factor = 0.15  # kg CO2 per km
            elif "Medium car" in car_type:
                car_factor = 0.2  # kg CO2 per km
            elif "Large car/SUV" in car_type:
                car_factor = 0.3  # kg CO2 per km
            elif "Hybrid" in car_type:
                car_factor = 0.1  # kg CO2 per km
            elif "Electric" in car_type:
                car_factor = 0.05  # kg CO2 per km
                
            # Apply diesel modifier if applicable
            if "diesel" in car_type:
                car_factor *= 1.1
                
            transport_emissions += car_distance * car_factor * 52  # Annual emissions
        
        # Flight emissions
        flights_per_year = int(request.form.get('flights_per_year', 0))
        flight_distance = request.form.get('flight_distance')
        
        if flight_distance == "Short (< 3 hours)":
            flight_factor = 300  # kg CO2 per flight
        elif flight_distance == "Medium (3-6 hours)":
            flight_factor = 700  # kg CO2 per flight
        else:
            flight_factor = 1800  # kg CO2 per flight
            
        transport_emissions += flights_per_year * flight_factor
        
        # Food emissions calculation
        food_emissions = 0
        diet_type = request.form.get('diet_type')
        
        # Diet type multipliers
        diet_multipliers = {
            "Meat with every meal": 2.5,
            "Meat-heavy": 2.0,
            "Average omnivore": 1.5,
            "Flexitarian": 1.2,
            "Pescatarian": 1.0,
            "Vegetarian": 0.8,
            "Vegan": 0.5
        }
        
        base_food_emissions = 1000  # kg CO2 per year base value
        food_emissions = base_food_emissions * diet_multipliers[diet_type]
        
        # Home energy calculation
        home_emissions = 0
        home_size = request.form.get('home_size')
        household_size = int(request.form.get('household_size', 1))
        
        # Base emissions by home size
        home_size_emissions = {
            "Small apartment": 1000,
            "Large apartment": 1800,
            "Small house": 2500,
            "Medium house": 3500,
            "Large house": 5000
        }
        
        base_home_emissions = home_size_emissions[home_size] / household_size
        home_emissions = base_home_emissions
        
        # Calculate total carbon footprint
        total_carbon_footprint = transport_emissions + food_emissions + home_emissions
        
        # Create carbon footprint breakdown chart
        categories = ['Transportation', 'Food & Diet', 'Home Energy']
        values = [transport_emissions, food_emissions, home_emissions]
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(categories, values, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
        ax.set_ylabel('Emissions (kg CO₂e)')
        ax.set_title('Carbon Footprint by Category')
        plt.tight_layout()
        
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        img.seek(0)
        carbon_breakdown_plot = base64.b64encode(img.getvalue()).decode('utf8')
        plt.close(fig)
        
        # Compare to global average
        global_avg_carbon = 5000  # kg CO2e per year (approximate)
        sustainable_carbon = 2000  # kg CO2e per year (approximate sustainable level)
        
        comparison_labels = ['Your Footprint', 'Global Average', 'Sustainable Level']
        comparison_values = [total_carbon_footprint, global_avg_carbon, sustainable_carbon]
        comparison_colors = ['#FFA726', '#64B5F6', '#81C784']
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(comparison_labels, comparison_values, color=comparison_colors)
        ax.set_ylabel('Carbon Footprint (kg CO₂e)')
        ax.set_title('How Your Footprint Compares')
        plt.tight_layout()
        
        img2 = io.BytesIO()
        plt.savefig(img2, format='png', bbox_inches='tight')
        img2.seek(0)
        comparison_plot = base64.b64encode(img2.getvalue()).decode('utf8')
        plt.close(fig)
        
        # Prepare results
        results = {
            'carbon_footprint': round(total_carbon_footprint, 1),
            'transport_emissions': round(transport_emissions, 1),
            'food_emissions': round(food_emissions, 1),
            'home_emissions': round(home_emissions, 1),
            'carbon_breakdown_plot': carbon_breakdown_plot,
            'comparison_plot': comparison_plot,
            'is_sustainable': total_carbon_footprint < sustainable_carbon,
            'is_below_average': total_carbon_footprint < global_avg_carbon
        }
    
    return render_template('calculator.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)