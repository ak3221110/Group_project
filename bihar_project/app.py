from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'places.csv')

def load_places():
    places = []
    with open(DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            places.append(row)
    return places

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    query = request.args.get('q', '').lower()
    results = []

    # Define all CSV data files and their type labels and fields to search
    data_files = [
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'places.csv'), 'type': 'Place', 'fields': ['Place Name', 'Location', 'Category']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Artists & Musicians.csv'), 'type': 'Artist/Musician', 'fields': ['Name', 'Field', 'Period of Influence', 'Key Contributions']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Business & Entrepreneurship.csv'), 'type': 'Business/Entrepreneurship', 'fields': ['Name', 'Description']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Film & Cinema.csv'), 'type': 'Film & Cinema', 'fields': ['Name', 'Description']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Traditional Dance Forms.csv'), 'type': 'Traditional Dance', 'fields': ['Name', 'Description']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Music & Performing Arts.csv'), 'type': 'Music & Performing Arts', 'fields': ['Name', 'Description']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Religious_Places_in_Bihar.csv'), 'type': 'Religious Place', 'fields': ['Name', 'Location', 'Religion', 'Deity/Saint', 'Significance']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Natural_Attractions_in_Bihar.csv'), 'type': 'Natural Attraction', 'fields': ['Attraction Name', 'Location', 'Type', 'Key Highlights']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Cultural_Heritage_Spots_in_Bihar.csv'), 'type': 'Cultural Heritage Spot', 'fields': ['Site Name', 'Location', 'Type', 'Key Highlights']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Wildlife_Eco_Tourism_Spots_in_Bihar.csv'), 'type': 'Wildlife Eco Tourism Spot', 'fields': ['Site Name', 'Location', 'Type', 'Key Highlights']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Adventure_Scenic_Locations_in_Bihar.csv'), 'type': 'Adventure Scenic Location', 'fields': ['Site Name', 'Location', 'Type', 'Key Highlights']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Political and Historical Leaders.csv'), 'type': 'Political/Historical Leader', 'fields': ['Leader Name', 'Political Affiliation', 'Period of Influence', 'Key Contributions']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Writers & Scholars.csv'), 'type': 'Writer/Scholar', 'fields': ['Name', 'Field', 'Period of Influence', 'Key Contributions']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Mammals_in_Bihar_Updated.csv'), 'type': 'Mammal', 'fields': ['Common Name', 'Local Name', 'Scientific Name', 'Habitat', 'Details']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Birds_in_Bihar.csv'), 'type': 'Bird', 'fields': ['Common Name', 'Local Name (Hindi)', 'Scientific Name', 'Habitat', 'Description']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'Reptiles & Amphibians.csv'), 'type': 'Reptile/Amphibian', 'fields': ['Common Name', 'Local Name (Hindi)', 'Scientific Name', 'Habitat', 'Description']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'aquatic_life.csv'), 'type': 'Aquatic Life', 'fields': ['Common Name', 'Local Name', 'Scientific Name', 'Habitat', 'Description']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'GI_Agricultural_Products_in_Bihar.csv'), 'type': 'GI Agricultural Product', 'fields': ['Product Name', 'Region', 'Type', 'Key Highlights']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'GI_Handicrafts_Arts_in_Bihar.csv'), 'type': 'GI Handicraft/Art', 'fields': ['Product Name', 'Region', 'Type', 'Key Highlights']},
        {'file': os.path.join(os.path.dirname(__file__), 'data', 'GI_Food_Products_in_Bihar.csv'), 'type': 'GI Food Product', 'fields': ['Product Name', 'Region', 'Type', 'Key Highlights']}
    ]

    for data in data_files:
        if not os.path.exists(data['file']):
            continue
        try:
            with open(data['file'], newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if any(query in (row.get(field, '') or '').lower() for field in data['fields']):
                        results.append({
                            'type': data['type'],
                            'name': row.get('Name', row.get('Place Name', row.get('Site Name', row.get('Common Name', row.get('Leader Name', row.get('Product Name', '')))))),
                            'description': row.get('Description', row.get('Key Highlights', row.get('Details', row.get('Key Contributions', '')))),
                            'location': row.get('Location', row.get('Region', '')),
                            'category': row.get('Category', row.get('Type', ''))
                        })
        except Exception:
            continue

    return render_template('search.html', results=results, query=query)

@app.route('/navbar')
def navbar():
    return render_template('navbar.html')

@app.route('/popular-people')
def popular_people():
    return render_template('popular_people.html')

@app.route('/historical-sites')
def historical_sites():
    return render_template('historical_sites.html')

RELIGIOUS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'Religious_Places_in_Bihar.csv')

