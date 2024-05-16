with open("text.txt","r",encoding="utf-8") as file:
    upper=file.readline().upper()
    # print(upper)
with open("new_text.txt","w",encoding="utf-8"):
    pass
with open("new_text.txt","w", encoding="utf-8") as line:
    line.write(upper)
    
