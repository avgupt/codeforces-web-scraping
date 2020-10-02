import requests
from lxml import html
from time import sleep
import json

# see start and end pages and specify in range
# will throw an error at hidden submissions
def returnAcceptedSubmissions(Username, number_of_pages):

    for foo in range(1,number_of_pages):
        sleep(5)
        # change address below accordingly
        page = requests.get('https://codeforces.com/submissions/' + Username + '/page/'+ str(foo))
        tree = html.fromstring(page.text)
    
        res = []

        checkStatus = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[1]/*/@class')
        verdict = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[6]/span/@submissionverdict')
        contestID = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[4]/a/@href')
        problemID = tree.xpath('//*[@id="pageContent"]/div[4]/div[6]/table/tr[position() > 1]/td[1]/*/text()')
        
        for i in range(len(contestID)):
            r = list(map(str,contestID[i].split("/")))
            contestID[i] = r[2]

        for i in range(len(problemID)):
            res.append([contestID[i],verdict[i], problemID[i], checkStatus[i]])
           

        for i in range(len(res)):
            # change verdict or dont specify at all
            if res[i][1] == "OK" and res[i][3] == "view-source":
                solutionPage = requests.get('https://codeforces.com/contest/'+ res[i][0]+'/submission/'+ res[i][2])
                tree2 = html.fromstring(solutionPage.text)
                address = './/div[@id="pageContent"]/div[@class="roundbox SubmissionDetailsFrameRoundBox-'+res[i][2]+'"]/pre[@id="program-source-text"]//text()'
                
                code = tree2.xpath(address)

                lines = code[0].split("\r\n")
                save_data(lines)
                sleep(5)
            


def save_data(sub_data):
    with open('AcceptedSubmissions.txt', 'a') as sub_outfile:
        json.dump(sub_data, sub_outfile)
    return


returnAcceptedSubmissions("Benq",4)
