def solution(today, terms, privacies):    
    today_y = int(today[0:4])
    today_m = int(today[5:7])
    today_d = int(today[8:10])

    term_type = {}
    for i in range(len(terms)):
        term_type[terms[i][0]]=int(terms[i][2:])
        
    answer = []
    for i in range(len(privacies)):
        year = int(privacies[i][0:4])
        month = int(privacies[i][5:7])
        date = int(privacies[i][8:10])
        month += term_type[privacies[i][11]]
        date -= 1
        if date == 0:
            month -= 1
            date = 28
        if month > 12:
            if month%12 == 0:
                year += (month//12-1)
                month = 12
            else:
                year += (month//12)
                month %= 12            
        if today_y > year or (today_y == year and today_m > month) or (today_y == year and today_m == month and today_d > date):
            answer.append(i+1)

    return answer