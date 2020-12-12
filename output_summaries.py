import collections

filename = 'output.txt'

with open(filename,'r') as file:
    id_list =[]
    missing_ids = []
    for lines in file:
        ids = int(lines[0:3])
        id_list.append(ids)
        id_list.sort()
    for id in range(1,501):
        if id not in id_list:
            missing_ids.append(id)
    
    print(f"\nSuccessful match IDs: {id_list}\n") 
    print(f"Duplicate lines: {[item for item, count in collections.Counter(id_list).items() if count > 1]}\n") 
    print(f"Missing IDs: {missing_ids}")
        
        
