


def timeConversion(s):
    

    if not s:
        return
    else:

        result = s.replace(s[8:],"")

        if s[8:] == "PM" and int(s[:2]) < 12:
            time = int(s[:2])
            time = time + 12
            result = result.replace(s[:2],str(time))
            print(result)
            return
        
        if s[8:] == "PM" and int(s[:2]) == 12:
            print(result)
            return
       
        if s[8:] == "AM" and int(s[:2]) < 12:
            print(result)
            return
        
        if s[8:] == "AM" and int(s[:2]) == 12:
            result = result.replace(s[:2],"00")
            print(result)
            return
    
    return



s = "07:05:45PM"
timeConversion(s)



            



