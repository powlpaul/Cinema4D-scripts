# Appends take names from take selection to each child take name seperated with a _ 

import c4d
from c4d import gui
    
  
def main():
    TakeData = doc.GetTakeData()
    if TakeData is None:
        return
        
    # Get a list of all children of the take selection
    TakeSelection = [x for x in TakeData.GetTakeSelection(True) if x not in TakeData.GetTakeSelection(False)]
    if TakeSelection is None:
        return
    
    # Change name of all takes in the list
    for s in TakeSelection:
        TakeName = s.GetName()
        TakeParentName = s.GetUp().GetName()
        #Check if already renamed
        if TakeParentName in TakeName:
            return
        TakeNewName = TakeName+'_'+TakeParentName
        s.SetName(TakeNewName)
    
if __name__=='__main__':
    main()