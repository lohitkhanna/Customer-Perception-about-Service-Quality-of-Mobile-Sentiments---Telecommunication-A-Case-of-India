library(readxl)
Comments <- read_excel("D:/Comments.xlsx")
library(sentimentr)
data <- as.vector(Comments[[1]])
# sentiment(as.vector(Comments[[1]]))
(sentiment_score <-sentiment(data))
(freq_terms <- extract_sentiment_terms(data))
# get_sentences(data)
x11()
plot(sentiment_score)
