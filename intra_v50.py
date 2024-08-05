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
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and hope you are too. How can I help; You?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)


    response('The available colours are : \n1.White\n2.Black\n3.Silver\n4.Blue\n', ['what', 'are', 'colours', 'available'], required_words=['colours'])
    response('The available colours are : \n1.White\n2.Black\n3.Silver\n4.Blue\n  ', ['what', 'are', 'colour', 'available'], required_words=['colour'])
    response('The available colours are : \n1.White\n2.Black\n3.Silver\n4.Blue\n    ', ['what', 'are', 'color', 'available'], required_words=['color'])
    response('The available colours are : \n1.White\n2.Black\n3.Silver\n4.Blue\n     ', ['what', 'are', 'colors', 'available'], required_words=['colors'])

    response('It has loading area of 2960 mm x 1607 mm (9.8 x 5.3 feet). (Roughly, 215 - 15" radial tyres', ['what','is','its','load','loading','capacity'], required_words=['capacity'])
    response('Power of 59 KW is generated @ 4000 RPM (79 HP)', ['how','much','power','generated'], required_words=['power'])
    response('It packs Torque of 220 Nm @ 1750-2500 RPM', ['how','much','torque','genrated'], required_words=['torque'])
    response('It has High Ground clearance: 188mm', ['how','much','what','ground','clearance'], required_words=['clearance'])
    response('Smaller turning circle radius of 5.25mm', ['what','turning','radius'], required_words=['turning'])
    response('The Tyre Size/Type 215/75 R15 8PR (With Tube)', ['what','tyre','tire','size'], required_words=['tire'])
    response('The Tyre Size/Type 215/75 R15 8PR (With Tube)', ['what','tyre','tire','size'], required_words=['tyre'])
    response('Length : 4734\nWidth : 1694\nHeight : 2008\nWheelbase : 2600\nGround Clearance : 175\nMin TCR : 6000\nMax TCR : 2940', ['dimension','dimensions'])
    response('The Gross Vehicle Weight is 2940kg\nPayload weight(max) can be 1500kg', ['how','much','carry','weight','load'], required_words=['weight'])
    response('The warranty provided will be 2 Years / 72000 Kms *(Valid till whatever expires first)', ['what','how','much','warranty'], required_words=['warranty'])
    response('For getting more information on your vehicle, please visit our website:\n\thttps://smalltrucks.tatamotors.com/product/intra/tata-intra-v50', ['site','website','online','web','pics','pictures','look'])
    response('It is a Front 2-Seater loading vehicle.', ['number', 'of', 'seats'], required_words=['seats'])
    response('This vehicle is not equipped with airbags', ['how', 'many', 'airbags', 'are' , 'provided'], required_words=['airbags'])
    response('The music system is equipped with bluetooth', ['Does', 'the', 'music', 'system' , 'has' , 'bluetooth'], required_words=['bluetooth'])
    response('It is not equipped with parking sensors', ['Does' ,'it' ,'have' ,'parking' ,'sensors'], required_words=['parking','sensors'])
    response('It has a mileage of 18 to 20 kmpl varying upon loads', ['how', 'much', 'is', 'the','mileage'], required_words=['mileage'])
    response('It has a fuel tank capacity of 35 litres.', ['what', 'is', 'the', 'fuel' , 'tank','capacity'], required_words=['fuel'])
    response('Yes, the vehicle is fully air conditioned.', ['does', 'the', 'vehicle', 'have','air-conditioning'], required_words=['air-conditioning'])
    response('Yes, the vehicle is fully air conditioned. ', ['does', 'the', 'vehicle', 'have','ac'], required_words=['ac'])
    response('Yes, it does have fog lights.', ['does', 'the', 'vehicle', 'have','fog','lights'], required_words=['fog'])
    response('It is a manual vehicle. ', ['is', 'it', 'manual', 'or','automatic'], required_words=['automatic'])
    response('It is a manual vehicle.', ['is', 'it', 'manual', 'or','automatic'], required_words=['manual'])
    response('It does not have rear window wipers.', ['does', 'it', 'have', 'rear','wiper'], required_words=['wiper','rear'])
    response('It does not have leather seats.', ['does', 'it', 'have', 'leather','seats'], required_words=['leather','seats'])
    response('It is not equipped with voice control.', ['does', 'it', 'have', 'voice','control'], required_words=['voice'])
    response('It does not have alloy wheels.', ['does', 'it', 'have', 'alloy','wheels'], required_words=['alloy','wheels'])
    response('It does not have a parking camera', ['does', 'it', 'have', 'parking','camera'], required_words=['camera','parking'])
    response('It does come with have a child safety locks.', ['does', 'it', 'have', 'child','safety','locks'], required_words=['child','safety'])
    response('The mini truck starts at  price of 8.67 lakhs and is offered in a single variant ', ['what', 'is', 'price', 'range'], required_words=['price'])
    response('It is a manual vehicle.  ', ['what', 'is', 'type', 'of','vehicle'], required_words=['transmission','type'])
    response('It is a manual vehicle.    ', ['what', 'is', 'type', 'of','vehicle'], required_words=['transmission','type'])
    response('Yes, It is available in diesel.', ['what', 'is', 'type', 'fuel'], required_words=['fuel','type'])
    response('Oops, It is only available in diesel', ['is', 'it','petrol'], required_words=['petrol'])
    response('Yes, It is available in diesel.   ', ['is', 'it','diesel'], required_words=['diesel'])
    response('It\'s average user rating is 4.3', ['what', 'is','the','average','rating'], required_words=['rating'])
    response('For booking a test drive , please  visit aor website :\n\thttps://intra.tatamotors.com/', ['how', 'to','book','test','drive'], required_words=['test','drive'])
    response('For booking , please visit our website:\n\thttps://smalltrucks.tatamotors.com/product/intra/tata-intra-v50', ['how', 'to','book','vehicle'], required_words=['book','vehicle'])
    response('You will be provided 3 free services from our company.', ['many','how', 'services','free'], required_words=['free','services'])
    response('You will be provided 3 free services from our company. ', ['many','how', 'service','free','servicing','services'])
    response('For getting your vehicle serviced, please visit our website:\n\thttps://smalltrucks.tatamotors.com/product/intra/tata-intra-v50', ['vehicle','service','get'], required_words=['service'])
    
    best=max(high_prob, key=high_prob.get)
    return i.unknown() if high_prob[best] < 1 else best


def user_res(user_msg):
    message=re.split(r'\s+|[,;?!.-]\s*', user_msg.lower())
    response= check_all_mess(message)
    return response


print('Hi! I\'m Wall-E I\'m here to help you')
print("!!!!You Can Press 1 to exit Anytime!!!")
f = open("truck.txt", "a")
while 1:
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