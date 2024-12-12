

def get_words(text):
    buftext=text
    buftext=buftext.replace("\n", " ")
    buftext=buftext.replace(",", " ").replace(".", " ").replace("?", " ").replace("!", " ")
    buftext=buftext.lower()
    words=buftext.split()
    words.sort()
    return words

def get_words_dict(words):
    words_dict=dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict

def get_word_value(words):
    bufwords=words
    buforwords = bufwords.replace("\n", " ")
    bufwords = bufwords.replace(",", " ")
    bufwords_splitt=bufwords.split(".")
    sum_all=0
    for c in bufwords_splitt:
        buf_str=c
        sum=0
        for n in buf_str:
            if n==" ":
                sum=sum+1
        if sum!=0:
            sum_all=sum_all+sum+1
    n=len(bufwords_splitt)-1
    return sum_all/n

def get_median_words(words):
    buf_text = words
    buf_text = buf_text.replace("\n", " ")
    buf_text = buf_text.replace(",", " ")
    buf_text = buf_text.lower()
    buf_words_splitt = buf_text.split(".")
    for n in buf_words_splitt:
        words_dict = dict()
        words_sortt=n.split()
        for c in words_sortt:
            if c in words_dict:
                words_dict[c] = words_dict[c] + 1
            else:
                words_dict[c] = 1
        sum=0
        for c in words_dict:
            sum=sum+words_dict[c]
            num=len(words_dict)
            i=1
        if sum != 0:
            print(F"Median-{sum / num}")

def get_gramma(K,N,words):
    buf_text = words
    buf_text = buf_text.replace("\n", "")
    buf_text = buf_text.replace(",", "").replace(".", "").replace(" ","")
    buf_text = buf_text.lower()
    #print(buf_text)
    gramma_dict = dict()
    i=0
    for n in buf_text:
        buf=buf_text[i:i+N]
        if buf in gramma_dict:
            gramma_dict[buf] = gramma_dict[buf] + 1
        else:
            gramma_dict[buf] = 1
        i=i+1
    num=0
    while num<K:
        buf = 0
        buf_name = ""
        for n in gramma_dict:
            if buf < gramma_dict[n]:
                buf = gramma_dict[n]
                buf_name = n
        print(f"{buf_name} : {buf}")
        del gramma_dict[buf_name]
        num+=1
def main():
    text=input("Write the text ")
    words = get_words(text)
    words_dict=get_words_dict(words)
    for word in words_dict:
        print(word.ljust(20), words_dict[word])
    words_avg=get_word_value(text)
    print(F"AVG-{words_avg}")
    get_median_words(text)
    K = int(input("Write K"))
    N = int(input("Write N"))
    get_gramma(K,N,text)

if __name__ == "__main__":
    main()


    #Hello,my dear friend,best.I love you hello,i my love.I have lock write hello.