import yaml


def read_and_append_yaml_data_with_multiple_blocks(filename, new_item):

    with open(f"{filename}.yaml", "r") as f:
        data = yaml.safe_load_all(f)
        loaded_data = list(data)
        loaded_data.append(new_item)

    with open(f"{filename}.yaml", "w") as f:
        yaml.dump_all(loaded_data, f)


new_book = {
    "title": "Little Women",
    "author": "Louisa May Alcott",
    "publication_year": "2011"
    }

read_and_append_yaml_data_with_multiple_blocks("library", new_book)
