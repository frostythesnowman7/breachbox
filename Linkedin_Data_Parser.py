import time
import json
start = time.perf_counter()


def parsefile():
    file1 = open("MyFile.txt", "a")
    with open('part-00000', 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            str = json.loads(line)
            try:
                url = str['linkedin_url']
                if not url:
                    url = 'none'
            except:
                url = 'none'
            try:
                first = str['first_name']
                if not first:
                    first = 'none'
            except:
                first = 'none'
            try:
                last = str['last_name']
                if not last:
                    last = 'none'
            except:
                last = 'none'
            try:
                wemail = str['work_email']
                if not wemail:
                    wemail = 'none'
            except:
                wemail = 'none'
            try:
                title = str['job_title']
                if not title:
                    title = 'none'
            except:
                title = 'none'
            try:
                mphone = str['mobile_phone']
                if not mphone:
                    mphone = 'none'
            except:
                mphone = 'none'
            try:
                wphone = str['phone_numbers'][0]
                if not wphone:
                    wphone = 'none'
            except:
                wphone = 'none'
            try:
                employer = str['experience'][0]['company']['name']
                if not employer:
                    employer = 'none'
            except:
                employer = 'none'            
            try:
                email = str['emails'][0]['address']
                if not email:
                    email = 'none'
            except:
                email = 'none'

            writestr = email + ', ' + wemail + ', ' + employer + ', ' + first + ', ' + last + ', ' + title + ', ' + mphone + ', ' + wphone + ', ' + url
            print(writestr)
            file1.writelines(writestr + "\n")

            
    
    file1.close() 
#####

parsefile()



finish = time.perf_counter()
print(f'Finishing in {round(finish-start, 2)} seconds')
