# Title     : Labs
# Objective : Normal distribution experiments
# Created by: alexandr.omarov
# Created on: 19.03.2020

require(graphics)
require(dplyr)
require(ggpubr)
require(readr)
require(Quandl)

# Task 1.
iris <- read.csv("resources/csv/IRIS.csv")
set.seed(0)
shapiro.test(rnorm(iris$petal_length, mean = 2, sd = 5))
set.seed(0)
shapiro.test(rnorm(iris$petal_width, mean = 2, sd = 5))
print("p-value > a, values are in normal distribution")

# Task 2.
set.seed(124)
colsmir <- function(mean) {
  norm <- rnorm(200, mean, sqrt(mean))
  norm_x2 <- dchisq(200, mean)
  ks.test(norm,norm_x2, alternative = ("two.sided"))
}
colsmir(10)
colsmir(15)
colsmir(20)
colsmir(25)
colsmir(30)
print("Datasets aren't in the same distribution")

# Task 3.
set.seed(0)
countries <- read.csv("resources/csv/countries.csv")
filtered_countries <- subset(countries, LandArea != "N.A." & LandArea > 10 & Population != "N.A.")
area_log <- log10(log10(filtered_countries$LandArea))
population_log <- log10(log10(filtered_countries$Population))
model <- lm(population_log ~ area_log)
coefficients <- coefficients(model)
print(coefficients)
function_vector <- coefficients["(Intercept)"] + coefficients["area_log"]*area_log
ks.test(population_log,function_vector, alternative = ("two.sided"))
print("p-value > 0.05, Vectors are in the same distribution")

# Task 4.
set.seed(0)
hair_eye_color <- data.frame(HairEyeColor)
chisq.test(hair_eye_color$Hair, hair_eye_color$Eye)
print("p-value > 0.05, values are independent")

# Task 5.
set.seed(0)
readingspeed <- read.csv("resources/csv/readingspeed.csv",sep = " ")
# Полагаем в качестве альтернативной гипотезы то, что мат. ожидания не равны
t.test(readingspeed$DRA, readingspeed$SC)
print("p-value < 0.05, alternative hyposis should be accepted - it's equal")
# Полагаем в качестве альтернативной гипотезы то, что мат. ожидания не равны
t.test(readingspeed$DRA, readingspeed$SC, alternative = "less")
print("p-value > 0.05, default hyposis should be accepted - DRA more than SC")

#Misc
key <- read_file("resources/quandl/key.txt")
Quandl.api_key(key)
data <- Quandl('LPPM/PALL', start_date='2018-08-12', end_date='2020-04-16', column_index=1,
               collapse = "monthly", type = "ts")
print(data)