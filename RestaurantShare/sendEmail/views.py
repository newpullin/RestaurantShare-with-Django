from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Create your views here.
from shareRes.models import *


def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']
    inputEmailAddress = request.POST['inputEmailAddress']
    inputEmailPassword = request.POST['inputEmailPassword']

    mail_html = "<html><body>"
    mail_html += "<h1>맛집 공유 </h1>"
    mail_html += "<p>" + inputContent +"<br>"
    mail_html += "발신자님께서 공유하신 맛집은 다음과 같습니다. </p>"
    for checked_res_id in checked_res_list:
        restaurant = Restaurant.objects.get(id = checked_res_id)
        mail_html += "<h2>"+restaurant.restaurant_name+"</h2>"
        mail_html += "<h4>* 관련 링크</h4>"+"<p>"+restaurant.restaurant_link+"</p><br>"
        mail_html += "<h4>* 상세 내용</h4>" + "<p>" + restaurant.restaurant_content + "</p><br>"
        mail_html += "<h4>* 관련 키워드</h4>" + "<p>" + restaurant.restaurant_keyword + "</p><br>"
        mail_html += "<br>"
    mail_html += "</body></html>"

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(inputEmailAddress, inputEmailPassword)

    msg = MIMEMultipart('alternative')
    msg['Subject'] = inputTitle
    msg['From'] = inputEmailAddress
    msg['To'] = inputReceiver
    mail_html = MIMEText(mail_html, 'html')
    msg.attach(mail_html)
    server.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
    server.quit()


    return HttpResponseRedirect(reverse('index'))