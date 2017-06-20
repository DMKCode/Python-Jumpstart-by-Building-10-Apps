import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond, temp, scale, loc')

def main():
    # print the header
    print_the_header()

    # get city, country from user
    city_country = get_city_country()

    # get html from the web
    html = get_html(city_country)

    # get weather from html
    report = get_weather_from_html(html)

    # display the forecast
    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))

def print_the_header():
    print('----------------------------------------------')
    print('            WEATHER CLIENT APP')
    print('----------------------------------------------')

def get_city_country():
    city_country = input('Please enter the city and country (e.g. london, united kingdom): ')
    return city_country

def get_html(city_country):
    url = 'https://www.wunderground.com/cgi-bin/findweather/getForecast?query={}'.format(city_country)
    response = requests.get(url)

    #print(response.status_code)
    #print(response.text[0:250])

    return response.text

def get_weather_from_html(html : str):

    # cityCss = 'div#location h1'
    # weatherConditionCss = 'div#curCond span.wx-value'
    # weatherTempCss = 'div#curTemp span.wx-data span.wx-value'
    # weatherScaleCss = 'div#curTemp span.wx-data span.wx-unit'
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(id='location').find('h1').get_text()
    condition = soup.find(id='curCond').find(class_='wx-value').get_text()
    temp = soup.find(id='curTemp').find(class_='wx-value').get_text()
    scale = soup.find(id='curTemp').find(class_='wx-unit').get_text()

    loc = cleanup_string(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_string(condition)
    temp = cleanup_string(temp)
    scale = cleanup_string(scale)

    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report

def cleanup_string(text: str):
    if not text:
        return text

    text = text.strip()
    return text

def find_city_and_state_from_location(loc: str):
    parts = loc.split('\n')
    return parts[0].strip()

if __name__ == "__main__":
    main()

