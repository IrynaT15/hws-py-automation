import xml.etree.ElementTree as ET


data = ET.Element("Goods")
element1 = ET.SubElement(data, "Item1")
element1.set("title", "Coffee 'Coffee'")
element1.set("price", "17.49")
element1.set("number", "5")

element2 = ET.SubElement(data, "Item2")
element2.set("title", "Tea 'Tea'")
element2.set("price", "7.12")
element2.set("number", "15")

element3 = ET.SubElement(data, "Item3")
element3.set("title", "Juice 'Juice'")
element3.set("price", "5.00")
element3.set("number", "13")

element4 = ET.SubElement(data, "Item4")
element4.set("title", "Milk 'Milk'")
element4.set("price", "4.60")
element4.set("number", "20")

element5 = ET.SubElement(data, "Item5")
element5.set("title", "Water 'Water'")
element5.set("price", "2.30")
element5.set("number", "50")

b_xml = ET.tostring(data)

with open("goods.xml", "wb") as f:
    f.write(b_xml)


def total_price_of_goods_from_xml(file, price_att, number_att):
    tree = ET.parse(file)
    root = tree.getroot()

    total_cost = 0

    for item in root:
        price = float(item.attrib[price_att])
        number = int(item.attrib[number_att])
        total_cost += price * number

    return f"Total cost of all items: {total_cost}"


print(total_price_of_goods_from_xml("goods.xml", "price", "number"))
