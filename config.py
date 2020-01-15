"""
For Details of the Call of Duty API please view https://documenter.getpostman.com/view/7896975/SW7aXSo5?version=latest
This library is built around mw / Modern Warefare so some or all functionality as I am only interested in mw
game options:
> mw
> bo4
> wwii
platform options:
> 'battle' for mw/bo4
> 'steam' for wwii
May need your unique # for username. I only needed my xbox live gamertag and my activision account name#no didn't work
"""
username = "MattyMoore08"
game = 'mw'
platform = 'xbl'
payload = {}
headers = {}
# url for your own stats
baseUrl = "https://my.callofduty.com/api/papi-client/stats/cod/v1"
# url for my stats only
myUrl = baseUrl + "/title/" + game +  "/platform/" + platform + "/gamer/" + username + "/profile/type/mp"
# url for all stats of those in your friends list
flUrl =  baseUrl + "/title/" + game +  "/platform/" + platform + "/gamer/" + username + "/profile/friends/type/mp"