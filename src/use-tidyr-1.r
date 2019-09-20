library(tidyr)
install.packages("tidyr")

# readr
# purrr
# tidyr
# dplyr

reaction <- readr::read_tsv('data/reaction.txt')

# flat into long form
reaction %>% gather(key=Stat, value=Data,
                    Age, BMI, React, Regulate) %>% 
    dplyr::arrange(ID, Test) %>% 
    head(20)

reactionlong <-  reaction %>% 
    gather(key=Stat, value=Data,
                                     
           Age, BMI, React, Regulate)

reactionlong %>% 
    spread(key=Stat, value=Data)

coefplot::invlogit(-6:6)
useful::MapToInterval(num=-6:6,start=0, stop=1)

# combine columns
reaction %>% 
    unite(col=Indentifier, ID, Test, sep='_')

# uncombine
reaction %>% 
    unite(col=Indentifier, ID, Test, sep='_') %>% 
    separate(clo=Indentifier, into=c('ID','TestNum'), sep="_")

