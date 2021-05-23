## Intro- printed
hello = input("Welcome to my Weather Program! -- Press Enter to Continue")
 
## If user requests info by city
def by_city():
    city = input('Please Enter Your City Name: ')
    ## where to request from- my API key
   
    ## transferring data to Json for readability
    data = res.json()
    show_data(data)
 
 
    ## does the user want to go again?
    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes' or question == 'yes':
        main()
    if question == 'No' or question == 'no':
        print("Thank you for using my weather program. Have a nice day!")
        exit()
 
## If user requests info by zip code
def by_zip():
    zip_code = int(input('Please Enter Your Zip Code: '))
    ## where to request from- my API key
   
 
    ## does the user want to go again?
    question = input('Do you want to do another search ? Type Yes or No: ')
    if question == 'Yes' or question == 'yes':
        main()
    if question == 'No' or question == 'no':
        print("Thank you for using my weather program. Have a nice day!")
        exit()
\