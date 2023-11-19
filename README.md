# CookCheap
<img src=”https://github.com/thabnir/grocget/assets/115143411/1817408f-5320-401e-bc39-7361573ff11e" alt=”my banner”>
<p align=”center”>

<img width=”200" height=”200" src=”https://user-images.githubusercontent.com/75753187/123358567-aac7b900-d539-11eb-8275-0b380264bb4c.png" alt=”my banner”>

</p>
## Inspiration
Inflation is skyrocketing. Life is expensive. Students are poor. Sometimes, the carrots are Metro are cheap. CookCheap helps you minimize the costs of feeding yourself by comparing the prices for each item at different grocery stores. We hope to help people enjoy the pleasures of life, like relishing a delicious meal, without straining their already tight budgets.
## What it does
CookCheap receives a picture of a dish from a user, determines the ingredients present in the dish and returns the grocery store and shopping cart where the ingredients can be bought for the cheapest price.
## How we built it
We built a web interface that pulls food recipe and ingredient data from the Spoonacular API. The user can get a recommendation of dishes by: a) providing a list of ingredients, b) providing personal food preference and c) providing an image of a dish from which the food name and recipe ingredients are detected. We then scraped websites of different groceries stores such as Provigo, Adonis, Metro and more to get the price of ingredients. Our app then sums up the prices of a list of ingredients for each store and selects the store with the cheapest prices for the ingredients of a particular dish.
## Challenges we ran into
Daniel:
Being my first time working with an API, it took me some time to get used to it and reading through the documentation. Finding the right API calls and dealing with big JSON files to process user data took some time getting used to but I gradually got the hang of it. Connecting Flask with HTML and Javascript is something I have had a bit of experience in, but it took some time finding my footing on this.

One of the biggest challenges we faced as a team is files reverting back to older versions when one team member is pushing code on GitHub. For some of us, it was our first experience using git commands while coding in a team and we faced multiple instances of merge conflicts between files.

A challenge encountered during web scraping is dealing with .csv files which contain the data from the grocery stores.

## Accomplishments that we're proud of
We are proud that we developed an accessible interface to dishes we love.
## What we learned
Using real-time data is not as complicated as we may have imagined.
## What's next for CookCheap
The next steps could be to implement a dish recommendation system.

