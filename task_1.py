book_profile ={
    "title": "Основи програмування",
    "author": "Іван Петренко",
    "year": 2023,
    "publisher_info":{
        "name": "Наукова думка",
        "city": "Киів"
    }
}
print(book_profile["title"], book_profile["author"])
print(book_profile["publisher_info"]["name"])
print("Книга '",book_profile["title"],"' автора",book_profile["author"],"УБла видана у місті", book_profile["publisher_info"]["city"])
if book_profile.get("year")!= None :
    print(book_profile["year"])
else:
    print("Рік видання невідомий")