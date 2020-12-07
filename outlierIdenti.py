def outlierIdenti(var_):
    q1=var_.quantile(0.25)
    q3=var_.quantile(0.75)
    iqr=q3-q1
    lower_whisker = q1-1.5*iqr
    upper_whisker = q3+1.5*iqr
    
    return [q1,q3,iqr,lower_whisker,upper_whisker]