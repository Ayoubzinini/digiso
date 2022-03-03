Results=DataFrame([npns,adresses,phones,cp]).T
Results.columns=["Nom","Adresses","Phones","CP"]
Results.to_excel("/home/az/Downloads/Scrapper/to_merge/"+target_location+".xlsx")