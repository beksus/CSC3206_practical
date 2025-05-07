def main():
    
    print(filterFriend("James", "", ""))


def filterFriend(name = "", home_country = "", home_state = ""):
    friends = [["James", "Malaysia", "Malacca"], ["Goh", "Australia", "Brisbane"], ["Don", "Malaysia", "Pahang"]]
    result = []
    
    for filtered in friends:
        friend_name, friend_country, friend_state = filtered
        
        if (name == "" or friend_name == name) and \
           (home_country == "" or friend_country == home_country) and \
           (home_state == "" or friend_state == home_state):
            result.append(filtered)
    
    return result

main()