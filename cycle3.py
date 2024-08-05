import re
import invalid as i


def mess_prob(user_msg,req_words,single_response=False,required_words=[]):
    mess_certain=0
    has_required_words= True
    for word in user_msg:
        if word in req_words:
            mess_certain+=1

    percentage=float(mess_certain)/float(len(req_words))

    for word in required_words:
        if word not in user_msg:
            has_required_words=False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0    



def check_all_mess(mes):
    high_prob={}
    def response(bot_res,words,single_response=False,required_words=[]):
        nonlocal high_prob
        high_prob[bot_res]=mess_prob(mes,words,single_response,required_words)

    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo','heelo'], single_response=True)
    response('See you!For more information you can visit our website https://www.herocycles.com/', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('2000  ',['price'], required_words=['price'])
    response('2000 ',['cost'], required_words=['cost'])
    response('Bicycle is available in many colour such as :\n1.black\n2.red\n3.blue\n4.green', ['colour','how','does','many','color'])
    response('Bicycle is available in many colour:\n1.black\n2.red\n3.blue\n4.blue ', ['colours','colour','colors','color'],)
    response('Yes the bicycle has no disc  breaks', ['disc','brakes'], required_words=['brakes'])
    response('Bicycle have no gears ', ['gear','gears'], required_words=['many'])
    response('Yes Bike Have NO Shock Ups', ['shock','up','shockup'], required_words=['shock','up'])
    response('Yes Bike Have NO Shock Ups', ['shock','up','shockup'], required_words=['shockup'])
    response('Bicycle have 6 months of Warranty On body-frame', ['warranty',], required_words=['warranty'])
    response('Bicycle is made up of moderete weight steel alloy', ['made','material','up'], required_words=['material'])
    response('The Bicycle is available in only one models\n\tmodel 1:sprint-2000',['model','models'])
    response('Our Bicycle is rated 4.2 stars out of 5', ['rating'], required_words=['rating'])
    best=max(high_prob, key=high_prob.get)
    return i.unknown() if high_prob[best] < 1 else best


def user_res(user_msg):
    message=re.split(r'\s+|[,;?!.-]\s*', user_msg.lower())
    response= check_all_mess(message)
    return response


print('Welcome To The Bicycle Section! I\'m Wall-E I\'m here to help you')
print("!!!!You Can Press 1 to exit Anytime!!!")
while 1:
    f = open("bicycle3.txt", "a")
    a=input('You: ')
    if(a=='1'):
     f.write("\n")   
     f.close()
     print('Have a Great Day! Its Great interacting with you! ')
     exit()
     
    else: 
     print('Wall-E : '+user_res(a))
     f.write("You: "+ a)
     f.write("\n")
     f.write("Bot: " + user_res(a))
     f.write("\n")