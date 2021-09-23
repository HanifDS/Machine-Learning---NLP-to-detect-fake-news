# Machine-Learning---NLP-to-detect-fake-news
Machine learning: Natural language Processing to detect fake news

This was a machine learning project where I used natural language processing to help detect Fake news. I sourced the dataset from the popular kaggle source (https://www.kaggle.com/c/fake-news/data)

Overall the dataset was very balanced and quite substansive. The model achieved a 91% accuracy rate. I then, using streamlit deployed the model in order to test it on headlines.

The model overal worked very well however it had a bias in that, I beleive, many of the labels for "real news" on the dataset were largely from the New York Times. As a result of this, news that was attributed to the New York Times in the text would be more likely than not labelled as true news even if they were in some cases blatantly not.

Going forward, I'd love to scrape my own data in the future with a broader diversity, and not so heavily leaning on certain publications (NYT), to see how the model performs on broader, more diverse, data.

A lot of fun.
