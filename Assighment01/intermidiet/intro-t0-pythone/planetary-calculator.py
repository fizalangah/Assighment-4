def planetary_calculator():
    weight = float(input("Enter the weight on Earth: "))
    planet = str(input("Enter the planet name: "))

    if planet == "mars":
        marsweight = weight * 0.378
        finalweight = round(marsweight,2)
        print(f" The equivalent on Mars: {finalweight}" )
    elif planet == "jupitor":
         jupitorweight = weight * 2.36
         jupifinal = round(jupitorweight,2)
         print(f" The equivalent on Jupitor: {jupifinal}")
    elif planet == "neptune":
         neptuneweight = weight * 1.14
         nepfinal = round(neptuneweight,2)
         print(f" The equivalent on Neptune: {nepfinal}")
    elif planet =="mercury" :
         murcaryweight = weight * 0.376
         murfinal = round(murcaryweight,2)
         print(f"  The equivalent on Mercury: {murfinal}") 
    elif planet == "venus":
         venusweight = weight *0.889
         venfinal = round(venusweight,2)
         print(f" The equivalent on Venus: {venfinal}")
    elif planet == "saturn" :
         saturnweight = weight * 1.081
         satfinal = round(saturnweight,2)
         print(f" The equivalent on Saturn: {satfinal}") 
    elif planet == "uranus" :
         uranusweight = weight * 0.815
         uranfinal = round(uranusweight,2)
         print(f" The equivalent on Uranus: {uranfinal}")
    else:
         print("please enter valid planet name!") 
planetary_calculator()                     

       
