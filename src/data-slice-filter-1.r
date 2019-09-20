library(dplyr)

# split - apply - combine

library(ggplot2)

data(diamonds, package='ggplot2')
diamonds

head(diamonds)
a <-  head(diamonds, n=4) 
a
tail(a, n=1)

diamonds %>% head(n=4) %>% tail(n=1)

# ctrl+shift+M (control captital M) for %>% piping

diamonds

# plyr function verb against noune

select(diamonds, carat, cut, price)
diamonds %>% select(carat, cut, price)
diamonds %>% filter(-price)

diamonds %>% filter(carat >1)

diamonds %>% filter(cut == 'Ideal')
diamonds %>% filter(cut == 'Ideal' & carat >1)
diamonds %>% filter( cut =='Ideal' | color == 'I')

diamonds %>% filter(cut %in% c('Ideal', 'Premium', 'Good') )
2:7
diamonds %>%  slice(2:7)
diamonds    %>%  slice(c(2,9, 14))                

diamonds %>%  mutate(price / carat)
# Nija Turtles mutate - change

diamonds %>% mutate(Ratio = price/carat)

diamonds %>% 
    mutate(Ratio = price/carat) %>% 
    mutate(Double = Ratio*2)

diamonds %>%  
    mutate(Ratio=price/carat, Double=Ratio*2)

diamonds %>% summarize(mean(price))
diamonds %>% summarize(AvgPrice=mean(price), MedianSize=median(carat))

diamonds %>% 
    group_by(cut)

diamonds %>% 
    group_by(cut, color) %>% 
    summarize(AvgPrice = mean(price), MedianSize=median(carat))

diamonds

diamonds %>%  
    filter(c(carat)>1) %>% 
    group_by(cut) %>% 
    summarize(MedPrice = median(price), AvgSize=mean(carat)) %>% 
    arrange(-MedPrice)

arrange(
    summarize(
        group_by(
            filter(
                diamonds, carat > 1
            ), cut
        ), MedPrice = median(price), AvgSize=mean(carat)
    ), -MedPrice
)

diamonds %>% 
    group_by(cut) %>% 
    summarize(n())

diamonds %>% count(cut)


