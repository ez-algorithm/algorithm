def solution(s):
    
    answer = ''
    
    words = s.split(' ')
    
    for i in range(len(words)):
        words[i] = words[i].capitalize()
        
    answer = ' '.join(words)
    
    return answer

def main():
    s = "3people unFollowed me"
    print(solution(s))

if __name__ == "__main__":
    main()