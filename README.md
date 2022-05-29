# Book Recommender System: [[WebApp link]](https://share.streamlit.io/luke-chugh/book-recommender-webapp/main/app.py)
Book Recommendation Using **Word2vec algorithm**

Content-based and Collaborative based are the two popular recommendation systems. This project is content based recommender system where user has to select one book title from a list of 4000 books, then recommender system lists top 5 similar books based on the description or features.

# Below are the screenshots of my WebApp:

![Capture](https://github.com/luke-chugh/Book-Recommender-WebApp/blob/main/screenshots/1.png)

![Capture1](https://github.com/luke-chugh/Book-Recommender-WebApp/blob/main/screenshots/2.png)

![Capture2](https://github.com/luke-chugh/Book-Recommender-WebApp/blob/main/screenshots/3.png)

# About this project:

This project, I have used goodreads scraped dataset which contains around 4000 book titles, author name and description of each book and author.

After text preprocessing, the main thing is to convert each book descriptions into numerical vectors. For this we have used 3 method such as **Bag-of-words model, TF-IDF model, Word2vec algorithm**. From the above method, Word2vec model was an best one.

Word2vec is an neural network model uses **semantic meaning of words**. Word2vec understand the semantic meaning of each words in the book description feature very well than the other two models such as bag of words and tf-idf. 

Training word2vec algorithm from scratch is an computationally expensive and also need humonguous data. As i have less data, so i have used **Google pretrained word2vec neural network** for this project. 

So, Convert the book descriptions into a numeric vector and find the similarity between these vectors to recommend the book. I have used **euclidean distance** for finding similarity..

# Installation
To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```
# Author
[Luke Chugh](https://www.linkedin.com/in/luke-chugh-2b2043181/)
