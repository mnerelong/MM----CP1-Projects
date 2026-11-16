# MM, 1st period Programming I, Dictionaries Notes

# COLLECTION of key and value pairs. <-------
# anatomy of a dictionary

# key: value
tool = {
    "eyebrow r": "great",
    "shaving r": "not great at all",
    "kitchen k": "scary"
}
# keys must be valid data types.

print(tool["kitchen k"]) # how to get individual items.
keys = list(tool.keys())
for key in keys:
    print(f"{key}? I had one once. It was {tool[key]}.")

tool["eyebrow r"] = "lost"
tool.pop("shaving r")

# welcome to my nest
elements = {
    "Anemo": {
        "Venti": "Archon",
        "Sucrose": "Assistant Scientist",
        "Varka": "Grandmaster"
    },
    "Geo": {
        "Zhongli": "Archon",
        "Gorou": "Dog"
    },
    "Dendro": {
        "Baizhu": "Doctor",
        "Nahida": "Archon",
        "Kaveh": "Architect"
    },
    "Pyro": {
        "Gaming": "Dancer",
        "Xiangling": "Chef",
        "Mavuika": "Archon"
    },
    }

# How to print from the key "Baizhu"
print(elements["Dendro"]["Baizhu"])

# if you don't have a certain thing in your dictionary then this will just say "None"
print(elements.get("Pyro").get("Bennett"))
