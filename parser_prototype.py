import csv
cnt = 0
cnt1 = 0
cnt2 = 0
reTweets = list()
replyTweets = list()
tweets = list()
data = open("Malaysia_Airlines_201406232240.csv","r")
op1 = csv.writer(open("retweets.csv", "wb"), delimiter=',', quotechar="", quoting=csv.QUOTE_NONE, escapechar = ",")
# op2 = csv.writer(open("replytweets.csv", "wb"), delimiter=',', quotechar="", quoting=csv.QUOTE_NONE, escapechar = ",")
# op3 = csv.writer(open("tweets.csv", "wb"), delimiter=',', quotechar="", quoting=csv.QUOTE_NONE, escapechar = ",")
header = ["Tweeter","Re-Tweeter", "Message"]
op1.writerow(header)
# header1 = ["Reply-to", "Tweeter", "Message"]
# op2.writerow(header1)
# header2 = ["Tweeter","Message"]
# op3.writerow(header2)
for tweet in data:
    tweet = tweet.strip()
    tweet = tweet[31:]
    validation = tweet.find("RT @") # Over here to filter out the retweeted data
    if validation >= 0:
        cnt = cnt + 1
        sp1 = tweet.find("-")
        rtw1 = tweet[:sp1-1]
        atp1 = tweet.find("@")
        asp1 = tweet.find(" ",atp1)
        tw1 = tweet[atp1 + 1:asp1-1] 
        me1 = tweet.find("http:")
        msg1 = tweet[asp1 + 1: me1]
        msg1 = msg1.replace(',','')
        msg1 = msg1.replace('!','')
        msg1 = msg1.replace('#','')
        msg1 = msg1.replace('@','')
        msg1 = msg1.replace('"','')
        msg1 = msg1.replace('.','')
        msg1 = msg1.replace('-','')
        msg1 = msg1.replace('$','')
        msg1 = msg1.replace('&','')
        data1 = [tw1, rtw1, msg1]
        op1.writerow(data1)
#     elif validation < 0:
#         validation1 = tweet.find("@")
#         if validation1 >= 0 and validation < 0:
#             cnt1 = cnt1 + 1
#             sp2 = tweet.find("-")
#             rtw2 = tweet[:sp2-1]
#             atp2 = tweet.find("@")
#             asp2 = tweet.find(" ",atp2)
#             tw2 = tweet[atp2 + 1:asp2]
#             msg2 = tweet[asp2 + 1:]
#             msg2 = msg2.replace(',','')
#             data2 = [tw2, rtw2, msg2]
#             op2.writerow(data2)
#         else:
#             tweet = tweet.replace('-','')
#             cnt2 = cnt2 + 1
#             sp3 = tweet.find("-")
#             if sp3 < 0:
#                 s = tweet.find(" ")
#                 t = tweet[:s]
#                 m = tweet[s+1:]
#                 m = m.replace(',','')
#                 data3 = [t, m]
#                 op3.writerow(data3)
#             tw3 = tweet[:sp3-1]
#             msg3 = tweet[sp3 + 3:]
#             msg3 = msg3.replace(',','')
#             data3 = [tw3, msg3]
#             op3.writerow(data3)
# Summary of the dataset
print "+=+=+=+= SUMMARY =+=+=+=+"           
print "No. of RT:", cnt
# print "No. of Replies:", cnt1
# print "No. of Tweets", cnt2
print " reTweets done!!"
# print " replyTweets done!!"
# print " tweets done!!"

###
print "Parsing Challenge Inprogress!"