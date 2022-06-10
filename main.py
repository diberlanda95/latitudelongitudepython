#import pycep_correios
import pandas as pd
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="test_app")
# R. Dragão do Mar, 81 - Praia de Iracema, Fortaleza - CE, 60060-390
#endereco = pycep_correios.get_address_from_cep('60060390')
dataframe = pd.read_excel('exportar.xlsx')
#dataframe2 = dataframe.copy()
dataframe.drop_duplicates(subset='BAIRRO', inplace=True)
for index, values in dataframe.iterrows():
    try: 
        if not 'SEM BAIRRO' in values['NOMEBAI'] or not 'EX' in values['UF']:
            location = geolocator.geocode(values['NOMEBAI'] + ',' + values['NOMECID'] + ',' + values['UF'])
            if not location is None:
                dataframe.at[index, 'LATITUDE'] = location.latitude
                dataframe.at[index, 'LONGITUDE'] = location.longitude
        elif  'SEM BAIRRO' in values['NOMEBAI'] and not 'SEM DESCRIÇÃO' in values ['NOMECID']:
            location = geolocator.geocode(values['NOMECID'] + ',' + values['UF'])
            if not location is None:
                dataframe.at[index, 'LATITUDE'] = location.latitude
                dataframe.at[index, 'LONGITUDE'] = location.longitude
    except Exception as e:
        print(e, values['CODPARC'])
dataframe.to_excel('coordenadas.xlsx', index=False)
    # geolocator = Nominatim(user_agent="test_app")
# location = geolocator.geocode(endereco['bairro'] + "," + endereco['cidade'] + ", " + endereco['uf'])
# print(location)
# print(location.latitude, location.longitude)