from copy import deepcopy
import json

def create_routes(items_info):
    rotas = []

    for itemKey in items_info:
        item = items_info[itemKey]

        if item['type'] == 'PollingConsumer' or item['type'] == "Message":
            rotas.append(generate_code(items_info, itemKey, "", []))

    return rotas

def generate_code(items_info, current_node_number="0", generated_code="", visited_nodes=[]):
    print(current_node_number)
    if current_node_number not in visited_nodes:
        current_node = items_info[str(current_node_number)]
        
        new_visited_nodes = deepcopy(visited_nodes)
        new_visited_nodes.append(current_node_number)
        print("visited nodes", visited_nodes)
        print("generated_code", generated_code)

        if current_node['type'] == 'PollingConsumer' or current_node['type'] == "Message":
            new_generated_code = f"from(\"{current_node['protocol'][1]}:{current_node['url']}\")"

            for child_node_number in current_node['connectsTo']:
                return new_generated_code + generate_code(items_info, child_node_number, generated_code, new_visited_nodes)

        if current_node['type'] == "ContentBasedRouter":

            choices = []            
            for [child_node_number, choice] in current_node['choices']:
                choices.append(f".when(\"{choice}\")" + generate_code(items_info,
                                                                  child_node_number, generated_code, new_visited_nodes))
            
            return generated_code + ".choice()" + "".join(choices) + ".end()"

        if current_node['type'] == 'MessageFilter':
            new_generated_code = ".filter()"

            for child_node_number in current_node['connectsTo']:
                return generated_code + new_generated_code + generate_code(items_info, child_node_number, generated_code, new_visited_nodes)

        if current_node['type'] == "MessageEndpoint":
            new_generated_code = f".to(\"{current_node['protocol'][1]}:{current_node['url']}\")"

            return generated_code + new_generated_code

        return generated_code

