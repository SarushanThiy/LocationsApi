from werkzeug.exceptions import BadRequest

locations = [
    {
        "id": 1,
        "Name": "Ottawa",
        "cityBeach": "City",
        "Country": "Canada",
        "Continent": "North America",
        "Img": "https://content.r9cdn.net/rimg/dimg/66/6f/19cfcc07-city-9618-1629b990c4d.jpg?crop=true&width=1366&height=768&xhint=1491&yhint=1383" 
    },
    {
        "id": 2,
        "Name": "Ahmedabad",
        "cityBeach": "City",
        "Country": "India",
        "Continent": "Asia",
        "Img": "https://www.tripsavvy.com/thmb/18jukZwmonkaOB7Gk2t_ua9GDYQ=/2121x1414/filters:no_upscale():max_bytes(150000):strip_icc()/sidi-bashir-mosque-in-ahmedabad-1322198135-18dddfc8f76e4a2f8cbce7d522ad4cb7.jpg"
    },
    {
        "id": 3,
        "Name": "Tiverton",
        "cityBeach": "City",
        "Country": "United Kingdom",
        "Continent": "Europe",
        "Img": "https://eu-assets.simpleview-europe.com/southdevon2018/imageresizer/?image=%2Fdmsimgs%2FRiver_Exe_1_-_c_Dennis_Knowles_sm_1744811111.jpg&action=ProductDetailPro"        
    },
    {
        "id": 4,
        "Name": "Boulogne-sur-Mer",
        "cityBeach": "Beach",
        "Country": "France",
        "Continent": "Europe",
        "Img": "https://media.istockphoto.com/photos/beautiful-landscape-of-the-coast-in-the-north-of-france-picture-id1180007907?k=20&m=1180007907&s=612x612&w=0&h=4qVTKD8Y71QQfS7PV6HFDFtgZlU6iLLP5ykQnSTf5uU="
    },
    {
        "id": 5,
        "Name": "Buffalo",
        "cityBeach": "City",
        "Country": "United States",
        "Continent": "North America",
        "Img": "https://www.americancityandcounty.com/files/2021/11/Ele-Tower-Cirtscape-Sunset-Uncropped-2x3-small-1024x512.jpg"
    },
    {
        "id": 6,
        "Name": "Los Angeles",
        "cityBeach": "City",
        "Country": "United States",
        "Continent": "North America",
        "Img": "https://www.gousa.in/sites/default/files/styles/hero_l/public/images/hero_media_image/2017-01/Getty_515070156_EDITORIALONLY_LosAngeles_HollywoodBlvd_Web72DPI_0.jpg?itok=lst_2_5d"        
    },
    {
        "id": 7,
        "Name": "Adeje",
        "cityBeach": "Beach",
        "Country": "Spain",
        "Continent": "Europe",
        "Img": "https://www.kyero.com/guides/wp-content/uploads/2018/12/xAdeje-beach-2400x1603.jpg.pagespeed.ic.anX56D5Pn_.jpg"
    },
    {
        "id": 8, 
        "Name": "Havana",
        "cityBeach": "City",
        "Country": "Cuba",
        "Continent": "South America",
        "Img": "https://media.gq.com/photos/5914dd2943572d096b80c8f3/4:3/w_1728,h_1296,c_limit/guide-to-old-havana-cuba.jpg"
    },
    {
        "id": 9, 
        "Name": "Alberta",
        "cityBeach": "City",
        "Country": "Canada",
        "Continent": "North America",
        "Img": "https://assets.justenergy.com/wp-content/uploads/2021/10/moving-to-alberta-canada-guide-and-faqs-image-of-lake.jpg"        
    },
    {
        "id": 10,
        "Name": "New York City",
        "cityBeach": "City",
        "Country": "United States",
        "Continent": "North America",
        "Img": "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-688899881-1519413300.jpg"
    },
    {
        "id": 11,
        "Name": "Penida Island",
        "cityBeach": "Beach",
        "Country": "Indonesia",
        "Continent": "Asia",
        "Img": "https://i0.wp.com/girleatworld.net/wp-content/uploads/2018/04/nusa-penida-kelingking-1.jpg?fit=1400%2C1116&ssl=1"
    },
    {
        "id": 12,
        "Name": "Cox's Bazaar",
        "cityBeach": "Beach",	
        "Country": "Bangladesh",
        "Continent": "Asia",
        "Img": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/10/e2/f8/43/longest-sea-beach-in.jpg?w=700&h=-1&s=1"
    },
    {
        "id": 13,
        "Name": "Sharm-el-Sheikh",
        "cityBeach": "Beach",
        "Country": "Egypt",
        "Continent": "Africa",
        "Img": "https://media.istockphoto.com/photos/beach-at-sharm-el-sheikh-picture-id496255780?k=20&m=496255780&s=612x612&w=0&h=xyrZ8Aas2f0v4S1Zdz8U9KyZYIyppZMEWoB3nSh9CO4="
    },
    {
        "id": 14,
        "Name": "Copenhagen",
        "cityBeach": "City",
        "Country": "Denmark",
        "Continent": "Europe",
        "Img": "https://media.timeout.com/images/105659619/image.jpg"
    },
    {
        "id": 15,
        "Name": "Cabo San Lucas",
        "cityBeach": "Beach",
        "Country": "Mexico",
        "Continent": "South America",
        "Img": "https://www.planetware.com/wpimages/2018/09/mexico-cabo-san-lucas-things-to-do-sunset-lands-end.jpg"
    },
    {
        "id": 16,
        "Name": "Lagos",
        "cityBeach": "City",
        "Country": "Nigeria",
        "Continent": "Africa",
        "Img": "https://media.newyorker.com/photos/5909523dc14b3c606c103bac/16:9/w_1280,c_limit/Victoria-Island-580.jpg"
    },
    {
        "id": 17,
        "Name": "Unguja",
        "cityBeach": "Beach",
        "Country": "Tanzania",
        "Continent": "Africa",
        "Img": "https://photo620x400.mnstatic.com/6d8b6d2dfd308fa5b26d517a6bff7fa3/unguja-ukku.jpg"
    },
    {
        "id": 18,
        "Name": "Corwnall",
        "cityBeach": "Beach",
        "Country": "United Kingdom",
        "Continent": "North America",
        "Img": "https://www.telegraph.co.uk/content/dam/Travel/Destinations/Europe/United%20Kingdom/Cornwall/cornwall-things-to-do-guide-xlarge.jpg"        
    },
    {
        "id": 19,
        "Name": "Majorca",
        "cityBeach": "Beach",
        "Country": "Spain",
        "Continent": "Europe",
        "Img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSTn-TE55WwRGFWAhWMpsWDkEbp5Aew2M3gBQ&usqp=CAU"
    },
    {
        "id": 20,
        "Name": "Paris",
        "cityBeach": "City",
        "Country": "France",
        "Continent": "Europe",
        "Img": "https://pix10.agoda.net/geo/city/15470/1_15470_02.jpg?ca=6&ce=1&s=1920x822"        
    },
    {
        "id": 21,
        "Name": "Positano",
        "cityBeach": "Beach",
        "Country": "Italy",
        "Continent": "Europe",
        "Img": "https://media.tacdn.com/media/attractions-splice-spp-674x446/0b/3c/40/d0.jpg"
    },
    {
        "id": 22,
        "Name": "Mombasa",
        "cityBeach": "Beach",
        "Country": "Kenya",
        "Continent": "Africa",
        "Img": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/ff/d4/cb/mbabamb-3-largejpg.jpg?w=600&h=400&s=1"        
    },
    {
        "id": 23,
        "Name": "Rabat",
        "cityBeach": "Beach",
        "Country": "Morocco",
        "Continent": "Africa",
        "Img": "https://www.isdb.org/sites/default/files/styles/hero/public/image1.jpg?itok=TaECZ3uS"
    },
    {
        "id": 24,
        "Name": "Goa",
        "cityBeach": "Beach",
        "Country": "India",
        "Continent": "Asia",
        "Img": "https://www.planetware.com/wpimages/2020/06/india-goa-best-beaches-colva-beach.jpg"        
    },
    {
        "id": 25,
        "Name": "Sentosa Island",
        "cityBeach": "Beach",
        "Country": "Singapore",
        "Continent": "Asia",
        "Img": "https://www.sentosa.com.sg/-/media/sentosa/article-listing/articles/2020/swimming-in-sentosa/swimmmingatsentosamain.jpg?revision=88869462-b375-48a5-91a7-07147f804532"        
    },
    {
        "id": 26,
        "Name": "Kuala Lumpur",
        "cityBeach": "City",
        "Country": "Malaysia",
        "Continent": "Asia",
        "Img": "https://static.independent.co.uk/s3fs-public/thumbnails/image/2018/08/21/15/kuala-lumpur.jpg?quality=75&width=1200&auto=webp"
    },
    {
        "id": 27,
        "Name": "Tokyo",
        "cityBeach": "City",
        "Country": "Japan",
        "Continent": "Asia",
        "Img": "https://rimage.gnst.jp/livejapan.com/public/article/detail/a/00/02/a0002533/img/basic/a0002533_main.jpg?20210122155600&q=80&rw=750&rh=536"
    },
    {
        "id": 28,
        "Name": "Ishigaki",
        "cityBeach": "Beach",
        "Country": "Japan",
        "Continent": "Asia",
        "Img": "https://visitokinawajapan.com/wp-content/uploads/2021/11/de103_kv_ishigaki-island-scenery.jpg"
    },
    {
        "id": 29,
        "Name": "Sanya",
        "cityBeach": "Beach",
        "Country": "China",
        "Continent": "Asia",
        "Img": "https://rccl-h.assetsadobe.com/is/image/content/dam/royal/data/ports/sanya-china/overview/sanya-china-beach.jpg?$750x320$"
    },
    {
        "id": 30,
        "Name": "Patong",
        "cityBeach": "Beach",
        "Country": "Thailand",
        "Continent": "Asia",
        "Img": "https://a.cdn-hotels.com/gdcs/production2/d1117/295d586d-6a84-415f-8551-0eb1deb169ba.jpg?impolicy=fcrop&w=800&h=533&q=medium"
    },
    {
        "id": 31,
        "Name": "Miami Beach",
        "cityBeach": "Beach",
        "Country": "United States",
        "Continent": "North America",
        "Img": "http://wikireviews.com/blog/wp-content/uploads/2015/03/Top-10-Beaches-in-North-America.jpg"
    },
    {
        "id": 32,
        "Name": "Tulum Beach",
        "cityBeach": "Beach",
        "Country": "Mexico",
        "Continent": "North America",
        "Img": "https://www.worlds50beaches.com/wp-content/uploads/2018/11/header-top100-beach5-580x276.jpg"
    },
    {
        "id": 33,
        "Name": "Cannon Beach",
        "cityBeach": "Beach",
        "Country": "United States",
        "Continent": "North America",
        "Img": "https://www.worlds50beaches.com/wp-content/uploads/2018/10/header-north-america-beach11-580x276.jpg"
    },
    {
        "id": 34,
        "Name": "Green Sand Beach",
        "cityBeach": "Beach",
        "Country": "United States",
        "Continent": "North America",
        "Img": "https://www.worlds50beaches.com/wp-content/uploads/2018/10/header-north-america-beach12-580x276.jpg"
    },
    {
        "id": 35,
        "Name": "Cape Town",
        "cityBeach": "City",
        "Country": "South Africa",
        "Continent": "Africa",
        "Img": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/10/2e/1e/cape-town.jpg?w=700&h=-1&s=1"
    },
    {
        "id": 36,
        "Name": "Nairobi",
        "cityBeach": "City",
        "Country": "Kenya",
        "Continent": "Africa",
        "Img": "https://content.r9cdn.net/rimg/dimg/c6/b2/7e865843-city-26243-164a4a25d83.jpg?width=1366&height=768&xhint=3968&yhint=1450&crop=true"
    },
    {
        "id": 37,
        "Name": "Rio de Janeiro",
        "cityBeach": "City",
        "Country": "Brazil",
        "Continent": "South America",
        "Img": "https://media.tacdn.com/media/attractions-splice-spp-674x446/06/6f/5f/fa.jpg"
    },
    {
        "id": 38,
        "Name": "S??o Paulo",
        "cityBeach": "City",
        "Country": "Brazil",
        "Continent": "South America",
        "Img": "https://cdn.britannica.com/54/101754-050-3FA9B4A0/Downtown-Sao-Paulo.jpg"
    },
    {
        "id": 39,
        "Name": "Ica",
        "cityBeach": "Beach",
        "Country": "Peru",
        "Continent": "South America",
        "Img": "https://img.theculturetrip.com/768x/smart/wp-content/uploads/2021/02/2atcn88.jpg"
    },
    {
        "id": 40,
        "Name": "Valpara??so",
        "cityBeach": "Beach",
        "Country": "Chile",
        "Continent": "South America",
        "Img": "https://img.theculturetrip.com/768x/smart/wp-content/uploads/2021/02/r28370.jpg"
    },
    {
        "id": 41,
        "Name": "Concha",
        "cityBeach": "Beach",
        "Country": "Colombia",
        "Continent": "South America",
        "Img": "https://img.theculturetrip.com/768x/smart/wp-content/uploads/2021/02/c3ty28.jpg"
    },
]

# Function to get all locations
def index(req):
    return [location for location in locations], 200

# Function to show all names
def show_names(req):
    return list(dict.fromkeys([location["Name"] for location in locations])), 200

# Function to show all countries
def show_countries(req):
    return list(dict.fromkeys([location["Country"] for location in locations])), 200

# Function to show all continents
def show_continents(req):
    return list(dict.fromkeys([location["Continent"] for location in locations])), 200

# Functions to find locations by id
def show_by_id(req, uid):
    return find_by_uid(uid), 200

def find_by_uid(uid):
    try:
        return next(location for location in locations if location['id'] == uid)
    except:
        raise BadRequest(f"Can't find the location with {uid}")

# Functions to find locations by name
def show_by_name(req, Name):
    return find_by_name(Name), 200

def find_by_name(Name):
    try:
        return next( location['Name'] for location in locations if location['Name'] == Name)
    except:
        raise BadRequest(f"Can't find the location by name {Name}")


# Functions to show locations by country
def show_by_country(req, Country):
    return find_by_country(Country), 200

def find_by_country(Country):
    try:
        return next( location for location in locations if location['Country'] == Country)
    except:
        raise BadRequest(f"Can't find the location by country {Country}")
