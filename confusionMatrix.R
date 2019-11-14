cnf_mtrx <- function(target_var, predictions){
  a = confusionMatrix(
    target_var,
    as.factor(ifelse(predictions < 0.3, 0, 1))
  )
  over.All <- a$overall[1]
  sensitivity <- a[4]$byClass["Sensitivity"]
  specificity <- a[4]$byClass["Specificity"]
  Precision  <-  a[4]$byClass["Precision"]
  Recall <-      a[4]$byClass["Recall"]
  f1 <-  a[4]$byClass["F1"]
  c(over.All, sensitivity, specificity, Precision, Recall, f1)
}