def load_religious_places():
    religious_places = []
    image_mapping = {
        "Mahavir Mandir": "Mahavir Mandir.jpg",
        "Mundeshwari Temple": "Mundeshwari Temple.jpg",
        "Vishnupad Temple": "Vishnupad Temple.jpg",
        "Ajgaibinath Temple": "Ajgaibinath Temple.avif",
        "Hariharnath Temple": "Hariharnath Temple.avif",
        "Baba Garibnath Dham": "Baba Garibnath Dham.jpg",
        "Thawe Mandir": "Thawe Mandir.jpg",
        "Sundarnath Temple": "Sundarnath Temple.jpg",
        "Ahalya Sthan": "Ahalya Sthan.jpg",
        "Ugratara Temple": "Ugratara Temple.jpeg",
        "Shiv Shakti Temple": "Shiv Shakti Temple.jpg",
        "Budhanath Temple": "Budhanath Temple.jpg",
        "Ramchaura Mandir": "Ramchaura Mandir.jpg",
        "Janki Temple": "Janki Temple.jpg",
        "Mahabodhi Temple": "Mahabodhi Temple.webp",
        "Nalanda University Ruins": "Nalanda University Ruins.jpg",
        "Griddhakuta Hill": "Griddhakuta Hill.jpg",
        "Sujata Kuti": "Sujata Kuti.webp",
        "Vaishali Stupa": "Vaishali Stupa.jpg",
        "Jal Mandir": "Jal Mandir.jpg",
        "Samosharan Mandir": "Samosharan Mandir.jpg",
        "Vaishali Jain Temple": "Vaishali Jain Temple.jpg",
        "Champapuri": "Champapuri.jpg",
        "Lachhuar Jain Temple": "Lachhuar Jain Temple.jpg",
        "Maner Sharif": "Maner Sharif.jpg",
        "Bari Dargah": "Bari Dargah.jpeg",
        "Chhoti Dargah": "Chhoti Dargah.jpg",
        "Phulwari Sharif": "Phulwari Sharif.jpg",
        "Padri Ki Haveli": "Padri Ki Haveli.jpg",
        "St. Joseph's Church": "St. Joseph's Church.jpg",
        "Queen of Apostles Church": "Queen of Apostles Church.jpg",
        "Takht Sri Patna Sahib": "Takht Sri Patna Sahib.avif",
        "Gurudwara Gai Ghat": "Gurudwara Gai Ghat.jpg",
        "Gurudwara Bal Leela": "Gurudwara Bal Leela.jpg"
    }
    with open(RELIGIOUS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['Image'] = image_mapping.get(row['Name'], None)
            religious_places.append(row)
    return religious_places

@app.route('/religious-places')
def religious_places():
    religious_places = load_religious_places()
    return render_template('religious_places.html', religious_places=religious_places)

NATURAL_ATTRACTIONS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'Natural_Attractions_in_Bihar.csv')

def load_natural_attractions():
    natural_attractions = []
    with open(NATURAL_ATTRACTIONS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            natural_attractions.append(row)
    return natural_attractions

@app.route('/natural-attractions')
def natural_attractions():
    natural_attractions = load_natural_attractions()
    return render_template('natural_attractions.html', natural_attractions=natural_attractions)

CULTURAL_HERITAGE_SPOTS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'Cultural_Heritage_Spots_in_Bihar.csv')

def load_cultural_heritage_spots():
    cultural_heritage_spots = []
    with open(CULTURAL_HERITAGE_SPOTS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cultural_heritage_spots.append(row)
    return cultural_heritage_spots

@app.route('/cultural-heritage-spots')
def cultural_heritage_spots():
    cultural_heritage_spots = load_cultural_heritage_spots()
    return render_template('cultural_heritage_spots.html', cultural_heritage_spots=cultural_heritage_spots)

WILDLIFE_ECO_TOURISM_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'Wildlife_Eco_Tourism_Spots_in_Bihar.csv')

def load_wildlife_eco_tourism_spots():
    wildlife_eco_tourism_spots = []
    with open(WILDLIFE_ECO_TOURISM_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            wildlife_eco_tourism_spots.append(row)
    return wildlife_eco_tourism_spots

@app.route('/wildlife-eco-tourism')
def wildlife_eco_tourism():
    wildlife_eco_tourism_spots = load_wildlife_eco_tourism_spots()
    return render_template('wildlife_eco_tourism.html', wildlife_eco_tourism_spots=wildlife_eco_tourism_spots)

ADVENTURE_SCENIC_LOCATIONS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'Adventure_Scenic_Locations_in_Bihar.csv')

def load_adventure_scenic_locations():
    adventure_scenic_locations = []
    with open(ADVENTURE_SCENIC_LOCATIONS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            adventure_scenic_locations.append(row)
    return adventure_scenic_locations

@app.route('/adventure-scenic-locations')
def adventure_scenic_locations():
    adventure_scenic_locations = load_adventure_scenic_locations()
    return render_template('adventure_scenic_locations.html', adventure_scenic_locations=adventure_scenic_locations)


POLITICAL_HISTORICAL_LEADERS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'Political and Historical Leaders.csv')

