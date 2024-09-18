from flask import Flask, render_template, request
from astropy.time import Time, TimeDelta
from astropy.coordinates import solar_system_ephemeris, get_body_barycentric_posvel, SkyCoord
import astropy.units as u
from astropy.constants import G, c  # Import gravitational constant and speed of light
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Define a dictionary of star masses (in solar masses)
STAR_MASSES = {
    'sun': 1.0,  # Sun's mass in solar masses
    'sirius': 2.02,  # Sirius A mass in solar masses
    'proxima_centauri': 0.1221,  # Proxima Centauri mass in solar masses
    'vega': 2.135,  # Vega mass in solar masses
    'betelgeuse': 11.6  # Betelgeuse mass in solar masses
}

def calculate_blackhole_schwarzschild_radius(star_name):
    # Get the mass of the selected star in solar masses
    star_mass_in_solar_masses = STAR_MASSES.get(star_name.lower(), 1.0)

    # Calculate Schwarzschild radius
    solar_mass = 1.98847e30 * u.kg  # Mass of the sun in kilograms

    # Schwarzschild radius formula: Rs = 2 * G * M / c^2
    star_mass_kg = star_mass_in_solar_masses * solar_mass
    schwarzschild_radius = (2 * G * star_mass_kg / c**2).to(u.km)

    return f"The Schwarzschild radius for a black hole with the mass of {star_name.capitalize()} is {schwarzschild_radius:.2f}"
@app.route('/calculate', methods=['POST'])
def calculate():
    query_type = request.form.get('query_type')

    if query_type == 'alignment':
        # Planet alignment logic here
        planet1 = request.form.get('planet1')
        planet2 = request.form.get('planet2')
        auto_date = request.form.get('auto_date')

        if auto_date:
            years_to_check = int(request.form.get('years', 5))
            result = calculate_next_alignment(planet1, planet2, years_to_check)
        else:
            date = request.form.get('date')
            result = calculate_alignment(planet1, planet2, date)

        return render_template('index.html', result=result)

    elif query_type == 'blackhole_sun':
        mass_option = request.form.get('mass_option')

        if mass_option == 'star':
            star = request.form.get('star', 'sun')
            result = calculate_blackhole_schwarzschild_radius(star)
        elif mass_option == 'mass':
            mass = float(request.form.get('mass'))
            result = calculate_custom_schwarzschild_radius(mass)

        return render_template('index.html', result=result)

    return render_template('index.html', result="Invalid request")

def calculate_blackhole_schwarzschild_radius(star_name):
    # Get the mass of the selected star in solar masses
    star_mass_in_solar_masses = STAR_MASSES.get(star_name.lower(), 1.0)

    # Call the generic Schwarzschild radius calculation
    return calculate_schwarzschild_radius(star_mass_in_solar_masses, star_name)

def calculate_custom_schwarzschild_radius(star_mass_in_solar_masses):
    # Call the generic Schwarzschild radius calculation
    return calculate_schwarzschild_radius(star_mass_in_solar_masses, "Custom star")

def calculate_schwarzschild_radius(star_mass_in_solar_masses, star_name):
    solar_mass = 1.98847e30 * u.kg  # Mass of the sun in kilograms

    # Schwarzschild radius formula: Rs = 2 * G * M / c^2
    star_mass_kg = star_mass_in_solar_masses * solar_mass
    schwarzschild_radius = (2 * G * star_mass_kg / c**2).to(u.km)

    return f"The Schwarzschild radius for a black hole with the mass of {star_name} is {schwarzschild_radius:.2f}."


def calculate_alignment(planet1, planet2, date):
    solar_system_ephemeris.set('builtin')
    time = Time(date)

    planet1_pos, _ = get_body_barycentric_posvel(planet1, time)
    planet2_pos, _ = get_body_barycentric_posvel(planet2, time)

    planet1_coord = SkyCoord(planet1_pos.xyz[0], planet1_pos.xyz[1], planet1_pos.xyz[2], representation_type='cartesian', unit=u.au, frame='icrs')
    planet2_coord = SkyCoord(planet2_pos.xyz[0], planet2_pos.xyz[1], planet2_pos.xyz[2], representation_type='cartesian', unit=u.au, frame='icrs')

    angle = planet1_coord.separation(planet2_coord).to(u.deg).value
    if angle < 1.0:
        return f"{planet1.capitalize()} and {planet2.capitalize()} are aligned on {date}!"
    else:
        return f"{planet1.capitalize()} and {planet2.capitalize()} are not aligned on {date}. The angle is {angle:.2f} degrees."

def calculate_next_alignment(planet1, planet2, years_to_check):
    solar_system_ephemeris.set('builtin')
    start_time = Time.now()  # Start checking from the current time
    time_step = TimeDelta(1, format='jd')  # Check each day

    current_time = start_time
    while current_time < start_time + 365 * years_to_check:  # Check up to the number of years specified
        planet1_pos, _ = get_body_barycentric_posvel(planet1, current_time)
        planet2_pos, _ = get_body_barycentric_posvel(planet2, current_time)

        planet1_coord = SkyCoord(planet1_pos.xyz[0], planet1_pos.xyz[1], planet1_pos.xyz[2], representation_type='cartesian', unit=u.au, frame='icrs')
        planet2_coord = SkyCoord(planet2_pos.xyz[0], planet2_pos.xyz[1], planet2_pos.xyz[2], representation_type='cartesian', unit=u.au, frame='icrs')

        angle = planet1_coord.separation(planet2_coord).to(u.deg).value

        if angle < 1.0:  # If planets are aligned within 1 degree
            return f"{planet1.capitalize()} and {planet2.capitalize()} will be aligned on {current_time.iso}!"

        current_time += time_step  # Move to the next day

    return f"No alignment found between {planet1.capitalize()} and {planet2.capitalize()} within the next {years_to_check} years."


if __name__ == '__main__':
    app.run()
