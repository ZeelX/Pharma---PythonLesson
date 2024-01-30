from bs4 import BeautifulSoup
import Cheese
import ConnexionETL


class CheeseController:

    def transform(self, data_from_connexion):
        """
        see it later.
        """

        cheese_names = []
        cheese_familys = []
        cheese_doughs = []
        cheese_prices = []
        cheese_imgs = []
        cheese_descriptions = []

        soup = BeautifulSoup(data_from_connexion, 'html.parser')
        cheese_array = soup.find('table')

        for row in cheese_array.find_all('tr'):
            columns = row.find_all('td')

            if columns[0].text.strip() == "Fromage":
                continue

            if columns:
                cheese_name = columns[0].text.strip()
                cheese_family = columns[1].text.strip()
                cheese_dough = columns[2].text.strip()

                # region Evolution
                anchor = columns[0].find('a')
                if anchor:
                    href = anchor.get('href')
                    full_url = "https://www.laboitedufromager.com/" + href
                    new_connexion = ConnexionETL.ConnexionETL(full_url)
                    more_data = new_connexion.extract_data()
                    more_soup = BeautifulSoup(more_data, 'html.parser')

                    # Image
                    img = more_soup.find('div', class_='woocommerce-product-gallery__image')
                    a_tags = img.find('a')
                    img_tag = a_tags['href']
                    cheese_imgs.append(img_tag)

                    # Description
                    ugly_description = more_soup.find('div', class_='woocommerce-product-details__short-description')
                    data_desc = ugly_description.get_text()
                    almost_cleaned_data = [element.replace('\n', '').replace('\xa0', '') for element in data_desc]
                    cleaned_data = ''.join(almost_cleaned_data)
                    cheese_descriptions.append(cleaned_data)

                    # Price
                    ugly_price = more_soup.find('p', class_='price')
                    cheese_prices.append(ugly_price.get_text())

                    # Nombre d'avis
                    rev = more_soup.find('div', class_='woocommerce-product-rating')
                    rev.find('span', class_='rating')

                    print(f'nb avis ={rev.find('span', class_='rating').get_text()}')
                    print(f'moyenne = {rev.find('strong', class_='rating').get_text()}')


                else:
                    cheese_prices.append('No cheese data')
                    cheese_imgs.append('No cheese data')
                    cheese_descriptions.append('No cheese data')
                # # endregion

                # # Ignore les lignes vides
                if cheese_name != '' and cheese_family != '' and cheese_dough != '':
                    cheese_names.append(cheese_name)
                    cheese_familys.append(cheese_family)
                    cheese_doughs.append(cheese_dough)

        for i in range(len(cheese_names)):
            new_cheese = Cheese.Cheese(cheese_names[i],
                                       cheese_familys[i],
                                       cheese_doughs[i],
                                       cheese_prices[i],
                                       cheese_imgs[i],
                                       cheese_descriptions[i])
            new_cheese.load()
