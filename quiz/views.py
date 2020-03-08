from django.shortcuts import render
import logic
# Create your views here.
def home(request):
    return render(request,'quiz/home.html')
def score(request):
    sum = 0
    for i in range(1,15):
        sum+=int(request.POST.get('w{}'.format(i),False))
    name = 'Ritik'
    logic.sendmail('ritikpmota@gmail.com',name,'Your score!','<p>Good work taking the test again! Here is your score:</p><p><b><u>{} out of 70.</b></u></p><p>Keep taking these tests to gove you and your therapist regular updates of how youre doing!'.format(sum))
    logic.sendmail('govind.thakur11@gmail.com','Govind','Score update on {}'.format(name),'<p>The patient just took the quiz again, and the score is:</p><p><b><u>{} out of 70.</b></u></p><p>Like always, we leave it to you to take the next call.'.format(sum))
    return render(request, 'quiz/score.html',{'score':sum})
