dataset = read.csv('D:/Arman/Course/1/Datasets/50_Startups.csv')
dataset$State = factor(x = dataset$State, levels = c('New York','California','Florida'),labels = c(1,2,3))
dataset 
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State,data = dataset)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend ,data = dataset)
summary(regressor)
regressor = lm(formula = Profit ~ R.D.Spend  + Marketing.Spend,data = dataset)
summary(regressor)
