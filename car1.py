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
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('The available colours are : \n1.White\n2.Black\n3.Silver\n4.Blue\n5.Red', ['colour' 'colours',])
    response('The available colours are : \n1.White\n2.Black\n3.Silver\n4.Blue\n5.Red ', ['color', 'colors'])
    response('It is a five seater car.', ['number', 'of', 'seats'], required_words=['seats'])
    response('This car is not equipped with airbags', ['how', 'many', 'airbags', 'are' , 'provided'], required_words=['airbags'])
    response('This car is not equipped with airbags ', ['how', 'many', 'air', 'bags' , 'provided'], required_words=['air','bags'])
    response('The music system is equipped with bluetooth', ['Does', 'the', 'music', 'system' , 'has' , 'bluetooth'], required_words=['bluetooth'])
    response('It is not equipped with parking sensors', ['Does' ,'it' ,'have' ,'parking' ,'sensors'], required_words=['parking','sensors'])
    response('It has a mileage of 18 to 20 kmpl', ['how', 'much', 'is', 'the','mileage'], required_words=['mileage'])
    response('It has a fuel tank capacity of 35 litres.', ['what', 'is', 'the', 'fuel' , 'tank','capacity'], required_words=['fuel'])
    response('Yes, the car is fully air conditioned.', ['does', 'the', 'car', 'have','air-conditioning'], required_words=['air-conditioning'])
    response('Yes, the car is fully air conditioned. ', ['does', 'the', 'car', 'have','ac'], required_words=['ac'])
    response('No, it does not have fog lights.', ['does', 'the', 'car', 'have','fog','lights'], required_words=['fog'])
    response('It is a manual car. ', ['is', 'it', 'manual', 'or','automatic'], required_words=['automatic'])
    response('It is a manual car . ', ['auto'], required_words=['auto'])
    response('It is a manual car.', ['is', 'it', 'manual', 'or','automatic'], required_words=['manual'])
    response('It does not have rear window wipers.', ['does', 'it', 'have', 'rear','wiper'], required_words=['wiper','rear'])
    response('It does not have leather seats.', ['does', 'it', 'have', 'leather','seats'], required_words=['leather','seats'])
    response('It is not equipped with voice control.', ['does', 'it', 'have', 'voice','control'], required_words=['voice'])
    response('It does not have alloy wheels.', ['does', 'it', 'have', 'alloy','wheels'], required_words=['alloy','wheels'])
    response('It does not have a parking camera', ['does', 'it', 'have', 'parking','camera'], required_words=['camera','parking'])
    response('It does not have a sun roof.', ['does', 'it', 'have', 'sun','roof'], required_words=['sun','roof'])
    response('It does not have a sun roof. ', ['does', 'it', 'have', 'sunroof'], required_words=['sunroof'])
    response('It does not have a child safety locks.', ['does', 'it', 'have', 'child','safety','locks'], required_words=['child','safety'])
    response('Models available are:\n\t1.i20 lite\n\t2.i20 magna\n\t3.i20 sports\n\t4.i20 Asta ', ['what', 'models', 'are', 'available'], required_words=['models'])
    response('Models available are \n\t1.i20 lite\n\t2.i20 magna\n\t3.i20 sports\n\t4.i20 Asta', ['what', 'model', 'is', 'available'], required_words=['model'])
    response('Price range for this car is 4 lacs to 7 lacs', ['what', 'is', 'price', 'range'], required_words=['price'])
    response('It is a manual car.  ', ['what', 'is', 'type', 'of','vehicle'], required_words=['vehicle','type'])
    response('It is a manual car.    ', ['what', 'is', 'type', 'of','car'], required_words=['car','type'])
    response('It is available in both petrol and deisel.', ['what', 'is', 'type', 'fuel'], required_words=['fuel','type'])
    response('It is available in both petrol and deisel. ', ['is', 'it','petrol'], required_words=['petrol'])
    response('It is available in both petrol and deisel.  ', ['is', 'it','deisel'], required_words=['deisel'])
    response('It is available in both petrol and diesel.   ', ['is', 'it','diesel'], required_words=['diesel'])
    response('It\'s average user rating is 3.7', ['what', 'is','the','average','rating'], required_words=['rating'])
    response('For booking a test drive , please  visit aor website :\n\twww.buycars.com', ['how', 'to','book','test','drive'], required_words=['test','drive'])
    response('For booking , please visit our website:\n\twww.buycars.com', ['how', 'to','book','car'], required_words=['book','car'])
    response('You will be provided 3 free services from our company.', ['many','how', 'services','free'], required_words=['free','services'])
    response('You will be provided 3 free services from our company. ', ['many','how', 'service','free','servicing','services'])
    response('For getting your car serviced, please visit our website:\n\twww.buycars.com', ['car','service','get'], required_words=['service'])
    response('It Has Maximum speed of 120kmph', ['speed'], required_words=['speed'])
    response('It Has 400 Horsepower(HP) petrol and diesel engine', ['engine'], required_words=['engine'])
    best=max(high_prob, key=high_prob.get)
    return i.unknown() if high_prob[best] < 1 else best


def user_res(user_msg):
    message=re.split(r'\s+|[,;?!.-]\s*', user_msg.lower())
    response= check_all_mess(message)
    return response


print('Hi! I\'m Wall-E I\'m here to help you')
print("!!!!You Can Press 1 to exit Anytime!!!")

while 1:
    f = open("car1.txt", "a")
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