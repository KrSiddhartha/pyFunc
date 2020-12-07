def freqTab(df, colName):
    freqC = pd.DataFrame(dat.cement.value_counts())
    freqC.columns = ['Freq']
    freqP = pd.DataFrame(dat.cement.value_counts('normalise')*100)
    freqP.columns = ['Perc']
    freqP.Perc = round(freqP.Perc,2)
    freqT = pd.merge(freqC, freqP, left_index=True, right_index=True)
    freqT[colName] = freqC.index
    freqT = freqT[[colName,'Freq','Perc']]
    freqT.reset_index(inplace=True, drop=True)
    
    return freqT
