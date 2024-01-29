from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID" : "fgglQ8C_D_MoZAAIRa8xBG_UrS_CLI3UlyanlvkT5KjPcMEuKacInF5QPoNAI1UvnEwTHg.",
    "__Secure-1PSIDTS" : "sidts-CjEBPVxjSsoF_qt3IT9WvIJoSkrd9nLiEY_DcMpPbIk53WuhKp7aJL6r22TFd-wmb6CrEAA",
    "__Secure-1PSIDCC" : "ABTWhQFwiw1Ct0lqkMFY7HyiBmyZA3hNxy1lnXj9syif2JRf_sctXrxqPL8SqMuv7cxqIE6J-YA"    
    }

bard = BardCookies(cookie_dict=cookie_dict)

while True:
    Quary = input("Enter your Quary: ")
    Reply = bard.get_answer(Quary)['content']
    print(Reply)
