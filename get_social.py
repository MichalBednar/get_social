
import re
import requests
from bs4 import BeautifulSoup
from colored import fore, back, style

class App():

    def __init__(self):
        self.welcome()
        self.get_website_url()

    # Print Welcome Intro
    def welcome(self):

        welcome_text = "\n"
        welcome_text += (("x" * 89) + "\n" + ("x" * 40) +
                         " Welcome " + ("x" * 40) + "\n")
        welcome_text += ("xxxxxxxxxxxxx" + back.CYAN +
                         " >This App Was Created For My Personal Purpose To Learn Python< " + style.RESET + "xxxxxxxxxxxx" + "\n")
        welcome_text += (("x" * 89) + "\n" + ("x" * 89))
        print(f"{welcome_text}")

    # Check If The User Wants To Continue To Check Another Website Or To Quit The Program
    def continue_or_quit_function(self):
        continue_or_quit_input = input(
            f"{fore.YELLOW}\n> If You Wish To Continue And Check Another Website's GET Status Type 'c', If You Wish To Quit The Program Press Any Other Letter:{style.RESET} ")

        if continue_or_quit_input.lower() == "c":
            self.get_website_url()
        else:
            pass

    # Check If Website Is Responding And If Yes, Scrape All The Social Media Links
    def get_website_url(self):
        entered_url = input(
            f"{fore.YELLOW}\n> Type website's url to check it's GET status code(like: www.example.com):{style.RESET} ")
        if entered_url:
            try:
                r = requests.get(f"https://{entered_url}")

                if r.status_code == 200:
                    print("Success. Status Code: " + back.DARK_GREEN +
                          str(r.status_code) + style.RESET + "\n")

                    scrape_links_input = input(
                        f"{fore.YELLOW}> Do You Wish To Scrape All The Social Media Links?(y/n):{style.RESET} ")

                    if scrape_links_input.lower() == "y":
                        soup = BeautifulSoup(r.text, "html.parser")

                        fb_link = soup.findAll(
                            "a", href=re.compile("facebook"))
                        tw_link = soup.findAll("a", href=re.compile("twitter"))
                        insta_link = soup.findAll(
                            "a", href=re.compile("instagram"))

                        social_links = set(fb_link + tw_link + insta_link)

                        if len(social_links) >= 1:
                            with open("linksfile.txt", "w") as f:
                                for link in social_links:
                                    print(f"{link.get('href')}")
                                    f.write(f"{link.get('href')}\n")
                        else:
                            print(f"No Social Media Links Were Found.")
                            self.continue_or_quit_function()

                    else:
                        self.continue_or_quit_function()

                elif r.status_code == 100:
                    print("Informational Response. Status Code: " + back.YELLOW +
                          str(r.status_code) + style.RESET + "\n")
                elif r.status_code == 300:
                    print("Redirection. Status Code: " + back.YELLOW +
                          str(r.status_code) + style.RESET + "\n")
                elif r.status_code == 400:
                    print("Client Error. Status Code: " + back.RED +
                          str(r.status_code) + style.RESET + "\n")
                    self.continue_or_quit_function()
                else:
                    print("Server Error. Status Code: " + back.RED +
                          str(r.status_code) + style.RESET + "\n")

            except requests.exceptions.ConnectionError:
                print(
                    f"{fore.RED} Make Sure To Type Website's URL In This Format: www.example.com{style.RESET} ")
                self.continue_or_quit_function()


a = App()
