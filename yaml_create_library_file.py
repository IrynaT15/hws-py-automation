import yaml


def create_and_read_yaml_file_with_multiple_blocks(filename, data):
    with open(f"{filename}.yaml", "w", encoding="utf-8") as f:
        yaml.dump_all(data, f, sort_keys=False)
        print("YAML File is successfully created")

    with open(f"{filename}.yaml", "r", encoding="utf-8") as f:
        output = yaml.safe_load_all(f)
        print(list(output))


books = [
    {"title": "Don Quixote",
     "author": "Miguel de Cervantes",
     "publication_year": "2005"
     },

    {"title": "Alice's Adventures in Wonderland",
     "author": "Lewis Carroll",
     "publication_year": "2015"
     },

    {"title": "Pride and Prejudice",
     "author": "Jane Austen",
     "publication_year": "1997"
      },

    {"title": "Moby Dick",
     "author": "Herman Melville",
     "publication_year": "1986"
     },

    {"title": "Gulliver's Travels",
     "author": "Jonathan Swift",
     "publication_year": "2001"
     }
]


create_and_read_yaml_file_with_multiple_blocks("library", books)
