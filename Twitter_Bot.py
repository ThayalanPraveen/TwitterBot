

import tweepy
import time

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

d_index = ['ena vachu comedy geemedy panalaye', 'aaniye pudungavenaa', 'aahan', 'vada poche', 'naa apdiye shock aagite', 'venaam…valikudhu….aluthuruve', 'why blood. same blood', 'trisha ilanaa nayanthara', 'naanum rowdythaan', 'jil jung juk', 'vandhutaanyaa vandhutaan', 'ipove rolling aaguthe', 'ipave kanakatuthe', 'ethayume plan pani pananum', 'nalaathane poitu irundhichu', 'ena nalavenu solitaanda', 'naan ethuku sari patu vara maate', 'elaathayu samaalichuthane aaganu', 'decent aa mudichukalaam', 'pechu pechathaa irukanu', 'dei avanaa nee', 'intha kota thaandi neeyu vara koodaathu naanu vara maate', 'ithu oru ratha boomi', 'adivaanguravanthaanda periya rowdy', 'building strong u basement weaku', 'payapula polachitu pora', 'yaaruda nee', 'katathuraiku katam sari illa', 'podaa dubuku', 'haiyo haiyooo', 'i am your bestu friend', 'avan oru human being', 'ungalalaa paatha enaku romba paavamaa iruku', 'kakakapo', 'maapu vachitaanda aapu', 'kudumbathula kumiadichaathinga', 'be careful naa ena sone', 'risk alaa enaku rusku saapudra maathiri', 'enaku kovo vandhichu', 'enaa oru villathanam', 'podaa ye vendru', 'marupadiyu muthala irundhaa', 'apdiye padi eri vaara maathiriye oru peeling', 'onaa pola ona pola', 'marupadiyu muthala irundhaa', 'athu pona maaso', 'ithu uchakata avamaanam', 'ei ei mariyaatha mariyaatha', 'ipdiye usupethi usupethi odamba ranagalam aakitaanga', 'kundaka mandaka', 'betaa engamaa thaaraanga', 'adichaangayaa appointement orderu', 'sali sali yaa norukitaaingale', 'onalaa vachu oru urugaa koda poda mudiyaathu', 'enaye serupaalaiye adichukanu', 'dei appracentingulaa', 'mela mela sevaruku valika poguthu', 'nee aaniye pudunga venaa', 'nee pudungurathu pooraave theva ilaatha aanitha', 'rightu vidu', 'nextu restu', 'sina pula thanamaa ila', 'enga akka oru super figureu', 'enaa enaa feeling', 'enakuthaanda feeling', 'that rowdy and police play basketball in my life', 'lochak machak bachak', 'hello dubai yaa', 'my family, total damage', 'talk me', 'ey ey y mister adhigaari nu sonatha ena', 'naa apdiye shock aayute', 'engaluku risk edukurathelaa rusk saapudra maathiri', 'maapu vachitaangadaa aapu', 'ithu vaaliba vaysau', 'this is drunken monkey style', 'suruthiiii', 'ohh ithuthaan alagula mayangurathaa', 'ithuku malaiyu alagu venumaa', 'oru katha solre', 'evalavu adichaalu thaangura ive romba nalavanu solitaanga da', 'vaa maa minnal', 'intha ranagalathulaiyu onaku oru kilukilupu kekuthu', 'ahaa kelambitaayaa', 'maamanuku epa kanju oothapora', 'neenga oru kena ku', 'snaaakkkee baabu', 'heyy youuuuu', 'am alert arumugam', 'paraaa', 'idhu vaaliba vayasu']


FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    import random
    print('retrieving and replying to tweets...')
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text )
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#guessthevadivelvasanam' in mention.full_text.lower():
            count = 91
            generate = random.randint(1, count-1)
            print('found #guessthevadivelvasanam')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name + " "+
                    d_index[generate] + "  Guess the movie!", mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)

