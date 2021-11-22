try:
    d1={"happy":"elated",
        "sad":"dejected",
        "sorry":"apologize",
        "nervous":"anxitey"}

    d2=input("enter a word")
    print(d1[d2])

except Exception as e:
    print(e)
