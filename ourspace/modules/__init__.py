



# list to string for displaying all options to discord.
def ListToString(lists):
    new_list = []
    n = 0
    for name in lists:
        new_list.append(f'{n}. {name}')
        n += 1

    output = """```
{}
```""".format('\n'.join(new_list))
    return output
