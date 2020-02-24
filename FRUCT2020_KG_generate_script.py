import xml.etree.ElementTree as xml
import random
from random import randrange
from datetime import datetime
from datetime import timedelta

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('2/1/2020 12:00 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('2/2/2020 12:00 AM', '%m/%d/%Y %I:%M %p')

#print(random_date(d1, d2))

Max_Hubs = 3
Max_Devices = 1000
Max_Users = 1000
Max_Actions = 50000


def createXML(filename):
    """
    Создаем XML файл.
    """
# Add header
    header = str("<?xml version='1.0' encoding='UTF-8'?>\n<rdf:RDF\nxmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'\nxmlns:vCard='http://www.w3.org/2001/vcard-rdf/3.0#'\nxmlns:my='http://127.0.0.1/bg/ont/test1#'\n>")
#    print(header)

# Add Hubs definitions
    f = open(filename, "wt")
    f.write(header)
    f.write("\n<!--Hubs definitions-->\n")
    f.close()

    i=1
    while i <= Max_Hubs:
        body = str("<rdf:Description rdf:about='http://127.0.0.1/Hub_") + str(i) + str("/'>\n<my:has_id>H") + str (i) + str("</my:has_id>\n</rdf:Description>\n")
        f = open(filename, "at")
        f.write(body)
        f.close()
        i=i+1


# Add Device models definitions
    f = open(filename, "at")
    f.write("\n<!--Device models definitions-->\n")
    f.close()

    i=1
    for j in ('Moto2k','Cisco3260','ArrisWB11','ArrisWB20'):
        body = str("<rdf:Description rdf:about='http://127.0.0.1/Device_model_") + str(i) + str("/'>\n<my:has_id>") + str (j) + str("</my:has_id>\n</rdf:Description>\n")
        f = open(filename, "at")
        f.write(body)
        f.close()
        i=i+1


# Add Device  definitions
    f = open(filename, "at")
    f.write("\n<!--Device definitions-->\n")
    f.close()

    i=1
    j = ['Moto2k','Cisco3260','ArrisWB11','ArrisWB20']
    while i <= Max_Devices:
        body = str("<rdf:Description rdf:about='http://127.0.0.1/Device_") + str(i) + str("/'>\n<my:has_id>D") + str (i) + str("</my:has_id>\n<my:is_connected_to_hub>H") + str(random.randint(1, Max_Hubs)) + str("</my:is_connected_to_hub>\n<my:has_the_device_model>") + str(random.choice(j)) + str("</my:has_the_device_model>\n</rdf:Description>\n")
        f = open(filename, "at")
        f.write(body)
        f.close()
        i=i+1

# Add Users  definitions
    f = open(filename, "at")
    f.write("\n<!--Users definitions-->\n")
    f.close()

    i = 1
    while i <= Max_Users:
        body = str("<rdf:Description rdf:about='http://127.0.0.1/User_") + str(i) + str("/'>\n<my:has_id>U") + str(i) + str("</my:has_id>\n<my:uses_device>D") + str(i) + str("</my:uses_device>\n</rdf:Description>\n")
        f = open(filename, "at")
        f.write(body)
        f.close()
        i = i + 1


# Add tariffs definitions
    f = open(filename, "at")
    f.write("\n<!--Tariffs definitions-->\n")
    f.close()

    i = 1
    for j in ('Promo', 'Basic', 'Advance', 'Advance+', 'Profi'):
        body = str("<rdf:Description rdf:about='http://127.0.0.1/Tariff_") + str(i) + str("/'>\n<my:has_id>") + str(j) + str("</my:has_id>\n</rdf:Description>\n")
        f = open(filename, "at")
        f.write(body)
        f.close()
        i = i + 1

 # Add Accounts  definitions
    f = open(filename, "at")
    f.write("\n<!--Accounts definitions-->\n")
    f.close()

    i = 1
    j = ['Promo', 'Basic', 'Advance', 'Advance+', 'Profi']
    while i <= Max_Users:
        body = str("<rdf:Description rdf:about='http://127.0.0.1/Account_") + str(i) + str("/'>\n<my:has_id>A") + str(i) + str("</my:has_id>\n<my:has_tariff_plan>") + str(random.choice(j)) + str("</my:has_tariff_plan>\n<my:includes_user>U") + str(i) + str("</my:includes_user>\n</rdf:Description>\n")
        f = open(filename, "at")
        f.write(body)
        f.close()
        i = i + 1

# Add Services definitions
    f = open(filename, "at")
    f.write("\n<!--Services definitions-->\n")
    f.close()

    i = 1
    for j in ('WatchTV', 'VOD', 'nPVR', 'PPV'):
        body = str("<rdf:Description rdf:about='http://127.0.0.1/Service_") + str(i) + str("/'>\n<my:has_id>") + str(j) + str("</my:has_id>\n</rdf:Description>\n")
        f = open(filename, "at")
        f.write(body)
        f.close()
        i = i + 1

# Add Assets definitions
    f = open(filename, "at")
    f.write("\n<!--Assets definitions-->\n")
    f.close()

    i = 1
    for j in ('Football World Championship 2020', 'CNN daily news 07:00 PM', 'Animal planet review with Nancy Gram', 'MTV weekly rating'):
        body = str("<rdf:Description rdf:about='http://127.0.0.1/Asset_") + str(i) + str("/'>\n<my:has_id>Asset") + str(i) + str("</my:has_id>\n<my:has_description>") + str(j) + str("</my:has_description>\n</rdf:Description>\n")
        f = open(filename, "at")
        f.write(body)
        f.close()
        i = i + 1

# Add Users actions  definitions
    f = open(filename, "at")
    f.write("\n<!--Users actions definitions-->\n")
    f.close()

    i = 1
    j = ['WatchTV', 'VOD', 'nPVR', 'PPV']
    while i <= Max_Actions:
        body = str("\n<rdf:Description rdf:about='http://127.0.0.1/User_") + str(random.randint(1, Max_Users)) + str("/'>\n<my:requests>\n<rdf:Description rdf:about='http://127.0.0.1/Request_") + str(i) + str("/'>\n<rdf:property rdf:datatype='http://www.w3.org/2001/XMLSchema#datetime'>") + str(random_date(d1, d2)) + str("</rdf:property>\n<my:request_detailes>\n<rdf:Description>\n<rdf:type>:statement</rdf:type>\n<rdf:predicat>:is_requested_with</rdf:predicat>\n<rdf:subject>") + str(random.choice(j)) + str("</rdf:subject>\n<rdf:object>\n<rdf:Description rdf:about='http://127.0.0.1/Asset_") + str(random.randint(1,4)) + str("/'>\n</rdf:Description>\n</rdf:object>\n</rdf:Description>\n</my:request_detailes>\n</rdf:Description>\n</my:requests>\n</rdf:Description>\n")
        f = open(filename, "at")
        f.write(body)
        f.close()
        i = i + 1

    f = open(filename, "at")
    f.write("\n</rdf:RDF>\n")
    f.close()

if __name__ == "__main__":
    createXML("KG_telecom.xml")
