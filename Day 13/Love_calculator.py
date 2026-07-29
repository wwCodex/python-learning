def calculate_love_score(name1, name2):
    n=0
    m=0
    o=0
    p=0
    for letter in name1.lower():
        for char in "true":
            if char==letter:
                n+=1
    for letter in name2.lower():
        for char in "true":
            if char==letter:
                m+=1
    score1=str(m+n)
    for letter in name1.lower():
        for char in "love":
            if char==letter:
                o+=1
    for letter in name2.lower():
        for char in "love":
            if char==letter:
                p+=1
                
    score2=str(p+o)
    final_score=score1+score2
    print(f"Love score: {final_score}")
    

calculate_love_score(input("What is the first person's name? "), input("What is the second person's name? "))