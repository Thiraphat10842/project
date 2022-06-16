from conDB import Con      

class Action:
     def insertHW(name, hw_name): 
        ID = Con.insertHW(name, hw_name) 
        if(ID):
            data = Con.getHWByID(ID) 
        else:
            data = {"error": True}
        return data

     def updateStatusHW(ID, status):
        t = Con.updateStatusHW(ID, status)
        if( t == True):
            data = Con.updateStatusHW(ID)
        else:
            data = {"error": True}
        return data
     
     def updateStatusHW(ID, value):
        t = Con.updateStatusHW(ID, value)
        if( t == True):
            data = Con.updateStatusHW(ID)
        else:
            data = {"error": True}
        return data
     
     def DeleteHW(ID):
        boolean = Con.DeleteHW(ID)
        if boolean:
            data = {"error": False, "Delete": "Succeses"}
        else:
            data = {"error": True}
        return data