userurl=input("Enter your custom url: ")

match userurl:
    case "https://197.0.0.1":

        print ("kenya.com")
    case "https://197.0.0.2":

        print ("Uganda.com")
    case "https://197.0.0.3":

        print ("Tanzania.com")

    case default:
         print("Enter correct url format in the range of https://197.0.0.1  to https://197.0.0.3")
  