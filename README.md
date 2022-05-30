# Book Recommender System: [[WebApp link]](https://share.streamlit.io/luke-chugh/book-recommender-webapp/main/app.py)
Book Recommendation using **Word2vec + Euclidean distance**

Content-based and Collaborative based are the two popular recommendation systems. This project is content based recommender system where user has to select one book title from a list of 4000 books, then recommender system lists top 5 similar books based on the description or features.

# Below are the screenshots of this WebApp:

![Capture](https://github.com/luke-chugh/Book-Recommender-WebApp/blob/main/screenshots/1.png)

![Capture1](https://github.com/luke-chugh/Book-Recommender-WebApp/blob/main/screenshots/2.png)

![Capture2](https://github.com/luke-chugh/Book-Recommender-WebApp/blob/main/screenshots/3.png)

# About this project:

This project utilized goodreads scraped [dataset](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks) which contains around 4000 book titles, author name and description of each book and author.

The main task was to convert each book's description into numerical vectors. For this, processing techniques such as **Bag-of-words model, TF-IDF model and Word2vec algorithm** were used. **Word2vec** (neural network based) model which uses **semantic meaning of words** proved out to be the best one for this use case.

Training word2vec algorithm from scratch is computationally expensive and also needs humonguous data. Since this dataset was not big enough, **Google's pretrained word2vec neural network** was implemented for this project. 

After converting the book descriptions into numeric vectors I used **euclidean distance** for finding similarity. The top 5 books whos description had the closest euclidean distance with the book selected by the user on the WebApp was shown as recommendations.

# Installation:
To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```
To run this app in your local machine open a command prompt or terminal in the cloned directory and run:
```bash
streamlit run app.py
```
# Author:
[Luke Chugh](https://www.linkedin.com/in/luke-chugh-2b2043181/)
