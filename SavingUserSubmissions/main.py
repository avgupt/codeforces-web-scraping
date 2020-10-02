import requests
from lxml import html
from time import sleep

# see start and end pages and specify in range
# will throw an error at hidden submissions
def returnAcceptedSubmissions(Username, number_of_pages):

    for foo in range(1,number_of_pages):
        sleep(10)
        # change address below accordingly
        page = requests.get('https://codeforces.com/submissions/' + Username + '/page/'+ str(foo))
        tree = html.fromstring(page.text)
    
        res = []

        checkStatus = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[1]/a/@class')
        verdict = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[6]/span/@submissionverdict')
        contestID = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[4]/a/@href')
        problemID = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[1]/a/text()')
        #print(checkStatus)
        for i in range(len(contestID)):
            r = list(map(str,contestID[i].split("/")))
            #print(r)
            contestID[i] = r[2]

        for i in range(len(problemID)):
            res.append([contestID[i],verdict[i], problemID[i], checkStatus[i]])
            #print(contestID[i],verdict[i], problemID[i], checkStatus[i])
        #print(problemID)
        
        for i in range(len(res)):
            # change verdict or dont specify at all
            if res[i][1] == "OK" and res[i][3] == "view-source":
                solutionPage = requests.get('https://codeforces.com/contest/'+ res[i][0]+'/submission/'+ res[i][2])
                print('https://codeforces.com/contest/'+ res[i][0]+'/submission/'+ res[i][2])
                tree2 = html.fromstring(solutionPage.text)
                address = './/div[@id="pageContent"]/div[@class="roundbox SubmissionDetailsFrameRoundBox-'+res[i][2]+'"]/pre[@id="program-source-text"]//text()'
                #print(address)
                code = tree2.xpath(address)

                #print(code)
                lines = code[0].split("\r\n")
            
                for i in lines:
                    print(i)
                sleep(5)
            

returnAcceptedSubmissions("Um_nik",5)