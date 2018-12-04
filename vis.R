setwd("Documents/UCU/Coffee/daily_ico/")

library(dplyr)
library(tidyverse)

df = read.csv("merged_data.csv")

col_mild = df %>%
  select(-other_milds, -brazilian_nat, -robustas, -composite_ind, -date, -X)
model = lm(columbian_milds ~ ., data=col_mild)

par(mfrow=c(2,2)) # Plot 4 plots in same screen
plot(model)

coefs <- summary(model)$coefficients
summary(model)



other_mild = df %>%
  select(-columbian_milds, -brazilian_nat, -robustas, -composite_ind, -date, -X)
model = lm(other_milds ~ ., data=other_mild)

par(mfrow=c(2,2)) # Plot 4 plots in same screen
plot(model)

coefs <- summary(model)$coefficients
summary(model)



braz_nat = df %>%
  select(-columbian_milds, -other_milds, -robustas, -composite_ind, -date, -X)
model = lm(brazilian_nat ~ ., data=braz_nat)

par(mfrow=c(2,2)) # Plot 4 plots in same screen
plot(model)

coefs <- summary(model)$coefficients
summary(model)







robusta = df %>%
  select(-columbian_milds, -other_milds, -brazilian_nat, -composite_ind, -date, 
         -X, -BRL, -COP, -CUP, -DOP, -ETB, -GHS, -HNL, -IDR, -INR, -JMD, -LRD, -MGA, 
         -MWK, -PAB, -PEN, -RWF, -SVC, -XAF, -XOF, -YER, -UGX, -ZWL, -ZMW)
model = lm(robustas ~ ., data=robusta)

par(mfrow=c(2,2)) # Plot 4 plots in same screen
plot(model)

coefs <- summary(model)$coefficients
summary(model)





smp_size <- floor(0.75 * nrow(robusta))

## set the seed to make your partition reproducible
set.seed(123)
train_ind <- sample(seq_len(nrow(robusta)), size = smp_size)

train <- robusta[train_ind, ]
test <- robusta[-train_ind, ] %>% select(-robustas)


model = lm(robustas ~ ., data=train)

par(mfrow=c(2,2)) # Plot 4 plots in same screen
plot(model)

coefs <- summary(model)$coefficients
summary(model)

pred <- predict(model, test)

