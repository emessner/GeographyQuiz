### SETTINGS ###

# Window Settings
NAME = "The ultimate Geography Quiz"
WIDTH = 900
HEIGHT = 600
ANZAHL = 500
FPS = 60
TIME = 60
FONT = 'arial'
HS_FILE = 'highscore.txt'
BG_IMG = 'weltkarte_gross.jpg'
FLAGS = 'flaggen.jpg'
COUNTRY_FLAGS = ['Abkhazia', 'Afghanistan', 'Aland Islands', 'Albania', 
                 'Algeria', 'Andorra', 'Angola', 'Anguilla', 'Antigua', 
                 'Antilles', 'Argentina', 'Armenia', 'Aruba', 'Australia',
                 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
                 'Barbados', 'Bashkortostan', 'Belarus', 'Belgium', 'Belize',
                 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
                 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 
                 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 
                 'Central African Republic', 'Chad', 'Chile', 'China', 'Chuvashia',
                 'Colombia', 'Comoros', 'Dem. Rep. of the Congo', 'Rep. of the Congo',
                 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus',
                 'Czech Republic', 'Dagestan', 'Denmark', 'Djibouti', 'Dominica',
                 'Dominican Republic', 'East Timor', 'East Turkestan', 'Ecuador',
                 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
                 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia',
                 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 
                 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 
                 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 
                 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 
                 'North Korea', 'South Korea', 'Kosovo', 'Kuwait', 'Kyrgystan', 'Laos',
                 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
                 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 
                 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 
                 'Mauritania', 'Mauritius', 'Mexico', 'Federated States of Micronesia',
                 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique',
                 'Myanmar', 'Nagorno Karabakh', 'Namibia', 'Nauru', 'Nepal', 
                 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
                 'Niue', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine',
                 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland',
                 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis',
                 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 
                 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
                 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia',
                 'Slovenia', 'Solomon Islands', 'Somalia', 'Somaliland', 'South Arica',
                 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland',
                 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand',
                 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 
                 'Turkish Republic of Northern Cyprus', 'Turkmenistan', 'Tuvalu',
                 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 
                 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City',
                 'Venezuela', 'Vietnam', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']
BG_POS = (0, 0)

# Data
with open("Land.txt", "r") as tf:
    country = tf.readlines()
    
for i in range(len(country)):
    country[i] = country[i].replace(" \n", "")
    country[i] = country[i].replace("\n", "")
    
    
with open("Hauptstadt.txt", "r") as tf:
    capital = tf.readlines()
    
for i in range(len(capital)):
    capital[i] = capital[i].replace(" \n", "")
    capital[i] = capital[i].replace("\n", "")
    
COUNTRY = country
CAPITAL = capital

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 176, 240)
ROYAL_BLUE = (0, 0, 255)
DARKRED = (195, 0, 0)
GOLD = (255, 215, 0)
MAYGREEN = (146, 208, 80)
BG_COLOR = MAYGREEN
GREY = (213, 213, 213)
BG_FLAG = (217, 218, 220)
