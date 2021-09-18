import re


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

def getLabel(Input,labelName):
    label = (lambda s: re.findall(r'-{}=(.*)'.format(labelName),s))(Input)
    if label:
        return label[0]
    return None
