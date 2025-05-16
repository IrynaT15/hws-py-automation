import xml.etree.ElementTree as ET


class GoodsXML:

    def __init__(self, file_name):
        self.file_name = file_name
        self.data = ET.Element("Goods")

    def add_items(self, item_id, title, price, number):
        item = ET.SubElement(self.data, item_id)
        item.set("title", title)
        item.set("price", str(price))
        item.set("number", str(number))

    def save_to_xml(self):
        b_xml = ET.tostring(self.data)
        with open(self.file_name, "wb") as f:
            f.write(b_xml)


def total_price_of_goods_from_xml(file_name, price_att, number_att):
    tree = ET.parse(file_name)
    root = tree.getroot()

    total_cost = 0

    for item in root:
        price = float(item.attrib[price_att])
        number = int(item.attrib[number_att])
        total_cost += price * number

    return f"Total cost of all items: {total_cost}"


goods_xml = GoodsXML("goods.xml")

goods_xml.add_items("Item1", "Coffee 'Coffee'", 17.49, 5)
goods_xml.add_items("Item2", "Tea 'Tea'", 7.12, 15)
goods_xml.add_items("Item3", "Juice 'Juice'", 5.00, 13)
goods_xml.add_items("Item4", "Milk 'Milk'", 4.60, 20)
goods_xml.add_items("Item5", "Water 'Water'", 2.30, 50)

goods_xml.save_to_xml()

print(total_price_of_goods_from_xml("goods.xml", "price", "number"))
