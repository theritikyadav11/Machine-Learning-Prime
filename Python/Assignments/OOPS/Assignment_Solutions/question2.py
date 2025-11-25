class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)
        print("Review added successfully.")

    def review_count(self):
        return len(self.reviews)

    def display_reviews(self):
        if not self.reviews:
            print("No reviews yet.")
        else:
            for review in self.reviews:
                print(review)


b1 = Book("Python", "Apna College")
b1.add_review("Nice book")
print(b1.review_count())

b1.add_review("Nice Explanations")
b1.display_reviews()
