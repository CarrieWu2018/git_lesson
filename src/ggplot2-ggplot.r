library(ggplot2)
# grammer of graphics - book of it

data(diamonds, package = 'ggplot2')

ggplot(diamonds)
# blank canvas

# aesthetics
# x
# y
# color
# shape
# size

# x: carat
# y: price

ggplot(diamonds, aes(x=carat, y=price))
# haven't what to plot

ggplot(diamonds, aes(x=carat, y=price)) + geom_point()
ggplot(diamonds, aes(x=carat, y=price, color=cut)) + geom_point()
ggplot(diamonds, aes(x=carat, y=price, color=cut)) + geom_point(shape=1)
ggplot(diamonds, aes(x=carat, y=price, color=cut)) + geom_point(shape=1, size=1)
head(diamonds)
ggplot(diamonds, aes(x=carat, y=price, color=cut, shape=cut)) + geom_point(size=1)

ggplot(diamonds, aes(x=carat, y=price, color=cut, shape=cut)) +
    geom_point(size=1, shape=1) +
    scale_color_brewer(palette = 'Dark2')

ggplot(diamonds, aes(x=carat, y=price, color=cut, shape=cut)) +
    geom_point(size=1, shape=1) 
ggplot(diamonds, aes(x=carat, y=price)) +
    geom_point(size=1, shape=1, aes(color=cut)) 

ggplot(diamonds, aes(x=carat, y=price, color=cut)) +
    geom_point(size=1, shape=1) +
    geom_smooth()

ggplot(diamonds, aes(x=carat, y=price)) +
    geom_point(shape=1, size=1, aes(color=cut)) +
    geom_smooth()

ggplot(diamonds, aes(x=carat, y=price)) +
    geom_smooth()

ggplot(diamonds, aes(x=carat, y=price)) +
    geom_point(shape=1, size=1, aes(color=cut)) +
    geom_smooth(aes(color=cut)) +
    geom_smooth(color='hotpink')

ggplot(diamonds, aes(x=carat, y=price)) +
    geom_point(shape=1, size=1, aes(color=cut)) +
    geom_smooth(aes(color=cut)) +
    geom_smooth(color='hotpink') +
    facet_wrap( ~ cut )

# rm legend
ggplot(diamonds, aes(x=carat, y=price)) +
    geom_point(shape=1, size=1, aes(color=cut)) +
    geom_smooth(aes(color=cut)) +
    geom_smooth(color='hotpink') +
    facet_wrap( ~ cut ) +
    theme(legend.position = 'none')

# alpha make is opaque
ggplot(diamonds, aes(x=carat, y=price)) +
    geom_point(shape=1, size=1, aes(color=cut), alpha=1/3) +
    geom_smooth(aes(color=cut)) +
    geom_smooth(color='red') +
    facet_wrap( ~ cut ) +
    theme(legend.position = 'none')

ggplot(diamonds, aes(x=price)) + 
    geom_histogram()

ggplot(diamonds, aes(x=price, fill=cut)) + 
    geom_histogram()

ggplot(diamonds, aes(x=price, fill=cut)) + 
    geom_density(alpha= 0.3)

ggplot(diamonds, aes(x=price, fill=cut)) + 
    geom_density(alpha= 0.3) + 
    facet_wrap( ~ cut) +
    theme(legend.position = 'none')


install.packages("ggridges")
library(ggridges)

ggplot(diamonds, aes(x=price, y=cut)) +
    geom_density_ridges()

ggplot(diamonds, aes(x=price, y=cut, fill=cut)) +
    geom_density_ridges() 


library(ggthemes)
install.packages("ggthemes")
g <- ggplot( diamonds, aes(x=carat, y=price, color=cut))
g
g + geom_point()

p <- g + geom_point()
p

# like economist magazine
p + theme_economist()

p + theme_economist() + scale_color_economist()
p + theme_tufte()
p + theme_clean()
p + theme_excel_new() + scale_color_excel_new()
