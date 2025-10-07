class InvalidChaiException(Exception):pass
     
def bill(flavour , cups):
        
        menu = {"khawa":20 , "black":30}

        try:
            if flavour not in menu:
                raise InvalidChaiException("This Flavour is Not avalible")
            if not isinstance(cups , int):
                raise TypeError("Value of Cups must be interger")
            
            total = menu[flavour]*cups
            print(f"your bill for {cups} cups and flavour {flavour} is total :  {total}")
        except Exception as e:
            print("Error :" , e)
        finally:
            print("Thanks for visiting chai code")

bill("khawa" , 2)

