# User guide for the WebApp by UE

`This file is to write a guideline of the use of web page http://sunxinyu.pythonanywhere.com/`

- Style: all buttons are highlighted with the color `slateblue`

## Home page (Home)

- The home page `/` will give an overview of the locations that can be visited, with head bar displaying certain functions in buttons and side bar displaying different levels:
  - Head bar (Functions included):
    - `Home`: the button will return to the home page, or admin home page if login in already
    - `Login`: the button will head to the login page, allowing the user to login in as an admin. Specific details are explained above.
    - `Search`: the search bar allows the user to find location(s) with certain keywords. For example, the keyword `cs` will lead to the result of `cs21, cs22, cs23`, three locations with keyword `cs` inside. After typing in the keyword in the bar, click the `search` button to perform the operation.
  - side bar:
    - `All` is a button that removes the current **filter** and return the `home` page
    - The other bars `1.0` `2.0` `3.0` will namely change the filter of the items, so that it will only display the locations at the certain level.
  - The `manycards` section will display an overview of the locations:
    - In each card, it includes two parts: the `image` of the location and the `name` of the location. The `name` button will direct to the specific page `item`

## Login

- The section is triggered by clicking `Login` button in the main page head bar
- The admin account: Username: `Admin` Password: `20190831`
  - If login successfully will lead to the admin home page, allowing update, delete operations
  - Fail to login will trigger displaying of an error message and will still remain at the login page `/loginpage`
  - An easter egg may be triggered with the date of last day of term 3 :)

## Visitor mode (without logging in)

- The user is able to view the specific details of each location by clicking the `name` of the location and head to `item` page
- In `item` page: a list of details are provided: `name`, `level`, `image`, `description` and `Nearby Locations`
  - `Nearby Location` section will list all the locations that can be reached from this location. By clicking the `name` of the thumbview of the location, it will lead to the `item` page of the selected location

## Admin mode (after login in)

- The `/loginpage` has been explained in the earlier section
- After logining in as an admin, the user is able to edit and add in new location / link, namely at the page `/addLocation` and `/addLink`
- At `/addLocation`: the image is required to complete an `add` operation
- At `/addLink`: the two locations selected have to be present inside the current available locations to add in the linkage. Otherwise, it will display an error message and remain at the page `/addLink`
- At `/admin`: similar to the `/` but with additional features:
  - There is one more `X` at the right up corner of each location. Once clicked, the location will be deleted and all linkings to the location will be deleted.
  - At each view, besides the `image` and `name`, there is additional `edit` function. When clicked, it will pop up the `/edit/<location>` page for the user to update information about the location. 