def load_political_historical_leaders():
    leaders = []
    with open(POLITICAL_HISTORICAL_LEADERS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for row in reader:
            # Strip whitespace from keys and values
            clean_row = {k.strip(): v.strip() for k, v in row.items()}
            leaders.append(clean_row)
    return leaders

@app.route('/political-historical-leaders')
def political_historical_leaders():
    leaders = load_political_historical_leaders()
    return render_template('political_historical_leaders.html', leaders=leaders)

WRITERS_SCHOLARS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'Writers & Scholars.csv')

def load_writers_scholars():
    writers_scholars = []
    with open(WRITERS_SCHOLARS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for row in reader:
            clean_row = {k.strip(): v.strip() for k, v in row.items()}
            writers_scholars.append(clean_row)
    return writers_scholars

@app.route('/writers-scholars')
def writers_scholars():
    writers_scholars = load_writers_scholars()
    return render_template('writers_scholars.html', writers_scholars=writers_scholars)

ARTISTS_MUSICIANS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'Artists & Musicians.csv')

def load_artists_musicians():
    artists_musicians = []
    with open(ARTISTS_MUSICIANS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        for row in reader:
            clean_row = {k.strip(): v.strip() for k, v in row.items()}
            artists_musicians.append(clean_row)
    return artists_musicians

@app.route('/artists-musicians')
def artists_musicians():
    artists_musicians = load_artists_musicians()
    return render_template('artists_musicians.html', artists_musicians=artists_musicians)

@app.route('/business-entrepreneurship')
def business_entrepreneurship():
    return render_template('business_entrepreneurship.html')

@app.route('/film-cinema')
def film_cinema():
    return render_template('film_cinema.html')

@app.route('/music-performing-arts')
def music_performing_arts():
    return render_template('music_performing_arts.html')

@app.route('/traditional-dance-forms')
def traditional_dance_forms():
    return render_template('traditional_dance_forms.html')

@app.route('/culture')
def culture():
    return render_template('culture.html')

MAMMALS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'Mammals_in_Bihar_Updated.csv')

def load_mammals():
    mammals = []
    with open(MAMMALS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mammals.append(row)
    return mammals

@app.route('/mammals')
def mammals():
    mammals = load_mammals()
    return render_template('mammals.html', mammals=mammals)

BIRDS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'Birds_in_Bihar.csv')

def load_birds():
    birds = []
    with open(BIRDS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            birds.append(row)
    return birds

@app.route('/birds-species')
def birds_species():
    birds = load_birds()
    return render_template('birds_species.html', birds=birds)

REPTILES_AMPHIBIANS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'Reptiles & Amphibians.csv')

def load_reptiles_amphibians():
    reptiles_amphibians = []
    with open(REPTILES_AMPHIBIANS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            reptiles_amphibians.append(row)
    return reptiles_amphibians

@app.route('/reptiles-amphibians')
def reptiles_amphibians():
    reptiles_amphibians = load_reptiles_amphibians()
    return render_template('reptiles_amphibians.html', reptiles_amphibians=reptiles_amphibians)

AQUATIC_LIFE_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'aquatic_life.csv')

def load_aquatic_life():
    aquatic_life = []
    with open(AQUATIC_LIFE_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            aquatic_life.append(row)
    return aquatic_life

@app.route('/aquatic-life')
def aquatic_life():
    aquatic_life = load_aquatic_life()
    return render_template('aquatic_life.html', aquatic_life=aquatic_life)

GI_AGRICULTURAL_PRODUCTS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'GI_Agricultural_Products_in_Bihar.csv')

def load_gi_agricultural_products():
    gi_agricultural_products = []
    with open(GI_AGRICULTURAL_PRODUCTS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            gi_agricultural_products.append(row)
    return gi_agricultural_products

@app.route('/gi-agricultural-products')
def gi_agricultural_products():
    gi_agricultural_products = load_gi_agricultural_products()
    return render_template('gi_agricultural_products.html', gi_agricultural_products=gi_agricultural_products)

GI_HANDICRAFTS_ARTS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'GI_Handicrafts_Arts_in_Bihar.csv')

def load_gi_handicrafts_arts():
    gi_handicrafts_arts = []
    with open(GI_HANDICRAFTS_ARTS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            gi_handicrafts_arts.append(row)
    return gi_handicrafts_arts

@app.route('/gi-handicrafts-arts')
def gi_handicrafts_arts():
    gi_handicrafts_arts = load_gi_handicrafts_arts()
    return render_template('gi_handicrafts_arts.html', gi_handicrafts_arts=gi_handicrafts_arts)

GI_FOOD_PRODUCTS_DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'GI_Food_Products_in_Bihar.csv')

def load_gi_food_products():
    gi_food_products = []
    with open(GI_FOOD_PRODUCTS_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            gi_food_products.append(row)
    return gi_food_products

@app.route('/gi-food-products')
def gi_food_products():
    gi_food_products = load_gi_food_products()
    return render_template('gi_food_products.html', gi_food_products=gi_food_products)

@app.route('/animals')
def animals():
    return render_template('animals.html')

@app.route('/birds')
def birds():
    return render_template('birds.html')

@app.route('/entertainment')
def entertainment():
    return render_template('entertainment.html')

if __name__ == '__main__':
    app.run(debug=True)
