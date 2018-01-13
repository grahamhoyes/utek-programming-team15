def get_count(dataset):
    """
        Input: string dataset
        Output: dictionary of counts
    """
    count_dict = {}
    
    for i in range(len(dataset)):
        n_gram = ""
        end = i + 7
        if end >= len(dataset):
            end = len(dataset)
        
        j = i        
        while j < end:
            
            if dataset[j] == " ":
                end += 1
                if end >= len(dataset):
                    end = len(dataset)
                j += 1
                continue
            else:
                n_gram += dataset[j]
            

            if not count_dict.__contains__(n_gram):
                count_dict[n_gram] = 1
            else:
                count_dict[n_gram] += 1 
            
            j += 1

    
    
    return count_dict

def parse_input(input):
    """
        Input: string
        Return: string
    """
    clean = ""
    for i in range(len(input)):
        if ord(input[i]) < 65 or ord(input[i]) > 90:
            continue
        else:
            clean += input[i]
    return clean


if  __name__ == "__main__":
    with open("../dataset.txt") as file:  
        data = file.read() 
    
    #data = "HELLO WORLD"
    
    #clean_input = parse_input("THE")

    counts = get_count(data)
    
    clean_input = "TION"
    
    print(clean_input)
    if counts.__contains__(clean_input):
        print(counts[clean_input])
    else:
        print("0")