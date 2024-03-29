c(1,2,4,8)
c(1, 'red', 2, 1,'blue')

list(c(3,13,4),c('red', 'blue','red','green'))

list2 <- list(1:5, list, head(iris))
list2

list3 <- list(A=1:5, B=LETTERS, Sport=c('Hockey', 'Lacrosse', 'Curling'))
list3

# 2nd element, access the object instead of list list3[2]
list3[[2]]
list3[['B']]
list3$B
list3[2]

class(list3[[2]])
class(list3[2])

list4 <- list(A=1:100, B=17, C=c(3,1,8,12), D=10:-5)
sum(list4[[1]])
sum(list4[[3]])

library(purrr)

# sum up each function indidually
map(list4, sum)
list4 %>%  map(sum)

list4 %>% map(length)
list4 %>%  map(sum) %>% class() 

list4 %>% map_dbl(sum)
list4 %>% map_dbl(sum) %>% is_vector()
# is Vector is True if map_dbl(), False if map()
list4 %>% map_dbl(sum) %>% mean()

list4 %>%  map(class)
list4 %>% map_chr(class)
list4 %>% map_if(is.integer, mean)
list4 %>% map_if(negate(is.integer), mean)

NA

simple <- c(1, NA, 3, 4)
mean(simple)
simple %>% 
    mean(na.rm=TRUE)
