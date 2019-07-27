'''
import json
import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(todos)
'''
import json

data = {}
data['steps'] = []

data['steps'].append({
    'Type': 'Begin'
})

data['steps'].append({
    'Type': 'Pause',
    'Time': '1200000'
})

data['steps'].append({
    'Type': 'Charge',
    'Time': '1200000',
    'Current': '20.0'
})

data['steps'].append({
    'Type': 'Pause',
    'Time': '60000'
})

data['steps'].append({
    'Type': 'End'
})


def remove_char(input_string, index):
    first_part = input_string[:index]
    second_part = input_string[index+1:]
    return first_part + second_part

def prepare_toSend(dataOrig):

    #print(dataOrig)
    data2 = str(dataOrig).replace("{\"steps\": ", '')
    #print(data2)
    value_index = len(data2)-1
    data3 = remove_char(data2, value_index)
    #print(data3)
    return data3


with open('program1.json', 'w') as outfile:
    json.dump(data, outfile)

f= open("program1.json","r")
contents = f.read()
f.close()

print(prepare_toSend(contents))


